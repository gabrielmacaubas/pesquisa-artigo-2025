# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 3 em andamento — `03-metodo` escrita em rascunho
**Atualizado:** 03/09/2026 (retomada; corrigido na sessão 4)
**Próxima ação:** `/escrever-secao 04-resultados` — sem bloqueios pendentes.

**O autor precisa providenciar:**
1. `pandoc` instalado e modelo `.docx` oficial da Principia baixado (bloqueia só o build)

Nada mais bloqueia a escrita: D-10, D-11 e D-12 (03/09/2026) fecharam as três pendências
que restavam.

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
| D-7 | Tempo do processo manual: **40 min/aluno** |
| D-8 | `refs.md` é levantado **depois** de método e resultados, antes do referencial |
| D-9 | Certificados não têm registro no banco; evidência = PDFs no Google Drive |
| D-10 | Certificação descrita como implementada, **não acoplada** ao fluxo de emissão |
| D-11 | **Sem número de certificados** — emissão é funcionalidade demonstrada, sem volume |
| D-12 | D-7 reconfirmado: 40 min, com procedência do "≈1 h" corrigida |

## Decisões pendentes

- [ ] Título em português e inglês
- [ ] Se as duas vagas restantes de autoria serão usadas

## Seções

| Arquivo | Status | Palavras (real/alvo) |
|---|---|---|
| 00-resumo | não iniciada | 0 / 550 |
| 01-introducao | não iniciada | 0 / 1.100 |
| 02-referencial | não iniciada | 0 / 1.600 |
| 03-metodo | **rascunho** | 1.989 / 2.200 |
| 04-resultados | **próxima** | 0 / 2.800 |
| 05-conclusao | não iniciada | 0 / 700 |
| 06-declaracoes | não iniciada | 0 / 100 |

Estimativa atual: **7,2 páginas** de 12 a 18 (só a seção 3 escrita).

## Figuras

Três declaradas em `03-metodo`, todas com `status: criar` — nenhuma produzida ainda:

| ID | O que é |
|---|---|
| `TAB:03-1` | Quadro editável das 10 competências avaliadas |
| `FIG:03-1` | Diagrama de arquitetura (n8n + API + banco + Google Workspace) |
| `FIG:03-2` | DER das 7 entidades do domínio |

⚠️ A revista exige 300 dpi e texto interno em TNR ≥18, o que inviabiliza screenshots de
código; tabelas têm de ser editáveis.

## Resolvido na sessão 3

- ✅ **Relatórios de estágio lidos integralmente** — fatos em `mapa-de-fatos.md` §14
- ✅ **Regra de 2/3 localizada no código** — `Discente.aptosCertificacao()` em
  `api-repo/.../models/discente.py:31-160`. A descrição anterior estava **incompleta**:
  o salto exigido é de **dois níveis** (`+2`), a referência é a **menor medição** (não a
  primeira unidade), e há filtros de permanência (365 dias), cobertura (≥3 competências)
  e piso (1,0). Corrigido em `mapa-de-fatos.md` §5
- ✅ Hospedagem do n8n: **contêiner Docker auto-hospedado** (resolve parcialmente um
  `[[VERIFICAR]]` antigo)
- ✅ `03-metodo` escrita: 1.989 palavras, 4 citações, 0 bloqueantes no gate
- ✅ Dois defeitos do `gate.py` corrigidos (ver `LOG.md` sessão 3)

## Bloqueios

1. **Referencial sem literatura revisada por pares** sobre automação em educação,
   low-code em ensino e avaliação de soft skills. Busca dirigida após `04-resultados`
   (D-8). `refs.md` tem 16 entradas, todas dos relatórios de estágio, 12 ainda órfãs

Nenhum bloqueio para `04-resultados`.

## Ambiente

- Banco Neon **ativo** (PostgreSQL 15.18), consultado em 27/07/2026 via `/consultar-banco`
- [ ] `pandoc` não instalado — necessário só na etapa 7
- [ ] Modelo oficial `.docx` da Revista Principia não baixado
