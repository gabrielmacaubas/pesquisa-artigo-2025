---
description: Etapa 4 — escreve UMA seção do artigo (uso: /escrever-secao 03-metodologia)
---

Escreve **uma única seção**: $ARGUMENTS

Se nenhum argumento foi passado, consulte a ordem de escrita em `00-outline.md` e
proponha a próxima.

## Antes de escrever
1. Leia `00-outline.md` — a função declarada desta seção e seu alvo de palavras
2. Leia `00-contexto/mapa-de-fatos.md` — só os fatos pertinentes a ela
3. Leia `.claude/rules/escrita-academica.md` e `fontes-e-citacoes.md`
4. Leia as seções **vizinhas** já escritas, para não repetir nem contradizer

## Ao escrever
- Só conteúdo. Zero formatação ABNT.
- Todo número vem do mapa de fatos. Sem fonte → `[[VERIFICAR: pergunta específica]]`.
- Toda citação tem entrada em `refs.md` com campo `origem`. Sem isso → `[[CIT]]`.
- Nunca preencha uma lacuna com valor plausível. A lacuna explícita é o produto correto.
- Escolha do autor (ordem de autoria, recorte, o que omitir) → `[[DECIDIR: A vs B]]`.

## Depois
1. Rode `python3 scripts/gate.py`
2. Reporte: contagem de palavras vs alvo, lacunas abertas com a pergunta de cada uma,
   e as referências novas adicionadas a `refs.md`
3. **Pare.** Não emende a próxima seção — o autor revisa esta primeiro.
