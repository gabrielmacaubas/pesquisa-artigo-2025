---
description: Etapa 1 — lê o dump do Gemini + docs/ e produz o mapa de fatos do projeto
---

Primeira etapa do fluxo. Objetivo: transformar as fontes brutas em um **mapa de fatos
verificáveis** que sustentará todo o artigo.

## Entrada
- `00-contexto/contexto-projeto.md` (dump do Gemini)
- `docs/` (TCCs, artigo 2024, diretrizes do veículo, manuais)
- `api-repo/` (código da API, se relevante como evidência)

## Procedimento

1. **Leia tudo.** Não amostre. Um fato perdido aqui vira `[[VERIFICAR]]` depois.

2. **Extraia para `00-contexto/mapa-de-fatos.md`**, com a fonte de cada item
   (`arquivo`, seção/página):
   - Identificação: título do projeto, período, instituições, financiamento
   - Pessoas: participantes, orientação, parcerias, papéis
   - Produção: os 4 TCCs (autor, título, ano), o artigo 2024 (onde saiu)
   - Arquitetura: n8n, API, hospedagem, geração de gráficos/planilhas, envio de e-mail
   - Dados quantitativos: **todo número que existir**, com unidade e período
   - Resultados já reportados no artigo de 2024

   Marque `[[VERIFICAR: ...]]` em tudo que estiver ausente ou conflitante entre fontes.
   Conflito entre fontes é achado importante — registre os dois valores, não escolha.

3. **Registre as referências** dos TCCs e do artigo 2024 em `refs.md`, formato completo.

4. **Leia as diretrizes do veículo** em `docs/` e registre em `LOG.md`: limite de
   páginas/palavras, estrutura de seções exigida, norma de citação, prazo. Isso
   **restringe o outline** — precisa estar decidido antes da etapa 2.

5. **Reporte ao autor**: o que foi encontrado, e uma lista objetiva das lacunas
   (`[[VERIFICAR]]`) que só ele pode preencher.

Não escreva nenhuma parte do artigo nesta etapa.
