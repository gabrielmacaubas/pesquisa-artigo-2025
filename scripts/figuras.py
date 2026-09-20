#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera as duas figuras vetorizáveis do artigo como PNG em 300 dpi.

Exigências da Revista Principia atendidas aqui (ver .claude/rules/figuras.md):
  - 300 dpi, gravado no cabeçalho do PNG
  - texto interno em serifada métrica do Times New Roman, nunca abaixo de 18 pt
  - nenhuma captura de tela, nenhum hostname, nenhum dado de discente

A fonte usada é a Liberation Serif, metricamente compatível com a Times New Roman
(a TNR não está instalada nesta máquina). Em 300 dpi, 18 pt = 75 px; usa-se 76.

  python3 scripts/figuras.py          # gera as duas
  python3 scripts/figuras.py 03-1     # só a de arquitetura
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGS = os.path.join(RAIZ, 'figuras')
DPI = 300
PT = DPI / 72.0
CM = DPI / 2.54

REG = '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'
BOL = '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'
CORPO = ImageFont.truetype(REG, 76)      # 18,2 pt
TITULO = ImageFont.truetype(BOL, 76)
CARD = ImageFont.truetype(REG, 76)

TINTA = (17, 17, 17)
TRACO = (34, 34, 34)
FUNDO = (255, 255, 255)
CAIXA = (242, 242, 242)

LARGURA_TRACO = 5
ALTURA_LINHA = 88
PAD_X = 46
PAD_Y = 24


def largura(texto, fonte=CORPO):
    return fonte.getbbox(texto)[2] - fonte.getbbox(texto)[0]


class Caixa(object):
    def __init__(self, linhas, fonte=CORPO, preenchida=True):
        self.linhas = linhas
        self.fonte = fonte
        self.preenchida = preenchida
        self.w = max(largura(l, fonte) for l in linhas) + 2 * PAD_X
        self.h = len(linhas) * ALTURA_LINHA + 2 * PAD_Y
        self.x = self.y = 0

    @property
    def centro(self):
        return (self.x + self.w // 2, self.y + self.h // 2)

    def desenhar(self, d):
        d.rectangle([self.x, self.y, self.x + self.w, self.y + self.h],
                    fill=CAIXA if self.preenchida else FUNDO,
                    outline=TRACO, width=LARGURA_TRACO)
        y = self.y + PAD_Y
        for linha in self.linhas:
            d.text((self.x + self.w // 2, y + ALTURA_LINHA // 2), linha,
                   font=self.fonte, fill=TINTA, anchor='mm')
            y += ALTURA_LINHA


def fileira(caixas, x0, x1, y, folga=70):
    """Distribui as caixas centradas na horizontal entre x0 e x1."""
    total = sum(c.w for c in caixas)
    n = len(caixas) - 1
    g = folga if n == 0 else min(folga, max(24, ((x1 - x0) - total) // max(n, 1)))
    largura_total = total + g * n
    x = x0 + ((x1 - x0) - largura_total) // 2
    for c in caixas:
        c.x, c.y = x, y
        x += c.w + g
    if largura_total > (x1 - x0):
        print('  ⚠️  fileira em y=%d estourou %d px' % (y, largura_total - (x1 - x0)))
    return caixas


def seta(d, p1, p2, rotulo=None, dupla=False):
    d.line([p1, p2], fill=TRACO, width=LARGURA_TRACO)
    for origem, destino in ([(p1, p2)] if not dupla else [(p1, p2), (p2, p1)]):
        cabeca(d, origem, destino)
    if rotulo:
        mx, my = (p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2
        desloca = (0, -56) if p1[1] == p2[1] else (74, 0)
        d.text((mx + desloca[0], my + desloca[1]), rotulo,
               font=CARD, fill=TINTA, anchor='mm')


def cabeca(d, origem, destino, tam=38):
    import math
    ang = math.atan2(destino[1] - origem[1], destino[0] - origem[0])
    pontos = [destino]
    for giro in (2.6, -2.6):
        pontos.append((destino[0] + tam * math.cos(ang + giro),
                       destino[1] + tam * math.sin(ang + giro)))
    d.polygon(pontos, fill=TRACO)


def tela(largura_cm, altura_cm):
    img = Image.new('RGB', (int(largura_cm * CM), int(altura_cm * CM)), FUNDO)
    return img, ImageDraw.Draw(img)


def salvar(img, nome):
    caminho = os.path.join(FIGS, nome)
    img.save(caminho, dpi=(DPI, DPI))
    print('  %s — %dx%d px, %d dpi' % (nome, img.width, img.height, DPI))


# --- FIG:03-1 arquitetura ----------------------------------------------------
def arquitetura():
    print('FIG:03-1 arquitetura')
    img, d = tela(16, 8)
    W, H = img.width, img.height
    x0, x1 = 340, W - 40

    faixas = [
        ('Entrada', [Caixa(['Formulário de', 'autoavaliação']),
                     Caixa(['Planilha de', 'respostas'])]),
        ('Fluxos', [Caixa(['Quatro fluxos no n8n em contêiner'])]),
        ('Núcleo', [Caixa(['API Django e DRF']), Caixa(['PostgreSQL'])]),
        ('Saída', [Caixa(['Planilhas e', 'gráficos']),
                   Caixa(['Certificados', 'em PDF']),
                   Caixa(['Mensagens', 'de e-mail'])]),
    ]

    alturas = [max(c.h for c in cs) for _, cs in faixas]
    vao = (H - sum(alturas) - 60) // (len(faixas) - 1)
    y, posicoes = 30, []
    for (rotulo, caixas), alt in zip(faixas, alturas):
        fileira(caixas, x0, x1, y, folga=110)
        d.text((40, y + alt // 2), rotulo, font=TITULO, fill=TINTA, anchor='lm')
        for c in caixas:
            c.desenhar(d)
        posicoes.append((y, alt, caixas))
        y += alt + vao

    a, b = faixas[0][1]
    seta(d, (a.x + a.w + 14, a.centro[1]), (b.x - 14, b.centro[1]))
    a, b = faixas[2][1]
    seta(d, (a.x + a.w + 14, a.centro[1]), (b.x - 14, b.centro[1]), dupla=True)

    # a orquestração lê a planilha de respostas, não o formulário
    saida = {0: -1}
    for i in range(len(posicoes) - 1):
        de = posicoes[i][2][saida.get(i, 0)]
        para = posicoes[i + 1][2][0]
        x = min(de.centro[0], para.centro[0])
        seta(d, (x, de.y + de.h + 10), (x, para.y - 10))

    salvar(img, 'fig-03-1.png')


# --- FIG:03-2 modelo de dados ------------------------------------------------
def modelo():
    print('FIG:03-2 modelo de dados')
    img, d = tela(16, 9)
    W, H = img.width, img.height

    mentor, projeto, macro = Caixa(['Mentor']), Caixa(['Projeto']), Caixa(['Competência macro'])
    discente, vinculo, sub = Caixa(['Discente']), Caixa(['Vínculo']), Caixa(['Subcompetência'])
    aval, nota = Caixa(['Autoavaliação']), Caixa(['Nota'])

    COL = {'e': 300, 'm': 900, 'd': 1440}
    linhas = {1: 30, 2: 30 + 136 + 190, 3: 30 + 2 * (136 + 190)}

    def por(caixa, coluna, linha):
        caixa.x = COL[coluna] - caixa.w // 2
        caixa.y = linhas[linha]
        return caixa

    por(mentor, 'e', 1); por(projeto, 'm', 1); por(macro, 'd', 1)
    por(discente, 'e', 2); por(vinculo, 'm', 2); por(sub, 'd', 2)
    por(aval, 'e', 3); por(nota, 'd', 3)

    for c in (mentor, projeto, macro, discente, vinculo, sub, aval, nota):
        c.desenhar(d)

    def h_seta(a, b):
        seta(d, (a.x + a.w + 14, a.centro[1]), (b.x - 14, b.centro[1]), '1:N')

    def v_seta(a, b):
        x = min(a.centro[0], b.centro[0])
        seta(d, (x, a.y + a.h + 10), (x, b.y - 10), '1:N')

    h_seta(mentor, projeto)
    v_seta(projeto, vinculo)
    h_seta(discente, vinculo)
    v_seta(discente, aval)
    h_seta(aval, nota)
    v_seta(macro, sub)
    v_seta(sub, nota)

    # competência macro alimenta nota diretamente, contornando pela direita
    desvio = W - 60
    ym, yn = macro.centro[1], nota.centro[1]
    d.line([(macro.x + macro.w + 14, ym), (desvio, ym)], fill=TRACO, width=LARGURA_TRACO)
    d.line([(desvio, ym), (desvio, yn)], fill=TRACO, width=LARGURA_TRACO)
    seta(d, (desvio, yn), (nota.x + nota.w + 14, yn), '1:N')

    rodape = ['Todas as entidades guardam data e usuário de criação e de',
              'atualização. Chaves estrangeiras com restrição de proteção.']
    y = H - 30 - len(rodape) * ALTURA_LINHA
    for linha in rodape:
        d.text((W // 2, y + ALTURA_LINHA // 2), linha, font=CORPO, fill=TINTA, anchor='mm')
        y += ALTURA_LINHA

    salvar(img, 'fig-03-2.png')


# --- FIG:04-1 gráfico de perfil ----------------------------------------------
def perfil():
    """Radar de perfil, com dados SINTÉTICOS — nenhuma nota real de discente."""
    import math
    print('FIG:04-1 gráfico de perfil (dados sintéticos)')
    img, d = tela(16, 9)
    W, H = img.width, img.height

    cx, cy, raio = W // 2, 470, 360
    eixos = 7
    # dados sintéticos, declarados como tal na legenda e no corpo do artigo
    series = [('Unidade 1', [2, 1, 2, 3, 1, 2, 2], (120, 120, 120), 6),
              ('Unidade 2', [3, 2, 2, 4, 3, 3, 2], (17, 17, 17), 9)]

    def ponto(i, valor):
        ang = -math.pi / 2 + 2 * math.pi * i / eixos
        r = raio * valor / 4.0
        return (cx + r * math.cos(ang), cy + r * math.sin(ang))

    for anel in (1, 2, 3, 4):
        d.polygon([ponto(i, anel) for i in range(eixos)],
                  outline=(176, 176, 176), width=3)
    for i in range(eixos):
        d.line([(cx, cy), ponto(i, 4)], fill=(176, 176, 176), width=3)
        rotulo = ponto(i, 4.55)
        d.text(rotulo, str(i + 1), font=TITULO, fill=TINTA, anchor='mm')
    # escala à esquerda, na direção em que não há eixo, para não colidir com os
    # números das competências
    for anel in (2, 4):
        d.text((cx - raio * anel / 4.0 - 46, cy), str(anel), font=CORPO,
               fill=(90, 90, 90), anchor='mm')

    for _, valores, cor, esp in series:
        d.polygon([ponto(i, v) for i, v in enumerate(valores)], outline=cor, width=esp)

    y = H - 150
    x = 300
    for nome, _, cor, esp in series:
        d.line([(x, y), (x + 150, y)], fill=cor, width=esp)
        d.text((x + 180, y), nome, font=CORPO, fill=TINTA, anchor='lm')
        x += 620
    d.text((W // 2, H - 60), 'Escala de 0 a 4 · eixos numerados conforme o Quadro 1',
           font=CORPO, fill=TINTA, anchor='mm')

    salvar(img, 'fig-04-1.png')


# --- FIG:04-2 produtos das duas camadas --------------------------------------
def produtos():
    """Certificado e mensagem de recomendação, ambos SINTÉTICOS."""
    print('FIG:04-2 produtos das camadas (exemplos sintéticos)')
    img, d = tela(16, 7)
    W, H = img.width, img.height
    margem, vao = 30, 60
    largura = (W - 2 * margem - vao) // 2
    topo, altura = 30, H - 60

    def painel(x, titulo, linhas, centralizado=False):
        d.rectangle([x, topo, x + largura, topo + altura], fill=FUNDO,
                    outline=TRACO, width=LARGURA_TRACO)
        d.rectangle([x, topo, x + largura, topo + 130], fill=CAIXA,
                    outline=TRACO, width=LARGURA_TRACO)
        d.text((x + largura // 2, topo + 65), titulo, font=TITULO, fill=TINTA,
               anchor='mm')
        y = topo + 190
        for linha, destaque in linhas:
            fonte = TITULO if destaque else CORPO
            if centralizado:
                d.text((x + largura // 2, y), linha, font=fonte, fill=TINTA, anchor='mm')
            else:
                d.text((x + 40, y), linha, font=fonte, fill=TINTA, anchor='lm')
            y += ALTURA_LINHA

    painel(margem, 'CERTIFICADO', [
        ('Certificamos que', False),
        ('A. B. C. (nome fictício)', True),
        ('participou do programa', False),
        ('Capacitação 4.0, com', False),
        ('cinco unidades avaliadas.', False),
    ], centralizado=True)

    painel(margem + largura + vao, 'RECOMENDAÇÃO', [
        ('Competência: liderança', False),
        ('Motivo: queda em relação', False),
        ('à unidade anterior', False),
        ('Prática sugerida: conduzir', False),
        ('uma reunião de equipe do', False),
        ('projeto e relatar o', False),
        ('resultado ao mentor.', False),
    ])

    salvar(img, 'fig-04-2.png')


if __name__ == '__main__':
    alvo = sys.argv[1] if len(sys.argv) > 1 else 'todas'
    if alvo in ('todas', '03-1'):
        arquitetura()
    if alvo in ('todas', '03-2'):
        modelo()
    if alvo in ('todas', '04-1'):
        perfil()
    if alvo in ('todas', '04-2'):
        produtos()
