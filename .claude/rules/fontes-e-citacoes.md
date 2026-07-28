# Fontes e Citações — NBR 10520/2023 e NBR 6023/2018

> Defesa contra o modo de falha mais grave deste projeto: **citação inventada**. Um LLM
> produz referências plausíveis e inexistentes com a mesma fluência das verdadeiras.

## Regra dura

Nunca escrevo uma citação cuja entrada completa eu não possa preencher em `refs.md` a
partir de uma fonte que **li ou recebi**. Sem isso, escrevo `[[CIT]]`.

Fontes legítimas:
1. Arquivos em `00-contexto/` e `docs/`
2. Documentos/links que o autor fornecer explicitamente
3. Páginas que eu efetivamente busquei e li com WebSearch/WebFetch

**Não é fonte:** minha memória de treinamento. "Sei que existe um artigo do Fulano sobre
isso" autoriza uma busca, não uma citação.

## O que a Revista Principia NÃO aceita como referência

- **Trabalhos em avaliação.** Exclui o manuscrito de 2024 do próprio grupo.
- **Materiais didáticos** (slides, notas de aula, apostilas). Exclui a apresentação de
  29/10/2024.
- Relatórios de estágio protocolados internamente — documento não publicado.

**Isso não impede falar da continuidade do projeto.** O artigo pode e deve narrar que o
ciclo anterior do mesmo projeto automatizou a geração de indicadores e que este dá
sequência — como histórico do trabalho próprio, na Introdução e no Método, **sem citação
bibliográfica**. O que não se pode é apoiar uma afirmação em "(Autor, 2024)" ou tratar o
manuscrito anterior como literatura.

Consequência prática: toda afirmação factual sobre o ciclo de 2024 que aparecer no artigo
precisa se sustentar em dado próprio verificável (mapa de fatos), não em referência.

## Preferências da revista

- Publicações dos **últimos sete anos** (≥ 2019 para submissão em 2026). Clássicos fora
  dessa janela são aceitáveis quando o conceito exige, mas não devem dominar a lista.
- **DOI sempre que houver**, ou link primário do periódico/repositório. Evitar
  ResearchGate.
- Nome completo do periódico, sem abreviação.
- Pré-prints aceitos se em repositório reconhecido (arXiv, SciELO Preprints…) e
  identificados como tal; preferir a versão final publicada quando existir.

## Formato de `refs.md` (machine-readable — o gate faz parse)

```markdown
## [Silva, 2020]
- **tipo:** artigo
- **autores:** SILVA, João Pedro; COSTA, Maria Helena
- **titulo:** Automação de fluxos de trabalho em pesquisa aplicada
- **veiculo:** Revista Brasileira de Informática, v. 12, n. 3, p. 45-62
- **ano:** 2020
- **doi_url:** https://doi.org/10.xxxx/yyyy
- **acesso_em:** 2026-07-27
- **origem:** WebFetch em 2026-07-27
- **usada_em:** secoes/02-referencial.md
```

`origem` é obrigatório: diz **como sabemos que a referência existe**. Entrada sem origem
verificável é tratada como inventada e bloqueia o gate.

Chave = `[Sobrenome-do-primeiro-autor, Ano]`. Mesmo autor e ano → sufixo `a`, `b`.
No campo `autores`, o sobrenome vai em caixa alta (formato NBR 6023 da lista final); na
**chave** e nas **citações**, só a inicial maiúscula (formato NBR 10520/2023).

## Citação no texto — NBR 10520/2023

⚠️ A versão de 2023 **abandonou a caixa alta** nas citações entre parênteses. Não escreva
`(SILVA, 2020)`.

| Caso | Forma |
|---|---|
| Indireta, entre parênteses | `... reduz o tempo (Silva, 2020).` |
| Autor incorporado ao texto | `Silva (2020) demonstra que...` |
| Dois ou três autores | `(Silva; Costa; Lima, 2020)` |
| Quatro ou mais | `(Costa Junior et al., 2020)` |
| Com página | `(Silva, 2020, p. 45)` · intervalo: `p. 4-9` |
| Duas obras | `(Silva, 2020; Costa, 2021)` |
| Direta curta (até 3 linhas) | aspas + página |
| Direta longa (4+ linhas) | recuo 4 cm, TNR 10, simples, **sem aspas**, com página, linha em branco antes e depois |

Citação direta **sempre** leva página.

No markdown, citação longa vai como blockquote (`>`); o build aplica o recuo.

## Referências órfãs e citações fantasma

O gate cruza os dois sentidos:
- Citação no texto sem entrada em `refs.md` → **bloqueante**
- Entrada em `refs.md` nunca citada → pendência (a revista exige que só constem as
  fontes efetivamente citadas)
