#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplica edições de texto aos arquivos de `secoes/`, preservando a estrutura do markdown.

Existe porque os .md são quebrados em 88 colunas: uma substituição ingênua com sed
falha sempre que o trecho atravessa a quebra de linha. Aqui cada parágrafo de prosa é
normalizado em uma linha, a substituição é aplicada, e o parágrafo volta quebrado.
Blocos de figura, de código, tabelas, títulos e divs de estilo não são tocados.

Uso programático:

    from aplicar_edicoes import editar, juntar
    editar('secoes/02-referencial.md', [('texto antigo', 'texto novo')])
    juntar('secoes/01-introducao.md', 'início do primeiro parágrafo')
"""

import os
import re
import sys
import textwrap

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLUNAS = 88


def _protegido(bloco):
    b = bloco.lstrip()
    return (b.startswith('[[') or b.startswith('```') or b.startswith('#')
            or b.startswith('|') or b.startswith(':::') or b.startswith('> '))


def _partes(texto):
    """Devolve (frontmatter, lista de blocos).

    Blocos cercados — ``` de código e [[FIG/TAB ...]] — podem conter linha em branco
    no meio. Eles são isolados ANTES do corte por parágrafo, senão o split os fatia e
    o conteúdo volta reescrito como prosa.
    """
    m = re.match(r'^(---\n.*?\n---\n)(.*)$', texto, re.S)
    fm, corpo = (m.group(1), m.group(2)) if m else ('', texto)
    cercados = []

    def guardar(mo):
        cercados.append(mo.group(0))
        return '\x00%d\x00' % (len(cercados) - 1)

    corpo = re.sub(r'```.*?```', guardar, corpo, flags=re.S)
    corpo = re.sub(r'\[\[(?:FIG|TAB):.*?\n\]\]', guardar, corpo, flags=re.S)
    blocos = [re.sub(r'\x00(\d+)\x00', lambda mo: cercados[int(mo.group(1))], b)
              for b in corpo.split('\n\n')]
    return fm, blocos


def _montar(fm, blocos):
    saida = []
    for b in blocos:
        b = b.strip('\n')
        if not b.strip():
            continue
        if _protegido(b):
            saida.append(b)
        else:
            saida.append('\n'.join(textwrap.wrap(' '.join(b.split()), COLUNAS,
                                                 break_on_hyphens=False)))
    return fm + '\n'.join(s + '\n\n' for s in saida).rstrip('\n') + '\n'


def editar(caminho, pares, obrigatorio=True):
    """Aplica (antigo, novo) sobre cada parágrafo de prosa. Erra se não encontrar."""
    caminho = caminho if os.path.isabs(caminho) else os.path.join(RAIZ, caminho)
    fm, blocos = _partes(open(caminho, encoding='utf-8').read())
    achados = {a: 0 for a, _ in pares}
    novos = []
    for b in blocos:
        if not _protegido(b) and b.strip():
            linha = ' '.join(b.split())
            for antigo, novo in pares:
                if antigo in linha:
                    linha = linha.replace(antigo, novo)
                    achados[antigo] += 1
            b = linha
        novos.append(b)
    faltando = [a for a, n in achados.items() if n == 0]
    if faltando and obrigatorio:
        raise SystemExit('não encontrado em %s:\n  %s'
                         % (os.path.basename(caminho), '\n  '.join(faltando)))
    open(caminho, 'w', encoding='utf-8').write(_montar(fm, novos))
    return achados


def juntar(caminho, inicio_do_primeiro):
    """Funde o parágrafo que começa com `inicio_do_primeiro` com o seguinte."""
    caminho = caminho if os.path.isabs(caminho) else os.path.join(RAIZ, caminho)
    fm, blocos = _partes(open(caminho, encoding='utf-8').read())
    saida, i, feito = [], 0, False
    while i < len(blocos):
        b = blocos[i]
        linha = ' '.join(b.split())
        if not _protegido(b) and linha.startswith(inicio_do_primeiro) and i + 1 < len(blocos):
            seguinte = ' '.join(blocos[i + 1].split())
            saida.append(linha + ' ' + seguinte)
            i += 2
            feito = True
            continue
        saida.append(b)
        i += 1
    if not feito:
        raise SystemExit('parágrafo não encontrado em %s: %s'
                         % (os.path.basename(caminho), inicio_do_primeiro))
    open(caminho, 'w', encoding='utf-8').write(_montar(fm, saida))


if __name__ == '__main__':
    print(__doc__)
    sys.exit(0)
