# Continuidade entre Sessões e Tomada de Decisão

> O autor trabalha em conversas curtas: `/clear` e um comando. Ele **não deve precisar
> reexplicar o projeto nunca**. Isso só funciona se o estado viver em arquivo, não na
> conversa.

## Ao iniciar qualquer sessão

Antes de executar qualquer comando, leia **nesta ordem**:

1. `CLAUDE.md` — como este repositório funciona
2. `ESTADO.md` — onde o projeto está agora, e qual é a próxima ação
3. `LOG.md` — decisões já tomadas e o que já foi descartado

Depois leia só o que a tarefa exigir (`00-outline.md`, a seção alvo, o mapa de fatos).
Não releia `docs/` inteiro a cada sessão — foi para isso que
`00-contexto/mapa-de-fatos.md` foi criado.

Se `ESTADO.md` estiver desatualizado em relação aos arquivos (ex.: diz que a seção 3 não
existe, mas `secoes/03-*.md` está escrita), **corrija `ESTADO.md` primeiro** e avise.

## Ao encerrar qualquer sessão

Obrigatório, mesmo em sessão curta:

1. **Reescreva `ESTADO.md`** — situação, próxima ação, tabela de seções com
   palavras/alvo, figuras pendentes, decisões em aberto, bloqueios. É um retrato do
   agora; não acumule histórico aqui.
2. **Acrescente uma entrada em `LOG.md`** — o que foi feito, por quê, e o que ficou
   pendente. Nunca reescreva entradas antigas.
3. **Commit local** — `git add -A && git commit`. Mensagem descrevendo a etapa, não o
   arquivo (`escreve seção 3 (metodologia), 1.380 palavras, 2 figuras pendentes`).

Uma sessão que termina sem atualizar esses dois arquivos **desperdiça o trabalho**: a
próxima conversa parte de informação errada.

## Decisões: quando perguntar

Use **`AskUserQuestion`** — não decida sozinho e não escreva um parágrafo de opções em
texto — sempre que:

- A escolha é do autor por natureza: tese, recorte, ordem de autoria, o que cortar,
  título, veículo de destino.
- Duas leituras da fonte levam a artigos materialmente diferentes.
- Um comentário da orientadora é ambíguo ou contradiz o outline aprovado.
- O corte necessário para caber em 20 páginas é maior que ~15%.
- Uma fonte contradiz outra sobre um fato e ambas são plausíveis.

Como perguntar bem:
- 2 a 4 opções concretas, mutuamente exclusivas, cada uma com a consequência real
  ("isso reduz a seção 2 em 300 palavras e enfraquece o argumento X").
- Recomende uma, e coloque-a primeiro com `(Recomendado)`.
- Use `preview` quando as opções forem trechos de texto ou estruturas de seção
  comparáveis lado a lado.

**Não** pergunte o que você pode verificar sozinho nos arquivos, nem o que tem default
óbvio. Pergunta desnecessária custa a mesma interrupção que uma necessária.

## Decisões: depois de perguntar

Toda resposta do autor vira entrada `D-<n>` em `LOG.md`, com motivo e impacto. Decisão
que só existe no histórico da conversa está perdida no próximo `/clear`.
