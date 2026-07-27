# Outline — Artigo 2025

> Preenchido pelo comando `/definir-argumento` (etapa 2). **Nenhuma seção pode ser
> escrita antes deste arquivo estar aprovado pelo autor.** Este é o "PRD" do artigo.

---

## Identificação

- **Título provisório:** [[DECIDIR]]
- **Veículo:** [[VERIFICAR: confirmar destino e suas diretrizes em `docs/`]]
- **Teto:** 20 páginas · **alvo de trabalho:** 18 · **orçamento de texto:** ~6.000 palavras
- **Pessoa verbal:** [[DECIDIR: terceira pessoa vs. primeira do plural]]

## Tese

Uma frase. A afirmação que o artigo inteiro sustenta.

> _(a definir)_

## Contribuição incremental sobre o artigo de 2024

O que existe aqui que não existia lá. **Este é o parágrafo que decide se o artigo é
publicável.** Se não for possível escrevê-lo com evidência, o problema é de resultado,
não de redação — e precisa ser resolvido antes de escrever qualquer seção.

> _(a definir)_

## Limitações declaradas

O que o estudo **não** demonstra. Declarar aqui evita que a conclusão ultrapasse os
resultados depois.

> _(a definir)_

---

## Mapa de seções

Para cada seção: função no argumento, alvo de palavras, fontes que a alimentam, figuras
previstas. Os alvos abaixo são a distribuição sugerida em
`.claude/rules/orcamento-paginas.md` — ajuste conforme o argumento escolhido, mantendo o
total em ~6.000.

| # | Arquivo | Função no argumento | Alvo | Fontes | Figuras |
|---|---|---|---|---|---|
| 00 | `secoes/00-resumo.md` | Resumo + abstract + palavras-chave (escrever **por último**) | 500 | todo o artigo | — |
| 01 | `secoes/01-introducao.md` | Problema, lacuna, tese, contribuição | 900 | mapa-de-fatos, artigo 2024 | — |
| 02 | `secoes/02-referencial.md` | Posiciona a contribuição na literatura (não prova que leu) | 1.000 | refs externas | — |
| 03 | `secoes/03-metodologia.md` | Arquitetura n8n + API + geração + envio; reprodutibilidade | 1.400 | mapa-de-fatos, `api-repo/` | diagrama de arquitetura |
| 04 | `secoes/04-resultados.md` | O que foi medido, sem interpretar | 1.200 | dados do n8n, TCCs | gráficos |
| 05 | `secoes/05-discussao.md` | Interpreta; compara com 2024; limitações | 700 | — | — |
| 06 | `secoes/06-conclusao.md` | Retoma a tese; trabalhos futuros | 500 | — | — |

## Ordem de escrita

Seções mais ancoradas em evidência primeiro; as que dependem do conjunto, por último.

1. `03-metodologia` — a mais factual, ancora o resto
2. `04-resultados`
3. `02-referencial`
4. `05-discussao`
5. `01-introducao`
6. `06-conclusao`
7. `00-resumo` — **sempre por último**

## Front matter obrigatório de cada seção

O gate lê estes campos. Toda seção começa com:

```markdown
---
secao: 03-metodologia
titulo: Metodologia
alvo_palavras: 1400
status: rascunho
---
```

`status`: `rascunho` | `revisado-autor` | `revisado-orientadora` | `final`
