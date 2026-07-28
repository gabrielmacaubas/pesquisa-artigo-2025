# Orçamento de Páginas — janela de 12 a 18

## A restrição

A Revista Principia exige **no mínimo 12 e no máximo 18 páginas**, incluindo referências,
tabelas e ilustrações. **As duas pontas rejeitam**: curto demais é barrado na triagem,
longo demais também. Alvo de trabalho: **16 páginas**, com folga nas duas direções.

Verificar a cada seção escrita, nunca só no fim — descobrir o desvio na formatação final
significa desmontar argumento já revisado.

## Modelo de estimativa

Formato Principia (A4, TNR 11, **espaçamento simples**, margens 3,5/2/2,5/2,5):
área útil de 16 × 24,2 cm ≈ **700 palavras por página**.

Atenção: espaçamento simples cabe quase o dobro de um layout ABNT 1,5. Um artigo de 16
páginas aqui tem ~10.000 palavras — bem mais texto do que a contagem de páginas sugere.

| Elemento | Custo |
|---|---|
| 700 palavras | 1,0 página |
| Figura `1col`, altura `H` cm | `(H + 1,5) / 24` página |
| Figura `meia` | metade do acima |
| Tabela | `(linhas × 0,55 + 2) / 24` página |
| Referências | ≈ 5 por página (TNR 11, simples) |

`scripts/gate.py` calcula e reporta. Erro típico de ±5%.

## Distribuição alvo (~16 páginas)

Referência: o manuscrito de 2024 tem 8.495 palavras. Este precisa ser maior, porque
cobre duas frentes (persistência/API e certificação/n8n).

| Seção | Palavras | ~Páginas |
|---|---|---|
| Resumo + Abstract + palavras-chave | 550 | 0,8 |
| 1 Introdução | 1.100 | 1,6 |
| 2 Referencial teórico | 1.600 | 2,3 |
| 3 Método da pesquisa | 2.200 | 3,1 |
| 4 Resultados e discussões | 2.800 | 4,0 |
| 5 Conclusão | 700 | 1,0 |
| Financiamento + Conflito de interesses + Agradecimentos | 100 | 0,1 |
| **Subtotal texto** | **9.050** | **12,9** |
| Figuras (≈6, média 6 cm) | — | 1,9 |
| Referências (≈20) | — | 1,2 |
| **Total estimado** | | **≈16,0** |

Cada seção declara seu alvo no front matter; o gate compara com o real.

## Se faltar página (abaixo de 12)

Mais provável do que sobrar, dado o espaçamento simples. Na ordem, expanda:

1. **Resultados e discussões** — discutir cada achado à luz da literatura, que é
   exatamente o que a revista pede e o que costuma faltar.
2. **Referencial teórico** — o campo (automação de processos educacionais, low-code,
   avaliação de competências) tem literatura recente e a revista prefere ≥2019.
3. **Método** — reprodutibilidade é critério explícito da revista; detalhar o fluxo de
   decisão da regra de 2/3 e o modelo de dados agrega valor real.

Não infle com adjetivo nem com repetição do que já foi dito. Página ganha por conteúdo.

## Se passar de 18

1. **Detalhe de implementação** → pseudocódigo + link do repositório (a revista recomenda
   isso explicitamente).
2. **Referencial** que não sustenta a contribuição.
3. **Figuras redundantes** — duas que mostram o mesmo fenômeno viram uma.

Nunca corte: limitações, origem dos dados, ou a discussão dos resultados à luz da
literatura.

Se o ajuste necessário passar de ~15%, o problema é de escopo, não de redação — use
`AskUserQuestion` para o autor decidir o que entra ou sai.
