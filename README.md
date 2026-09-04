# Artigo 2025 — automação de certificação e recomendação pedagógica

Repositório de escrita de um **artigo científico original** submetido à *Revista Principia*,
sobre o ciclo de 2025 do projeto de automação do programa **Capacitação 4.0**
(Polo de Inovação IFPB / EMBRAPII).

> **A versão atual do artigo está em [`build/`](build/).**
> `build/artigo.pdf` é o documento montado e paginado · `build/artigo.docx` é o destino de
> colagem no modelo oficial da revista · `build/artigo.md` é o markdown consolidado.
> São artefatos **gerados** — nunca edite ali. A fonte de verdade é `secoes/`.

---

## O que este repositório é

Não é um repositório de código: é um repositório de **escrita com verificação automática**.
A hipótese por trás dele é que um artigo escrito com apoio de LLM falha de um modo
específico e caro — a invenção fluente de números, citações e datas que passam despercebidas
na leitura. A resposta adotada aqui é mecânica: regras explícitas, um *gate* que roda antes
de cada commit e uma base factual única com procedência para todo dado.

A metodologia (regras versionadas, gate pré-commit, checklist de review) foi adaptada de um
repositório de engenharia. Os projetos não têm relação técnica.

## O argumento

**Tese.** A automação de um ciclo formativo não se completa na geração de indicadores de
desempenho. Ela exige a **camada de decisão** — a certificação por critério objetivo — e a
**camada de intervenção** — a recomendação pedagógica dirigida. Ambas só se sustentam sobre
persistência estruturada com rastreabilidade histórica, e não sobre planilhas.

**Contribuição sobre o ciclo anterior.** O ciclo de 2024 automatizou a produção de
indicadores a partir de planilhas, reduzindo o processamento de 40 minutos para cerca de 12
segundos por discente. Persistia a etapa que efetivamente encerra o ciclo formativo. O ciclo
de 2025 entregou:

1. Modelo de dados com rastreabilidade histórica, que torna possível a comparação
   longitudinal entre unidades avaliativas
2. A regra de certificação operacionalizada como consulta computável exposta em serviço
3. Módulo de recomendação pedagógica com envio autônomo por e-mail
4. Migração de infraestrutura, com a API em execução sem servidor

## Estrutura

```
ESTADO.md              # retrato do agora e próxima ação — leia primeiro
LOG.md                 # append-only: decisões (D-1…D-24), achados, o que foi descartado
00-outline.md          # tese, contribuição e mapa de seções
refs.md                # referências, machine-readable; o gate faz parse
secoes/                # o artigo, uma seção por arquivo — a fonte de verdade
build/                 # >>> ARTIGO MONTADO: .md, .docx e .pdf <<<
figuras/               # imagens finais (as 6 declaradas ainda não foram produzidas)
00-contexto/
  contexto-projeto.md  # dump bruto, imutável
  mapa-de-fatos.md     # base factual com procedência — todo número do artigo sai daqui
docs/                  # diretrizes da revista, manuscrito anterior, relatórios de estágio
api-repo/              # código da API e exportações dos workflows n8n (evidência)
scripts/               # gate.py, build.py, build.sh
.claude/               # regras e comandos do fluxo de escrita
```

## Fluxo de trabalho

| Etapa | Comando | Artefato |
|---|---|---|
| 1. Ingestão | `/ingerir-contexto` | `00-contexto/mapa-de-fatos.md` |
| 2. Argumento | `/definir-argumento` | `00-outline.md` |
| 3. Escrita | `/escrever-secao 03-metodo` | `secoes/NN-*.md` |
| 4. Gate | `python3 scripts/gate.py` | — |
| 5. Review | `/revisar-artigo` | `build/review-<data>.md` |
| 6. Orientadora | `/aplicar-review-orientadora` | correção + entrada no `LOG.md` |
| 7. Build | `bash scripts/build.sh` | `build/artigo.pdf` |

## O gate

```bash
python3 scripts/gate.py            # 0 limpo · 1 bloqueante · 2 pendências
python3 scripts/gate.py --figuras  # o que ainda falta produzir
python3 scripts/gate.py --estilo   # o texto parece gerado por IA?
```

**Bloqueia o commit:** citação sem entrada em `refs.md`, referência sem campo `origem`,
figura declarada e não chamada no texto (ou o inverso), primeira pessoa, acima de 18 páginas.

**Reporta como pendência:** marcadores `[[VERIFICAR]]` / `[[CIT]]` / `[[DECIDIR]]`,
referência órfã, desvio do alvo de palavras, marcadores de estilo de IA, abaixo de 12 páginas.

A checagem de estilo é calibrada empiricamente sobre o manuscrito de 2024 do próprio grupo
(331 frases): 25,4 palavras por frase, 81 por parágrafo, zero ocorrências de primeira pessoa.
O objetivo não é escrever bem em abstrato, é escrever como **estes autores** escrevem — um
artigo que destoa do texto anterior do mesmo grupo levanta suspeita em avaliação.

## Regras que valem mais que a fluência

Em `.claude/rules/`. As três que mais condicionam o resultado:

- **Nada de fato sem fonte.** Todo dado vem do mapa de fatos. Se não está lá, o texto recebe
  `[[VERIFICAR: pergunta específica]]`. Nunca um valor plausível. A lacuna explícita é o
  produto correto.
- **Nenhum dado individual de discente** em texto, tabela ou figura. A base de origem contém
  dados pessoais reais, e toda extração usada no artigo é agregada.
- **Decisões são do autor.** Escolhas de recorte, tese, título e corte não são adivinhadas:
  viram pergunta, e a resposta vira uma entrada `D-<n>` no `LOG.md`. Decisão que só existe no
  histórico de uma conversa se perde na seguinte.

## Restrições do veículo

| Restrição | Valor |
|---|---|
| Páginas | 12 a 18, incluindo referências e ilustrações (alvo 16) |
| Autores | máximo 6 |
| Submissão | PDF sem identificação de autoria, duplo-cega |
| Forma | português, impessoal |
| Normas | NBR 6023/2018 · citações NBR 10520/2023 · resumo NBR 6028 |

> "Trabalhos que não seguirem as instruções de formatação serão automaticamente rejeitados."
> Não é recomendação de estilo, é filtro pré-avaliação.

## Reproduzir o build

Requer `python3`, `pandoc` e `libreoffice`.

```bash
python3 scripts/gate.py      # tem de sair limpo
bash scripts/build.sh        # gera build/artigo.md, .docx e .pdf
bash scripts/build.sh --md   # só o markdown consolidado
```

O modelo oficial da revista (`docs/`) é o **destino de colagem** da etapa 7, não a fonte de
estilos do build: ele formata por formatação direta e tem o estilo `Normal` vazio.

## Estado

Quatro das sete seções em rascunho, gate limpo. `ESTADO.md` tem o retrato atual e a próxima
ação; `LOG.md` tem como se chegou até aqui.
