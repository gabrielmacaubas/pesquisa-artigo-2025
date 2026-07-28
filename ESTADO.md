# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 2 concluída (argumento aprovado) · ingestão parcial
**Atualizado:** 27/07/2026
**Próxima ação:** ler integralmente `docs/tcc_gabriel.pdf` e `docs/tcc_juliana.pdf`
(relatórios de estágio), completar `00-contexto/mapa-de-fatos.md`, e então
`/escrever-secao 03-metodo`

## O artigo

- **Veículo:** Revista Principia — artigo original · **12 a 18 páginas** (alvo 16)
- **Título:** `[[DECIDIR]]` (PT e EN, máx. 50 palavras)
- **Prazo:** `[[VERIFICAR: há data-limite de submissão?]]`
- **Tese:** aprovada — automação do ciclo formativo exige camada de decisão
  (certificação) e de intervenção (recomendação) sobre persistência estruturada
- **Autores (4 de 6):** Gabriel Macaúbas Melo · Juliana Ferreira Cavalcante ·
  Heremita Brasileiro Lira · Francisco Petrônio

## Decisões tomadas

| # | Decisão |
|---|---|
| D-1 | Tese: continuidade declarada do ciclo 2024 (certificação + recomendação) |
| D-2 | Manuscrito de 2024 **não publicado** → não citável; continuidade é narrada, não citada |
| D-3 | Autoria: os 4 acima |
| D-4 | Trabalhos-base são **relatórios de estágio**, não TCCs → regra dos 30% não se aplica |
| D-5 | Parecer do CEP **não se aplica** (dados operacionais, não pesquisa com seres humanos) |
| D-6 | Banco migrou Railway (fim de 2024) → Neon/Vercel (2025); faz parte da contribuição |

## Decisões pendentes

- [ ] Título em português e inglês
- [ ] Quais figuras produzir (depende de `03-metodo` escrita)
- [ ] Se as duas vagas restantes de autoria serão usadas

## Seções

| Arquivo | Status | Palavras (real/alvo) |
|---|---|---|
| 00-resumo | não iniciada | 0 / 550 |
| 01-introducao | não iniciada | 0 / 1.100 |
| 02-referencial | não iniciada | 0 / 1.600 |
| 03-metodo | **próxima** | 0 / 2.200 |
| 04-resultados | não iniciada | 0 / 2.800 |
| 05-conclusao | não iniciada | 0 / 700 |
| 06-declaracoes | não iniciada | 0 / 100 |

## Figuras

Nenhuma declarada — dependem das seções. ⚠️ A revista exige 300 dpi e texto interno em
TNR ≥18, o que inviabiliza screenshots de código; tabelas têm de ser editáveis.

## Bloqueios

1. **Relatórios de estágio não lidos** — impede Método e Resultados
2. **`refs.md` vazio** — nenhuma referência levantada; o referencial teórico precisa de
   busca ativa, priorizando 2019+ com DOI
3. `[[VERIFICAR]]` aberto: total de certificados emitidos e e-mails enviados — não há
   tabela desses eventos no banco; procurar em logs do n8n ou Google Drive
4. `[[VERIFICAR]]` aberto: conflito 40 min (manuscrito 2024) vs 1 h (dump) no tempo manual

## Ambiente

- Banco Neon **ativo** (PostgreSQL 15.18), consultado em 27/07/2026 via `/consultar-banco`
- [ ] `pandoc` não instalado — necessário só na etapa 7
- [ ] Modelo oficial `.docx` da Revista Principia não baixado
