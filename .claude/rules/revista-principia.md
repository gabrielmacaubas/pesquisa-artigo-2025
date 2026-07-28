# Revista Principia — normas do veículo (prevalecem sobre tudo)

> Fontes: `docs/Diretrizes_publicacao_Revista_Principia_Dez2024-OTH-1.docx` + Diretrizes
> aos Autores fornecidas pelo autor em 27/07/2026.
>
> **"Trabalhos que não seguirem as instruções de formatação serão automaticamente
> rejeitados."** Não é recomendação de estilo — é filtro pré-avaliação.

Tipo do manuscrito: **artigo original** (pesquisa científica).

## Restrições que condicionam o projeto inteiro

| Restrição | Valor |
|---|---|
| **Páginas** | **mínimo 12, máximo 18** — incluindo referências, tabelas e ilustrações |
| **Autores** | máximo 6, todos assinam declaração de autoria; **não se acrescenta autor depois** |
| **Submissão** | PDF **sem identificação de autoria**, inclusive nas *Propriedades do Arquivo* (duplo-cega) |
| Página | A4 vertical. Margens: sup 3,5 · inf 2 · lat 2,5 cm |
| Espaçamento | simples entre linhas E entre parágrafos (0 pt antes/depois) |
| Recuo | 1 cm na primeira linha |
| Fonte | Times New Roman (tamanhos abaixo) |
| Idioma | português, **na forma impessoal** |

O mínimo de 12 páginas vincula tanto quanto o máximo: artigo curto demais é barrado na
triagem. Ver `orcamento-paginas.md`.

## Tamanhos de fonte

| Elemento | Tamanho | Estilo |
|---|---|---|
| Título do artigo | 12 | negrito |
| Resumo | 11 | normal |
| Abstract | 11 | itálico |
| Títulos de seção/subseção | 11 | negrito, numerados |
| Corpo do texto | 11 | normal |
| Títulos de figuras/tabelas/quadros | 10 | normal |
| Corpo de tabelas e quadros | 10 | normal |
| Notas de rodapé e fontes de ilustração | 8 | normal |

## Estrutura obrigatória

```
Título em português (máx. 50 palavras, só a 1ª letra maiúscula, sem ponto final)
Resumo (200–300 palavras, parágrafo único, SEM citações)
Palavras-chave: 3 a 5, ordem alfabética, minúsculas, separadas por ponto e vírgula
Título em inglês
Abstract (itálico)
Keywords
1 Introdução
2 Referencial teórico          (título pode ser trocado pela temática)
3 Método da pesquisa
4 Resultados e discussões
5 Conclusão / Considerações finais
Agradecimentos                 (opcional, NÃO numerada)
Financiamento                  (OBRIGATÓRIA, não numerada)
Conflito de interesses         (OBRIGATÓRIA, não numerada)
Referências
```

Duas exigências estruturais fáceis de esquecer, ambas cobradas em avaliação:

1. **A introdução termina com um parágrafo apresentando as ideias principais das seções
   posteriores.** Exigência explícita da revista.
2. **Toda seção tem texto introdutório antes da primeira subseção.** Nunca `3 Método`
   seguido direto de `3.1`.

## Resumo — estrutura exigida para artigo original

Fundamentação breve → objetivo → método(s) → resultados → conclusão(ões). Parágrafo
único, 200–300 palavras, **sem citações**, sem repetir o título, sem revisão de
literatura. Incluir os principais resultados numéricos, citando-os sem explicá-los. Cada
frase deve conter uma informação completa. Norma: NBR 6028.

## Ilustrações, tabelas e equações

- Figuras: `.jpg`/`.png`, **mínimo 300 dpi**; texto interno em Times New Roman **≥ 18**.
- **Tabelas e quadros editáveis — nunca imagem.** Corpo em TNR 10.
- Elementos vêm **logo após serem citados**, em ordem sequencial.
- Proibido "tabela abaixo"/"quadro acima" — sempre "Tabela 1", "Figura 2".
- Toda ilustração leva `Fonte:` em TNR 8 (`dados da pesquisa`, `elaborado pelos autores`
  ou `Autor (ano, p. x)`).
- Equações: centralizadas, numeradas à direita, **editáveis**, variáveis em itálico.
- **Decimais com vírgula** (0,5 — nunca 0.5). Unidades SI.
- Código: não incluir rotinas na íntegra. **Pseudocódigo/algoritmo** é o recomendado,
  com link para o repositório.

## Origem do trabalho — o que se aplica e o que não se aplica

Os dois trabalhos que embasam este artigo foram protocolados como **relatórios de
estágio**, não como TCCs ou monografias institucionais (decisão D-4). Portanto:

- ✅ **Não se aplica** a regra de acréscimo mínimo de 30% para trabalhos previamente
  publicados em anais ou monografias.
- ✅ **Não se aplica** a exigência de declaração de derivação de tese/dissertação.
- ⚠️ Continua valendo o princípio geral de originalidade: relatório de estágio é
  documento interno não publicado, então **não entra em `refs.md` e não é citado** — o
  artigo simplesmente relata o trabalho próprio. Evitar transcrição literal extensa,
  porque ferramentas antiplágio comparam contra repositórios institucionais.

## Ética

A revista exige parecer de comitê de ética "caso a pesquisa envolva seres humanos e/ou
animais". Avaliação do autor (D-5): **não se aplica** — trata-se de dados operacionais de
um programa de capacitação, não de estudo de pesquisa com seres humanos no sentido da
resolução. Registrado como decisão; não é bloqueio.

Permanece valendo, independentemente disso, a proteção dos dados: o banco contém nome,
CPF, matrícula e e-mails reais. **Nenhum dado individual entra no artigo** — ver
`.claude/rules/dados-e-privacidade.md`.

## Referências — recomendações da revista

- Priorizar publicações dos **últimos sete anos** (≥ 2019 para submissão em 2026).
- **DOI sempre que disponível**, ou link primário. Evitar ResearchGate.
- Nome completo do periódico, sem abreviação.
- Norma: **NBR 6023/2018**. Citações: **NBR 10520/2023**. Notas: NBR 14724/2011.
- **Proibido citar:** trabalhos em avaliação, materiais didáticos (slides, notas de aula,
  apostilas). Isso exclui o manuscrito de 2024 e a apresentação de 29/10/2024.
- Só entram em Referências as fontes efetivamente citadas.

## Checklist de submissão (fora do manuscrito)

- [ ] Carta de apresentação (cover letter) com sugestão de avaliadores
- [ ] Declaração de ciência das diretrizes, assinada
- [ ] Declaração de autoria assinada por todos os autores
- [ ] ORCID, e-mail, filiação e país de cada autor nos metadados do sistema
- [ ] PDF sem identificação — **limpar as Propriedades do Arquivo**
- [ ] Tabelas e equações editáveis
- [ ] Entre 12 e 18 páginas no documento formatado
- [ ] Só fontes citadas na seção Referências

## Fluxo de produção

`secoes/*.md` → `scripts/build.py` → `build/artigo.docx` → **colar no modelo oficial da
Revista Principia** → conferir paginação → exportar PDF → limpar metadados.

A revista **não aceita LaTeX**. O modelo oficial dela é a referência final — se algo aqui
divergir do modelo, o modelo vence.
