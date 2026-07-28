# Escrita Acadêmica

## Voz e pessoa

Português brasileiro, registro acadêmico formal, **sempre na forma impessoal** —
exigência da Revista Principia e padrão do próprio grupo (zero ocorrências de primeira
pessoa no manuscrito de 2024). Use `foi/foram`, `utilizou-se`, `observou-se`,
`adotou-se`. Nunca `realizamos`, `nossa abordagem`.

> **Antes de escrever qualquer seção, leia `.claude/rules/voz-e-estilo.md`.** Ele traz o
> perfil medido de escrita do grupo (frases de ~25 palavras, parágrafos de ~81) e a lista
> de marcadores que denunciam texto gerado por IA. Não é preferência estética: é o que
> evita que o artigo destoe do texto anterior dos mesmos autores.

## Estrutura do parágrafo

Um parágrafo = uma ideia. Abre com a afirmação, sustenta com evidência, fecha ligando à
próxima. Parágrafo de uma frase é sinal de ideia não desenvolvida; parágrafo de 15 linhas
é sinal de duas ideias grudadas.

## O que evita retrabalho

- **Escreva a seção mais concreta primeiro.** Metodologia e Resultados são os que têm
  fonte direta em `00-contexto/`. Introdução e Conclusão dependem do que o resto disser —
  escrevê-las cedo garante reescrevê-las depois.
- **Resumo/Abstract por último.** Sempre.
- **Uma seção por vez, gate ao final de cada uma.** Não escreva quatro seções e revise
  no fim; o erro de premissa se propaga.

## Padrões que enfraquecem o texto (evitar)

| Evite | Prefira |
|---|---|
| "É importante ressaltar que X" | "X" |
| "Diversos autores apontam..." (sem citar) | "Silva (2020) e Costa (2022) apontam..." |
| "Os resultados foram muito satisfatórios" | "O tempo de processamento caiu de X para Y" |
| "Revolucionário", "inovador", "robusto" | descrever o que o sistema faz |
| Adjetivo avaliativo sem número atrás | número |

Rigor aqui não é estilo — banca e revisor cobram exatamente isso.

## Separação conteúdo × formatação

Os `.md` contêm **só conteúdo**. Nada de fonte, espaçamento, recuo, numeração de página
ou capa nos arquivos de seção. Tudo isso é aplicado no build (ver `abnt.md`). Misturar as
duas camadas faz você pagar custo de formatação a cada rodada de reescrita.

Markdown permitido nas seções: `##`/`###` para títulos, ênfase, listas, tabelas, blocos
de código, notas de rodapé (`[^1]`). Nada além disso.

## Marcadores de pendência

- `[[VERIFICAR: pergunta específica]]` — afirmação que precisa de confirmação factual.
  A pergunta tem que ser respondível: `[[VERIFICAR: quantos e-mails/mês o n8n enviou?]]`,
  não `[[VERIFICAR: números]]`.
- `[[CIT]]` — afirmação que precisa de referência ainda não localizada.
- `[[DECIDIR: opção A vs B]]` — escolha que é do autor, não minha.

O gate conta esses marcadores. Eles são o mecanismo que substitui inventar.

## Figuras, tabelas e o que veio do n8n

Gráficos e planilhas gerados pela automação são **resultados primários** deste artigo.
Cada um precisa de: origem (qual workflow/execução gerou), período dos dados, e legenda
autoexplicativa. Referencie no texto com `[[@FIG:id]]` (ver `figuras.md`) e registre em
`00-contexto/mapa-de-fatos.md` de onde o arquivo veio — a rastreabilidade é o que sustenta o resultado na
revisão.
