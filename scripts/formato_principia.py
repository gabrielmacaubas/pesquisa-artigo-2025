#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplica ao build/artigo.docx o que o reference-doc do pandoc não carrega:
tamanho de página A4 e as margens da Revista Principia (sup 3,5 · inf 2 · lat 2,5 cm),
extraídas do modelo oficial em docs/.

O pandoc 2.9 não copia o <w:sectPr> do reference-doc, então o documento sai em
letter com margens padrão — o que torna a contagem de páginas inútil justamente
na restrição que mais importa (12 a 18 páginas).

  python3 scripts/formato_principia.py [caminho.docx]
"""

import os
import re
import shutil
import sys
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PADRAO = os.path.join(RAIZ, 'build', 'artigo.docx')

# 1 cm = 567 twips · A4 = 21 x 29,7 cm
# Valores lidos diretamente do modelo oficial da revista,
# docs/Diretrizes_publicacao_Revista_Principia_Dez2024-OTH-1.docx (word/document.xml).
SECTPR = (
    '<w:sectPr>'
    '<w:pgSz w:w="11909" w:h="16834"/>'
    '<w:pgMar w:top="1985" w:right="1418" w:bottom="1134" w:left="1418"'
    ' w:header="720" w:footer="720" w:gutter="0"/>'
    '<w:cols w:space="720"/>'
    '</w:sectPr>'
)


def aplicar(caminho):
    if not os.path.exists(caminho):
        print(f'{caminho} não existe — rode o build antes.')
        return 1

    tmp = caminho + '.tmp'
    with zipfile.ZipFile(caminho) as zin:
        itens = [(i, zin.read(i.filename)) for i in zin.infolist()]

    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, dados in itens:
            if info.filename == 'word/document.xml':
                xml = dados.decode('utf-8')
                if re.search(r'<w:sectPr\b[^>]*/>', xml):
                    # o pandoc emite <w:sectPr /> autofechada
                    xml = re.sub(r'<w:sectPr\b[^>]*/>', SECTPR, xml)
                elif '<w:sectPr' in xml:
                    xml = re.sub(r'<w:sectPr\b.*?</w:sectPr>', SECTPR, xml, flags=re.S)
                else:
                    xml = xml.replace('</w:body>', SECTPR + '</w:body>')
                dados = xml.encode('utf-8')
            zout.writestr(info, dados)

    shutil.move(tmp, caminho)
    print('formato Principia aplicado: A4, margens 3,5/2/2,5/2,5 cm')
    return 0


if __name__ == '__main__':
    sys.exit(aplicar(sys.argv[1] if len(sys.argv) > 1 else PADRAO))
