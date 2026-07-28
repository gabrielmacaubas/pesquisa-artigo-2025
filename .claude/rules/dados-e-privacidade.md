# Dados e Privacidade

O banco de produção (Neon) contém **nome, CPF, matrícula e e-mail acadêmico reais** de 33
discentes, associados a avaliações de competências socioemocionais. Dado pessoal, e a
avaliação socioemocional é categoria sensível.

Isso não é um problema teórico: o artigo será publicado em acesso aberto, e figuras vindas
de screenshots são a via mais provável de vazamento — Swagger com payload real, planilha
do Google Sheets, tela do n8n com nomes na saída.

## Regras

1. **Toda consulta ao banco é agregada.** `count`, `avg`, `min`, `max`, `group by`.
   Nunca `select nome`, `select cpf`, nunca listagem de linhas individuais.
2. **Nenhum dado individual entra no artigo** — nem em tabela, nem em figura, nem em
   exemplo ilustrativo, nem anonimizado por iniciais.
3. **Screenshots são mascarados antes de virar figura.** Se o mascaramento ficar visível
   e feio, prefira um diagrama esquemático — a revista aceita, e comunica melhor.
4. **Nada de credencial no repositório.** `api-repo/.../.env` está no `.gitignore`;
   nunca cole host, usuário ou senha em arquivo versionado, seção do artigo ou figura.
   Ao documentar a arquitetura, escreva "instância gerenciada na região us-east-1", não
   o hostname.
5. **Exemplos são fictícios e declarados como tal.** Se o texto precisar de um caso
   ilustrativo, construa um sintético e diga que é sintético.

## Como consultar

Use o comando `/consultar-banco`, que carrega as credenciais do `.env` sem imprimi-las e
exige que a consulta seja agregada. Toda extração usada no artigo é registrada em
`00-contexto/mapa-de-fatos.md` com a **data da consulta** — o banco é vivo, então um
número sem data é irreproduzível.

## Ao escrever a seção de método

Descreva o tratamento dos dados: que os dados são operacionais do programa, que a análise
foi conduzida sobre agregados e que nenhum dado individual é reportado. Isso é uma
frase, custa nada, e é exatamente o que um avaliador procura quando vê "33 discentes".
