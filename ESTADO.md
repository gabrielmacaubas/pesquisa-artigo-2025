# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 3 — escrita. Quatro das sete seções em rascunho. **Gate LIMPO (exit 0).**
**Atualizado:** 03/09/2026 (sessão 8)
**Próxima ação:** `/escrever-secao 05-conclusao` (alvo 700). Tudo de que ela depende já
existe: introdução, método e resultados escritos. A conclusão retoma o objetivo declarado
na introdução, sintetiza o que a evidência sustenta e declara os desdobramentos — **sem
afirmar nada que a seção 4 não sustente**, em especial sobre acoplamento da certificação
(D-10) e sobre escala.

⚠️ **Observar D-21 ao escrever:** a conclusão **não** menciona a correção da API (D-15),
nem como trabalho futuro. O ciclo relatado é o de 2025, e a correção é posterior.

**O autor precisa providenciar:** nada. Não há decisão em aberto nem bloqueio — as oito
pendências que restavam foram resolvidas em 03/09/2026 (D-17 a D-24).

## O artigo

- **Veículo:** Revista Principia — artigo original · **12 a 18 páginas** (alvo 16)
- **Título (D-18):** "Automação de certificação e recomendação pedagógica em programa de capacitação profissional: da geração de indicadores à camada de decisão" · EN: "Automating certification and pedagogical recommendation in a professional training program: from indicator generation to the decision layer"
- **Prazo:** fluxo contínuo, sem data-limite (D-20)
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
| D-17 | **8 referências órfãs removidas** de `refs.md` (23 → 15); só constam fontes citadas |
| D-18 | **Título definido**, PT e EN (ver acima) |
| D-19 | **Autoria fechada em 4** — as duas vagas restantes não serão usadas |
| D-20 | Revista em **fluxo contínuo**, sem data-limite |
| D-21 | A correção da API (D-15) **não entra na conclusão** — recorte temporal do artigo é 2025 |
| D-22 | **Instância Neon apagada**; contagem de aptos não será apurada, argumento reancorado nos 49 pares |
| D-23 | Os tempos reportados (2–3 s · 12–15 s) **já incluem inicialização a frio** |
| D-24 | n8n rodava em **máquina pessoal** de um integrante — declarado como limitação em 4.6 |

## Decisões pendentes

**Nenhuma.** As cinco que constavam aqui foram resolvidas em 03/09/2026: título (D-18),
autoria (D-19), menção à correção da API (D-21), destino das órfãs (D-17) e corte de páginas
(resolvido por D-17, que sozinho eliminou o excesso).


## Seções

| Arquivo | Status | Palavras (real/alvo) | Lacunas abertas |
|---|---|---|---|
| 00-resumo | não iniciada | 0 / 550 | escrever **por último** |
| 01-introducao | rascunho | 1.085 / 1.100 | nenhuma |
| 02-referencial | rascunho | 1.561 / 1.600 | nenhuma |
| 03-metodo | rascunho | 2.002 / 2.200 | nenhuma |
| 04-resultados | rascunho | 2.786 / 2.800 | nenhuma |
| 05-conclusao | **próxima** | 0 / 700 | — |
| 06-declaracoes | não iniciada | 0 / 100 | — |

Gate: **LIMPO — exit 0**, zero bloqueantes e zero pendências, pela primeira vez no projeto.
Total de texto: **7.434 palavras**.

Estilo, todas as seções dentro do perfil do grupo (21–30 pal/frase, 60–105 por parágrafo):
introdução 27,1 · referencial 29,3 · método 22,2 · resultados 27,9.

### Lacunas remanescentes

**Nenhuma.** Os dois `[[VERIFICAR]]` de `04-resultados` foram fechados por D-22 e D-23, e a
tríade de `03-metodo` foi reescrita em dois pares. Não há `[[VERIFICAR]]`, `[[CIT]]` nem
`[[DECIDIR]]` em nenhuma seção.

## Orçamento — resolvido

| | Páginas |
|---|---|
| Estimativa do gate hoje (4 seções + 6 figuras + 15 refs) | **15,8** |
| Falta escrever: conclusão 700 + declarações 100 + resumo/abstract 550 | +1,9 |
| **Projeção final** | **≈17,7** |

Dentro da janela de 12 a 18. **A remoção das 8 órfãs (D-17) sozinha resolveu o estouro**,
que na sessão anterior projetava ~19,1. Não é necessário cortar figuras nem conteúdo.

A folga é de ~0,3 página, então vale a regra de sempre: escrever as três seções restantes no
alvo. Se a revisão da orientadora fizer o texto crescer, a primeira fonte de folga é fundir
`FIG:04-1` em `TAB:04-1`, que mostram o mesmo fenômeno (~0,3 página).

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

Zero órfãs (D-17 removeu as 8). Onze dentro da janela de sete anos contra quatro fora, todas
as de fora fundacionais: Fielding define REST, Merkel define Docker, Groover define
automação e Elmasri é o texto de referência em bancos de dados. As 7 revisadas por pares
acrescentadas na sessão 7 sustentam o referencial.

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

**Nenhum bloqueia a escrita.** Um item mudou de natureza e vale registrar:

- **O banco Neon foi apagado (D-22).** Não é mais um bloqueio a resolver, é uma condição
  permanente: **nenhuma consulta nova é possível**. `/consultar-banco` está encerrado como
  recurso, e o snapshot agregado de 27/07/2026, registrado no mapa de fatos §6, é a única
  base numérica do artigo. Qualquer número novo teria de vir de outra fonte com procedência.
- **A API corrigida (D-15) segue sem validação em ambiente com Django.** Deixou de importar
  para o artigo, porque D-21 a manteve fora do texto. Continua sendo trabalho de engenharia
  a fazer, se o autor quiser publicar a correção.

## Ambiente

- ✅ `pandoc` 2.9.2.1 e `libreoffice` instalados — build completo, com PDF
- ✅ **Modelo oficial da revista:** `docs/Diretrizes_publicacao_Revista_Principia_Dez2024-OTH-1.docx`.
  É o "Modelo **e** diretrizes". Dele saíram as margens do build
