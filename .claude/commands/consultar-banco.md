---
description: Extrai dados AGREGADOS do banco de produção (Neon) para o mapa de fatos
---

Consulta: $ARGUMENTS

## Regras inegociáveis

O banco contém **nome, CPF, matrícula e e-mail reais** de 33 discentes, associados a
avaliações socioemocionais. Ver `.claude/rules/dados-e-privacidade.md`.

1. **Somente consultas agregadas** — `count`, `avg`, `min`, `max`, `sum`, `group by`.
2. **Nunca** `select nome`, `select cpf`, `select email`, `select *`, nem listagem de
   linhas individuais. Se a pergunta do autor exigir isso, responda o agregado
   equivalente e explique por quê.
3. **Nunca imprima as credenciais.** Carregue-as do `.env` para variáveis de ambiente.
4. Se a consulta retornar poucos grupos (n < 5), avalie risco de reidentificação antes
   de registrar.

## Como conectar

```bash
cd api-repo/automacao-deploy-main && eval "$(python3 -c "
d={}
for l in open('.env',encoding='utf-8',errors='replace'):
    l=l.strip()
    if '=' in l and not l.startswith('#'):
        k,v=l.split('=',1); d[k.strip()]=v.strip().strip('\"').strip(\"'\")
print('export PGPASSWORD=%r PGHOST=%r PGPORT=%r PGDATABASE=%r PGUSER=%r PGSSLMODE=require' % (
    d['POSTGRES_PASSWORD'],d['POSTGRES_HOST'],d['POSTGRES_DB_PORT'],
    d['POSTGRES_DATABASE'],d['POSTGRES_USER']))
")" && timeout 60 psql -P pager=off -c "SUA_CONSULTA_AGREGADA"
```

Nomes de coluna úteis: `cadastrado_em` (não `criado_em`), `unidade`, `nota`,
`soft_skill_id`, `sub_soft_skill_id`, `discente_id`, `autoavaliacao_id`.

⚠️ `pg_stat_user_tables.n_live_tup` é **estimativa** e pode reportar zero para tabela
populada. Sempre confirme com `count(*)` antes de registrar um número.

## Depois de consultar

1. Registre em `00-contexto/mapa-de-fatos.md` §6, **com a data da consulta** — o banco é
   vivo; número sem data é irreproduzível.
2. Anote a consulta SQL usada, para que o resultado seja auditável.
3. Se o número contradisser algo já registrado, **não sobrescreva** — registre os dois e
   marque o conflito.
4. Ao reportar ao autor, diga o que o número sustenta e o que ele **não** sustenta. Um
   recorte de 33 discentes demonstra viabilidade em operação, não escala.
