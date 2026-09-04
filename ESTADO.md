# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 3 — escrita. Método e Resultados em rascunho.
**Atualizado:** 03/09/2026 (sessão 5)
**Próxima ação:** `/escrever-secao 02-referencial` — mas **não comece escrevendo**. A D-8
deixou o levantamento bibliográfico para este ponto: a sessão abre buscando de 6 a 10
referências revisadas por pares, e só então redige. Detalhe no bloco "Próxima sessão".

**O autor precisa providenciar:**
1. `pandoc` instalado e modelo `.docx` oficial da Principia baixado (bloqueia só o build)
2. Decidir se corrige os dois defeitos da API antes da submissão (ver "Riscos")

Nenhum bloqueio para a próxima seção.

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
| D-13 | Banco misturou produção e testes → contagens de população reenquadradas |
| D-14 | `bulk_create`/`select_related` **não existem no código** → saem do artigo |

## Decisões pendentes

- [ ] Título em português e inglês
- [ ] Se as duas vagas restantes de autoria serão usadas
- [ ] Corrigir ou não os dois defeitos da API antes de submeter (ver "Riscos")

## Seções

| Arquivo | Status | Palavras (real/alvo) | Lacunas abertas |
|---|---|---|---|
| 00-resumo | não iniciada | 0 / 550 | — |
| 01-introducao | não iniciada | 0 / 1.100 | — |
| 02-referencial | **próxima** | 0 / 1.600 | depende do levantamento |
| 03-metodo | **rascunho** | 1.994 / 2.200 | 1 tríade a reescrever (linha 183) |
| 04-resultados | **rascunho** | 2.834 / 2.800 | 3 `[[VERIFICAR]]` · 3 `[[CIT]]` |
| 05-conclusao | não iniciada | 0 / 700 | — |
| 06-declaracoes | não iniciada | 0 / 100 | — |

Gate: **0 bloqueantes**, 17 pendências. Estimativa **12,3 páginas** (janela 12–18, alvo 16).
As cinco seções que faltam somam ~4.050 palavras de alvo, o que projeta ~18 páginas — vai
exigir aperto no fim, não folga.

### Lacunas de `04-resultados`, uma a uma

| Linha | Marcador | Pergunta | Quem resolve |
|---|---|---|---|
| 136 | `[[VERIFICAR]]` | quantos discentes o endpoint `/discentes_aptos_certificacao/` retorna hoje, e em que data? | consulta ao banco |
| 208 | `[[VERIFICAR]]` | há medição de tempo de inicialização a frio? | autor |
| 279 | `[[VERIFICAR]]` | proporção de autoavaliações sem notas e sem discente — consulta de 03/09 falhou por DNS | consulta ao banco |
| 234 | `[[CIT]]` | explicitação de regra implícita como ganho de governança | levantamento |
| 244 | `[[CIT]]` | devolutiva dirigida vs. adaptativa | levantamento |
| 251 | `[[CIT]]` | transferibilidade de arquitetura entre contextos | levantamento |

Os três `[[CIT]]` caem exatamente na busca da próxima sessão. Os `[[VERIFICAR]]` de banco
são acréscimos, não bloqueios — o texto se sustenta sem eles.

## Figuras — 6 declaradas, **nenhuma produzida**

| ID | O que é | Onde |
|---|---|---|
| `TAB:03-1` | Quadro editável das 10 competências avaliadas | 03 |
| `FIG:03-1` | Diagrama de arquitetura (n8n + API + banco + Google Workspace) | 03 |
| `FIG:03-2` | DER das 7 entidades do domínio | 03 |
| `TAB:04-1` | Snapshot agregado do banco em 27/07/2026 | 04 |
| `FIG:04-1` | Autoavaliações por unidade (33×5, depois 7, 3, 1, 1) | 04 |
| `TAB:04-2` | Tempos: manual 40 min · 2024 ≈12 s · registro 2–3 s · gráfico 12–15 s | 04 |

⚠️ 300 dpi e texto interno em TNR ≥18 — inviabiliza screenshot. Tabelas e quadros
**editáveis, nunca imagem**: as três `TAB` saem como markdown, não como figura.

## Riscos a decidir antes de submeter

Dois defeitos encontrados no código na sessão 5. Nenhum bloqueia a escrita, ambos são
verificáveis por um avaliador que abra o repositório:

1. **`except Exception` que grava lixo e devolve 201.** `CreateAutoavaliacaoSerializer.create()`
   persiste `Autoavaliacao` vazia em caso de falha e reporta sucesso. É a causa dos 177
   registros contra 15 conjuntos de notas.
2. **`DeleteAllRecordsAPIView`** apaga as oito tabelas do domínio, exposto como rota
   autenticada da API de produção.

O artigo já os trata com honestidade (4.6 declara a ausência de segregação de ambientes
como limitação). A decisão em aberto é se o **código** é corrigido antes da submissão.

## Bloqueios

1. **Referencial sem literatura revisada por pares.** `refs.md` tem 16 entradas, todas de
   documentação técnica e gestão de projetos, **10 ainda órfãs**. É a fragilidade que um
   avaliador aponta primeiro. Resolve na próxima sessão.

## Próxima sessão — roteiro

1. Busca dirigida: 6 a 10 referências revisadas por pares, **≥2019**, com DOI, sobre
   automação de fluxos acadêmico-administrativos, low-code/no-code em instituições de
   ensino e mensuração de soft skills em programas de formação. Cada entrada com campo
   `origem` preenchido — sem isso o gate bloqueia.
2. Fechar os três `[[CIT]]` de `04-resultados`.
3. `/escrever-secao 02-referencial` (alvo 1.600).

## Ambiente

- Banco Neon: **inacessível em 03/09/2026** — o host não resolveu por DNS. Último snapshot
  válido é o de 27/07/2026. Verificar se a instância ainda existe antes de prometer consulta.
- [ ] `pandoc` não instalado — necessário só na etapa 7
- [ ] Modelo oficial `.docx` da Revista Principia não baixado
