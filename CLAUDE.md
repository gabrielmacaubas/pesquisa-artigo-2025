# CLAUDE.md — Artigo 2025

Instruções para o Claude Code neste repositório. **Este projeto não tem relação com o
v1surgicalweb** — não aplique nada daquele repo aqui (Python 2.7, Django, multi-tenant).
O que foi importado de lá é só a *metodologia*: rules explícitas, gate antes de commit,
checklist de review, e comandos por etapa.

## ⚠️ Ao iniciar QUALQUER sessão, leia nesta ordem

1. Este arquivo
2. **`ESTADO.md`** — onde o projeto está agora e qual é a próxima ação
3. **`LOG.md`** — decisões já tomadas, feedback da orientadora, o que foi descartado

O autor trabalha em conversas curtas (`/clear` + um comando) e **nunca deve precisar
reexplicar o projeto**. Isso só funciona porque o estado vive nesses dois arquivos.
Ao encerrar, `/encerrar-sessao` é obrigatório.

## O que é este repositório

Produção de **um artigo científico (2025)** sobre um projeto de pesquisa de 2 anos que
gerou: automação em n8n, API hospedada em plano gratuito, geração de gráficos e
planilhas, e recomendações enviadas por e-mail. O projeto já rendeu **4 TCCs** e **1
artigo (2024)**.

Repositório **local**, sem remote — nada é enviado para GitLab/GitHub.

## Regra fundamental: nada de fato sem fonte

A falha mais cara que posso cometer é **inventar** — uma citação, um número, um nome, uma
data. Em artigo científico isso é fraude, e é indetectável na revisão porque sai fluente.

- Todo dado empírico vem de `00-contexto/mapa-de-fatos.md` ou de `docs/`. Se não está
  lá, **não escrevo** — marco `[[VERIFICAR: pergunta específica]]`.
- Toda citação precisa de entrada em `refs.md` com campo `origem` preenchido. O gate
  bloqueia sem isso.
- **Nunca** preencho lacuna com valor plausível. A lacuna explícita é o produto correto.
- Minha memória de treinamento **não é fonte**. "Sei que existe um artigo sobre isso"
  autoriza uma busca, não uma citação.

## Restrições rígidas

| Restrição | Onde é verificada |
|---|---|
| **Máximo 20 páginas** (alvo de trabalho: 18) | `gate.py`, a cada seção |
| Conteúdo e formatação separados — ABNT só no build | `.claude/rules/abnt.md` |
| Uma seção por arquivo em `secoes/` | — |
| Figuras declaradas em bloco, nunca embutidas | `.claude/rules/figuras.md` |

## Fluxo de trabalho

| Etapa | Comando | Artefato |
|---|---|---|
| 1. Ingestão do contexto | `/ingerir-contexto` | `00-contexto/mapa-de-fatos.md` |
| 2. Argumento (o "PRD") | `/definir-argumento` | `00-outline.md` |
| 3. Escrita, uma seção por vez | `/escrever-secao 03-metodologia` | `secoes/NN-*.md` |
| 4. Gate | `python3 scripts/gate.py` | — |
| 5. Review completo | `/revisar-artigo` | `build/review-<data>.md` |
| 6. Feedback da orientadora | `/aplicar-review-orientadora` | correção + entrada no `LOG.md` |
| 7. Build | `bash scripts/build.sh` | `build/artigo.docx` |
| — | `/situacao` | diz onde estamos e o que fazer |
| — | `/encerrar-sessao` | atualiza `ESTADO.md` + `LOG.md` + commit |

**Nunca pule a etapa 2.** Escrever seções antes do outline aprovado produz prosa que não
sustenta argumento — e o retrabalho é total, não incremental.

## ⚠️ Gate antes de cada commit

```bash
python3 scripts/gate.py            # 0 limpo | 1 bloqueante | 2 pendências
python3 scripts/gate.py --figuras  # lista de imagens a produzir
```

Bloqueante: citação sem entrada em `refs.md`, referência sem `origem`, bloco de figura
malformado, figura sem chamada no texto, orçamento acima de 20 páginas.
Pendência: `[[VERIFICAR]]`/`[[CIT]]`/`[[DECIDIR]]` abertos, referência órfã, desvio de
alvo de palavras. Exit 2 permite commit de rascunho, **não** permite submeter.

## Decisões: pergunte, não adivinhe

Use **`AskUserQuestion`** para tese, recorte, ordem de autoria, título, o que cortar,
comentário ambíguo da orientadora, e conflito entre fontes. 2 a 4 opções concretas com a
consequência real de cada uma, recomendada primeiro. Toda resposta vira entrada `D-<n>`
em `LOG.md` — decisão que só existe no histórico da conversa se perde no próximo
`/clear`. Detalhes em `.claude/rules/continuidade-e-decisoes.md`.

## Estrutura

```
ESTADO.md              # onde estamos AGORA (reescrito a cada sessão)
LOG.md                 # histórico append-only: decisões, reviews, descartados
PROMPT-GEMINI.md       # prompt para extrair o contexto do projeto no Gemini
00-outline.md          # tese, contribuição sobre 2024, mapa de seções, alvos
refs.md                # referências (formato machine-readable, campo `origem`)

00-contexto/           # FONTE — imutável
  contexto-projeto.md  # dump do Gemini
  mapa-de-fatos.md     # fatos extraídos, com procedência (gerado na etapa 1)
docs/                  # TCCs, artigo 2024, diretrizes do veículo (PDF/DOCX)
api-repo/              # código da API, como evidência
secoes/NN-nome.md      # o artigo, uma seção por arquivo
figuras/               # imagens finais (fig-03-1.png etc.)
scripts/gate.py        # verificação
scripts/build.py       # monta artigo.md (numera figuras, gera referências)
scripts/build.sh       # + pandoc -> .docx ABNT
build/                 # saída (gitignored)
```

## Rules

- `continuidade-e-decisoes.md` — retomada entre sessões, quando usar `AskUserQuestion`
- `escrita-academica.md` — voz, parágrafo, o que enfraquece o texto
- `fontes-e-citacoes.md` — formato de `refs.md`, autocitação dos TCCs, antifabricação
- `figuras.md` — bloco de reserva de imagem e chamada `[[@FIG:id]]`
- `orcamento-paginas.md` — teto de 20 páginas, modelo de estimativa, o que cortar
- `abnt.md` — normas e onde são aplicadas (build, não no markdown)
- `review-artigo.md` — checklist com veredito

## Pendências de ambiente

- [ ] `pandoc` não instalado (`sudo apt install pandoc`) — só na etapa 7
- [ ] `scripts/reference-abnt.docx` (template de estilos) ainda não criado
