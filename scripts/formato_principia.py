#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplica ao build/artigo.docx o que o reference-doc do pandoc não carrega.

1. Tamanho de página A4 e margens da Revista Principia (sup 3,5 · inf 2 · lat 2,5 cm),
   extraídas do modelo oficial em docs/. O pandoc 2.9 não copia o <w:sectPr> do
   reference-doc, então o documento sai em letter com margens padrão — o que torna a
   contagem de páginas inútil justamente na restrição que mais importa (12 a 18).

2. Largura das tabelas. Para tabela de markdown sem largura declarada, o pandoc 2.9
   emite <w:tblW w:type="pct" w:w="0.0"/> e um <w:tblGrid/> VAZIO. O LibreOffice
   resolve isso jogando as colunas além da margem direita: na prática, some tudo
   menos a primeira coluna. Aqui a tabela recebe 100% da largura útil e uma grade
   proporcional ao conteúdo de cada coluna.

3. Identificação de autoria nas propriedades do arquivo. A submissão é duplo-cega e
   as Diretrizes mandam limpar as Propriedades do Arquivo. O pandoc já emite os campos
   vazios, mas qualquer passagem por Word ou LibreOffice grava o nome de quem salvou —
   foi o que aconteceu com o arquivo revisado pelo orientador, que chegou com
   `lastModifiedBy`. Aqui os campos de autoria são zerados de novo, sempre.

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


# largura útil do texto: A4 (21 cm) menos as margens laterais de 2,5 cm = 16 cm
LARGURA_UTIL = 9072  # twips


def _celulas_da_linha(linha_xml):
    return re.findall(r'<w:tc>.*?</w:tc>', linha_xml, re.S)


def _texto(xml):
    return ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml, re.S))


def ajustar_tabelas(xml):
    """Dá largura e grade a cada tabela, proporcional ao conteúdo das colunas."""
    ajustadas = 0

    def uma(m):
        nonlocal ajustadas
        tabela = m.group(0)
        linhas = re.findall(r'<w:tr>.*?</w:tr>', tabela, re.S)
        if not linhas:
            return tabela
        colunas = len(_celulas_da_linha(linhas[0]))
        if colunas == 0:
            return tabela

        # peso de cada coluna: o maior texto que ela precisa acomodar
        pesos = [4] * colunas          # 4 caracteres é o piso de uma coluna "#"
        for linha in linhas:
            for i, celula in enumerate(_celulas_da_linha(linha)[:colunas]):
                pesos[i] = max(pesos[i], len(_texto(celula)))
        # nenhuma coluna abaixo de 6% nem acima de 70% da largura útil
        total = float(sum(pesos))
        fracoes = [min(0.70, max(0.04, p / total)) for p in pesos]
        soma = sum(fracoes)
        larguras = [int(LARGURA_UTIL * f / soma) for f in fracoes]
        larguras[-1] += LARGURA_UTIL - sum(larguras)

        grade = '<w:tblGrid>%s</w:tblGrid>' % ''.join(
            '<w:gridCol w:w="%d"/>' % l for l in larguras)
        tabela = re.sub(r'<w:tblGrid\s*/>|<w:tblGrid>.*?</w:tblGrid>', grade,
                        tabela, count=1, flags=re.S)
        # sem tblLayout fixed o LibreOffice recalcula as colunas e ignora a grade.
        # jc=center: a tabela fica centralizada no bloco de texto, como o orientador
        # formatou na revisão de 09/10/2026
        tabela = re.sub(r'<w:tblW[^/]*/>',
                        '<w:tblW w:type="pct" w:w="5000"/>'
                        '<w:jc w:val="center"/>'
                        '<w:tblLayout w:type="fixed"/>', tabela, count=1)
        # cada célula declara a sua largura, senão o LibreOffice ignora a grade
        def celula(mc):
            i = celula.contador % colunas
            celula.contador += 1
            if '<w:tcW' in mc.group(0):
                return mc.group(0)
            return mc.group(0).replace(
                '<w:tcPr>', '<w:tcPr><w:tcW w:w="%d" w:type="dxa"/>' % larguras[i], 1)
        celula.contador = 0
        tabela = re.sub(r'<w:tc>.*?</w:tcPr>', celula, tabela, flags=re.S)
        # nenhuma linha se parte no meio. Manter a tabela inteira junta com
        # keepNext foi testado e custa uma página de espaço em branco: fica fora.
        tabela = tabela.replace('<w:trPr>', '<w:trPr><w:cantSplit/>')
        tabela = re.sub(r'<w:tr>(?!<w:trPr>)', '<w:tr><w:trPr><w:cantSplit/></w:trPr>',
                        tabela)
        # negrito só quando a primeira linha é mesmo cabeçalho: o pandoc marca essas
        # com cnfStyle firstRow. A tabela do algoritmo não tem cabeçalho, e sem essa
        # checagem o passo 1 do algoritmo saía em negrito.
        primeira = re.search(r'<w:tr>.*?</w:tr>', tabela, re.S)
        if primeira and 'w:firstRow="1"' in primeira.group(0):
            cab = primeira.group(0)
            novo_cab = re.sub(r'<w:rPr>', '<w:rPr><w:b/><w:bCs/>', cab)
            novo_cab = re.sub(r'<w:r>(?!<w:rPr>)', '<w:r><w:rPr><w:b/><w:bCs/></w:rPr>',
                              novo_cab)
            tabela = tabela.replace(cab, novo_cab, 1)
        ajustadas += 1
        return tabela


    xml = re.sub(r'<w:tbl>.*?</w:tbl>', uma, xml, flags=re.S)
    return xml, ajustadas


def monoespacada(xml_doc):
    """Garante a fonte do código por formatação direta.

    O estilo de caractere VerbatimChar declara Liberation Mono, mas o LibreOffice
    não o resolve dentro de célula de tabela e o algoritmo saía em serifada. Quem
    vence sempre é a formatação direta no run.
    """
    alvo = '<w:rStyle w:val="VerbatimChar" />'
    fonte = ('<w:rFonts w:ascii="Liberation Mono" w:hAnsi="Liberation Mono"'
             ' w:cs="Liberation Mono"/>')
    return xml_doc.replace(alvo, alvo + fonte), xml_doc.count(alvo)

def aplicar(caminho):
    if not os.path.exists(caminho):
        print(f'{caminho} não existe — rode o build antes.')
        return 1

    tmp = caminho + '.tmp'
    with zipfile.ZipFile(caminho) as zin:
        itens = [(i, zin.read(i.filename)) for i in zin.infolist()]

    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, dados in itens:
            if info.filename == 'docProps/core.xml':
                xml = dados.decode('utf-8')
                for campo in ['dc:creator', 'cp:lastModifiedBy', 'dc:title',
                              'cp:lastPrinted', 'dc:subject', 'cp:keywords',
                              'cp:category', 'dc:description']:
                    xml = re.sub(r'<%s>.*?</%s>' % (campo, campo),
                                 '<%s></%s>' % (campo, campo), xml, flags=re.S)
                    xml = re.sub(r'<%s/>' % campo, '<%s></%s>' % (campo, campo), xml)
                dados = xml.encode('utf-8')
            if info.filename == 'word/document.xml':
                xml = dados.decode('utf-8')
                if re.search(r'<w:sectPr\b[^>]*/>', xml):
                    # o pandoc emite <w:sectPr /> autofechada
                    xml = re.sub(r'<w:sectPr\b[^>]*/>', SECTPR, xml)
                elif '<w:sectPr' in xml:
                    xml = re.sub(r'<w:sectPr\b.*?</w:sectPr>', SECTPR, xml, flags=re.S)
                else:
                    xml = xml.replace('</w:body>', SECTPR + '</w:body>')
                xml, n = ajustar_tabelas(xml)
                if n:
                    print('  %d tabelas ajustadas à largura útil de 16 cm' % n)
                xml, m = monoespacada(xml)
                if m:
                    print('  %d trechos de código em monoespaçada' % m)
                dados = xml.encode('utf-8')
            zout.writestr(info, dados)

    shutil.move(tmp, caminho)
    print('formato Principia aplicado: A4, margens 3,5/2/2,5/2,5 cm')
    return 0


if __name__ == '__main__':
    sys.exit(aplicar(sys.argv[1] if len(sys.argv) > 1 else PADRAO))
