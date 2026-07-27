---
description: Etapa 6 — review completo do artigo contra o checklist, com veredito
---

Review completo. Escopo: $ARGUMENTS (se vazio, o artigo inteiro).

## Procedimento

1. Rode `python3 scripts/gate.py` e trate a saída como entrada do review, não como
   substituto dele. O gate pega o mecânico; o resto é leitura.

2. Percorra `.claude/rules/review-artigo.md` seção por seção do checklist.

3. **Verificação factual ativa** — não confie no que está escrito. Para cada número e
   cada nome próprio no artigo, encontre a origem em `00-contexto/mapa-de-fatos.md` ou
   em `docs/`. Um número que você não conseguir rastrear é 🔴 CRITICAL, mesmo que pareça
   correto.

4. **Verificação de citações** — para cada entrada de `refs.md` usada no texto, confira
   o campo `origem`. Entrada sem origem rastreável é 🔴 CRITICAL (presumir invenção).

5. **Leitura de coerência** — leia o artigo do início ao fim de uma vez, procurando:
   contradição entre seções, conclusão que ultrapassa os resultados, tese anunciada na
   introdução que não é entregue.

6. Produza o relatório em `build/review-<data>.md` com achados classificados
   (🔴/🟡/🟢/✅), cada um com `arquivo:linha` e sugestão de correção, e o veredito final
   conforme a tabela da rule.

Seja adversarial. Um review que não encontra nada em um artigo escrito por LLM
provavelmente não olhou direito — o modo de falha característico é texto fluente e bem
estruturado apoiado em um fato que ninguém conferiu.
