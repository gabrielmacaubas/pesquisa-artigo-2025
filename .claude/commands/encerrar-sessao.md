---
description: Fecha a sessão — atualiza ESTADO.md, registra em LOG.md e commita
---

Encerramento obrigatório. Sem isto, a próxima conversa (`/clear`) parte de informação
errada e o trabalho desta sessão se perde.

## Procedimento

1. **Rode `python3 scripts/gate.py`** e capture o resultado.

2. **Reescreva `ESTADO.md` inteiro** (é um retrato do agora, não um acumulado):
   - Etapa do fluxo, data, e **próxima ação** — específica o bastante para o autor só
     precisar dar `/clear` e o comando
   - Título, veículo, prazo, tese, contribuição sobre 2024 — conforme já decididos
   - Tabela de seções: arquivo, status, palavras real/alvo, lacunas abertas
   - Tabela de figuras pendentes (saída de `gate.py --figuras`)
   - Decisões ainda em aberto
   - Bloqueios — o que impede seguir e de quem depende

3. **Acrescente entrada em `LOG.md`** (append, nunca reescreva o que já está lá):
   `### <data> — Sessão N: <título>` com Feito / Decisões / Pendente / Próximo.
   Se houve decisão do autor nesta sessão, acrescente também um bloco `D-<n>`.

4. **Commit local:**
   ```bash
   git add -A && git commit -m "<etapa>: <o que mudou>"
   ```
   Mensagem descreve a etapa, não o arquivo. Ex.:
   `escreve metodologia: 1.380 palavras, 2 figuras pendentes, 3 lacunas`
   Não há remote — nada é enviado para lugar nenhum.

5. **Reporte ao autor** em 5 linhas: o que avançou, o que ele precisa decidir ou
   fornecer, e qual comando rodar na próxima conversa.
