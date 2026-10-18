#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Injeta em scripts/reference-abnt.docx os estilos que o pandoc usa e que o template
não tinha. Idempotente: rodar de novo não duplica nada.

  Legenda           título de figura, tabela e quadro — TNR 10, centralizado
  FonteIlustracao   a linha "Fonte: ..." — TNR 8, centralizado
  TituloArtigo      o título do artigo, em português e em inglês — TNR 12 negrito, que
                    é o que a revista pede e o que o orientador aplicou na revisão
  AbstractEN        o abstract e as keywords — a revista os exige em itálico
  SourceCode        bloco de pseudocódigo — monoespaçada 9, alinhado à esquerda

e corrige dois estilos que já existiam e vinham do default do pandoc:

  Figure            a imagem herdava o corpo justificado com recuo; passa a centralizada
  Table             margem de célula 0 em cima e embaixo; passa a 80 twips
  VerbatimChar      vinha em Consolas 11, fonte que não existe no Linux e cai em
                    substituta larga; passa a Liberation Mono 9, que é o que faz o
                    algoritmo caber na largura; 10 pt para acompanhar a tabela da página
  Compact           além do recuo, herdava o CORPO em 11 pt; a revista exige 10 pt
                    dentro de tabela e quadro, e foi o que o orientador aplicou
  Compact (recuo)   é o estilo do texto DENTRO da célula, e herdava o recuo de
                    primeira linha de 1 cm do corpo — o que empurrava a primeira
                    linha de cada célula para a direita e forçava quebra

Sem Legenda e FonteIlustracao, a legenda herda o corpo (TNR 11, justificado, recuo
de 1 cm) e sai desalinhada do padrão do veículo. Sem SourceCode, o pseudocódigo é
justificado como texto corrido, e o resultado é uma palavra por linha.

  python3 scripts/preparar_reference.py
"""

import os
import shutil
import sys
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(RAIZ, 'scripts', 'reference-abnt.docx')

ESTILOS = {
    'Legenda': (
        '<w:style w:type="paragraph" w:customStyle="1" w:styleId="Legenda">'
        '<w:name w:val="Legenda"/><w:basedOn w:val="Normal"/>'
        '<w:pPr><w:keepNext/>'
        '<w:spacing w:before="120" w:after="60" w:line="240" w:lineRule="auto"/>'
        '<w:ind w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
        '<w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr></w:style>'
    ),
    'FonteIlustracao': (
        '<w:style w:type="paragraph" w:customStyle="1" w:styleId="FonteIlustracao">'
        '<w:name w:val="Fonte da ilustração"/><w:basedOn w:val="Normal"/>'
        '<w:pPr>'
        '<w:spacing w:before="60" w:after="180" w:line="240" w:lineRule="auto"/>'
        '<w:ind w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
        '<w:rPr><w:sz w:val="16"/><w:szCs w:val="16"/></w:rPr></w:style>'
    ),
    'TituloArtigo': (
        '<w:style w:type="paragraph" w:customStyle="1" w:styleId="TituloArtigo">'
        '<w:name w:val="Título do artigo"/><w:basedOn w:val="Normal"/>'
        '<w:pPr><w:keepNext/>'
        '<w:spacing w:before="0" w:after="240" w:line="240" w:lineRule="auto"/>'
        '<w:ind w:firstLine="0"/><w:jc w:val="left"/></w:pPr>'
        '<w:rPr><w:b/><w:bCs/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>'
    ),
    'AbstractEN': (
        '<w:style w:type="paragraph" w:customStyle="1" w:styleId="AbstractEN">'
        '<w:name w:val="Abstract em inglês"/><w:basedOn w:val="Normal"/>'
        '<w:rPr><w:i/><w:iCs/></w:rPr></w:style>'
    ),
    'SourceCode': (
        '<w:style w:type="paragraph" w:customStyle="1" w:styleId="SourceCode">'
        '<w:name w:val="Source Code"/><w:basedOn w:val="Normal"/>'
        '<w:pPr>'
        '<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>'
        '<w:ind w:left="340" w:firstLine="0"/><w:jc w:val="left"/></w:pPr>'
        '<w:rPr><w:rFonts w:ascii="Liberation Mono" w:hAnsi="Liberation Mono"'
        ' w:cs="Liberation Mono"/><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>'
        '</w:style>'
    ),
}


def corrigir(xml):
    """Ajusta estilos que já existem no template. Idempotente."""
    mudou = []
    # a imagem entra em parágrafo de estilo Figure, que herdava Normal: justificado
    # e com recuo de 1 cm, o que empurra a figura para a direita
    alvo = ('<w:style w:type="paragraph" w:customStyle="1" w:styleId="Figure">')
    i = xml.find(alvo)
    if i >= 0:
        fim = xml.find('</w:style>', i)
        bloco = xml[i:fim]
        if '<w:pPr>' not in bloco:
            xml = (xml[:fim] + '<w:pPr><w:spacing w:before="120" w:after="0"/>'
                   '<w:ind w:firstLine="0"/><w:jc w:val="center"/></w:pPr>' + xml[fim:])
            mudou.append('Figure centralizada')
    # o run do código carrega VerbatimChar, que vence o tamanho do parágrafo
    i = xml.find('<w:style w:type="character" w:customStyle="1" w:styleId="VerbatimChar">')
    if i >= 0:
        fim = xml.find('</w:style>', i)
        bloco = xml[i:fim]
        novo = bloco.replace('<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" />',
                             '<w:rFonts w:ascii="Liberation Mono"'
                             ' w:hAnsi="Liberation Mono" w:cs="Liberation Mono" />')
        novo = novo.replace('<w:sz w:val="22" />',
                            '<w:sz w:val="20" /><w:szCs w:val="20" />')
        if novo != bloco:
            xml = xml[:i] + novo + xml[fim:]
            mudou.append('VerbatimChar em Liberation Mono 9')

    # o texto dentro da célula herdava o recuo de primeira linha do corpo
    i = xml.find('<w:style w:type="paragraph" w:customStyle="1" w:styleId="Compact">')
    if i >= 0:
        fim = xml.find('</w:style>', i)
        bloco = xml[i:fim]
        if 'w:firstLine="0"' not in bloco:
            novo = bloco.replace('<w:spacing w:before="36" w:after="36" />',
                                 '<w:spacing w:before="36" w:after="36" />'
                                 '<w:ind w:firstLine="0"/><w:jc w:val="left"/>')
            # corpo de tabela em 10 pt (sz é meio-ponto): exigência da revista
            novo = novo.replace('</w:style>', '')
            novo += '<w:rPr><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>'
            xml = xml[:i] + novo + xml[fim:]
            mudou.append('Compact sem recuo')

    # célula de tabela sem respiro em cima e embaixo
    i = xml.find('<w:style w:type="table" w:default="1" w:styleId="Table">')
    if i >= 0:
        fim = xml.find('</w:style>', i)
        bloco = xml[i:fim]
        novo = bloco.replace('<w:top w:w="0" w:type="dxa" />',
                             '<w:top w:w="80" w:type="dxa" />')
        novo = novo.replace('<w:bottom w:w="0" w:type="dxa" />',
                            '<w:bottom w:w="80" w:type="dxa" />')
        if novo != bloco:
            xml = xml[:i] + novo + xml[fim:]
            mudou.append('margem de célula')
    return xml, mudou


def aplicar(caminho=REF):
    if not os.path.exists(caminho):
        print('%s não existe' % caminho)
        return 1
    with zipfile.ZipFile(caminho) as zin:
        itens = [(i, zin.read(i.filename)) for i in zin.infolist()]

    novos = []
    tmp = caminho + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, dados in itens:
            if info.filename == 'word/styles.xml':
                xml = dados.decode('utf-8')
                for nome, bloco in ESTILOS.items():
                    if 'w:styleId="%s"' % nome not in xml:
                        xml = xml.replace('</w:styles>', bloco + '</w:styles>')
                        novos.append(nome)
                xml, ajustes = corrigir(xml)
                novos.extend(ajustes)
                dados = xml.encode('utf-8')
            zout.writestr(info, dados)
    shutil.move(tmp, caminho)
    print('reference-abnt.docx: %s' % (', '.join(novos) + ' adicionados'
                                       if novos else 'nada a fazer, já tem os três'))
    return 0


if __name__ == '__main__':
    sys.exit(aplicar())
