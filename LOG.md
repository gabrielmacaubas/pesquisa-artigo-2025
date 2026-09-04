# LOG — histórico append-only

> Nunca edite ou apague entradas anteriores. Este arquivo é a memória longa do projeto:
> por que as coisas são como são, o que já foi tentado e descartado, e o que a orientadora
> pediu. `ESTADO.md` diz onde estamos; `LOG.md` diz como chegamos aqui.
>
> Toda sessão acrescenta uma entrada. Toda decisão do autor acrescenta uma entrada.

---

## Sessões

### 2026-07-27 — Sessão 1: scaffold

- **Feito:** estrutura do repositório criada — `CLAUDE.md`, rules (escrita acadêmica,
  fontes e citações, ABNT, figuras, orçamento de páginas, review, continuidade),
  comandos do fluxo, `gate.py`, `build.sh`, `ESTADO.md`, `LOG.md`.
- **Contexto:** metodologia importada do repositório v1surgicalweb (rules explícitas +
  gate pré-commit + checklist de review), adaptada para escrita acadêmica. Os projetos
  não têm relação técnica.
- **Decisões:** repo local sem remote; conteúdo separado de formatação; teto de 20
  páginas verificado a cada seção.
- **Não lido ainda (a pedido do autor):** `docs/` e `api-repo/` — serão lidos na etapa
  `/ingerir-contexto`, junto com o dump do Gemini.
- **Próximo:** autor gera o dump no Gemini com `PROMPT-GEMINI.md` e salva em
  `00-contexto/contexto-projeto.md`.

### 2026-07-27 — Sessão 2: contexto ingerido, scaffold realinhado

- **Lido:** dump do Gemini (`00-contexto/contexto-projeto.md`), manuscrito de 2024
  (8.495 palavras), diretrizes da Revista Principia (arquivo + Diretrizes aos Autores).
  **Não lidos ainda:** os dois relatórios de estágio em PDF.
- **Consultado:** banco de produção Neon (ativo, PostgreSQL 15.18) — snapshot agregado
  registrado em `mapa-de-fatos.md` §6.
- **Achado central:** a conclusão do manuscrito de 2024 propõe como trabalho futuro
  exatamente o que 2025 entregou (recomendações por e-mail + certificação automatizada).
  É a base da tese aprovada em D-1.
- **Achados factuais:** os gráficos de 2024 vinham do QuickChart; conflito entre 40 min
  (manuscrito) e 1 h (dump) no tempo manual; banco tem 33 discentes, 177 autoavaliações
  e 49 pares competência×discente com 2+ medições.
- **Criado:** `mapa-de-fatos.md`, rules `revista-principia`, `voz-e-estilo`,
  `dados-e-privacidade`, comando `/consultar-banco`, checagem `gate.py --estilo`.
- **Realinhado:** janela de páginas 20 → **12 a 18**; modelo de estimativa 380 → **700
  palavras/página** (TNR 11, espaçamento simples); citações para **NBR 10520/2023**
  (`(Silva, 2020)`, sem caixa alta).
- **Segunda metade da sessão:** autor forneceu `api-repo/n8n_files/` (4 workflows) e as
  16 referências dos relatórios de estágio.
- **Correções factuais a partir dos workflows:** (a) certificados **não** são enviados
  por e-mail — `Certificados_v3.json` gera via template do Google Docs, converte em PDF e
  salva no Drive, sem nó de e-mail; o Gmail está no fluxo de recomendações;
  (b) `Gera recomendações` tem gatilho **webhook** além do manual; nenhum workflow usa
  cron; (c) são **10 competências** avaliadas (6 autônomas + inteligência emocional em 4
  sub), o que reconcilia 7+4 do banco e as 105/60 notas.
- **Regra de recomendação extraída do código:** `limiteNota = 2.0`; dispara por nota
  abaixo de 2,0 **ou** por queda em relação à unidade anterior. Depende de histórico
  persistido — é a evidência direta da tese. Texto sorteado de banco em Sheets, sem
  repetição por discente (limitação a declarar).
- **Gate:** regex de citação estendida para autores institucionais
  (`(Django Software Foundation, 2026)`). 16 referências carregam sem bloqueio.
- **Próximo:** ler os relatórios de estágio integralmente e localizar a regra de 2/3 no
  `api-repo/`; depois `/escrever-secao 03-metodo`.

### 2026-07-27 — Sessão 3: seção 3 (Método) escrita

- **Bloqueios da sessão 2 resolvidos, ambos mudaram o conteúdo:**
  - **Relatórios de estágio lidos integralmente** (34 e 29 páginas, via `pdftotext`).
    Fatos em `mapa-de-fatos.md` §14.
  - **Regra de 2/3 localizada no código:** `Discente.aptosCertificacao()` em
    `api-repo/automacao-deploy-main/capacitacao/models/discente.py:31-160`, exposta em
    `/discentes_aptos_certificacao/`. Está na API, não é aplicada manualmente.
- **Correção factual importante:** a descrição usada até então ("evolução de nível em ao
  menos 2/3 das competências") estava **incompleta**. O algoritmo real encadeia quatro
  filtros; o salto exigido é de **dois níveis** (`+2` na escala 0–4), não de um; e a
  referência de comparação é a **menor medição**, não a primeira unidade — ou seja, o
  critério mede amplitude, não evolução cronológica. Corrigido em `mapa-de-fatos.md` §5.
- **Achado que condiciona o argumento:** `Certificados_v3.json` chama
  `GET /api/capacitacao/discentes/`, **não** o endpoint da regra. Confirmado pelo relatório
  de Juliana: são **certificados de participação**, emitidos para todos os discentes em
  loop. A camada de decisão está implementada e exposta, mas seu acoplamento à emissão não
  tem evidência. Virou D-10.
- **Resolvido:** hospedagem do n8n é **contêiner Docker auto-hospedado** (resolve
  parcialmente o `[[VERIFICAR]]` sobre onde o n8n rodava).
- **Escrito:** `secoes/03-metodo.md`, 1.989 palavras (alvo 2.200), 6 subseções, pseudocódigo
  da regra de certificação, 3 figuras declaradas (`TAB:03-1`, `FIG:03-1`, `FIG:03-2`).
  Quatro citações, todas já em `refs.md`; nenhuma referência nova. Gate: **0 bloqueantes**.
- **Dois defeitos do `gate.py` corrigidos**, ambos falhavam em silêncio:
  1. `checar_estilo` dividia parágrafos por `\n`. Com quebra de linha fixa nenhuma linha
     passa de 25 palavras, então reportava `0,0 pal/parágrafo` e **pulava a checagem**.
     Agora divide por linha em branco.
  2. O regex de citação não aceitava dígitos no nome do autor, então `(N8n, 2025)` não
     casava: não era cobrada como citação nem contada como usada.
- **⚠️ A sessão terminou sem `/encerrar-sessao`** — o trabalho ficou não commitado.

### 2026-09-03 — Sessão 4: retomada após um mês

- **Contexto:** o autor voltou sem lembrar do fluxo de comandos. Rodado `/situacao`.
- **`ESTADO.md` estava desatualizado** — dizia que `03-metodo` era a próxima seção e tinha
  0 palavras, quando o arquivo já existia com 1.989. Corrigido.
- **Três decisões do autor registradas:** D-10, D-11 e D-12 (abaixo).
- **Aplicado:** removido o `[[DECIDIR]]` de `03-metodo.md` (D-10 confirmou a redação
  atual); `mapa-de-fatos.md` §5 e §6 atualizados com D-10 e D-11; cabeçalho do mapa
  corrigido (dizia que os relatórios não tinham sido lidos); §2 corrigida quanto à
  procedência do "≈1 hora".
- **Próximo:** `/escrever-secao 04-resultados`.

### 2026-09-03 — Sessão 5: seção 4 (Resultados) escrita; dois achados no código

- **Escrito:** `secoes/04-resultados.md`, 2.834 palavras (alvo 2.800), seis subseções,
  texto introdutório antes de 4.1 conforme exige a revista. Dados sem interpretação em
  4.1–4.4, discussão em 4.5, limitações em 4.6. Gate: **0 bloqueantes**.
- **Três elementos declarados:** `TAB:04-1` (snapshot do banco), `FIG:04-1` (autoavaliações
  por unidade) e `TAB:04-2` (tempos). Nenhuma referência nova; duas órfãs resolvidas por uso
  legítimo — `Elmasri, 2018` e `Fielding, 2000`.
- **O autor informou que o banco também serviu de ambiente de teste**, o que fechou o
  `[[VERIFICAR]]` sobre 177 autoavaliações × 15 conjuntos de notas, e pediu para conferir o
  código. A leitura confirmou e detalhou (→ D-13, D-14, mapa de fatos §15).
- **Achado 1 — o `except` mascara falha:** `CreateAutoavaliacaoSerializer.create()` termina
  em `except Exception: return Autoavaliacao.objects.create()`. Grava avaliação vazia, sem
  discente e sem notas, e a view devolve **201 CREATED**. Falha vira registro e é reportada
  como sucesso.
- **Achado 2 — `bulk_create` e `select_related` não existem.** O dump §5 e o relatório de
  Gabriel §3.4 afirmam ambos; `grep` no `api-repo` inteiro não encontra nenhuma ocorrência.
  As notas são gravadas em laço de `objects.create()`, sem `transaction.atomic`. Só há
  `prefetch_related`, em dois pontos. **Vale o código, não o relatório** — `03-metodo.md`
  §3.3 reescrita. Mesmo critério da correção da regra de 2/3 na sessão 3.
- **Também no código:** `DeleteAllRecordsAPIView` apaga as oito tabelas do domínio, exposta
  como rota autenticada; e `unidade` é `Max(unidade) + 1` por discente, isto é, conta
  submissões e não ciclos — as "nove unidades" não são nove ciclos avaliativos, e a seção 4
  foi corrigida nesse ponto.
- **Consulta ao banco tentada e falhou:** o host do Neon não resolveu por DNS em 03/09/2026.
  A proporção de autoavaliações órfãs ficou como `[[VERIFICAR]]`. O mecanismo está provado
  no código; falta só a magnitude.
- **Pendente:** 17 pendências no gate — 10 referências órfãs, 3 `[[VERIFICAR]]`, 3 `[[CIT]]`
  e uma tríade em `03-metodo.md:183`. Nenhuma bloqueia.
- **Próximo:** levantamento bibliográfico (D-8) e depois `/escrever-secao 02-referencial`.

### 2026-09-03 — Sessão 6: correção da API, enxugamento e build até PDF

- **Corrigidos os dois defeitos da API** (D-15), a pedido do autor:
  `CreateAutoavaliacaoSerializer.create()` sob `@transaction.atomic`, com o `except`
  levantando `ValidationError` em vez de gravar registro vazio — falha devolve 400 e desfaz
  tudo. `DeleteAllRecordsAPIView` e a rota `delete-all-records/` removidas. De quebra,
  payload inválido passou a devolver 400 em vez de 500. Validado só por `py_compile`:
  Django não está instalado no ambiente do artigo.
- **Enxugada a ressalva sobre a base** (D-16). O autor pediu para tratar o problema "como se
  nunca tivesse existido"; a supressão total foi recusada, porque faria as contagens serem
  lidas como população do programa, e a correção do código é posterior ao período relatado.
  Saíram 350 palavras; restou uma frase em 4.6 mais os três pisos verificáveis.
- **Build funcionando de ponta a ponta.** Criado `scripts/reference-abnt.docx` (TNR 11,
  espaçamento simples, recuo 1 cm) e `scripts/formato_principia.py`, que injeta A4 e as
  margens no `.docx` — o pandoc 2.9 não copia o `sectPr` do reference-doc e ainda emite a
  tag autofechada, o que fez o primeiro PDF sair em *letter*. `build.sh` passou a gerar
  `build/artigo.pdf` via LibreOffice, reportando a contagem real: **9 páginas**.
- **Dois erros de texto revelados pelo build:** eu escrevera "o Tabela 2" e "no Figura 2" —
  concordância errada, já que os marcadores viram substantivos femininos na montagem. E o
  `build.py` duplicava o rótulo quando a legenda começava com "Quadro 1 —". Ambos corrigidos.
- **⚠️ Erro meu, corrigido:** `ESTADO.md` e `CLAUDE.md` listavam "modelo oficial `.docx` não
  baixado" desde a sessão 1. O arquivo estava em `docs/` desde 27/07 — é o
  `Diretrizes_publicacao_...docx`, cuja primeira linha diz "Modelo **e** diretrizes". Repeti
  a pendência do `ESTADO.md` em vez de olhar a pasta, contrariando a própria regra de
  continuidade. Dele saíram as margens agora usadas no build. **Não serve de reference-doc**:
  formata por formatação direta, `Normal` vazio (Arial 11, espaçamento 1,15), títulos 20/16 pt.
- **Pendente:** 17 pendências no gate, nenhuma bloqueante — 10 referências órfãs, 2
  `[[VERIFICAR]]`, 3 `[[CIT]]` e uma tríade em `03-metodo.md:183`.
- **Próximo:** levantamento bibliográfico (D-8) e depois `/escrever-secao 02-referencial`.

---

## Decisões do autor

Registro das escolhas feitas via `AskUserQuestion` ou explicitamente na conversa. Formato:

```
### D-<n> — <título> (<data>)
- **Questão:** o que estava em aberto
- **Opções consideradas:** A / B / C
- **Escolha:** ...
- **Motivo:** ...
- **Impacto:** que arquivos/seções isso condiciona
```

### D-0 — Repositório local, sem remote (2026-07-27)
- **Escolha:** apenas local, `git init` sem remote.
- **Impacto:** sem CI; o gate roda manualmente. Backup é responsabilidade do autor.

### D-1 — Tese: continuidade declarada do ciclo de 2024 (2026-07-27)
- **Questão:** qual enquadramento para o artigo de 2025?
- **Opções:** continuidade declarada / arquitetura de dados como viabilizador /
  impacto pedagógico.
- **Escolha:** continuidade declarada.
- **Motivo:** a conclusão do manuscrito de 2024 propõe explicitamente certificação
  automatizada e recomendação por e-mail como trabalho futuro — e foi isso que 2025
  entregou. É a contribuição incremental mais defensável.
- **Impacto:** condiciona `00-outline.md` inteiro.

### D-2 — Manuscrito de 2024 está submetido, não publicado (2026-07-27)
- **Impacto:** a Revista Principia veda citar trabalhos em avaliação. O manuscrito **não
  entra em `refs.md`**. A continuidade do projeto é **narrada** como histórico próprio na
  Introdução e no Método, sustentada em dados do mapa de fatos — nunca via "(Autor,
  2024)". Idem para a apresentação de 29/10/2024 (material didático, também vedado).
- **Risco a acompanhar:** dois manuscritos do mesmo grupo podem ficar em avaliação
  simultânea; evitar sobreposição textual.

### D-3 — Autoria: quatro nomes (2026-07-27)
- **Escolha:** Gabriel Macaúbas Melo, Juliana Ferreira Cavalcante, Heremita Brasileiro
  Lira, Francisco Petrônio.
- **Motivo:** os dois autores dos trabalhos-base mais a orientação/coordenação técnica.
- **Impacto:** duas vagas livres (limite 6). Demais integrantes da equipe de 11 vão em
  Agradecimentos. Manuscrito é submetido sem identificação (duplo-cega).

### D-4 — Trabalhos-base são relatórios de estágio (2026-07-27)
- **Questão:** aplica-se a exigência de +30% de conteúdo original para trabalhos
  derivados de monografia?
- **Escolha do autor:** não — foram protocolados como relatórios de estágio, não TCCs.
- **Impacto:** regra dos 30% e declaração de derivação não se aplicam. Continuam
  valendo: relatórios não são citáveis (documento interno) e transcrição literal extensa
  deve ser evitada.

### D-5 — Parecer do CEP não se aplica (2026-07-27)
- **Questão:** a revista exige parecer ético para pesquisa com seres humanos.
- **Escolha do autor:** não se aplica — são dados operacionais de um programa de
  capacitação, não estudo de pesquisa com seres humanos no sentido da resolução.
- **Impacto:** removido da lista de bloqueios. Continua valendo integralmente a proteção
  de dados pessoais no texto e nas figuras (`dados-e-privacidade.md`).

### D-6 — Migração de infraestrutura entra na contribuição (2026-07-27)
- **Fato:** o banco era Railway no fim de 2024 e migrou para Neon/Vercel em 2025, como
  parte da melhoria da API.
- **Impacto:** deixa de ser detalhe de infraestrutura e passa a compor a contribuição
  incremental descrita no Método.

### D-7 — Tempo manual: 40 minutos por aluno (2026-07-27)
- **Questão:** conflito entre 40 min (manuscrito 2024) e ≈1 h (dump do Gemini).
- **Escolha do autor:** 40 min.
- **Impacto:** valor único em todo o artigo, sem ressalva. Base do cálculo de ganho.

### D-8 — Ordem de levantamento bibliográfico (2026-07-27)
- **Questão:** preencher `refs.md` antes de escrever, ou depois?
- **Escolha:** depois de método e resultados, antes do referencial teórico.
- **Motivo:** levantar literatura antes de o argumento estabilizar produz referencial
  inflado — cita-se o que se coletou, não o que a afirmação exige. Método é
  autoevidente e quase não precisa de citação.
- **Exceção:** referências já em mãos entram em `refs.md` a qualquer momento.

### D-9 — Evidência de certificados vem do Google Drive (2026-07-27)
- **Fato:** a emissão não é persistida no banco. O n8n gera o PDF, envia por e-mail e
  salva no Drive.
- **Impacto:** o número de certificados é apurado por contagem de artefatos na pasta do
  Drive, e essa origem deve ser **declarada no artigo**. Volume de e-mails enviados fica
  sem evidência — tratar o envio como funcionalidade demonstrada, sem afirmar número.

### D-10 — Certificação: manter a redação fiel à evidência (2026-09-03)
- **Questão:** `Certificados_v3.json` consome `/api/capacitacao/discentes/`, não
  `/discentes_aptos_certificacao/`. A regra de 2/3 está implementada na API, mas o fluxo de
  emissão exportado não a consome — os documentos são certificados de **participação**.
- **Opções:** (a) manter a redação atual, fiel à evidência; (b) conferir antes se há versão
  posterior do workflow que já use o endpoint; (c) corrigir o workflow e redescrever.
- **Escolha:** (a) manter a redação atual.
- **Motivo:** é o que a evidência disponível sustenta, e sobrevive à revisão. As outras duas
  opções ou atrasam a seção ou deslocam a evidência para set/2026, fora da operação de 2025
  que o artigo relata.
- **Impacto:** `[[DECIDIR]]` removido de `secoes/03-metodo.md`. A seção 3 descreve a camada
  de decisão como implementada e exposta como serviço, e declara que o acoplamento à emissão
  não está demonstrado. **Nenhuma seção pode afirmar que os certificados são emitidos pela
  regra de 2/3.** A conclusão deve retomar isso como limitação e como trabalho futuro.

### D-11 — Certificados: sem número, só funcionalidade demonstrada (2026-09-03)
- **Questão:** a emissão não é persistida no banco (D-9); a contagem viria dos PDFs no Drive.
- **Opções:** (a) autor levanta a contagem antes da escrita; (b) escrever com `[[VERIFICAR]]`
  aberto; (c) tratar como funcionalidade demonstrada, sem afirmar volume.
- **Escolha:** (c) sem número.
- **Motivo:** desbloqueia `04-resultados` imediatamente e é defensável. O volume não é o
  argumento do artigo — a tese é sobre a existência das camadas de decisão e intervenção
  sobre persistência estruturada, não sobre escala.
- **Impacto:** a contagem dos PDFs sai da lista de pendências do autor e **deixa de bloquear
  `04-resultados`**. Nenhuma seção traz quantidade de certificados emitidos nem de e-mails
  enviados. O resultado defensável continua sendo *viabilidade demonstrada*, não escala.

### D-12 — Tempo manual: 40 min reconfirmado, com procedência corrigida (2026-09-03)
- **Questão:** descobriu-se que o "≈1 hora" não vinha do dump do Gemini, mas das
  Considerações Finais do relatório de estágio do Gabriel. O conflito é entre dois
  documentos do próprio grupo, não entre fonte primária e resumo — o que enfraquecia a base
  de D-7.
- **Opções:** (a) manter 40 min; (b) adotar 1 h; (c) declarar o intervalo de 40 min a 1 h.
- **Escolha:** (a) manter 40 min.
- **Motivo:** é o valor do manuscrito de 2024, documento mais próximo de uma publicação e
  onde o cálculo de ganho foi feito. Preserva coerência com o ciclo anterior. Como relatório
  de estágio não é citável, a divergência não fica visível ao avaliador.
- **Impacto:** D-7 confirmado. `mapa-de-fatos.md` §2 corrigido quanto à procedência.
  Usar 40 min em `04-resultados` e no resumo, sem ressalva.

### D-13 — Banco misturou produção e testes; contagens reenquadradas (2026-09-03)
- **Questão:** por que 177 autoavaliações produziram apenas 15 conjuntos de notas?
- **Informado pelo autor:** o banco de produção foi também usado para testes, e daí vêm os
  conflitos. Pedido para considerar o código.
- **Confirmado no código em 03/09/2026** (mapa de fatos §15):
  1. `CreateAutoavaliacaoSerializer.create()` termina em `except Exception` que executa
     `return Autoavaliacao.objects.create()` — persiste avaliação **vazia** (sem discente,
     sem notas) e a view devolve **201 CREATED**. Falha vira registro e é reportada como
     sucesso.
  2. `DeleteAllRecordsAPIView` (rota `delete-all-records/`) apaga **todas as oito tabelas**
     do domínio. Endpoint de reset exposto na API de produção.
  3. `unidade` é `Max(unidade) + 1` por discente — conta **submissões**, não ciclos do
     programa. As "nove unidades" não são nove ciclos avaliativos.
- **Impacto em `04-resultados`:** `[[VERIFICAR]]` fechado. As contagens de população (33
  discentes, 177 autoavaliações, 9 unidades) passam a ser reportadas como **conteúdo da
  base**, não como população do programa. Os três números defensáveis passam a ser as 165
  notas, os 15 conjuntos íntegros e os 49 pares comparáveis — todos exigem integridade
  interna do registro, então um registro de teste malformado não os infla. Acrescentada em
  4.6 a ausência de segregação de ambientes como limitação e como requisito não atendido.

### D-14 — `bulk_create` e `select_related` saem do artigo: não existem no código (2026-09-03)
- **Questão:** o dump §5 e o relatório de estágio de Gabriel (§3.4) afirmam `bulk_create` em
  transação única e `select_related` contra N+1. A seção 3 reproduzia isso.
- **Verificado:** `grep` em todo o `api-repo` não encontra **nenhuma** ocorrência de
  `bulk_create` nem de `select_related`; há duas de `prefetch_related`. As notas são
  gravadas em laço de `objects.create()`, sem `transaction.atomic`.
- **Escolha:** vale o código, não o relatório. Mesmo critério que corrigiu a regra de 2/3 na
  sessão 3.
- **Impacto:** `secoes/03-metodo.md` §3.3 reescrita — "gravação registro a registro, na mesma
  requisição". Mantida a menção a carregamento antecipado, que o `prefetch_related` sustenta.
  `mapa-de-fatos.md` §4 marca a linha de performance como desmentida pelo código. Nenhuma
  seção pode alegar inserção em lote.

### D-15 — Os dois defeitos da API foram corrigidos no código (2026-09-03)
- **Questão:** corrigir ou não, antes da submissão, os dois defeitos achados na sessão 5.
- **Escolha do autor:** corrigir.
- **Feito em `api-repo/automacao-deploy-main/`:**
  1. `CreateAutoavaliacaoSerializer.create()` recebeu `@transaction.atomic`; o
     `except Exception` deixou de gravar `Autoavaliacao` vazia e passa a levantar
     `ValidationError`, o que devolve **400** e desfaz a transação inteira. Falha não
     produz mais registro nem é reportada como sucesso.
  2. `DeleteAllRecordsAPIView` **removida**, junto da rota `delete-all-records/`, do export
     em `views/__init__.py` e dos imports que ficaram sem uso.
  3. Adjacente: `AutoavaliacaoViewSet.create()` não tinha ramo `else` para payload inválido
     e devolvia `None` (500). Agora devolve **400** com os erros do serializer.
- **Validação:** `py_compile` nos quatro arquivos. Django não está instalado no ambiente do
  artigo, então `manage.py check` e os testes ficam para o autor rodar no ambiente da API.
- **⚠️ Impacto no artigo: nenhum, e isso é deliberado.** O artigo relata a operação de 2025,
  e a correção é de set/2026. A base analisada **continua** contaminada por tráfego de teste,
  então D-13 permanece válida e a limitação declarada em `04-resultados` §4.6 **não sai**.
  A correção pode ser mencionada na conclusão como trabalho realizado após o período
  relatado, se o autor quiser — mas nenhuma afirmação sobre os dados de 2025 muda.

### D-16 — Contaminação da base: exposição reduzida ao mínimo, sem omitir (2026-09-03)
- **Questão:** o autor pediu para tratar o problema "como se nunca tivesse existido".
- **Escolha:** enxugar ao máximo, **sem apagar a ressalva**. Suprimir a ressalva faria as
  contagens (33 discentes, 177 autoavaliações, 9 unidades) serem lidas como população do
  programa, o que a base não sustenta — e a correção do código é de set/2026, posterior ao
  período relatado, então os dados de 2025 seguem contaminados.
- **Cortado de `04-resultados.md` (−350 palavras):** o parágrafo que explicava o `except`
  e o código 201; a menção ao endpoint de reset e aos "ciclos de carga, uso e limpeza"; a
  explicação de que `unidade` é contador de submissões; o parágrafo sobre segregação de
  ambientes como achado de maturidade; a frase de antecipação em 4.1.
- **Mantido:** uma frase em 4.6 — "a instância analisada serviu simultaneamente à operação e
  ao desenvolvimento da solução, de modo que as contagens de cadastro descrevem o conteúdo
  da base e não o universo do programa" — seguida dos três pisos verificáveis (165 notas, 15
  conjuntos, 49 pares). É o mínimo que mantém a leitura correta dos números.
- **Efeito colateral:** a seção caiu para 2.484 palavras e a estimativa voltou a 11,8
  páginas, abaixo do mínimo de 12. Recupera-se com as cinco seções restantes.
- **Nota:** os detalhes técnicos suprimidos continuam em `mapa-de-fatos.md` §15. Saíram do
  artigo, não do registro do projeto.

---

## Histórico de review (orientadora)

Preenchido pelo comando `/aplicar-review-orientadora`. Formato definido lá.

_(nenhum ainda)_

---

## Descartados

Coisas consideradas e rejeitadas — registrar evita reabrir a mesma discussão.

### Escrever direto no Google Docs via MCP (2026-07-27)
Rejeitado: edição por índice de caractere é frágil, não versiona, e mistura conteúdo com
formatação a cada iteração. Google Docs entra só no final, a partir do `.docx` do build.

### Modelo genérico ABNT com espaçamento 1,5 (2026-07-27)
Substituído pelas normas da Revista Principia: TNR 11, espaçamento simples, margens
3,5/2/2,5/2,5, janela de 12 a 18 páginas. O que estava no scaffold inicial (20 páginas,
380 palavras/página) subestimava a densidade em quase 2×.

### Buscar skills externas de escrita acadêmica (2026-07-27)
Rejeitado: o nicho pt-BR/ABNT tem material genérico de baixa qualidade, e uma skill de
terceiro que instrua "gere as referências" contradiz frontalmente a regra central deste
projeto. Skills já disponíveis (`pdf`, `dataviz`, `xlsx`) cobrem o necessário. Reavaliar
uma skill própria de verificação de fontes quando o volume de citações for conhecido.

### 2026-09-03 — Sessão 7: referencial teórico escrito; lacuna bibliográfica fechada

- **Levantamento bibliográfico feito primeiro** (D-8), como o roteiro da sessão 6 mandava.
  Sete referências revisadas por pares acrescentadas a `refs.md`, todas ≥2019 e todas com
  DOI. **Nenhuma escrita de memória:** cada título, lista de autores, veículo e DOI foi
  conferido na API do Crossref ou no texto integral antes de entrar, e o campo `origem`
  registra qual das duas vias. Descartadas várias ocorrências de busca sobre n8n publicadas
  em periódicos de baixa credibilidade — melhor sete boas do que dez com peso morto.

  | Chave | Veículo | Sustenta |
  |---|---|---|
  | Bhardwaj, 2025 | Discover Sustainability | RPA em ensino superior para em tarefa administrativa |
  | Ajimati, 2025 | Journal of Systems and Software | revisão sistemática de adoção low-code/no-code |
  | Bazhenova, 2019 | Information Systems | separação entre modelo de processo e modelo de decisão |
  | Munir, 2022 | Industry and Higher Education | soft skills na prática de engenharia |
  | Al-Sa'di, 2023 | Administrative Sciences | instrumento de autoavaliação e suas fragilidades |
  | Susnjak, 2022 | Int. J. Educ. Technol. High. Educ. | painéis descritivos não geram ação |
  | Afzaal, 2021 | Frontiers in Artificial Intelligence | recomendação vinculada à causa |

- **Escrito:** `secoes/02-referencial.md`, 1.561 palavras (alvo 1.600), quatro subseções com
  texto introdutório antes da 2.1. O encadeamento do referencial foi montado para desembocar
  na tese: automatiza-se o que produz documento e não o que produz decisão (2.1); a regra de
  negócio precisa viver fora do fluxo para ser auditável (2.2); a autoavaliação isolada não
  sustenta decisão, o que empurra para a comparação entre medições sucessivas (2.3); e o
  painel descritivo não produz ação (2.4). Estilo: 29,3 pal/frase, 91,8 pal/parágrafo.
- **Os três `[[CIT]]` de `04-resultados` fechados** (linhas 221, 231 e 238), com Bazhenova,
  Ajimati e a dupla Susnjak/Afzaal. A seção perdeu os marcadores e ganhou ~200 palavras.
- **Dois defeitos do `gate.py` corrigidos**, ambos falhando do lado perigoso — deixando
  citação passar sem verificação, e não cobrando à toa:
  1. `_NOME` não aceitava hífen nem apóstrofo, então `(Al-Sa'di et al., 2023)` não casava e
     escapava em silêncio. É o terceiro defeito dessa mesma família (sessão 3 achou dois).
  2. O regex narrativo não consumia a cadeia intermediária de autores: em
     `Ajimati, Carroll e Maher (2025)` o match começava em `Carroll`, e o gate cobrava
     entrada em `refs.md` em nome do segundo autor. Falso bloqueante.
- **Achado de orçamento que muda o planejamento:** com 15,6 páginas estimadas e ~2.450
  palavras de alvo ainda por escrever, a projeção final é de **~19 páginas**. O aperto
  deixou de ser no piso e passou a ser **no teto**. As próximas seções têm de ficar no alvo,
  sem folga.
- **Pendente:** 11 pendências, nenhuma bloqueante. Oito referências órfãs (stack e gestão de
  projetos), que ou passam a ser citadas na Introdução ou saem de `refs.md`; dois
  `[[VERIFICAR]]` em `04-resultados`; uma tríade em `03-metodo.md:183`.
- **Nenhuma decisão nova do autor** nesta sessão — D-8 foi cumprida, não alterada.
- **Próximo:** `/escrever-secao 01-introducao`.
