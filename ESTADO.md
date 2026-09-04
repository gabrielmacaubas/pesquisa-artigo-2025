# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 3 — escrita. Quatro das sete seções em rascunho.
**Atualizado:** 03/09/2026 (sessão 8)
**Próxima ação:** `/escrever-secao 05-conclusao` (alvo 700). Tudo de que ela depende já
existe: introdução, método e resultados escritos. A conclusão retoma o objetivo declarado
na introdução, sintetiza o que a evidência sustenta e declara os desdobramentos — **sem
afirmar nada que a seção 4 não sustente**, em especial sobre acoplamento da certificação
(D-10) e sobre escala.

⚠️ **Escrever no alvo, sem folga.** O orçamento está em 17,2 páginas e a projeção final é
de ~19 — o aperto é no teto (ver Orçamento).

**O autor precisa providenciar:** nada para a próxima seção. Três itens dependem dele, e
nenhum bloqueia (ver Bloqueios e Decisões pendentes).

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
- [ ] **Destino das 8 referências órfãs** — a Introdução não as absorveu (ver abaixo)
- [ ] **Onde cortar para caber em 18 páginas** — decisão de escopo, não de redação

## Seções

| Arquivo | Status | Palavras (real/alvo) | Lacunas abertas |
|---|---|---|---|
| 00-resumo | não iniciada | 0 / 550 | escrever **por último** |
| 01-introducao | rascunho | 1.085 / 1.100 | nenhuma |
| 02-referencial | rascunho | 1.561 / 1.600 | nenhuma |
| 03-metodo | rascunho | 1.994 / 2.200 | 1 tríade (linha 183) |
| 04-resultados | rascunho | 2.631 / 2.800 | 2 `[[VERIFICAR]]` |
| 05-conclusao | **próxima** | 0 / 700 | — |
| 06-declaracoes | não iniciada | 0 / 100 | — |

Gate: **0 bloqueantes**, 12 pendências. Total de texto: **7.271 palavras**.

Estilo, todas as seções dentro do perfil do grupo (21–30 pal/frase, 60–105 por parágrafo):
introdução 27,1 · referencial 29,3 · método 22,4 · resultados 27,7.

### Lacunas remanescentes

| Arquivo:linha | Marcador | Pergunta | Quem resolve |
|---|---|---|---|
| 04-resultados:123 | `[[VERIFICAR]]` | quantos discentes `/discentes_aptos_certificacao/` retorna, e em que data? | consulta ao banco |
| 04-resultados:195 | `[[VERIFICAR]]` | há medição de tempo de inicialização a frio? | autor |
| 03-metodo:183 | tríade | "físicas, matrícula e endereços" — reescrever para dois itens | redação |

Ambos os `[[VERIFICAR]]` são acréscimos, não bloqueios.

## ⚠️ Orçamento — o aperto é no teto

| | Páginas |
|---|---|
| Estimativa do gate hoje (4 seções + 6 figuras + 23 refs) | **17,2** |
| Falta escrever: conclusão 700 + declarações 100 + resumo/abstract 550 | +1,9 |
| **Projeção final** | **≈19,1** |

O máximo da revista é **18**. Serão necessárias ~1,1 página de corte, e a regra de
`orcamento-paginas.md` diz onde: detalhe de implementação vira pseudocódigo, referencial
que não sustenta a contribuição sai, figuras redundantes se fundem. **Nunca cortar**
limitações, origem dos dados ou a discussão à luz da literatura.

Duas fontes de folga já identificadas, ambas decisão do autor:
1. **As 6 figuras custam 2,2 páginas.** `FIG:04-1` (autoavaliações por unidade) mostra o
   mesmo fenômeno que uma linha de `TAB:04-1`; fundi-las libera ~0,3 página.
2. **As 8 referências órfãs custam ~1,6 página** se permanecerem na lista. Removê-las
   resolve mais da metade do excesso — e a revista **exige** que só constem fontes
   citadas, então removê-las não é só economia, é conformidade.

## Referências órfãs (8) — a Introdução não as absorveu

`Bendoraitis 2020` · `Django REST Framework 2026` · `Kanban University 2025` ·
`Muniz 2021` · `Pahl 2015` · `PMI 2017` · `Scrum 2025` · `Trello 2025`.

A sessão 7 previu que a Introdução as citaria. **Não aconteceu, e por decisão de redação:**
são referências de stack (Django, DRF, Docker/PaaS, Trello) e de gestão de projetos (PMBOK,
Scrum, Kanban), e nenhuma tem terreno legítimo num texto de problema, lacuna e objetivo.
Forçá-las ali seria citação decorativa, exatamente o que um avaliador identifica.

Restam duas saídas, e a escolha é do autor:
- **Citar no Método**, onde cabem de fato — a equipe trabalhou com Scrum (mapa §14) e a
  stack é descrita em 3.2. Custa palavras numa seção que está 206 abaixo do alvo.
- **Remover de `refs.md`** — libera ~1,6 página do orçamento estourado e atende à exigência
  da revista. É a saída que o orçamento recomenda.

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

## Referências — 23 entradas

17 dentro da janela de sete anos contra 6 fora (obras fundacionais). As 7 revisadas por
pares acrescentadas na sessão 7 fecharam a lacuna do referencial. Ver a ressalva das 8
órfãs acima.

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

Nenhum bloqueia a escrita. Três itens dependem do autor:

1. **Banco Neon inacessível em 03/09/2026** (host não resolveu por DNS). Enquanto não
   voltar, o `[[VERIFICAR]]` da linha 123 de `04-resultados` fica aberto. Confirmar se a
   instância ainda existe antes de prometer consulta.
2. **API corrigida (D-15) ainda não validada em ambiente com Django.** Falta o autor rodar
   `manage.py check` e os testes, e publicar.
3. **Decisão de corte para caber em 18 páginas** — pode esperar até `06-declaracoes`, mas
   não até o resumo.

## Ambiente

- ✅ `pandoc` 2.9.2.1 e `libreoffice` instalados — build completo, com PDF
- ✅ **Modelo oficial da revista:** `docs/Diretrizes_publicacao_Revista_Principia_Dez2024-OTH-1.docx`.
  É o "Modelo **e** diretrizes". Dele saíram as margens do build
