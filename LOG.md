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

### D-1 — Repositório local, sem remote (2026-07-27)
- **Questão:** versionar em GitLab como o v1surgicalweb?
- **Escolha:** apenas local, `git init` sem remote.
- **Impacto:** sem CI; o gate roda manualmente. Backup é responsabilidade do autor.

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
