#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prepara as figuras que vêm de artefatos reais do projeto: extrai a imagem embutida
no PDF de origem, suprime o que não pode ser publicado e grava em figuras/ com a
densidade certa para a largura de impressão desejada.

O que é suprimido, e por quê:

  nome de discente   `.claude/rules/dados-e-privacidade.md` — nenhum dado individual
                     entra no artigo, nem mesmo borrado
  IFPB, Polo de      submissão duplo-cega: o manuscrito não pode identificar a
  Inovação, cidade   instituição dos autores (`revista-principia.md`)
  nomes de servidor  idem — são pessoas identificáveis da instituição
  URL da API         `dados-e-privacidade.md` regra 4, nada de hostname em figura

As origens são documentos internos do próprio grupo (o manuscrito do ciclo anterior e
os relatórios de estágio). Nenhum dos dois é citável pela revista, e nenhum dos dois é
publicado: as imagens entram como artefato do projeto, com `Fonte: dados da pesquisa`.

  python3 scripts/figuras_reais.py
"""

import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RAIZ, 'docs')
FIGS = os.path.join(RAIZ, 'figuras')

ARTIGO_2024 = os.path.join(DOCS, 'ARTIGO - PROJETO 2024 - Versão 2.docx.pdf')
RELATORIO = os.path.join(DOCS, 'tcc_juliana.pdf')

CINZA = (232, 232, 232)
ESCURO = (45, 45, 45)
TINTA = (90, 90, 90)
FONTE = '/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf'


def extrair(pdf, pagina, indice=0):
    """Devolve a imagem embutida `indice` da `pagina` do `pdf`, sem rasterizar."""
    tmp = tempfile.mkdtemp()
    subprocess.run(['pdfimages', '-png', '-f', str(pagina), '-l', str(pagina),
                    pdf, os.path.join(tmp, 'img')], check=True)
    arquivos = sorted(f for f in os.listdir(tmp) if f.endswith('.png'))
    return Image.open(os.path.join(tmp, arquivos[indice])).convert('RGB')


def suprimir(img, caixa, rotulo=None, cor=CINZA, altura_fonte=None):
    """Tapa uma região e, se pedido, escreve por que ela foi tapada."""
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = caixa
    d.rectangle(caixa, fill=cor)
    if rotulo:
        tam = altura_fonte or max(12, int((y1 - y0) * 0.55))
        d.text(((x0 + x1) // 2, (y0 + y1) // 2), rotulo,
               font=ImageFont.truetype(FONTE, tam), fill=TINTA, anchor='mm')
    return img


def gravar(img, nome, largura_cm):
    """Grava com o dpi que faz a imagem sair exatamente com `largura_cm`."""
    dpi = round(img.width / (largura_cm / 2.54))
    caminho = os.path.join(FIGS, nome)
    img.save(caminho, dpi=(dpi, dpi))
    print('  %-18s %5dx%-5d px  %3d dpi  %4.1f x %4.1f cm'
          % (nome, img.width, img.height, dpi, largura_cm,
             largura_cm * img.height / img.width))
    if dpi < 300:
        print('     ATENCAO: abaixo dos 300 dpi exigidos pela revista')


def relatorio_de_perfil():
    """Gráfico radar e tabela de níveis, saída do fluxo de gráficos."""
    img = extrair(ARTIGO_2024, 17)
    for caixa in [(238, 12, 532, 60), (1033, 12, 1332, 60)]:
        suprimir(img, caixa, 'nome do discente suprimido')
    gravar(img, 'fig-04-1.png', 13.0)


def certificado_frente():
    img = extrair(RELATORIO, 22, 0)
    suprimir(img, (1196, 0, 1398, 180), None)
    suprimir(img, (288, 250, 1172, 312), 'instituição suprimida para avaliação cega')
    suprimir(img, (1055, 648, 1200, 680), 'cidade suprimida')
    suprimir(img, (250, 836, 552, 870), 'nome suprimido')
    gravar(img, 'fig-04-2.png', 11.5)


def certificado_verso():
    img = extrair(RELATORIO, 22, 1)
    suprimir(img, (1196, 0, 1398, 180), None)
    suprimir(img, (1055, 545, 1200, 578), 'cidade suprimida')
    suprimir(img, (300, 755, 600, 790), 'nome suprimido')
    suprimir(img, (890, 755, 1180, 790), 'nome suprimido')
    gravar(img, 'fig-04-3.png', 11.5)


def fluxo_certificacao():
    """Fluxo de emissão no n8n. Corta o vazio embaixo e tapa os endpoints."""
    img = extrair(RELATORIO, 20).crop((0, 60, 1842, 530))
    for caixa in [(176, 148, 356, 172), (366, 148, 552, 172)]:
        suprimir(img, caixa, 'endpoint suprimido', cor=ESCURO, altura_fonte=15)
    gravar(img, 'fig-03-3.png', 15.5)


if __name__ == '__main__':
    print('Figuras vindas de artefato real (origem: acervo do próprio projeto)')
    relatorio_de_perfil()
    certificado_frente()
    certificado_verso()
    fluxo_certificacao()
    sys.exit(0)
