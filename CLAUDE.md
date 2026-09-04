# CLAUDE.md — Artigo 2025 (Revista Principia)

Instruções para o Claude Code neste repositório. **Sem relação com o v1surgicalweb** —
não aplique nada daquele repo aqui. O que veio de lá é só a *metodologia*: rules
explícitas, gate antes de commit, checklist de review, comandos por etapa.

## ⚠️ Ao iniciar QUALQUER sessão, leia nesta ordem

1. Este arquivo
2. **`ESTADO.md`** — onde o projeto está e qual a próxima ação
3. **`LOG.md`** — decisões tomadas (D-1…), feedback da orientadora, descartados
4. **`00-contexto/mapa-de-fatos.md`** — a base factual inteira do artigo

O autor trabalha em conversas curtas (`/clear` + um comando) e **nunca deve reexplicar o
projeto**. Ao encerrar, `/encerrar-sessao` é obrigatório.

## O artigo

Artigo original para a **Revista Principia**, sobre o ciclo 2025 do projeto de automação
do programa **Capacitação 4.0** (Polo de Inovação IFPB / EMBRAPII).

**Tese (D-1):** a automação de um ciclo formativo não se completa na geração de
indicadores; exige a camada de decisão (certificação) e a de intervenção (recomendação) —
e ambas só se sustentam sobre persistência estruturada, não sobre planilhas.

O ciclo de 2024 automatizou gráficos e planilhas. O de 2025 entregou certificação
automatizada pela regra de 2/3, recomendações pedagógicas por e-mail, API Django/DRF com
rastreabilidade histórica, e a migração Railway → Neon/Vercel.

Repositório **local**, sem remote.

## Regra fundamental: nada de fato sem fonte

Inventar um número, citação, nome ou data é a falha mais cara possível aqui — sai fluente
e passa despercebido.

- Todo dado vem de `00-contexto/mapa-de-fatos.md`. Se não está lá, marco
  `[[VERIFICAR: pergunta específica]]`. **Nunca preencho com valor plausível.**
- Toda citação tem entrada em `refs.md` com campo `origem`. O gate bloqueia sem isso.
- Minha memória de treinamento **não é fonte** — autoriza uma busca, não uma citação.

## Restrições rígidas

| Restrição | Onde é verificada |
|---|---|
| **12 a 18 páginas** (alvo 16) — as duas pontas rejeitam | `gate.py` |
| **Forma impessoal**, zero primeira pessoa | `gate.py --estilo` (bloqueante) |
| **Não parecer texto de IA** — calibrado no manuscrito de 2024 | `gate.py --estilo` |
| Submissão **duplo-cega** — nenhum nome de autor no manuscrito | review §6 |
| Máximo 6 autores (definidos 4, D-3) | — |
| **Nenhum dado pessoal de discente** em texto ou figura | `dados-e-privacidade.md` |
| Proibido citar trabalho em avaliação, slides, relatório de estágio | `fontes-e-citacoes.md` |

## Fluxo de trabalho

| Etapa | Comando | Artefato |
|---|---|---|
| 1. Ingestão | `/ingerir-contexto` | `00-contexto/mapa-de-fatos.md` ✅ parcial |
| 2. Argumento | `/definir-argumento` | `00-outline.md` ✅ |
| 3. Escrita | `/escrever-secao 03-metodo` | `secoes/NN-*.md` |
| 4. Gate | `python3 scripts/gate.py` | — |
| 5. Review | `/revisar-artigo` | `build/review-<data>.md` |
| 6. Orientadora | `/aplicar-review-orientadora` | correção + entrada no `LOG.md` |
| 7. Build | `bash scripts/build.sh` | `build/artigo.docx` |
| — | `/consultar-banco` | extração agregada do Neon |
| — | `/situacao` · `/encerrar-sessao` | retomada e fechamento |

## ⚠️ Gate antes de cada commit

```bash
python3 scripts/gate.py            # 0 limpo | 1 bloqueante | 2 pendências
python3 scripts/gate.py --figuras  # imagens a produzir
python3 scripts/gate.py --estilo   # voz: parece texto de IA?
```

**Bloqueante:** citação sem entrada em `refs.md`, referência sem `origem`, figura
malformada ou não chamada, primeira pessoa, acima de 18 páginas.
**Pendência:** `[[VERIFICAR]]`/`[[CIT]]`/`[[DECIDIR]]`, referência órfã, desvio de alvo,
marcadores de estilo de IA, abaixo de 12 páginas.

## Decisões: pergunte, não adivinhe

Use **`AskUserQuestion`** para escolhas que são do autor. Toda resposta vira `D-<n>` em
`LOG.md` — decisão que só existe na conversa se perde no próximo `/clear`.

## Estrutura

```
ESTADO.md · LOG.md          # retomada entre sessões
00-contexto/
  contexto-projeto.md       # dump do Gemini (fonte, imutável)
  mapa-de-fatos.md          # base factual com procedência ← consulte SEMPRE
docs/                       # manuscrito 2024, relatórios de estágio, diretrizes
api-repo/                   # código da API (evidência; .env NUNCA versionado)
00-outline.md · refs.md · secoes/ · figuras/
scripts/gate.py · build.py · build.sh
```

## Rules

- `revista-principia.md` — normas do veículo, prevalecem sobre tudo
- `voz-e-estilo.md` — perfil medido do grupo; como não soar como IA
- `dados-e-privacidade.md` — o banco tem CPF e nomes reais
- `fontes-e-citacoes.md` — NBR 10520/2023, o que não pode ser citado
- `orcamento-paginas.md` · `figuras.md` · `escrita-academica.md`
- `review-artigo.md` · `continuidade-e-decisoes.md`

## Ambiente (resolvido em 03/09/2026)

- ✅ `pandoc` e `libreoffice` instalados. `bash scripts/build.sh` gera `.md`, `.docx` e
  `.pdf`, reportando a contagem real de páginas
- ✅ Modelo oficial da revista: `docs/Diretrizes_publicacao_Revista_Principia_Dez2024-OTH-1.docx`.
  É o modelo **e** as diretrizes, no mesmo arquivo — foi dele que saíram as regras em
  `.claude/rules/revista-principia.md`. Serve de destino de colagem na etapa 7, **não** de
  reference-doc do pandoc (ver `ESTADO.md`)
