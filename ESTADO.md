# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 3 — escrita. Cinco das sete seções em rascunho. **Gate: 1 pendência (exit 2).**
**Atualizado:** 13/09/2026 (sessão 9)
**Próxima ação:** `/escrever-secao 06-declaracoes` (alvo 100). São as três seções não
numeradas exigidas pela revista: Agradecimentos (equipe não-autora, 11 integrantes contra 4
autores), Financiamento e Conflito de interesses. Fontes no mapa de fatos §1 e §3. Não
depende de nada nem de ninguém.

Depois dela, **`/revisar-artigo`** — o review completo contra o checklist, antes do resumo.
O `00-resumo` é o último de todos, por regra: ele precisa refletir o texto final, e o texto
ainda passa pela orientadora.

**O autor precisa providenciar:** nada. Não há decisão em aberto nem bloqueio.

## O artigo

- **Veículo:** Revista Principia — artigo original · **12 a 18 páginas** (alvo 16)
- **Título (D-18):** "Automação de certificação e recomendação pedagógica em programa de capacitação profissional: da geração de indicadores à camada de decisão" · EN: "Automating certification and pedagogical recommendation in a professional training program: from indicator generation to the decision layer"
- **Prazo:** fluxo contínuo, sem data-limite (D-20)
- **Tese:** aprovada — automação do ciclo formativo exige camada de decisão
  (certificação) e de intervenção (recomendação) sobre persistência estruturada
- **Contribuição sobre 2024:** o ciclo anterior automatizou indicadores; este entrega as
  camadas de decisão e de intervenção sobre persistência com rastreabilidade histórica,
  mais a migração de infraestrutura
- **Autores (4, fechado em D-19):** Gabriel Macaúbas Melo · Juliana Ferreira Cavalcante ·
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
| D-8 | Levantamento bibliográfico adiado para depois de método e resultados — cumprido na sessão 7 |
| D-10 | Certificação: a camada de decisão está implementada e exposta, mas seu acoplamento à emissão não tem evidência; o artigo diz isso |
| D-11 | Snapshot do banco de 27/07/2026 é a base numérica, sempre com data |
| D-12 | Reconfirmado o valor de 40 min |
| D-13 · D-14 | Vale o código, não o relatório: sem `bulk_create`/`select_related`; base serviu também de ambiente de teste |
| D-15 | Corrigir os dois defeitos da API (`except` mascarando falha; rota de exclusão total) |
| D-16 | Ressalva sobre a base **enxugada ao mínimo**, mantida em uma frase |
| D-17 | **8 referências órfãs removidas** de `refs.md` (23 → 15); só constam fontes citadas |
| D-18 | **Título definido**, PT e EN (ver acima) |
| D-19 | **Autoria fechada em 4** — as duas vagas restantes não serão usadas |
| D-20 | Revista em **fluxo contínuo**, sem data-limite |
| D-21 | A correção da API (D-15) **não entra na conclusão** — recorte temporal do artigo é 2025 |
| D-22 | **Instância Neon apagada**; contagem de aptos não será apurada, argumento reancorado nos 49 pares |
| D-23 | Os tempos reportados (2–3 s · 12–15 s) **já incluem inicialização a frio** |
| D-24 | n8n rodava em **máquina pessoal** de um integrante — declarado como limitação em 4.6 |
| D-25 | Repositório publicado como **público** no GitHub, sem depuração prévia (riscos aceitos e listados no `LOG.md`) |

## Decisões pendentes

**Nenhuma.**

## Seções

| Arquivo | Status | Palavras (real/alvo) | Lacunas abertas |
|---|---|---|---|
| 00-resumo | não iniciada | 0 / 550 | escrever **por último**, depois da revisão |
| 01-introducao | rascunho | 1.085 / 1.100 | nenhuma |
| 02-referencial | rascunho | 1.561 / 1.600 | nenhuma |
| 03-metodo | rascunho | 2.002 / 2.200 | nenhuma |
| 04-resultados | rascunho | 2.786 / 2.800 | nenhuma |
| 05-conclusao | **rascunho** (sessão 9) | 747 / 700 | nenhuma |
| 06-declaracoes | **próxima** | 0 / 100 | — |

Total de texto: **8.181 palavras**. Nenhuma seção traz `[[VERIFICAR]]`, `[[CIT]]` ou
`[[DECIDIR]]`.

Estilo, todas as seções dentro do perfil do grupo (21–30 pal/frase, 60–105 por parágrafo):
introdução 27,1 · referencial 29,3 · método 22,2 · resultados 27,9 · **conclusão 26,7**.

## Orçamento — a pendência única do gate

| | Páginas |
|---|---|
| Estimativa do gate hoje (5 seções + 6 figuras + 15 refs) | **16,9** |
| Falta escrever: declarações 100 + resumo/abstract 550 | +0,9 |
| **Projeção final** | **≈17,8** |

Dentro da janela de 12 a 18, **acima do alvo de 16** — é exatamente isso que o gate acusa
como pendência, e era o previsto desde a sessão 8 (projetava 17,7). Não bloqueia nada, mas
consome a folga: o artigo chega ao teto com ~0,2 página sobrando.

Se a revisão da orientadora fizer o texto crescer, a primeira fonte de folga continua sendo
**fundir `FIG:04-1` em `TAB:04-1`** (~0,3 página), que mostram o mesmo fenômeno. A segunda é
a conclusão, que está 47 palavras acima do alvo.

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

## Referências — 15 entradas, todas citadas

Zero órfãs. Onze dentro da janela de sete anos contra quatro fora, todas as de fora
fundacionais: Fielding define REST, Merkel define Docker, Groover define automação e Elmasri
é o texto de referência em bancos de dados. A conclusão não acrescentou nenhuma — ela retoma
o que as seções 3 e 4 sustentam com dado próprio.

## Build — funcionando de ponta a ponta

```bash
bash scripts/build.sh        # gate → build/artigo.md → .docx → .pdf (com nº de páginas)
bash scripts/build.sh --md   # só o markdown consolidado
```

⚠️ Os artefatos em `build/` são de 03/09/2026 e **não contêm a conclusão**. Regerar antes de
qualquer leitura completa do artigo.

- `scripts/reference-abnt.docx` — estilos do build: TNR 11, espaçamento simples, recuo 1 cm
- `scripts/formato_principia.py` — injeta A4 e margens no `.docx`; o pandoc 2.9 não copia o
  `sectPr` do reference-doc e emite `<w:sectPr />` autofechada
- ⚠️ **O modelo oficial não serve de reference-doc.** Ele formata por formatação direta,
  com `Normal` vazio (cairia em Arial 11, espaçamento 1,15) e títulos em 20/16 pt. É o
  destino de colagem da etapa 7, não a fonte de estilos do build

## Bloqueios

**Nenhum bloqueia a escrita.** Duas condições permanentes, já absorvidas pelo texto:

- **O banco Neon foi apagado (D-22).** Nenhuma consulta nova é possível. `/consultar-banco`
  está encerrado como recurso, e o snapshot agregado de 27/07/2026 (mapa de fatos §6) é a
  única base numérica do artigo. Qualquer número novo teria de vir de outra fonte com
  procedência.
- **A API corrigida (D-15) segue sem validação em ambiente com Django.** Não importa mais
  para o artigo, porque D-21 a manteve fora do texto. Continua sendo trabalho de engenharia
  a fazer, se o autor quiser publicar a correção.

## Ambiente

- ✅ `pandoc` 2.9.2.1 e `libreoffice` instalados — build completo, com PDF
- ✅ **Modelo oficial da revista:** `docs/Diretrizes_publicacao_Revista_Principia_Dez2024-OTH-1.docx`.
  É o "Modelo **e** diretrizes". Dele saíram as margens do build
