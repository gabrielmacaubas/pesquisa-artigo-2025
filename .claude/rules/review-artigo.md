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

- [ ] Pessoa verbal consistente em todo o artigo
- [ ] Sem adjetivo avaliativo sem número atrás
- [ ] Sem formatação manual dentro dos `.md`
- [ ] Alvos de palavras por seção respeitados (gate avisa)
- [ ] Resumo/abstract escritos por último e refletindo o texto final

## 6. Ética e autoria

- [ ] Todos os participantes/parceiros com contribuição relevante estão creditados
- [ ] Financiamento/apoio institucional declarado, se houver
- [ ] Dados de pessoas (se houver) anonimizados ou com consentimento registrado
- [ ] Ordem de autoria acordada — `[[DECIDIR]]` até confirmação explícita do autor

## Veredito

| Veredito | Critério |
|---|---|
| ✅ PRONTO PARA SUBMISSÃO | Zero CRITICAL e zero MAJOR; gate exit 0 |
| ⚠️ PRONTO COM RESSALVAS | Zero CRITICAL; MAJOR listados e aceitos conscientemente |
| 🔴 REVISÃO NECESSÁRIA | ≥1 CRITICAL ou vários MAJOR |

Justifique sempre apontando `arquivo:linha`.
