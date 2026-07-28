# Checklist de Review do Artigo

Análogo ao `code-review-checklist.md` do v1surgicalweb. Percorra por seção. Classifique
os achados:

- **🔴 CRITICAL** — bloqueia submissão. Citação inventada, número sem fonte, autoplágio,
  contradição entre seções, conclusão não sustentada pelos resultados.
- **🟡 MAJOR** — corrigir antes de submeter. Afirmação vaga, lacuna metodológica,
  contribuição incremental não explicitada, citação sem página em citação direta.
- **🟢 MINOR** — sugestão. Legibilidade, repetição, ordem de parágrafos.
- **✅ POSITIVE** — destacar o que está bem sustentado.

## 1. Integridade factual (🔴 se falhar)

- [ ] Todo número no texto tem origem rastreável em `00-contexto/` ou fonte citada
- [ ] Nenhuma referência de `refs.md` está sem campo `origem` verificável
- [ ] Nomes de pessoas, instituições e parcerias conferem com o dump de contexto
- [ ] Datas e período do projeto conferem entre seções
- [ ] Zero `[[VERIFICAR]]`, `[[CIT]]`, `[[DECIDIR]]` remanescentes
- [ ] Nenhuma citação foi produzida "de memória" sem busca ou fonte fornecida

## 2. Argumento

- [ ] A tese do `00-outline.md` aparece na introdução e é retomada na conclusão
- [ ] A **contribuição incremental sobre o artigo de 2024** está explícita e defendida
- [ ] Cada seção cumpre a função declarada no outline
- [ ] A conclusão não afirma nada que os resultados não sustentem
- [ ] Limitações do estudo estão declaradas (ausência disso é MAJOR garantido em revisão)

## 3. Citações e referências

- [ ] Toda citação no texto tem entrada em `refs.md` (gate confirma)
- [ ] Nenhuma referência órfã (gate confirma)
- [ ] Citações diretas têm página
- [ ] TCCs e artigo de 2024 estão citados onde seu conteúdo é usado
- [ ] Nenhum trecho literal reaproveitado sem marcação de citação

## 4. Método e resultados

- [ ] A metodologia é reprodutível por um terceiro a partir do texto
- [ ] A arquitetura (n8n + API + geração de gráficos/planilhas + e-mail) está descrita
      em nível que sustenta o resultado, não em nível de tutorial
- [ ] Cada figura/tabela tem origem, período e legenda autoexplicativa
- [ ] Resultados são apresentados sem interpretação; interpretação vive na discussão

## 5. Forma

- [ ] Forma impessoal em todo o artigo (exigência da revista) — zero primeira pessoa
- [ ] Sem adjetivo avaliativo sem número atrás
- [ ] Sem formatação manual dentro dos `.md`
- [ ] Alvos de palavras por seção respeitados (gate avisa)
- [ ] Resumo/abstract escritos por último e refletindo o texto final
- [ ] Entre 12 e 18 páginas estimadas
- [ ] Introdução termina com parágrafo apresentando as seções seguintes
- [ ] Nenhuma seção tem subseção sem texto introdutório antes

## 5b. Voz — o texto parece escrito por IA? (🟡 MAJOR, pode virar 🔴)

> Referência: `.claude/rules/voz-e-estilo.md`, calibrada sobre o manuscrito de 2024 do
> próprio grupo. Rodar `python3 scripts/gate.py --estilo` antes desta seção.

- [ ] Média de palavras por frase entre 21 e 30 (o grupo escreve 25,4). Frase curta
      demais é o marcador mais forte de geração automática neste projeto
- [ ] Parágrafos entre 60 e 105 palavras (o grupo escreve 81) — não blocos curtos uniformes
- [ ] Nenhum conectivo da lista proibida (`Ademais`, `Nesse sentido`, `Em suma`,
      `Vale ressaltar`, `Outrossim`, `Destarte`, `Por conseguinte`…)
- [ ] Léxico suspeito ausente (`robusto`, `abrangente`, `poderoso`, `holístico`,
      `panorama`, `na era digital`, `desempenha um papel`…)
- [ ] Sem tríades reflexas ("eficiência, escalabilidade e confiabilidade")
- [ ] Sem travessão duplo para aposto
- [ ] Sem frase-resumo vazia fechando parágrafos
- [ ] Sem lista com marcadores no corpo (o texto de 2024 é prosa corrida)
- [ ] Terminologia constante: sempre `discente`, `unidade`, `soft skill` — sem sinônimos
      alternando por elegância
- [ ] **Teste final:** um avaliador que leu o manuscrito de 2024 reconheceria a mesma mão?
      Se não, é problema de voz mesmo com o conteúdo correto

## 6. Normas da revista e autoria

- [ ] Manuscrito **sem qualquer identificação de autoria** (submissão duplo-cega)
- [ ] Seções obrigatórias presentes: Financiamento e Conflito de interesses
- [ ] Equipe não-autora creditada em Agradecimentos (11 integrantes, 4 autores)
- [ ] **Nenhum dado individual de discente** no texto, tabelas ou figuras
- [ ] Nenhuma credencial, hostname ou URL de banco no texto ou em figura
- [ ] Nada citado que a revista proíba: trabalho em avaliação (manuscrito 2024),
      slides (apresentação 2024), relatório de estágio
- [ ] Referências majoritariamente de 2019 em diante, com DOI quando disponível

## Veredito

| Veredito | Critério |
|---|---|
| ✅ PRONTO PARA SUBMISSÃO | Zero CRITICAL e zero MAJOR; gate exit 0 |
| ⚠️ PRONTO COM RESSALVAS | Zero CRITICAL; MAJOR listados e aceitos conscientemente |
| 🔴 REVISÃO NECESSÁRIA | ≥1 CRITICAL ou vários MAJOR |

Justifique sempre apontando `arquivo:linha`.
