#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gate de verificação do artigo — espelha o papel do static_analysis.sh do v1surgicalweb.

Verifica, sobre secoes/*.md e refs.md:
  1. citações no texto sem entrada em refs.md          -> BLOQUEANTE
  2. entradas de refs.md sem campo 'origem'            -> BLOQUEANTE (presumir invenção)
  3. blocos de figura malformados                      -> BLOQUEANTE
  4. figura sem chamada no texto / chamada sem figura  -> BLOQUEANTE
  5. orçamento de páginas acima do teto (20)           -> BLOQUEANTE
  6. referências órfãs (nunca citadas)                 -> pendência
  7. placeholders [[VERIFICAR]] / [[CIT]] / [[DECIDIR]] -> pendência
  8. desvio do alvo de palavras da seção               -> pendência

Exit: 0 limpo | 1 bloqueante | 2 apenas pendências

Uso:
  python3 scripts/gate.py             # verificação completa
  python3 scripts/gate.py --figuras   # só a lista de imagens a produzir
  python3 scripts/gate.py --estilo    # só a checagem de voz (parecer texto de IA)
"""

import os
import re
import sys
from collections import OrderedDict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECOES = os.path.join(RAIZ, 'secoes')
REFS = os.path.join(RAIZ, 'refs.md')

TETO_PAGINAS = 18.0
MIN_PAGINAS = 12.0
ALVO_PAGINAS = 16.0
PALAVRAS_POR_PAGINA = 700.0
CM_POR_PAGINA = 24.0
FOLGA_LEGENDA_CM = 1.5

CAMPOS_FIG = ['tipo', 'status', 'origem', 'dados', 'descricao',
              'legenda', 'largura', 'altura_cm', 'arquivo']
STATUS_FIG = ['criar', 'reutilizar', 'pronto']

# --- perfil de estilo do grupo, medido no manuscrito de 2024 -----------------
ALVO_PALAVRAS_FRASE = (21.0, 30.0)      # media do grupo: 25,4
ALVO_PALAVRAS_PARAGRAFO = (60.0, 105.0)  # media do grupo: 81
CONECTIVOS_PROIBIDOS = [
    'Ademais', 'Outrossim', 'Nesse sentido', 'Cumpre destacar', 'Vale salientar',
    'Vale ressaltar', 'Vale destacar', 'Por conseguinte', 'Destarte', 'Em suma',
    'Em síntese', 'É importante ressaltar', 'É importante notar', 'Cabe destacar',
]
LEXICO_SUSPEITO = [
    'robusto', 'robusta', 'abrangente', 'holístic', 'poderos', 'revolucionári',
    'aprofundar-se', 'mergulh', 'panorama', 'cenário atual', 'na era digital',
    'desempenha um papel', 'de suma importância', 'amplamente reconhecid',
]
PRIMEIRA_PESSOA = r'\b(realizamos|utilizamos|desenvolvemos|apresentamos|observamos|nossa|nosso|nossos|nossas)\b'

# --- padrões -----------------------------------------------------------------
# refs.md:  ## [SILVA, 2020]
RE_REF_CHAVE = re.compile(r'^##\s*\[([^\],]+),\s*(\d{4}[a-z]?)\]', re.M)
RE_REF_CAMPO = re.compile(r'^-\s*\*\*(\w+):\*\*\s*(.*)$', re.M)

# citação entre parênteses: (SILVA, 2020) (SILVA; COSTA, 2020) (SILVA et al., 2020)
# nome de autor pessoal (Silva, Costa Junior) ou institucional (Django Software Foundation)
# dígitos são aceitos no nome: sem isso, autores como (N8n, 2025) não casam e a
# citação escapa da verificação em silêncio, em vez de ser cobrada.
# hífen e apóstrofo fazem parte de sobrenomes reais (Al-Sa'di, Costa-Lima): sem eles
# a citação não casa e escapa da verificação em silêncio.
_NOME = (r"[A-ZÁÂÃÉÊÍÓÔÕÚÇ][A-Za-zÀ-ÿ0-9.\-'’]+"
         r"(?:\s+(?:de|da|do|dos|das)?\s*[A-ZÁÂÃÉÊÍÓÔÕÚÇ][A-Za-zÀ-ÿ0-9.\-'’]+){0,3}")
RE_CIT_PAREN = re.compile(r'\((' + _NOME + r'(?:\s*;\s*' + _NOME + r')*)'
                          r'(?:\s+et\s+al\.)?,\s*(\d{4}[a-z]?)'
                          r'(?:,\s*p\.\s*[\d\u2013\-]+)?\)')
# citação narrativa: Silva (2020) / Silva e Costa (2020) / Silva, Costa e Lima (2020)
# / Silva et al. (2020). A cadeia intermediária precisa ser consumida pelo mesmo match:
# sem ela, "Silva, Costa e Lima (2020)" casa a partir de "Costa", e o gate cobra uma
# entrada em nome do segundo autor.
_NOME_NARR = r"[A-ZÁÂÃÉÊÍÓÔÕÚÇ][A-Za-zÀ-ÿ\-'’]+"
RE_CIT_NARR = re.compile(r"\b(" + _NOME_NARR + r")"
                         r"(?:\s*,\s*" + _NOME_NARR + r")*"
                         r"(?:\s+(?:e|et\s+al\.)\s*(?:" + _NOME_NARR + r")?)?"
                         r"\s*\((\d{4}[a-z]?)\)")

RE_FIG_BLOCO = re.compile(r'\[\[(FIG|TAB):([\w\-]+)\s*\n(.*?)\]\]', re.S)
RE_FIG_REF = re.compile(r'\[\[@(FIG|TAB):([\w\-]+)\]\]')
RE_FIG_ABERTO = re.compile(r'\[\[(FIG|TAB):([\w\-]+)')

RE_PLACEHOLDER = re.compile(r'\[\[(VERIFICAR|CIT|DECIDIR)(:[^\]]*)?\]\]')
RE_FRONTMATTER = re.compile(r'\A---\s*\n(.*?)\n---\s*\n', re.S)

bloqueantes = []
pendencias = []


def erro(msg):
    bloqueantes.append(msg)


def aviso(msg):
    pendencias.append(msg)


def ler(caminho):
    with open(caminho, encoding='utf-8') as fh:
        return fh.read()


def sem_codigo(texto):
    """Remove blocos de código e blocos de figura antes de procurar citações."""
    texto = re.sub(r'```.*?```', '', texto, flags=re.S)
    texto = re.sub(r'`[^`]*`', '', texto)
    texto = RE_FIG_BLOCO.sub('', texto)
    return texto


def linha_de(texto, pos):
    return texto.count('\n', 0, pos) + 1


# --- refs.md -----------------------------------------------------------------
def carregar_refs():
    if not os.path.exists(REFS):
        erro('refs.md não existe')
        return {}
    bruto = ler(REFS)
    chaves = OrderedDict()
    marcas = list(RE_REF_CHAVE.finditer(bruto))
    for i, m in enumerate(marcas):
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(bruto)
        corpo = bruto[m.start():fim]
        campos = dict(RE_REF_CAMPO.findall(corpo))
        chave = (m.group(1).strip().upper(), m.group(2))
        chaves[chave] = campos
        origem = campos.get('origem', '').strip()
        if not origem or origem.lower() in ('', 'tbd', '?', '[[verificar]]'):
            erro('refs.md:%d [%s, %s] sem campo `origem` verificável '
                 '(referência sem procedência é tratada como inventada)'
                 % (linha_de(bruto, m.start()), m.group(1), m.group(2)))
    return chaves


# --- seções ------------------------------------------------------------------
def carregar_secoes():
    if not os.path.isdir(SECOES):
        return []
    nomes = sorted(n for n in os.listdir(SECOES) if n.endswith('.md'))
    return [(n, ler(os.path.join(SECOES, n))) for n in nomes]


def frontmatter(texto):
    m = RE_FRONTMATTER.search(texto)
    if not m:
        return {}
    dados = {}
    for linha in m.group(1).splitlines():
        if ':' in linha:
            k, v = linha.split(':', 1)
            dados[k.strip()] = v.strip()
    return dados


def contar_palavras(texto):
    corpo = RE_FRONTMATTER.sub('', texto)
    corpo = sem_codigo(corpo)
    corpo = RE_PLACEHOLDER.sub('', corpo)
    corpo = RE_FIG_REF.sub('', corpo)
    corpo = re.sub(r'^#{1,6}\s.*$', '', corpo, flags=re.M)
    return len([p for p in re.split(r'\s+', corpo) if p.strip()])


# --- verificações ------------------------------------------------------------
def checar_citacoes(secoes, refs):
    citadas = set()
    for nome, texto in secoes:
        corpo = sem_codigo(RE_FRONTMATTER.sub('', texto))
        achados = []
        for m in RE_CIT_PAREN.finditer(corpo):
            primeiro = re.split(r'[;,]', m.group(1))[0].strip().upper()
            achados.append((primeiro, m.group(2), m.start(), m.group(0)))
        for m in RE_CIT_NARR.finditer(corpo):
            achados.append((m.group(1).strip().upper(), m.group(2),
                            m.start(), m.group(0)))
        for autor, ano, pos, bruto in achados:
            chave = (autor, ano)
            if chave in refs:
                citadas.add(chave)
            else:
                erro('%s:%d citação %s sem entrada em refs.md'
                     % (nome, linha_de(corpo, pos), bruto.strip()))
    for chave in refs:
        if chave not in citadas:
            aviso('refs.md [%s, %s] nunca é citada no texto (órfã)' % chave)


def checar_figuras(secoes):
    """Retorna lista de (secao, tipo, id, campos) das figuras declaradas."""
    figuras = []
    refs_inline = set()
    for nome, texto in secoes:
        for m in RE_FIG_REF.finditer(texto):
            refs_inline.add((m.group(1), m.group(2)))
        ids_bloco = set()
        for m in RE_FIG_BLOCO.finditer(texto):
            tipo, ident, corpo = m.group(1), m.group(2), m.group(3)
            campos = {}
            for linha in corpo.splitlines():
                if ':' in linha:
                    k, v = linha.split(':', 1)
                    campos[k.strip()] = v.strip()
            faltando = [c for c in CAMPOS_FIG if not campos.get(c)]
            if faltando:
                erro('%s:%d [[%s:%s]] sem campos obrigatórios: %s'
                     % (nome, linha_de(texto, m.start()), tipo, ident,
                        ', '.join(faltando)))
            if campos.get('status') and campos['status'] not in STATUS_FIG:
                erro('%s:%d [[%s:%s]] status inválido "%s" (use: %s)'
                     % (nome, linha_de(texto, m.start()), tipo, ident,
                        campos['status'], '|'.join(STATUS_FIG)))
            if campos.get('legenda') and 'Fonte:' not in campos['legenda']:
                erro('%s:%d [[%s:%s]] legenda sem "Fonte:"'
                     % (nome, linha_de(texto, m.start()), tipo, ident))
            ids_bloco.add((tipo, ident))
            figuras.append((nome, tipo, ident, campos))
        # bloco aberto e nunca fechado
        abertos = len(RE_FIG_ABERTO.findall(texto)) - len(RE_FIG_REF.findall(texto))
        if abertos > len(ids_bloco):
            erro('%s: bloco [[FIG:...]] aberto sem "]]" de fechamento' % nome)

    declaradas = {(t, i) for _, t, i, _ in figuras}
    for tipo, ident in sorted(declaradas - refs_inline):
        erro('[[%s:%s]] declarada mas nunca chamada no texto '
             '(use [[@%s:%s]] no parágrafo que a referencia)'
             % (tipo, ident, tipo, ident))
    for tipo, ident in sorted(refs_inline - declaradas):
        erro('[[@%s:%s]] chamada no texto mas sem bloco de declaração'
             % (tipo, ident))
    return figuras


def checar_placeholders(secoes):
    for nome, texto in secoes:
        for m in RE_PLACEHOLDER.finditer(texto):
            detalhe = (m.group(2) or '').lstrip(':').strip()
            aviso('%s:%d [[%s]] %s' % (nome, linha_de(texto, m.start()),
                                       m.group(1), detalhe))
        for m in re.finditer(r'\b(TODO|FIXME|XXX)\b', texto):
            aviso('%s:%d marcador %s pendente'
                  % (nome, linha_de(texto, m.start()), m.group(1)))


def orcamento(secoes, figuras, refs):
    total_palavras = 0
    linhas = []
    for nome, texto in secoes:
        fm = frontmatter(texto)
        palavras = contar_palavras(texto)
        total_palavras += palavras
        alvo = fm.get('alvo_palavras')
        if alvo and alvo.isdigit():
            alvo_n = int(alvo)
            desvio = (palavras - alvo_n) / float(alvo_n) if alvo_n else 0
            marca = '  ' if abs(desvio) <= 0.15 else '!!'
            if abs(desvio) > 0.15:
                aviso('%s: %d palavras vs alvo %d (%+.0f%%)'
                      % (nome, palavras, alvo_n, desvio * 100))
            linhas.append('  %s %-32s %5d / %5d' % (marca, nome, palavras, alvo_n))
        else:
            linhas.append('     %-32s %5d /     ?' % (nome, palavras))
            aviso('%s: sem `alvo_palavras` no front matter' % nome)

    pag_texto = total_palavras / PALAVRAS_POR_PAGINA
    pag_fig = 0.0
    for _, _, _, campos in figuras:
        try:
            altura = float(str(campos.get('altura_cm', '0')).replace(',', '.'))
        except ValueError:
            altura = 0.0
        custo = (altura + FOLGA_LEGENDA_CM) / CM_POR_PAGINA
        if campos.get('largura') == 'meia':
            custo /= 2.0
        pag_fig += custo
    pag_refs = len(refs) / 5.0
    total = pag_texto + pag_fig + pag_refs

    print('\n── Orçamento de páginas ' + '─' * 40)
    for l in linhas:
        print(l)
    print('     %-32s %5d palavras' % ('TOTAL TEXTO', total_palavras))
    print('')
    print('     texto ......... %5.1f pág' % pag_texto)
    print('     figuras (%d) ... %5.1f pág' % (len(figuras), pag_fig))
    print('     referências ... %5.1f pág' % pag_refs)
    print('     ' + '-' * 30)
    print('     ESTIMADO ...... %5.1f pág   (janela %.0f-%.0f | alvo %.0f)'
          % (total, MIN_PAGINAS, TETO_PAGINAS, ALVO_PAGINAS))

    if total < MIN_PAGINAS and total > 1.0:
        aviso('abaixo do mínimo da revista: %.1f pág, exigido %.0f '
              '(faltam ~%d palavras)'
              % (total, MIN_PAGINAS,
                 int((ALVO_PAGINAS - total) * PALAVRAS_POR_PAGINA)))
    if total > TETO_PAGINAS:
        erro('orçamento estourado: %.1f páginas estimadas, teto é %.0f '
             '(cortar ~%d palavras)'
             % (total, TETO_PAGINAS,
                int((total - ALVO_PAGINAS) * PALAVRAS_POR_PAGINA)))
    elif total > ALVO_PAGINAS:
        aviso('orçamento em %.1f pág — acima do alvo de %.0f, sem folga para revisão'
              % (total, ALVO_PAGINAS))


def checar_estilo(secoes):
    print('\n── Voz e estilo ' + '─' * 48)
    print('   (perfil do grupo em 2024: %.0f-%.0f palavras/frase, %.0f-%.0f/parágrafo)'
          % (ALVO_PALAVRAS_FRASE + ALVO_PALAVRAS_PARAGRAFO))
    for nome, texto in secoes:
        corpo = sem_codigo(RE_FRONTMATTER.sub('', texto))
        corpo = RE_PLACEHOLDER.sub('', RE_FIG_REF.sub('', corpo))
        corpo = re.sub(r'^#{1,6}\s.*$', '', corpo, flags=re.M)

        frases = [f for f in re.split(r'(?<=[.!?])\s+', corpo) if len(f.split()) > 3]
        # parágrafo = bloco separado por linha em branco. Dividir por '\n' faria
        # qualquer arquivo com quebra de linha fixa reportar 0,0 e pular a checagem.
        paras = [p for p in re.split(r'\n\s*\n', corpo) if len(p.split()) > 25]
        if not frases:
            continue
        mf = sum(len(f.split()) for f in frases) / float(len(frases))
        mp = (sum(len(p.split()) for p in paras) / float(len(paras))) if paras else 0.0
        print('   %-30s %4.1f pal/frase   %5.1f pal/parágrafo  (%d frases)'
              % (nome, mf, mp, len(frases)))

        if mf < ALVO_PALAVRAS_FRASE[0]:
            aviso('%s: frases curtas demais (%.1f pal) — o grupo escreve ~25; '
                  'texto picotado é marcador de geração automática' % (nome, mf))
        elif mf > ALVO_PALAVRAS_FRASE[1]:
            aviso('%s: frases longas demais (%.1f pal) mesmo para o padrão do grupo'
                  % (nome, mf))
        if paras and mp < ALVO_PALAVRAS_PARAGRAFO[0]:
            aviso('%s: parágrafos curtos demais (%.0f pal) — o grupo escreve ~81'
                  % (nome, mp))

        for c in CONECTIVOS_PROIBIDOS:
            for m in re.finditer(r'\b' + c, corpo, re.I):
                aviso('%s:%d conectivo "%s" não é usado pelo grupo (marcador de IA)'
                      % (nome, linha_de(corpo, m.start()), c))
        for t in LEXICO_SUSPEITO:
            for m in re.finditer(t, corpo, re.I):
                aviso('%s:%d léxico suspeito "%s" — ausente no texto de 2024'
                      % (nome, linha_de(corpo, m.start()), m.group(0)))
        for m in re.finditer(PRIMEIRA_PESSOA, corpo, re.I):
            erro('%s:%d "%s" — a revista exige forma impessoal'
                 % (nome, linha_de(corpo, m.start()), m.group(0)))
        for m in re.finditer(r'\s—\s[^—\n]{3,60}\s—\s', corpo):
            aviso('%s:%d travessão duplo (aposto) — hábito de LLM; use vírgula'
                  % (nome, linha_de(corpo, m.start())))
        for m in re.finditer(r'\b(\w+),\s+(\w+)\s+e\s+(\w+)\b', corpo):
            if all(len(g) > 5 for g in m.groups()):
                aviso('%s:%d possível tríade "%s" — enumerar em três é reflexo de LLM'
                      % (nome, linha_de(corpo, m.start()), m.group(0)[:45]))
        for m in re.finditer(r'^\s*[-*•]\s+', corpo, re.M):
            aviso('%s:%d lista no corpo — o texto de 2024 é prosa corrida'
                  % (nome, linha_de(corpo, m.start())))


def listar_figuras(figuras):
    if not figuras:
        print('Nenhuma figura declarada ainda.')
        return
    print('\n── Imagens a produzir ' + '─' * 42)
    for estado in STATUS_FIG:
        grupo = [f for f in figuras if f[3].get('status') == estado]
        if not grupo:
            continue
        print('\n  [%s]' % estado.upper())
        for nome, tipo, ident, campos in grupo:
            print('    %s:%-8s  %-18s %s'
                  % (tipo, ident, campos.get('tipo', '?'),
                     campos.get('descricao', '')[:60]))
            print('        origem: %s' % campos.get('origem', '?'))
            print('        arquivo: %s   (%s, %scm)'
                  % (campos.get('arquivo', '?'), campos.get('largura', '?'),
                     campos.get('altura_cm', '?')))


def main():
    so_figuras = '--figuras' in sys.argv
    so_estilo = '--estilo' in sys.argv
    refs = carregar_refs()
    secoes = carregar_secoes()

    if not secoes:
        print('Nenhuma seção em secoes/ ainda — nada a verificar.')
        return 0

    figuras = checar_figuras(secoes)

    if so_figuras:
        listar_figuras(figuras)
        return 0

    if so_estilo:
        checar_estilo(secoes)
        for p in pendencias:
            print('  🟡 %s' % p)
        for b in bloqueantes:
            print('  🔴 %s' % b)
        return 1 if bloqueantes else (2 if pendencias else 0)

    checar_citacoes(secoes, refs)
    checar_placeholders(secoes)
    orcamento(secoes, figuras, refs)
    checar_estilo(secoes)
    listar_figuras(figuras)

    if bloqueantes:
        print('\n── BLOQUEANTE (%d) ' % len(bloqueantes) + '─' * 43)
        for b in bloqueantes:
            print('  🔴 %s' % b)
    if pendencias:
        print('\n── Pendências (%d) ' % len(pendencias) + '─' * 44)
        for p in pendencias:
            print('  🟡 %s' % p)

    print('')
    if bloqueantes:
        print('GATE: FALHOU — %d bloqueante(s), %d pendência(s)'
              % (len(bloqueantes), len(pendencias)))
        return 1
    if pendencias:
        print('GATE: OK com %d pendência(s) — pode commitar rascunho, '
              'não pode submeter' % len(pendencias))
        return 2
    print('GATE: LIMPO')
    return 0


if __name__ == '__main__':
    sys.exit(main())
