# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 3 — escrita. Três das sete seções em rascunho.
**Atualizado:** 03/09/2026 (sessão 7)
**Próxima ação:** `/escrever-secao 01-introducao` (alvo 1.100). Tudo de que ela depende já
existe: tese fechada, referencial escrito, método e resultados em rascunho. A introdução
**tem de terminar** com um parágrafo apresentando as seções seguintes — exigência explícita
da revista. É também onde o histórico do ciclo de 2024 é narrado **sem citação** (D-2).

**O autor precisa providenciar:** nada para a próxima seção. Duas pendências dependem dele,
mas não bloqueiam (ver Bloqueios).

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
| D-8 | Levantamento bibliográfico adiado para depois de método e resultados — **cumprido na sessão 7** |
| D-10 | Certificação: a camada de decisão está implementada e exposta, mas seu acoplamento à emissão não tem evidência; o artigo diz isso |
| D-11 | Snapshot do banco de 27/07/2026 é a base numérica, sempre com data |
| D-12 | Reconfirmado o valor de 40 min |
| D-13 · D-14 | Vale o código, não o relatório: sem `bulk_create`/`select_related`; base serviu também de ambiente de teste |
| D-15 | Corrigir os dois defeitos da API (`except` mascarando falha; rota de exclusão total) |
| D-16 | Ressalva sobre a base **enxugada ao mínimo**, mantida em uma frase |

## Decisões pendentes

- [ ] Título em português e inglês
- [ ] Se as duas vagas restantes de autoria serão usadas
- [ ] Se a conclusão menciona a correção da API como trabalho posterior ao ciclo relatado

## Seções

| Arquivo | Status | Palavras (real/alvo) | Lacunas abertas |
|---|---|---|---|
| 00-resumo | não iniciada | 0 / 550 | escrever **por último** |
| 01-introducao | **próxima** | 0 / 1.100 | — |
| 02-referencial | rascunho | 1.561 / 1.600 | nenhuma |
| 03-metodo | rascunho | 1.994 / 2.200 | 1 tríade (linha 183) |
| 04-resultados | rascunho | 2.631 / 2.800 | 2 `[[VERIFICAR]]` |
| 05-conclusao | não iniciada | 0 / 700 | — |
| 06-declaracoes | não iniciada | 0 / 100 | — |

Gate: **0 bloqueantes**, 11 pendências. Estimativa do gate: **15,6 páginas**.
As quatro seções que faltam somam ~2.450 palavras de alvo, ou ~3,5 páginas. Com as figuras
já contabilizadas, a projeção é de **~19 páginas** — ou seja, **o aperto final será no
teto**, não no piso. Escrever as próximas seções no alvo, sem folga, e prever corte.

### Lacunas remanescentes

| Arquivo:linha | Marcador | Pergunta | Quem resolve |
|---|---|---|---|
| 04-resultados:123 | `[[VERIFICAR]]` | quantos discentes `/discentes_aptos_certificacao/` retorna, e em que data? | consulta ao banco |
| 04-resultados:195 | `[[VERIFICAR]]` | há medição de tempo de inicialização a frio? | autor |
| 03-metodo:183 | tríade | "físicas, matrícula e endereços" — reescrever para dois itens | redação |

Ambos os `[[VERIFICAR]]` são acréscimos, não bloqueios.

### Referências órfãs (8)

`Bendoraitis 2020` · `Django REST Framework 2026` · `Kanban University 2025` ·
`Muniz 2021` · `Pahl 2015` · `PMI 2017` · `Scrum 2025` · `Trello 2025`.

Todas são de stack e de gestão de projetos: o terreno delas é a **Introdução** (histórico
do ciclo de 2024, metodologia de trabalho da equipe) e o **Método**. Ou passam a ser
citadas ao escrever `01-introducao`, ou saem de `refs.md` — a revista só aceita na lista
as fontes efetivamente citadas.

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

## Referências — 23 entradas, lacuna do referencial fechada

`refs.md` passou de 16 para **23 entradas**. As 7 novas são revisadas por pares, de 2019 em
diante, todas com DOI, e cada uma foi verificada no Crossref ou no texto integral antes de
entrar — o campo `origem` registra qual. Proporção dentro da janela de sete anos: 17 contra
6. A fragilidade apontada desde a sessão 2 está resolvida.

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

Nenhum bloqueia a escrita. Dois itens dependem do autor e podem ser resolvidos a qualquer
momento:

1. **Banco Neon inacessível em 03/09/2026** (host não resolveu por DNS). Enquanto não
   voltar, o `[[VERIFICAR]]` da linha 123 de `04-resultados` fica aberto. Confirmar se a
   instância ainda existe antes de prometer consulta.
2. **API corrigida (D-15) ainda não validada em ambiente com Django.** Falta o autor rodar
   `manage.py check` e os testes, e publicar.

## Ambiente

- ✅ `pandoc` 2.9.2.1 e `libreoffice` instalados — build completo, com PDF
- ✅ **Modelo oficial da revista:** `docs/Diretrizes_publicacao_Revista_Principia_Dez2024-OTH-1.docx`.
  É o "Modelo **e** diretrizes". Dele saíram as margens do build
