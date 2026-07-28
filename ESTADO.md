# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 2 concluída (argumento aprovado) · ingestão quase completa
**Atualizado:** 27/07/2026 (fim da sessão 2)
**Próxima ação:** ler integralmente `docs/tcc_gabriel.pdf` e `docs/tcc_juliana.pdf`
(relatórios de estágio), completar `00-contexto/mapa-de-fatos.md`, e então
`/escrever-secao 03-metodo`.

**O autor precisa providenciar:**
1. Contagem dos PDFs de certificado na pasta do Google Drive + intervalo de datas
   (bloqueia `04-resultados`)
2. Onde o n8n rodava em produção (uma frase no método, mas é limitação declarada)
3. `pandoc` instalado e modelo `.docx` oficial da Principia baixado (bloqueia só o build)

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
| D-7 | Tempo do processo manual: **40 min/aluno** (descartado o "≈1 hora" do dump) |
| D-8 | `refs.md` é levantado **depois** de método e resultados, antes do referencial |
| D-9 | Certificados não têm registro no banco; evidência = PDFs no Google Drive |

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

## Resolvido na sessão 2

- ✅ Workflows n8n de 2025 disponíveis em `api-repo/n8n_files/` (4 arquivos) — regras de
  recomendação e certificação extraídas para `mapa-de-fatos.md` §5
- ✅ `refs.md` com as 16 referências dos relatórios de estágio
- ✅ Snapshot agregado do banco Neon
- ✅ Gatilhos do n8n, as 10 competências, e o limiar de nota 2,0

## Bloqueios

1. **Relatórios de estágio não lidos integralmente** — `docs/tcc_gabriel.pdf` e
   `docs/tcc_juliana.pdf`. Primeira coisa a fazer em `/escrever-secao 03-metodo`
2. **Regra de 2/3 não localizada no código** — não está em `Certificados_v3.json`.
   Verificar `api-repo/` (provável: endpoint `/discentes_aptos_certificacao/`). Se for
   aplicada manualmente, muda a descrição do método
3. **Contagem de certificados** — depende do autor (PDFs no Drive)
4. **Referencial sem literatura revisada por pares** sobre automação em educação,
   low-code em ensino e avaliação de soft skills. Busca dirigida após `04-resultados`

## Ambiente

- Banco Neon **ativo** (PostgreSQL 15.18), consultado em 27/07/2026 via `/consultar-banco`
- [ ] `pandoc` não instalado — necessário só na etapa 7
- [ ] Modelo oficial `.docx` da Revista Principia não baixado
