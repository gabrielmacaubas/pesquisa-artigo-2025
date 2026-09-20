# ESTADO — leia isto primeiro

> Retrato do agora, reescrito ao final de cada sessão. Histórico acumulado em `LOG.md`.

---

## Situação atual

**Etapa:** 4 — **o artigo existe inteiro e o PDF está diagramado**. Sete seções, **nove
figuras/quadros/tabelas**, `.docx` e `.pdf` gerados. Gate: 1 pendência (exit 2).
**Atualizado:** 20/09/2026 (sessão 14 — figuras sintéticas trocadas por artefatos reais)
**Próxima ação:** **`/revisar-artigo`** — segunda passada de review sobre o artigo completo.
Depois dela, mandar `build/artigo.pdf` para a orientadora.

**O autor precisa decidir:** se aceita a fonte interna das figuras (ver **Figuras**). Só
isso, e não bloqueia nada.

⚠️ **`build/artigo.pdf` regerado em 20/09/2026: 19 páginas reais — uma acima do teto da
revista.** É consequência direta de D-30, decisão consciente do autor para caber as quatro
imagens de artefato real. **Como está, a Principia rejeita na triagem sem avaliar.** Para
voltar às 18: cortar ~460 palavras, ou dispensar uma figura (a `FIG:03-1`, diagrama de
arquitetura, é a candidata — o fluxo real em `FIG:03-3` cobre parte do que ela mostra).

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
| D-26 | **Agradecimentos anônimos** na submissão — sem nomes e sem instituição, por causa do duplo-cego |
| D-27 | **Financiamento:** repete "Esta pesquisa não recebeu financiamento" de 2024; os editais são vínculo, não repasse |
| D-28 | Pseudocódigo de 3.4 **corrigido** para espelhar o código, sem parágrafo explicativo; 4.5 permanece |
| D-29 | **`FIG:04-1` fundida em `TAB:04-1`** — cinco figuras; libera 0,3 pág que as correções consumiram |
| D-30 | **Teto de páginas elevado a 20** para caber quatro imagens de artefato real, e as duas figuras sintéticas foram descartadas. ⚠️ Diverge da norma do veículo, que rejeita acima de 18 |

## Decisões pendentes

**Uma, e não é bloqueante:** de onde tirar folga de orçamento, se o autor quiser entrar na
revisão da orientadora com margem. Ver **Orçamento**.

## Seções — todas escritas

| Arquivo | Status | Palavras (real/alvo) | Lacunas abertas |
|---|---|---|---|
| 00-resumo | rascunho | 612 / 550 | nenhuma |
| 01-introducao | revisada | 1.102 / 1.100 | nenhuma |
| 02-referencial | revisada | 1.561 / 1.600 | nenhuma |
| 03-metodo | revisada | 2.072 / 2.200 | nenhuma |
| 04-resultados | revisada | 2.931 / 2.800 | nenhuma |
| 05-conclusao | revisada | 747 / 700 | nenhuma |
| 06-declaracoes | revisada | 105 / 100 | nenhuma |

Total de texto: **9.136 palavras**. Nenhuma seção traz `[[VERIFICAR]]`, `[[CIT]]` ou
`[[DECIDIR]]`.

O `00-resumo` reúne título PT, resumo, palavras-chave, título EN, abstract e keywords. O
resumo tem **294 palavras** e o abstract **295**, ambos dentro da janela de 200 a 300 da NBR
6028, em parágrafo único e sem citação. Palavras-chave em minúsculas, separadas por ponto e
vírgula, em ordem alfabética nas duas línguas: *automação de processos; avaliação de
competências socioemocionais; baixo código; certificação; rastreabilidade histórica*.

Estilo, todas as seções dentro do perfil do grupo (21–30 pal/frase, 60–105 por parágrafo):
resumo 27,8 · introdução 27,6 · referencial 29,3 · método 22,8 · resultados 28,7 ·
conclusão 26,7 · declarações 26,2. O resumo aparece com 294 pal/parágrafo porque a NBR 6028
exige parágrafo único — é esperado, não é desvio.

## Orçamento — a pendência única do gate

| | Páginas |
|---|---|
| Texto (9.136 palavras) | 13,0 |
| Figuras (5) | 1,9 |
| Referências (15) | 3,0 |
| **Estimado pelo gate** | **18,7** |
| **Real, no PDF de 20/09/2026** | **19** |

O número que vale é o do documento formatado: **19 páginas reais**, uma acima do teto da
revista, por D-30. O modelo do gate foi calibrado contra esse PDF nesta sessão e agora bate com ele
(17,9 contra 18): as referências passaram de 5 para 15 por página, que é o que elas
realmente ocupam, e entrou uma linha explícita de **folga de diagramação, 1,2 página** — o
espaço que figura empurrada para a página seguinte, linha órfã e respiro de título consomem
e que o modelo antes ignorava.

**O manuscrito está fora da norma enquanto tiver 19 páginas.** Para voltar às 18, em ordem
de menor dano:

1. Dispensar a `FIG:03-1`, o diagrama de arquitetura → **0,40 pág**. O fluxo real da
   `FIG:03-3` cobre parte do que ela mostra, e a arquitetura está descrita em prosa
2. Seção 4, 203 palavras acima do alvo → **0,29 pág**
3. Conclusão, 47 palavras acima do alvo → **0,07 pág**
4. Reduzir a largura de impressão das três capturas, que hoje sobram em dpi → **~0,10 pág**

Nesta sessão já foram usadas duas fontes: o Quadro 1 e a Tabela 1 foram remontados em dois
pares de colunas (de 12 e 16 cm para 7 e 8 cm), e um parágrafo de 93 palavras saiu de 4.1. A fonte prevista antes (fundir `FIG:04-1`) já foi
usada em D-29.

## Figuras — 5 declaradas, **5 prontas**

| ID | Rótulo no artigo | Arquivo | O que é |
|---|---|---|---|
| `TAB:03-1` | **Quadro 1** | `figuras/tab-03-1.md` | As 10 competências avaliadas, macro e subcompetências |
| `FIG:03-1` | **Figura 1** | `figuras/fig-03-1.png` | Arquitetura em quatro faixas: entrada, fluxos, núcleo, saída |
| `FIG:03-2` | **Figura 2** | `figuras/fig-03-2.png` | DER das 8 entidades, com cardinalidades e nota de auditoria |
| `TAB:04-1` | **Tabela 1** | `figuras/tab-04-1.md` | Snapshot agregado de 27/07/2026, com a distribuição pelas 9 unidades |
| `TAB:04-2` | **Tabela 2** | `figuras/tab-04-2.md` | Tempos: manual 40 min · 2024 ≈12 s · registro 2–3 s · gráfico 12–15 s |
| `FIG:03-3` | **Figura 3** | `figuras/fig-03-3.png` | Fluxo de emissão no n8n — **captura real**, endpoints suprimidos |
| `FIG:04-1` | **Figura 4** | `figuras/fig-04-1.png` | Relatório de perfil gerado pelo fluxo — **real**, nome do discente suprimido |
| `FIG:04-2` | **Figura 5** | `figuras/fig-04-2.png` | Frente do modelo de certificado — **real**, identificação institucional suprimida |
| `FIG:04-3` | **Figura 6** | `figuras/fig-04-3.png` | Verso do modelo de certificado — **real**, idem |

As quatro últimas vêm de **artefato real do projeto** (D-30), extraídas dos PDFs em `docs/`
por `scripts/figuras_reais.py`, que também aplica as supressões. Substituíram as duas
figuras sintéticas da sessão 13, que foram descartadas.

⚠️ **O que foi suprimido, e por quê:** nome de discente no relatório de perfil
(`dados-e-privacidade.md`); nome da instituição, cidade e nomes de servidores no certificado
(**avaliação cega** — sem isso o manuscrito identifica os autores); endereços de endpoint no
fluxo do n8n (`dados-e-privacidade.md`, regra 4). O modelo de certificado é reproduzido com
as marcações `{{nome}}` e `{{cpf}}` no lugar, e não preenchido — não há dado de discente
nele.

⚠️ **Risco que fica:** as três capturas têm texto interno bem abaixo dos 18 pt que a revista
exige para figura. O manuscrito de 2024, do mesmo grupo, usou capturas nas mesmas condições
e foi submetido assim.

As três `TAB` são markdown editável, nunca imagem — exigência da revista. Os dois `.png`
saem de `python3 scripts/figuras.py`, que os regera do zero em **300 dpi**, com texto
interno em **18,2 pt** (o mínimo da revista é 18).

⚠️ **Decisão do autor:** o texto interno das figuras está em **Liberation Serif**, que é
metricamente compatível com a Times New Roman mas não é ela. A TNR não está instalada nesta
máquina. Ou se aceita a substituição, ou se regera `scripts/figuras.py` em máquina com a
fonte, trocando as constantes `REG` e `BOL`.

**Quadro e tabela têm sequências próprias** no artigo, como a revista exige: o quadro de
competências é Quadro 1, e as duas da seção 4 são Tabela 1 e Tabela 2. O bloco declara isso
pelo campo `rotulo:`.

## Referências — 15 entradas, todas citadas

Zero órfãs. Onze dentro da janela de sete anos contra quatro fora, todas as de fora
fundacionais: Fielding define REST, Merkel define Docker, Groover define automação e Elmasri
é o texto de referência em bancos de dados. O resumo não acrescentou referência — não pode,
por norma.

## Dívidas registradas

⚠️ **Dívida de D-28:** a subseção 4.5 sustenta que codificar o critério o tornou auditável,
sem registrar o que a inspeção do código encontrou — o agrupamento de inteligência emocional
produz dois conjuntos contra um denominador de sete, e no ramo das subcompetências a
comparação ocorre entre atributos de uma mesma avaliação, não entre unidades. O autor optou
por corrigir só o pseudocódigo. O repositório é público (D-25), então o comportamento é
verificável por um avaliador.

⚠️ **Dívida de D-26, para a versão final e não para a submissão:** os Agradecimentos estão
anônimos de propósito. A equipe é de 11 integrantes contra 4 autores (mapa de fatos §3), e
os **7 nomes não-autores têm de ser acrescentados depois do aceite**. O próprio texto da
seção declara a omissão, para que ela não seja lida como descuido.

## Build — funcionando de ponta a ponta

```bash
bash scripts/build.sh        # gate → build/artigo.md → .docx → .pdf (com nº de páginas)
bash scripts/build.sh --md   # só o markdown consolidado
```

✅ Regerado em 20/09/2026 com o artigo inteiro: **17 páginas reais**, 7 seções, 5
figuras/tabelas, 15 referências. `build/artigo.pdf` é o arquivo para mandar à orientadora.

- `scripts/figuras.py` — gera os dois diagramas em 300 dpi (arquitetura e DER)
- `scripts/figuras_reais.py` — **novo**, extrai as quatro imagens de artefato real dos PDFs
  em `docs/`, aplica as supressões e grava com o dpi que dá a largura de impressão desejada.
  É o único lugar onde as supressões existem: refazer a figura sem ele republica o que foi
  suprimido
- `scripts/build.py` — tabela e quadro entram como markdown editável, com título acima e
  `Fonte:` abaixo; figura leva o título abaixo (NBR 14724)
- `scripts/preparar_reference.py` — **novo**, injeta no `reference-abnt.docx` os estilos que
  faltavam (legenda, fonte da ilustração, pseudocódigo, abstract em itálico) e corrige os
  que vinham errados do pandoc. Idempotente; rodar depois de qualquer troca do template
- `scripts/formato_principia.py` — além da página A4, agora dá largura e grade às tabelas.
  Sem isso o pandoc 2.9 emite `<w:tblGrid/>` vazio e o LibreOffice joga todas as colunas
  menos a primeira para fora da margem direita

- `scripts/reference-abnt.docx` — estilos do build: TNR 11, espaçamento simples, recuo 1 cm
- `scripts/formato_principia.py` — injeta A4 e margens no `.docx`; o pandoc 2.9 não copia o
  `sectPr` do reference-doc e emite `<w:sectPr />` autofechada
- ⚠️ **O modelo oficial não serve de reference-doc.** Ele formata por formatação direta,
  com `Normal` vazio (cairia em Arial 11, espaçamento 1,15) e títulos em 20/16 pt. É o
  destino de colagem da etapa 7, não a fonte de estilos do build

## Bloqueios

**Nenhum bloqueia a revisão.** Três condições permanentes, já absorvidas pelo texto:

- **O banco Neon foi apagado (D-22).** Nenhuma consulta nova é possível. `/consultar-banco`
  está encerrado como recurso, e o snapshot agregado de 27/07/2026 (mapa de fatos §6) é a
  única base numérica do artigo. Qualquer número novo teria de vir de outra fonte com
  procedência.
- **A API corrigida (D-15) segue sem validação em ambiente com Django.** Não importa mais
  para o artigo, porque D-21 a manteve fora do texto.
- **A estimativa do gate fica acima do alvo de 16** enquanto o texto tiver este tamanho.
  O PDF real tem 17 páginas, dentro da janela.

## Git

- **Há remote** (D-25): `origin` = `git@github-pessoal:gabrielmacaubas/pesquisa-artigo-2025.git`,
  público. O `CLAUDE.md` ainda diz "repositório local, sem remote" — está desatualizado.
- **`master` está 5 commits à frente de `origin/master`** (conclusão, declarações, review
  aplicado, gitignore e este). Nada foi enviado: o push é decisão do autor, e o repositório
  é público.

## Ambiente

- ✅ `pandoc` 2.9.2.1 e `libreoffice` instalados — build completo, com PDF
- ✅ **Modelo oficial da revista:** `docs/Diretrizes_publicacao_Revista_Principia_Dez2024-OTH-1.docx`.
  É o "Modelo **e** diretrizes". Dele saíram as margens do build
