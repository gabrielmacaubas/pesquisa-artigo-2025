# Outline — Artigo 2025 · Revista Principia

> Aprovado em 27/07/2026 (D-1). Alterações aqui exigem nova decisão do autor.

## Identificação

- **Título provisório:** `[[DECIDIR]]` — máx. 50 palavras, só a 1ª letra maiúscula, sem
  ponto final. Precisa de versão em inglês.
- **Veículo:** Revista Principia — artigo original
- **Janela:** 12 a 18 páginas · **alvo 16** · ~9.050 palavras de texto
- **Voz:** impessoal (exigência da revista e padrão do grupo)
- **Autores (D-3):** Gabriel Macaúbas Melo · Juliana Ferreira Cavalcante ·
  Heremita Brasileiro Lira · Francisco Petrônio — **não identificados no manuscrito**

## Tese (D-1)

> A automação de um ciclo formativo não se completa na geração de indicadores de
> desempenho; ela exige a camada de decisão — a certificação por critério objetivo — e a
> camada de intervenção — a recomendação pedagógica dirigida. Ambas só se sustentam sobre
> persistência estruturada com rastreabilidade histórica, e não sobre planilhas.

## Contribuição

O ciclo anterior do projeto automatizou a produção de indicadores (gráficos radar e
tabelas) a partir de planilhas. Persistia a etapa que efetivamente encerra o ciclo
formativo: decidir quem está apto à certificação e devolver ao discente uma orientação
acionável. Este trabalho apresenta:

1. Modelo de dados com rastreabilidade histórica (`models.PROTECT`), que torna a
   comparação longitudinal entre unidades possível
2. Operacionalização da regra de certificação — evolução de nível em ao menos 2/3 das
   competências avaliadas — como consulta sobre dados persistidos
3. Módulo de recomendação pedagógica (práticas *hands-on* / PBL) com envio autônomo
4. Migração de infraestrutura Railway → Neon/Vercel, com API serverless

⚠️ **O manuscrito de 2024 não pode ser citado** (trabalho em avaliação). A continuidade é
narrada como histórico do projeto, sustentada em dados próprios do mapa de fatos — nunca
em "(Autor, 2024)".

## Limitações a declarar

- Recorte de operação real, não censo do programa: o resultado é **viabilidade
  demonstrada**, não escala.
- Latência: API e banco em `us-east-1`; hospedagem local no IFPB apontada como mitigação.
- Autoavaliação como instrumento — `[[VERIFICAR: há mecanismo contra notas infladas?]]`

## Mapa de seções

| # | Arquivo | Função no argumento | Alvo | Fontes | Figuras |
|---|---|---|---|---|---|
| 00 | `secoes/00-resumo.md` | Resumo (200–300 pal, sem citações) + Abstract + palavras-chave. **Escrever por último** | 550 | todo o artigo | — |
| 01 | `secoes/01-introducao.md` | Problema, lacuna, objetivo. **Termina com parágrafo apresentando as seções** | 1.100 | mapa §1, §2 | — |
| 02 | `secoes/02-referencial.md` | Automação de processos educacionais, low-code/n8n, avaliação de competências. Prioriza ≥2019 | 1.600 | literatura a levantar | — |
| 03 | `secoes/03-metodo.md` | Arquitetura, modelo de dados, regra de 2/3, tratamento dos dados. Reprodutibilidade | 2.200 | mapa §4, §5, §11; `api-repo/` | arquitetura, DER |
| 04 | `secoes/04-resultados.md` | Snapshot do banco, cobertura longitudinal, desempenho, discussão à luz da literatura | 2.800 | mapa §6, §9 | cobertura, distribuição |
| 05 | `secoes/05-conclusao.md` | Retoma objetivo, limitações, trabalhos futuros | 700 | — | — |
| 06 | `secoes/06-declaracoes.md` | Agradecimentos (equipe não-autora) · Financiamento · Conflito de interesses | 100 | mapa §1, §3 | — |

## Ordem de escrita

1. `03-metodo` — mais ancorada em evidência
2. `04-resultados`
3. `02-referencial` — depende de levantamento bibliográfico ainda não feito
4. `01-introducao`
5. `05-conclusao` · `06-declaracoes`
6. `00-resumo` — **sempre por último**

## Front matter obrigatório

```markdown
---
secao: 03-metodo
titulo: Método da pesquisa
alvo_palavras: 2200
status: rascunho
---
```

`status`: `rascunho` | `revisado-autor` | `revisado-orientadora` | `final`

## Bloqueios conhecidos

- Relatórios de estágio (`docs/tcc_*.pdf`) ainda não lidos integralmente — obrigatório
  antes de `03-metodo` e `04-resultados`
- Referencial teórico sem nenhuma referência levantada — `refs.md` está vazio
- `[[VERIFICAR]]` de certificados/e-mails emitidos: não há tabela desses eventos no banco
