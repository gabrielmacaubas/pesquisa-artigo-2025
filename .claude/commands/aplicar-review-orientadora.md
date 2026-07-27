---
description: Aplica correção a partir de comentário da orientadora colado junto do trecho revisado
---

Você vai aplicar uma correção no artigo a partir de feedback da orientadora.

O usuário colou abaixo (em qualquer ordem, possivelmente em vários blocos):
- o **comentário** da orientadora
- o **trecho** do artigo ao qual o comentário se refere

$ARGUMENTS

## Procedimento

### 1. Localizar
Encontre o trecho em `secoes/` (Grep pelo texto ou por um fragmento distintivo). Se não
achar exatamente — o texto pode ter sido copiado do `.docx` já formatado, com quebras
diferentes — busque por uma frase curta e característica. **Se não localizar com
certeza, pergunte antes de editar.** Editar o parágrafo errado é pior que não editar.

Se o comentário se referir a algo estrutural (ordem das seções, ausência de uma
discussão inteira), o alvo pode não ser um trecho — trate como item de plano e registre
em `LOG.md`.

### 2. Classificar o comentário

| Tipo | Exemplo | Ação |
|---|---|---|
| **Factual** | "esse número está errado" | Verificar em `00-contexto/`/`docs/`. Corrigir só com fonte. Sem fonte → `[[VERIFICAR]]` e avisar. |
| **Referência** | "falta citar", "de onde veio isso?" | Localizar fonte real e adicionar em `refs.md`. **Nunca inventar citação para satisfazer o comentário** — esse é o caminho de falha mais provável aqui. |
| **Argumento** | "não ficou claro por que", "isso não se sustenta" | Reescrever o raciocínio. Pode exigir mexer em parágrafos vizinhos — o problema raramente está só na frase apontada. |
| **Forma** | "muito longo", "pessoa verbal", "vago" | Reescrever aplicando `.claude/rules/escrita-academica.md`. |
| **Escopo** | "tire isso", "acrescente uma seção sobre X" | Não decida sozinho se contraria o `00-outline.md`. Aponte o conflito e pergunte. |
| **Ambíguo** | "rever", "melhorar" | **Pergunte** o que ela quis dizer. Não adivinhe. |

### 3. Aplicar

- Edite **apenas** o necessário para atender o comentário. Não aproveite a passagem para
  "melhorar" outras coisas — isso polui o diff e a orientadora perde a referência do que
  pediu.
- Preserve citações e números existentes que o comentário não questionou.
- Se atender o comentário criar contradição com outra seção, **pare e aponte** antes de
  propagar a mudança.

### 4. Registrar

Anexe em `LOG.md`, na seção `## Histórico de review`:

```markdown
### <data> — <seção afetada>
- **Comentário:** <literal, resumido se muito longo>
- **Classificação:** factual | referência | argumento | forma | escopo
- **Ação:** <o que mudou, ou por que não mudou>
- **Pendência:** <[[VERIFICAR]] aberto, ou nenhuma>
```

Esse histórico é o que permite responder "o que você fez com meus comentários?" na
próxima reunião — e evita reintroduzir algo que já foi cortado a pedido dela.

### 5. Fechar

- Rode `python3 scripts/gate.py`
- Reporte: trecho localizado (arquivo:linha), classificação, o que mudou, e o que ficou
  pendente. Mostre o antes/depois do parágrafo alterado.

## Se o comentário estiver factualmente errado

Acontece — a orientadora pode ter lido rápido ou partido de premissa desatualizada.
Nesse caso: **não aplique silenciosamente e não recuse silenciosamente.** Aponte a
divergência com a evidência (`00-contexto/` diz X, na p. Y do TCC consta Z) e deixe a
decisão com o autor. Aplicar uma correção que introduz um erro é pior que devolver a
pergunta.
