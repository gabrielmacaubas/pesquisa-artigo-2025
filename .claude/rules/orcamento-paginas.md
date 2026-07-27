# Orçamento de Páginas — teto rígido de 20

## A restrição

O artigo **não pode passar de 20 páginas** formatadas. Isso não é meta, é teto. Se as
diretrizes do veículo (`docs/`) impuserem limite menor, o menor prevalece — registre em
`ESTADO.md`.

Estourar o limite é caro no pior momento: você descobre na formatação final, quando cortar
significa desmontar argumento já revisado. Por isso o orçamento é verificado a **cada
seção escrita**, não no fim.

## Modelo de estimativa

Base ABNT (Arial 12, espaçamento 1,5, margens 3/2 cm): **≈ 380 palavras por página** de
texto corrido.

| Elemento | Custo |
|---|---|
| 380 palavras | 1,0 página |
| Figura `1col`, `altura_cm: H` | `(H + 1,5) / 24` página (o +1,5 é legenda + respiro) |
| Figura `meia` | metade do acima |
| Tabela | conte as linhas: `(linhas × 0,7 cm + 2) / 24` |
| Referências | ≈ 3 por página, espaçamento simples |
| Pré-textuais (capa, resumo, sumário) | conforme veículo — orce 2 páginas se exigidos |

`scripts/gate.py` calcula isso e reporta. A estimativa erra para mais ou para menos em
torno de 5% — trabalhe com **18 páginas como alvo**, deixando folga.

## Distribuição inicial sugerida (ajuste no outline)

Para 20 páginas com ~4 figuras, sobram ~16 páginas de texto ≈ **6.000 palavras**:

| Seção | Palavras | Páginas |
|---|---|---|
| Resumo + Abstract | 500 | 1,3 |
| 1. Introdução | 900 | 2,4 |
| 2. Referencial teórico | 1.000 | 2,6 |
| 3. Metodologia / Arquitetura | 1.400 | 3,7 |
| 4. Resultados | 1.200 | 3,2 |
| 5. Discussão | 700 | 1,8 |
| 6. Conclusão | 500 | 1,3 |
| Referências | — | 1,5 |
| Figuras (4 × 6 cm) | — | 1,3 |

Cada seção declara seu alvo em `00-outline.md`. O gate compara o real com o alvo.

## Quando estourar

Na ordem, corte:
1. **Referencial teórico** — é onde quase sempre há excesso. Ele existe para posicionar
   a contribuição, não para provar que você leu.
2. **Descrição de implementação** — detalhe de configuração do n8n vai para apêndice ou
   para o repositório, com link. Artigo descreve decisão de projeto, não passo a passo.
3. **Figuras redundantes** — duas que mostram o mesmo fenômeno viram uma.

Nunca corte: limitações, contribuição incremental sobre 2024, ou origem dos dados.

Se o corte necessário for maior que ~15%, o problema é de escopo, não de redação —
**use `AskUserQuestion`** para o autor decidir o que sai, em vez de comprimir tudo
uniformemente até o texto ficar ilegível.
