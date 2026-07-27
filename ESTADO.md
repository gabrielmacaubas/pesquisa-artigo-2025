# ESTADO — leia isto primeiro

> **Este é o arquivo de retomada.** Toda conversa nova começa lendo `CLAUDE.md` e depois
> este arquivo. Ele descreve **onde o projeto está agora**. É reescrito (não acumulado) ao
> final de cada sessão. O histórico acumulado vive em `LOG.md`.

---

## Situação atual

**Etapa do fluxo:** 0 — scaffold criado, contexto ainda não ingerido
**Última atualização:** 2026-07-27
**Próxima ação:** o autor cola o dump do Gemini em `00-contexto/contexto-projeto.md`,
depois roda `/ingerir-contexto`

## O artigo

- **Título provisório:** [[DECIDIR]]
- **Veículo de destino:** [[VERIFICAR: confirmar se é a Revista Principia — há diretrizes em `docs/`]]
- **Prazo:** [[VERIFICAR]]
- **Teto:** 20 páginas (alvo de trabalho: 18)
- **Tese:** ainda não definida — etapa 2
- **Contribuição sobre o artigo de 2024:** ainda não definida — etapa 2

## Decisões já tomadas

| # | Decisão | Quando |
|---|---|---|
| 1 | Repositório local apenas, sem remote (sem GitLab/GitHub) | 2026-07-27 |
| 2 | Conteúdo em `.md` por seção; ABNT aplicada só no build | 2026-07-27 |
| 3 | Formato final: `.docx` via pandoc → ajuste no Google Docs | 2026-07-27 |

## Decisões pendentes (usar `AskUserQuestion`)

- [ ] Tese do artigo de 2025
- [ ] Ordem de autoria
- [ ] Pessoa verbal (terceira pessoa vs. primeira do plural)
- [ ] Destino final é Google Docs ou PDF direto (muda a estratégia de build)

## Seções

| Arquivo | Status | Palavras (real/alvo) | Lacunas abertas |
|---|---|---|---|
| — | outline não definido | — | — |

## Figuras a produzir

| ID | Status | O que é |
|---|---|---|
| — | — | ainda não há seções escritas |

## Pendências de ambiente

- [ ] `pandoc` não instalado (`sudo apt install pandoc`) — necessário só na etapa 7
- [ ] `scripts/reference-abnt.docx` ainda não criado

## Bloqueios

- Aguardando dump do Gemini em `00-contexto/contexto-projeto.md`
