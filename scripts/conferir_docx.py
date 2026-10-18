#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Confere o .docx gerado contra o .docx de referência revisado pelo orientador.

Existe por causa da revisão de 09/10/2026: o orientador corrigiu o artigo direto no
Word, e o pedido foi que o documento gerado aqui ficasse igual ao que ele enviou. Sem
uma conferência mecânica, "ficou igual" é promessa; com ela, é verificável a cada build.

Compara o TEXTO, parágrafo a parágrafo, normalizando espaço. Formatação não entra:
essa parte vive em `preparar_reference.py` e `formato_principia.py`.

  python3 scripts/conferir_docx.py                      # usa a referência padrão
  python3 scripts/conferir_docx.py outro.docx           # contra outro arquivo

Saída 0 quando não há divergência de texto, 1 quando há.
"""

import difflib
import os
import re
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOSSO = os.path.join(RAIZ, 'build', 'artigo.docx')
REFERENCIA = os.path.join(RAIZ, 'docs', 'revisao-orientador-2026-10-09.docx')

# Divergências aceitas, com o motivo. O que estiver aqui não conta como erro.
# Toda entrada nova precisa de justificativa escrita: é o que impede a lista de virar
# um tapete para esconder divergência não resolvida.
ESPERADAS = [
    ('Automating the longitudinal assessment',
     'título em inglês refeito para acompanhar o título em português que ele sugeriu'),
    ('Automating certification and pedagogical recommendation',
     'título em inglês antigo, substituído pelo acima'),
    ('Essa concentração explica um padrão',
     'cortado para caber nas 18 páginas que ele exigiu; repetia a introdução'),
    ('O programa que constitui o contexto deste trabalho',
     'cortado para caber nas 18 páginas; repetia a subseção 3.1'),
    ('As duas linhas convergem em um ponto',
     'cortado para caber nas 18 páginas; repetia o fecho da introdução'),
    ('O relato apoia-se em evidência de operação real',
     'condensado para caber nas 18 páginas; nenhum dado ou ressalva foi perdido'),
    ('A separação entre esses dois planos',
     'condensado para caber nas 18 páginas; mantidos os 49 pares e a dependência'),
    ('Essas medições cobrem um recorte específico',
     'condensado para caber nas 18 páginas; mantida a distinção esforço x duração'),
    ('Essas medições dizem respeito ao tempo de execução',
     'versão condensada do parágrafo acima'),
    ('O que os resultados acrescentam ao ciclo anterior',
     'versão condensada do parágrafo acima'),
    ('ARREDONDAR(∣restantes∣',
     'a barra vertical virou o sinal de divisibilidade: no arquivo dele a barra é '
     'delimitador de célula e some na extração; aqui ela sobrevive'),
    ('ARREDONDAR( restantes',
     'mesma linha, como sai da extração do arquivo dele'),
]


def paragrafos(docx):
    """Texto em parágrafos, com o desenho das tabelas normalizado.

    O `pandoc -t plain` desenha a mesma tabela de formas diferentes conforme a origem
    (grade com +---+ ou linha simples). Sem normalizar, cada linha da tabela do
    algoritmo aparece como divergência, e a conferência vira ruído.
    """
    saida = subprocess.run(['pandoc', docx, '-t', 'plain', '--wrap=none'],
                           capture_output=True, text=True, check=True).stdout
    out = []
    for linha in saida.splitlines():
        if not linha.strip():
            continue
        if re.fullmatch(r'[\s+|=-]+', linha):      # moldura de tabela
            continue
        linha = linha.replace('|', ' ')
        linha = re.sub(r'\\(?=[|_*])', '', linha)   # escapes que vazam do markdown
        out.append(' '.join(linha.split()))
    return out


def esperada(linha):
    return any(chave in linha for chave, _ in ESPERADAS)


def main():
    referencia = sys.argv[1] if len(sys.argv) > 1 else REFERENCIA
    if not os.path.exists(referencia):
        print('referência não encontrada: %s' % referencia)
        return 1
    if not os.path.exists(NOSSO):
        print('build/artigo.docx não existe — rode o build antes.')
        return 1

    nosso, dele = paragrafos(NOSSO), paragrafos(referencia)
    sm = difflib.SequenceMatcher(None, nosso, dele, autojunk=False)

    divergencias = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        for p in nosso[i1:i2]:
            if not esperada(p):
                divergencias.append(('só no nosso', p))
        for p in dele[j1:j2]:
            if not esperada(p):
                divergencias.append(('só no dele ', p))

    print('parágrafos: %d no nosso, %d na referência' % (len(nosso), len(dele)))
    if not divergencias:
        print('TEXTO IDÊNTICO ao da revisão do orientador.')
        return 0

    print('\n%d divergência(s) de texto:\n' % len(divergencias))
    for onde, p in divergencias[:40]:
        print('  [%s] %s' % (onde, p[:150]))
    if len(divergencias) > 40:
        print('  … e mais %d' % (len(divergencias) - 40))
    print('\nCada uma precisa ser decidida: ou o .md acompanha a revisão dele, ou a')
    print('divergência é deliberada e entra em ESPERADAS, com o motivo escrito.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
