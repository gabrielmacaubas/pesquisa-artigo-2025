# Fontes e Citações

> Esta rule é a defesa contra o modo de falha mais grave deste projeto: **citação
> inventada**. Um LLM produz referências plausíveis e inexistentes com a mesma fluência
> com que produz as verdadeiras. O gate e o formato abaixo existem para tornar isso
> impossível de passar despercebido.

## Regra dura

Nunca escrevo uma citação cuja entrada completa eu não possa preencher em `refs.md`
a partir de uma fonte que eu **li ou recebi**. Se não tenho os dados, escrevo `[[CIT]]`.

Fontes legítimas neste projeto:
1. Arquivos em `00-contexto/` (dump do Gemini, TCCs, artigo 2024)
2. Documentos/links que o autor fornecer explicitamente na conversa
3. Páginas que eu efetivamente busquei e li com WebSearch/WebFetch

Não é fonte: minha memória de treinamento. "Eu sei que existe um artigo do Fulano sobre
isso" não autoriza citação — autoriza uma busca.

## Formato de `refs.md` (machine-readable — o gate depende dele)

Cada referência é um bloco iniciado por `## [SOBRENOME, ANO]`:

```markdown
## [SILVA, 2020]
- **tipo:** artigo
- **autores:** SILVA, João Pedro; COSTA, Maria
- **titulo:** Automação de fluxos de trabalho em pesquisa aplicada
- **veiculo:** Revista Brasileira de Informática, v. 12, n. 3, p. 45-62
- **ano:** 2020
- **doi_url:** https://doi.org/10.xxxx/yyyy
- **acesso_em:** 2026-07-27
- **origem:** WebFetch em 2026-07-27 / p. 34 do TCC de Fulano / dump Gemini §4
- **usada_em:** secoes/02-referencial.md
```

`origem` é obrigatório e é o campo mais importante: diz **como eu sei que essa referência
existe**. Uma entrada sem `origem` verificável é tratada como inventada.

Chaves duplicadas do mesmo autor/ano: sufixo de letra — `[SILVA, 2020a]`, `[SILVA, 2020b]`.

## Citação no corpo do texto (ABNT autor-data)

- Indireta, fim de frase: `... reduz o tempo de resposta (SILVA, 2020).`
- Dois autores: `(SILVA; COSTA, 2020)`
- Três ou mais: `(SILVA et al., 2020)`
- Autor na frase: `Silva (2020) demonstra que...` — nome em caixa alta e baixa
- Direta curta (até 3 linhas): aspas + página — `"texto" (SILVA, 2020, p. 45).`
- Direta longa (4+ linhas): bloco recuado, sem aspas, corpo menor, com página. No
  markdown, use blockquote (`>`) — o build aplica o recuo ABNT.

Citação direta **sempre** leva página. Sem exceção.

## Autocitação — os TCCs e o artigo de 2024

Este artigo se apoia em trabalhos do próprio grupo. Isso é legítimo e esperado, mas:

- Cada TCC e o artigo de 2024 entram em `refs.md` como referência normal e são
  **citados** quando o conteúdo vem deles. Reaproveitar texto próprio sem citar é
  autoplágio e é detectado.
- O artigo de 2025 precisa declarar sua **contribuição incremental** sobre o de 2024
  (campo obrigatório em `00-outline.md`). "O que há aqui que não estava lá" é a primeira
  pergunta de qualquer revisor.
- Texto reaproveitado literalmente de um TCC deve ser reescrito ou marcado como citação
  direta com página.

## Referências órfãs e citações fantasma

O gate cruza os dois sentidos:
- Citação no texto sem entrada em `refs.md` → **bloqueante**
- Entrada em `refs.md` nunca citada → aviso (limpe antes de submeter)
