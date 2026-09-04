# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 3 — escrita. Método e Resultados em rascunho.
**Atualizado:** 03/09/2026 (sessão 6)
**Próxima ação:** `/escrever-secao 02-referencial` — mas **não comece escrevendo**. A D-8
deixou o levantamento bibliográfico para este ponto: a sessão abre buscando de 6 a 10
referências revisadas por pares, e só então redige. Roteiro no fim deste arquivo.

**O autor precisa providenciar:** nada. As duas pendências antigas de ambiente eram falsas
ou já foram resolvidas — ver "Ambiente".

## O artigo

- **Veículo:** Revista Principia — artigo original · **12 a 18 páginas** (alvo 16)
- **Título:** `[[DECIDIR]]` (PT e EN, máx. 50 palavras)
- **Prazo:** `[[VERIFICAR: há data-limite de submissão?]]`
- **Tese:** aprovada — automação do ciclo formativo exige camada de decisão
  (certificação) e de intervenção (recomendação) sobre persistência estruturada
- **Contribuição sobre 2024:** o ciclo anterior automatizou indicadores; este entrega as
  camadas de decisão e de intervenção sobre persistência com rastreabilidade histórica,
  mais a migração de infraestrutura
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
| D-15 | Os dois defeitos da API foram **corrigidos no código** |
| D-16 | Ressalva sobre a base **enxugada ao mínimo**, mantida em uma frase |

## Decisões pendentes

- [ ] Título em português e inglês
- [ ] Se as duas vagas restantes de autoria serão usadas
- [ ] Se a conclusão menciona a correção da API como trabalho posterior ao ciclo relatado

## Seções

| Arquivo | Status | Palavras (real/alvo) | Lacunas abertas |
|---|---|---|---|
| 00-resumo | não iniciada | 0 / 550 | escrever **por último** |
| 01-introducao | não iniciada | 0 / 1.100 | — |
| 02-referencial | **próxima** | 0 / 1.600 | depende do levantamento |
| 03-metodo | rascunho | 1.994 / 2.200 | 1 tríade (linha 183) |
| 04-resultados | rascunho | 2.484 / 2.800 | 2 `[[VERIFICAR]]` · 3 `[[CIT]]` |
| 05-conclusao | não iniciada | 0 / 700 | — |
| 06-declaracoes | não iniciada | 0 / 100 | — |

Gate: **0 bloqueantes**, 17 pendências. Estimativa do gate: **11,8 páginas**.
**PDF real: 9 páginas** — a diferença são as seis figuras, que ainda não existem.
As cinco seções que faltam somam ~4.050 palavras de alvo. O aperto final será no teto.

### Lacunas de `04-resultados`

| Linha | Marcador | Pergunta | Quem resolve |
|---|---|---|---|
| 123 | `[[VERIFICAR]]` | quantos discentes `/discentes_aptos_certificacao/` retorna, e em que data? | consulta ao banco |
| 195 | `[[VERIFICAR]]` | há medição de tempo de inicialização a frio? | autor |
| 221 | `[[CIT]]` | explicitação de regra implícita como ganho de governança | levantamento |
| 231 | `[[CIT]]` | devolutiva dirigida vs. adaptativa | levantamento |
| 238 | `[[CIT]]` | transferibilidade de arquitetura entre contextos | levantamento |

Os três `[[CIT]]` caem na busca da próxima sessão. Os dois `[[VERIFICAR]]` são acréscimos,
não bloqueios.

## Figuras — 6 declaradas, **nenhuma produzida**

| ID | O que é | Onde |
|---|---|---|
| `TAB:03-1` | Quadro editável das 10 competências avaliadas | 03 |
| `FIG:03-1` | Diagrama de arquitetura (n8n + API + banco + Google Workspace) | 03 |
| `FIG:03-2` | DER das 7 entidades do domínio | 03 |
| `TAB:04-1` | Snapshot agregado do banco em 27/07/2026 | 04 |
| `FIG:04-1` | Autoavaliações por unidade (33×5, depois 7, 3, 1, 1) | 04 |
| `TAB:04-2` | Tempos: manual 40 min · 2024 ≈12 s · registro 2–3 s · gráfico 12–15 s | 04 |

No PDF elas aparecem como blocos "IMAGEM AUSENTE" com a descrição do que produzir.
⚠️ 300 dpi e texto interno em TNR ≥18. As três `TAB` são markdown editável, nunca imagem.

## Build — funcionando de ponta a ponta

```bash
bash scripts/build.sh        # gate → build/artigo.md → .docx → .pdf (com nº de páginas)
bash scripts/build.sh --md   # só o markdown consolidado
```

- `scripts/reference-abnt.docx` — estilos do build: TNR 11, espaçamento simples, recuo 1 cm
- `scripts/formato_principia.py` — injeta A4 e margens no `.docx`; o pandoc 2.9 não copia o
  `sectPr` do reference-doc e emite `<w:sectPr />` autofechada
- ⚠️ **O modelo oficial não serve de reference-doc.** Ele formata por formatação direta,
  com `Normal` vazio (cairia em Arial 11, espaçamento 1,15) e títulos em 20/16 pt. É o
  destino de colagem da etapa 7, não a fonte de estilos do build

## Bloqueios

1. **Referencial sem literatura revisada por pares.** `refs.md` tem 16 entradas, todas de
   documentação técnica e gestão de projetos, **10 ainda órfãs**. É a fragilidade que um
   avaliador aponta primeiro. Resolve na próxima sessão.

## Próxima sessão — roteiro

1. Busca dirigida: 6 a 10 referências revisadas por pares, **≥2019**, com DOI, sobre
   automação de fluxos acadêmico-administrativos, low-code/no-code em instituições de
   ensino e mensuração de soft skills em programas de formação. Campo `origem` obrigatório.
2. Fechar os três `[[CIT]]` de `04-resultados`.
3. `/escrever-secao 02-referencial` (alvo 1.600).

## Ambiente

- ✅ `pandoc` 2.9.2.1 e `libreoffice` instalados — build completo, com PDF
- ✅ **Modelo oficial da revista:** `docs/Diretrizes_publicacao_Revista_Principia_Dez2024-OTH-1.docx`.
  É o "Modelo **e** diretrizes", e esteve em `docs/` desde 27/07/2026 — as sessões
  anteriores o davam como não baixado, o que era falso. Dele saíram as margens do build
- ⚠️ Banco Neon **inacessível em 03/09/2026** (host não resolveu por DNS). Último snapshot
  válido é o de 27/07/2026. Confirmar se a instância existe antes de prometer consulta
- ✅ API corrigida (D-15) — falta o autor rodar `manage.py check` e os testes no ambiente
  da API, e publicar
