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
