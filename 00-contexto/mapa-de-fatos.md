# Mapa de Fatos — base factual do artigo 2025

> Extraído de `contexto-projeto.md` (dump do Gemini), do manuscrito de 2024
> (`docs/ARTIGO - PROJETO 2024 - Versão 2.docx.md`), das diretrizes da Revista Principia
> e de **consulta direta ao banco de produção** em 27/07/2026.
>
> **Todo número escrito no artigo tem de estar aqui, com procedência.** Se não está,
> vira `[[VERIFICAR]]` — nunca um valor plausível.
>
> ⚠️ **Pendente:** `docs/tcc_gabriel.pdf` e `docs/tcc_juliana.pdf` (que são **relatórios
> de estágio**, não TCCs — ver D-4) ainda **não foram lidos integralmente**. O dump do
> Gemini os resume, mas resumo não é fonte primária. Ler antes de Método e Resultados.

---

## 1. Identificação

| Item | Valor | Procedência |
|---|---|---|
| Projeto | Automação de Recomendações e Certificações de Soft Skills em Programas de Capacitação Profissional | dump §1 (TCC Gabriel) |
| Nome anterior (2024) | Automação de Atividades Repetitivas em Processos de Gerenciamento de Projetos de Software | dump §1 |
| Instituição | Instituto Federal da Paraíba (IFPB) — Unidade Acadêmica de Informação e Comunicação | dump §1 |
| Curso | Tecnologia em Sistemas para Internet | dump §1 |
| Programa | Capacitação 4.0 — Polo de Inovação IFPB / EMBRAPII | dump §1, manuscrito 2024 |
| Editais | nº 02/2024 e nº 02/2025 (fluxo contínuo) | dump §1 |
| Período | 2024–2025. Gabriel: 01/03/2024–31/12/2025 (22 meses). Juliana: out/2024–jan/2025 (4 meses) | dump §1, §6 |
| Financiamento | "Esta pesquisa não recebeu financiamento" (declarado no manuscrito de 2024) | manuscrito 2024, seção Financiamento |

## 2. Problema

- Gestão manual e descentralizada em Google Sheets; dificultava análise histórica e
  correlação evolutiva (dump §2).
- **Tempo do processo manual: 40 minutos por aluno** — valor decidido pelo autor
  (D-7, 27/07/2026), coincidente com o manuscrito de 2024. A menção a "≈1 hora" no dump
  do Gemini fica descartada. Usar 40 min em todo o artigo, sem ressalva.
- Quem sofria: mentores do Capacitação 4.0 (dump §2).

## 3. Pessoas — autoria definida (D-3)

Assinam o artigo (limite Principia = 6; definidos 4):

| Nome | Papel | Procedência |
|---|---|---|
| Gabriel Macaúbas Melo | autor do TCC de backend/API; desenvolvedor backend | dump §3 |
| Juliana Ferreira Cavalcante | autora do trabalho de automação de certificados (n8n) | dump §3, §7 |
| Heremita Brasileiro Lira (Dra.) | orientadora, coordenadora do projeto | dump §3 |
| Francisco Petrônio | orientador/coordenador técnico | dump §3 |

Equipe total do projeto: 11 integrantes (dump §3, §6). Demais nomes vão em
**Agradecimentos**, não em autoria.
⚠️ Submissão é **cega**: o manuscrito não pode identificar autores nem filiação.

## 4. Arquitetura

### Ciclo 2024 (escopo do manuscrito anterior)
n8n + Google Sheets + API Django REST + **QuickChart** + Google Drive. Dois fluxos:
cadastro de notas e geração de gráficos radar + tabelas (manuscrito 2024, §4 e conclusão).

### Ciclo 2025 (escopo DESTE artigo)
| Componente | Detalhe | Procedência |
|---|---|---|
| Backend | Django 4.2.11 + Django REST Framework 3.15.1, Python 3.9/3.12 | dump §5 |
| Banco | PostgreSQL 15 | dump §5 |
| **Migração de infraestrutura** | **Railway (final de 2024) → Neon/Vercel (2025), como parte da melhoria da API** | informado pelo autor, 27/07/2026 |
| Host da API | Vercel, serverless (`vercel.json` + `build.sh`) | dump §5, `api-repo/` |
| Host do banco (2025) | Neon — `ep-summer-firefly-a4o12qb6-pooler.us-east-1.aws.neon.tech`, **PostgreSQL 15.18** | consulta direta 27/07/2026 |
| Endpoints | `/api/capacitacao/autoavaliacao_notas/` (POST), `/discentes/` (GET), `/discentes_aptos_certificacao/` (GET), `/login`, `/signup` | dump §5 |
| Segurança | JWT, rotas com `IsAuthenticated`, credenciais em variáveis de ambiente | dump §5 |
| Integridade | FKs com `models.PROTECT` (rastreabilidade histórica) | dump §5 |
| Performance | `select_related`, `prefetch_related`, `bulk_create` | dump §5 |
| Contêineres | Docker + Docker Compose | dump §5 |

**Gatilho do n8n:** os dois workflows exportados em `api-repo/automacao-deploy-main/`
(`sheets_n8n.json` — "Automação capacitação", 8 nós; `graficos_n8n.json` — "gráficos",
8 nós) usam **`manualTrigger`**, não cron nem webhook. Verificado na exportação em
27/07/2026. Nós presentes: `googleSheets`, `httpRequest`, `set`, `splitInBatches`,
`function`.

### Workflows n8n — exportações em `api-repo/n8n_files/` (fornecidas em 27/07/2026)

| Arquivo | Nome no n8n | Nós | Data | Ciclo |
|---|---|---|---|---|
| `graficos_v2.json` | graficos v2 | 28 | nov/2024 | 2024 |
| `Cadastra_notas_form_novo_v2.json` | Cadastra notas form novo v2 | 9 | mar/2025 | 2025 |
| `Certificados_v3.json` | Certificados v2 | 11 | jul/2025 | **2025** |
| `Gera recomendações.json` | Gera recomendações | 34 | set/2025 | **2025** |

**Gatilhos:** `Cadastra notas`, `graficos` e `Certificados` usam `manualTrigger`.
`Gera recomendações` tem **`webhook`** ("Receber requisição do Site") **e** `manualTrigger`
— é o único disparável externamente. Não há nó de cron em nenhum deles: a execução é
sob demanda, não periódica. *Verificado nas exportações em 27/07/2026.*

**Certificação — `Certificados_v3.json` (11 nós):**
`manualTrigger` → `Get discentes` (HTTP) → `Loop Over Items` → `Nome Formatado` (code) →
`HTTP Request` → `Merge` → `Faz login na API` → **`googleDrive` (cria)** →
**`googleDocs` (preenche o template)** → **`googleDrive` (salva como PDF)** →
`googleDrive` (concede permissões).

⚠️ **Não há nó de e-mail neste workflow.** O certificado é gerado a partir de um template
do Google Docs, convertido em PDF e salvo no Drive com permissões — não é enviado por
e-mail. O envio por e-mail pertence ao fluxo de recomendações. Corrigir qualquer
afirmação em contrário (o dump §5 sugeria envio conjunto).

**Recomendação — `Gera recomendações.json` (34 nós):** o maior e mais complexo.
Banco de recomendações em Google Sheets → `Buscar discentes` e `Buscar notas` na API →
`Analisar notas` (code, regra abaixo) → `Montar template` (HTML) → `convertToFile` →
`Converter arquivo` (HTTP, para PDF) → `Mesclar arquivos` → **`gmail` (Enviar e-mail)**.
Usa `wait` em três pontos para controle de ciclo e `if` ("Sem recomendações") para pular
discentes sem apontamento.

`[[VERIFICAR: onde o n8n esteve hospedado em produção]]`

## 5. Regras de negócio

### As 10 competências avaliadas
O nó `Definir competências` (`Gera recomendações.json`) lista **10 itens**, o que
reconcilia a contagem do banco (7 soft skills + 4 sub-soft skills): são **6 competências
autônomas** mais **inteligência emocional desdobrada em 4 sub-competências**.

1. Pensamento crítico e inovação
2. Aprendizagem ativa e estratégias de aprendizagem
3. Empreendedorismo
4. Criatividade, originalidade e iniciativa
5. Liderança e influência social
6. Resolução de problemas complexos
7. Inteligência emocional: autorregulação
8. Inteligência emocional: percepção social
9. Inteligência emocional: autoconhecimento
10. Inteligência emocional: habilidades de relacionamento

Confere com o banco: 105 notas de soft skill (105 ÷ 7 = 15) e 60 de sub-soft skill
(60 ÷ 4 = 15) — 15 medições de cada. *Verificado em 27/07/2026.*

No código, `inteligência emocional` é excluída das notas principais e substituída pelas
quatro sub-competências renomeadas como `Inteligência Emocional: X` — o achatamento é o
que produz os 10 itens comparáveis.

### Escala
0–4 → quatro níveis: 0–1 Abaixo do básico · 1–2 Básico · 2–3 Adequado · 3–4 Avançado
(dump §6, §12).

### Regra de recomendação — extraída do código (`Analisar notas`)
Constante `limiteNota = 2.0`. Para cada competência de cada unidade, a recomendação é
disparada quando **qualquer** condição ocorre:

| Gatilho | Condição | Rótulo gravado |
|---|---|---|
| Desempenho | `nota < 2,0` | "Recomendação por desempenho abaixo da média" |
| Queda | `nota < nota da unidade anterior` | "Recomendação por queda de desempenho" |

As autoavaliações são ordenadas por `unidade` antes da comparação, e a comparação só
ocorre a partir da segunda unidade — o que torna o histórico persistido pré-requisito da
regra, e é exatamente o argumento da tese.

O texto da recomendação é **sorteado aleatoriamente** de um banco em Google Sheets,
agrupado por competência, **sem repetição para o mesmo discente**. Esgotado o banco,
grava "Todas as recomendações já foram utilizadas para essa competência".

⚠️ Dois pontos a tratar no artigo: (a) o comentário do código menciona "abaixo de 2.5"
enquanto a constante é `2.0` — **o valor real é 2,0**; (b) a seleção aleatória é uma
**limitação a declarar**: a recomendação é sorteada, não adaptada ao perfil do discente.

### Regra de certificação
Evolução de nível em ao menos **2/3 das competências avaliadas** (dump §6).
`[[VERIFICAR: essa regra está implementada no endpoint /discentes_aptos_certificacao/ ou
é aplicada manualmente? Certificados_v3.json não contém a lógica de 2/3]]`

## 6. Snapshot do banco de produção — consulta em 27/07/2026

Consulta agregada, sem extração de dados pessoais.

| Métrica | Valor |
|---|---|
| Discentes cadastrados | **33** (cadastros de 23/01/2025 a 01/04/2025) |
| Autoavaliações | **177** (23/01/2025 a 06/09/2025), distribuídas em **9 unidades** |
| Unidades 1 a 5 | 33 discentes cada (cobertura completa da turma) |
| Unidades 6 a 9 | 7, 3, 1 e 1 avaliações |
| Notas registradas | **165** (105 vinculadas a soft skill, 60 a sub-soft skill) |
| Faixa das notas | 0,00 a 4,00 · média **2,47** |
| Soft skills / sub-soft skills | **7 / 4** (confirma a matriz EMBRAPII) |
| Mentores / projetos | 2 / 3 |
| Discentes com notas lançadas | **7** |
| **Pares competência × discente com 2+ medições** | **49** |
| Registros de auditoria (`django_admin_log`) | 1.792 |

**Leitura do snapshot para o artigo:** a base sustenta com segurança (a) a modelagem e a
integridade referencial, (b) a cobertura da turma nas cinco primeiras unidades, e (c) a
**computabilidade efetiva da regra de 2/3** — há 49 pares competência×discente com duas
ou mais medições, que é exatamente o insumo longitudinal que a certificação exige.

**Como enunciar sem exceder a evidência:** este é um recorte de operação real, não um
censo do programa. O resultado defensável é *viabilidade demonstrada em operação*, não
*escala*. Toda afirmação de volume deve vir acompanhada da data da consulta.

### Certificados e e-mails — evidência fora do banco

Confirmado pelo autor (27/07/2026): **esses eventos não são registrados no banco**. A
automação do n8n gera o certificado, envia por e-mail e salva no Google Drive. A
evidência disponível é:

| Evidência | Onde | O que sustenta |
|---|---|---|
| **PDFs de certificados já gerados** | pasta do Google Drive do projeto | contagem de certificados emitidos, e datas pelos metadados dos arquivos |
| Workflow de certificação | n8n (a exportar) | descrição do método, critério aplicado |

**Extração a fazer:** contar os PDFs na pasta do Drive e obter a data do primeiro e do
último. Isso produz o número de certificados emitidos com procedência auditável.
`[[VERIFICAR: quantos PDFs há na pasta do Drive e qual o intervalo de datas?]]`

**Limitação a declarar no artigo:** como a emissão não é persistida no banco, o número de
certificados é apurado por contagem de artefatos no Drive, não por registro
transacional. Isso é honesto e não enfraquece o resultado — mas precisa estar escrito,
porque um avaliador vai perguntar de onde veio o número.

O total de **e-mails enviados** não tem artefato equivalente; se não houver log
exportável do n8n, o artigo deve tratar o envio como funcionalidade implementada e
demonstrada, sem afirmar volume.

## 7. Produção acadêmica

| Trabalho | Autoria | Situação | Citável? |
|---|---|---|---|
| Manuscrito 2024 — "Automação de processos na avaliação de competências socioemocionais em projetos de capacitação" | equipe | Submetido, **não publicado** (D-2) | ❌ trabalho em avaliação |
| Relatório de estágio — "Sistema integrado de backend e automação para certificação de soft skills no programa Capacitação 4.0" | Gabriel Macaúbas Melo, 2025 | protocolado (D-4) | ❌ documento interno |
| Relatório de estágio — "Automação da emissão de certificados em projetos EMBRAPII com o uso da ferramenta n8n" | Juliana Ferreira Cavalcante, 2025 | protocolado (D-4) | ❌ documento interno |
| Apresentação, 29/10/2024 | equipe de 5 alunos | — | ❌ material didático |

### ⚠️ Nada disso é citável — mas a continuidade é narrável
A Revista Principia veda citar trabalhos em avaliação e materiais didáticos; relatório de
estágio é documento interno não publicado.

**O que isso NÃO impede:** o artigo pode e deve narrar que o ciclo anterior do mesmo
projeto automatizou a geração de indicadores, e que este dá sequência — como histórico do
trabalho próprio, na Introdução e no Método. O que não se pode é apoiar afirmação em
"(Autor, 2024)" nem tratar o texto anterior como literatura.

**Consequência prática:** toda afirmação factual sobre o ciclo de 2024 precisa se
sustentar em dado próprio deste mapa de fatos, não em referência bibliográfica.

Como os relatórios são documentos internos, **não se aplica** a regra de acréscimo de 30%
para trabalhos previamente publicados (D-4). Ainda assim, evitar transcrição literal
extensa — antiplágio compara contra repositórios institucionais.

## 8. Contribuição incremental 2024 → 2025 (tese aprovada, D-1)

O manuscrito de 2024 encerra propondo como trabalho futuro exatamente: (a) relatórios
com **recomendações** para discentes com queda de desempenho, **enviados por e-mail**, e
(b) módulo de **emissão automatizada de certificados** por critério de desempenho.

O ciclo de 2025 entregou os dois, mais:
1. Certificação automatizada pela regra de evolução em 2/3 das competências
2. Módulo de recomendações pedagógicas (práticas *hands-on* / PBL)
3. Envio autônomo de e-mails
4. Persistência estruturada com rastreabilidade histórica (`models.PROTECT`)
5. Migração de infraestrutura Railway → Neon/Vercel

**Tese:** a automação de um ciclo formativo não se completa na geração de indicadores;
exige a camada de decisão (certificação) e a de intervenção (recomendação) — e ambas só
se sustentam sobre persistência estruturada, não sobre planilhas.

## 9. Desempenho

| Medida | Valor | Procedência |
|---|---|---|
| Processo manual | 40 min/aluno | manuscrito 2024 (ver conflito em §2) |
| Ciclo automatizado 2024 | ≈12 s/aluno · ganho > 99% | manuscrito 2024, conclusão |
| Registro de notas (2025) | 2–3 s | dump §6 |
| Gráfico + envio ao Drive (2025) | 12–15 s | dump §6 |
| Relatórios gerados (2024) | mais de 160 | manuscrito 2024, resumo |
| Validação pedagógica (2024) | 4 mentores, em iterações | manuscrito 2024, conclusão |

## 10. Limitações a declarar

- Latência: API e banco nos EUA (Vercel/Neon `us-east-1`); a equipe apontou hospedagem
  local no IFPB como mitigação (dump §9).
- Recorte de dados: snapshot de operação real, não censo — não sustenta afirmação de escala.
- `[[VERIFICAR: restrições do plano gratuito da Vercel — timeouts, cold starts]]`
- `[[VERIFICAR: viés de autoavaliação — há mecanismo contra notas infladas?]]`

## 11. Ética / LGPD — **atenção crítica**

O banco contém **nome, CPF, matrícula e e-mails acadêmicos reais** de 33 discentes,
associados a avaliações socioemocionais — dado pessoal, e a avaliação socioemocional é
categoria sensível.

- Nenhum dado individual, nome ou identificador pode aparecer no artigo, em figura,
  tabela ou screenshot. **Toda extração é agregada.**
- Screenshots de sistema (Swagger, n8n, planilhas) precisam de máscara antes de virar figura.
**Parecer do CEP: não se aplica** (D-5) — dados operacionais de um programa de
capacitação, não estudo de pesquisa com seres humanos no sentido da resolução. Decisão do
autor, registrada; não é bloqueio de submissão.

- `[[VERIFICAR: há anonimização/criptografia dos dados na base?]]` — não bloqueia, mas a
  resposta rende uma frase na seção de método.

## 12. Material visual disponível

Do TCC do Gabriel: DER (Discente, Mentor, SoftSkill, Autoavaliacao…); schema Django
nativo (muito técnico, reavaliar); trechos de código JWT/`bulk_create`; screenshot do
Swagger; diagrama do fluxo n8n; `docker-compose`/`Dockerfile`/`vercel.json`.
Da apresentação de 2024: gráficos radar reais e planilha formatada.

⚠️ A Principia exige figuras com **≥300 dpi** e **texto interno em Times New Roman ≥18**;
tabelas e quadros **editáveis, nunca imagem**. Screenshot de código provavelmente não
passa — preferir pseudocódigo, que a revista recomenda explicitamente.

## 13. Vocabulário

Soft skills (7 macro) · Sub-soft skills (4) · PBL · Projeto Real/Espelho · Discente ·
Níveis qualitativos (Abaixo do básico, Básico, Adequado, Avançado) · Unidade (ciclo de
avaliação; há 9 no banco).
