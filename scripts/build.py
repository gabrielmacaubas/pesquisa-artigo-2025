#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monta o artigo completo a partir de secoes/*.md.

  - concatena as seções na ordem numérica do nome do arquivo
  - remove o front matter
  - numera figuras e tabelas na ordem de aparição
  - troca [[@FIG:03-1]] por "Figura 3" e insere a imagem + legenda no lugar do bloco
  - gera a lista de referências em ABNT a partir de refs.md (só as citadas)

Saída: build/artigo.md  (o build.sh converte para .docx com pandoc)
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECOES = os.path.join(RAIZ, 'secoes')
BUILD = os.path.join(RAIZ, 'build')
REFS = os.path.join(RAIZ, 'refs.md')
SAIDA = os.path.join(BUILD, 'artigo.md')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate import (RE_FIG_BLOCO, RE_FIG_REF, RE_FRONTMATTER, RE_REF_CHAVE,
                  RE_REF_CAMPO, RE_CIT_PAREN, RE_CIT_NARR, ler, sem_codigo)

ROTULO = {'FIG': 'Figura', 'TAB': 'Tabela'}


def numerar(secoes):
    """Percorre na ordem final e atribui número a cada FIG/TAB."""
    numeros = {}
    contador = {'FIG': 0, 'TAB': 0}
    for _, texto in secoes:
        for m in RE_FIG_BLOCO.finditer(texto):
            tipo, ident = m.group(1), m.group(2)
            if (tipo, ident) not in numeros:
                contador[tipo] += 1
                numeros[(tipo, ident)] = contador[tipo]
    return numeros


def campos_do_bloco(corpo):
    campos = {}
    for linha in corpo.splitlines():
        if ':' in linha:
            k, v = linha.split(':', 1)
            campos[k.strip()] = v.strip()
    return campos


def render_figura(tipo, ident, campos, numero):
    rotulo = ROTULO[tipo]
    legenda = campos.get('legenda', '')
    # normaliza "Figura 3 — ..." para o número real
    legenda = re.sub(r'^(Figura|Tabela|Quadro)\s*\d*\s*[—-]\s*', '', legenda).strip()
    arquivo = campos.get('arquivo', '')
    caminho = os.path.join(RAIZ, arquivo)
    partes = ['', '**%s %d — %s**' % (rotulo, numero, legenda), '']
    if arquivo and os.path.exists(caminho):
        partes.insert(1, '![](%s)' % arquivo)
        partes.insert(2, '')
    else:
        partes.insert(1, '> ⚠️ IMAGEM AUSENTE: `%s` — %s'
                      % (arquivo or '(sem caminho)', campos.get('descricao', '')))
        partes.insert(2, '')
    return '\n'.join(partes)


def processar(texto, numeros):
    texto = RE_FRONTMATTER.sub('', texto)

    def sub_bloco(m):
        tipo, ident = m.group(1), m.group(2)
        campos = campos_do_bloco(m.group(3))
        return render_figura(tipo, ident, campos, numeros.get((tipo, ident), 0))

    texto = RE_FIG_BLOCO.sub(sub_bloco, texto)

    def sub_ref(m):
        tipo, ident = m.group(1), m.group(2)
        n = numeros.get((tipo, ident))
        return '%s %d' % (ROTULO[tipo], n) if n else '%s ??' % ROTULO[tipo]

    return RE_FIG_REF.sub(sub_ref, texto).strip()


def carregar_refs():
    if not os.path.exists(REFS):
        return {}
    bruto = ler(REFS)
    bruto = re.sub(r'<!--.*?-->', '', bruto, flags=re.S)
    marcas = list(RE_REF_CHAVE.finditer(bruto))
    out = {}
    for i, m in enumerate(marcas):
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(bruto)
        campos = dict(RE_REF_CAMPO.findall(bruto[m.start():fim]))
        out[(m.group(1).strip().upper(), m.group(2))] = campos
    return out


def citadas_no_texto(secoes):
    usadas = set()
    for _, texto in secoes:
        corpo = sem_codigo(RE_FRONTMATTER.sub('', texto))
        for m in RE_CIT_PAREN.finditer(corpo):
            usadas.add((re.split(r'[;,]', m.group(1))[0].strip().upper(), m.group(2)))
        for m in RE_CIT_NARR.finditer(corpo):
            usadas.add((m.group(1).strip().upper(), m.group(2)))
    return usadas


def formatar_abnt(campos):
    """NBR 6023 simplificada — conferir contra o template do veículo."""
    p = []
    autores = campos.get('autores', '').strip()
    if autores:
        p.append(autores.rstrip('.') + '.')
    titulo = campos.get('titulo', '').strip()
    if titulo:
        p.append('**%s**.' % titulo.rstrip('.'))
    veiculo = campos.get('veiculo', '').strip()
    if veiculo:
        p.append(veiculo.rstrip('.') + ',')
    ano = campos.get('ano', '').strip()
    if ano:
        p.append(ano + '.')
    url = campos.get('doi_url', '').strip()
    if url:
        p.append('Disponível em: %s.' % url)
    acesso = campos.get('acesso_em', '').strip()
    if acesso:
        p.append('Acesso em: %s.' % acesso)
    return ' '.join(p)


def main():
    if not os.path.isdir(SECOES):
        print('secoes/ não existe'); return 1
    nomes = sorted(n for n in os.listdir(SECOES) if n.endswith('.md'))
    if not nomes:
        print('Nenhuma seção para montar.'); return 1
    secoes = [(n, ler(os.path.join(SECOES, n))) for n in nomes]

    numeros = numerar(secoes)
    corpo = [processar(t, numeros) for _, t in secoes]

    refs = carregar_refs()
    usadas = citadas_no_texto(secoes)
    lista = sorted((k for k in refs if k in usadas), key=lambda k: (k[0], k[1]))
    if lista:
        corpo.append('# REFERÊNCIAS\n\n' +
                     '\n\n'.join(formatar_abnt(refs[k]) for k in lista))

    os.makedirs(BUILD, exist_ok=True)
    with open(SAIDA, 'w', encoding='utf-8') as fh:
        fh.write('\n\n'.join(corpo) + '\n')

    faltando = [k for k in usadas if k not in refs]
    print('build/artigo.md gerado — %d seções, %d figuras/tabelas, %d referências'
          % (len(secoes), len(numeros), len(lista)))
    if faltando:
        print('⚠️  citadas sem entrada em refs.md: %s'
              % ', '.join('%s %s' % k for k in sorted(faltando)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
