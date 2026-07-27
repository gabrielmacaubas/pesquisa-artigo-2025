# Prompt para o Gemini — extração do contexto do projeto

**Como usar:** abra a conversa do Gemini onde você construiu o TCC, cole o bloco abaixo
como última mensagem, e salve a resposta inteira em
`00-contexto/contexto-projeto.md` (texto puro, sem editar).

Se a resposta vier truncada, peça: *"continue exatamente de onde parou, sem repetir o que
já escreveu"* — e concatene no mesmo arquivo.

---

```
Preciso que você produza um documento de transferência de contexto sobre este projeto de
pesquisa. Ele será lido por outro assistente de IA (Claude), que NÃO tem acesso a esta
conversa e vai escrever, a partir dele, um artigo científico de 2025.

Esse assistente também terá acesso a arquivos PDF: os TCCs produzidos e o artigo
publicado em 2024. Portanto NÃO precisa reproduzir o conteúdo desses documentos — mas
precisa saber que eles existem, o que cada um cobre e como se relacionam.

REGRAS CRÍTICAS PARA ESTA RESPOSTA:

1. Escreva APENAS o que você efetivamente tem registrado nesta conversa. Este documento
   vai virar base factual de um artigo científico — informação inventada aqui se torna
   fraude acadêmica lá adiante.
2. Onde você não souber, escreva literalmente: [[LACUNA: <a pergunta específica que o
   autor precisa responder>]]. Uma lacuna explícita vale muito mais que um preenchimento
   plausível. Não estime, não arredonde, não complete por analogia.
3. Para CADA número, data e nome próprio, indique entre parênteses de onde veio nesta
   conversa (ex.: "(informado pelo autor)", "(consta no TCC do Gabriel)", "(saída do
   workflow n8n)"). Se não souber a procedência, marque [[LACUNA: procedência]].
4. Não escreva prosa de artigo, não faça introdução acadêmica, não tente ser eloquente.
   Isto é um dossiê de fatos. Denso, direto, organizado.
5. Não omita nada por parecer óbvio ou irrelevante. Quem vai ler não sabe nada.

ESTRUTURA OBRIGATÓRIA DA RESPOSTA:

## 1. Identificação do projeto
Nome/título do projeto. Instituição(ões). Curso/programa. Período exato de início e fim
(2 anos — quais?). Financiamento, edital, bolsa ou apoio institucional, se houve.
Vínculo com programas externos (ex.: EMBRAPII), se houver.

## 2. Problema e motivação
Qual problema real o projeto foi criado para resolver. Quem sofria esse problema.
Como era feito antes (o processo manual que a automação substituiu). Por que isso
importava.

## 3. Pessoas e papéis
Todos os envolvidos: nome completo, papel (autor, orientador, coorientador, bolsista,
parceiro externo, cliente). Quem fez o quê. Quem orientou. Se houver preferência ou
acordo sobre ordem de autoria já discutido, registre; se não, marque [[LACUNA]].

## 4. Parcerias
Organizações parceiras, natureza da parceria (dados, infraestrutura, validação, uso
real), o que cada uma forneceu ou recebeu. Se houve usuário/cliente real usando o
sistema, quem foi e em que escala.

## 5. Arquitetura técnica
Descreva o sistema em detalhe:
- Workflows n8n: quais existem, o que cada um faz, gatilho (cron? webhook?), frequência.
- A API: linguagem, framework, endpoints principais, o que ela expõe e por quê.
- Hospedagem: onde, em que plano gratuito, quais limites isso impôs ao design.
- Fontes de dados: de onde vêm os dados que entram no fluxo.
- Geração de gráficos: qual biblioteca/serviço, que gráficos são produzidos.
- Geração de planilhas: formato, conteúdo, destino.
- Recomendações por e-mail: como são geradas (regra? modelo? heurística?), para quem vão,
  com que frequência, qual o conteúdo típico.
- Decisões de projeto não óbvias e o motivo delas (por que n8n e não X; por que free tier;
  por que e-mail e não dashboard).

## 6. Dados quantitativos — SEÇÃO MAIS IMPORTANTE
Liste TODO número que aparecer nesta conversa, com unidade, período e procedência:
volume de dados processados, número de execuções, usuários atendidos, e-mails enviados,
tempo de processamento, taxa de erro, custo, economia de tempo, resultados de avaliação
ou validação. Se um número foi mencionado de forma vaga ("muitos", "quase todos"),
registre a forma vaga E marque [[LACUNA: valor exato]].
Se NÃO houver números nesta conversa, diga isso explicitamente — é uma informação
crucial para quem vai escrever o artigo.

## 7. Produção acadêmica
Os 4 TCCs: autor, título, ano, e o recorte específico de cada um (o que aquele TCC
cobriu que os outros não).
O artigo de 2024: título, veículo/evento onde saiu, autores na ordem correta, qual foi a
tese dele e quais resultados apresentou.
Qualquer outra produção: apresentações, relatórios, prêmios, registros de software.

## 8. O que mudou entre 2024 e 2025
Esta é a pergunta central do artigo novo. O que aconteceu depois do artigo de 2024:
funcionalidade nova, mais dados, novo parceiro, novo resultado, mudança de arquitetura,
uso em produção, validação com usuários. Seja específico e datado. Se nada substantivo
mudou, diga isso claramente.

## 9. Limitações e problemas conhecidos
O que o sistema não faz. O que deu errado. Restrições do plano gratuito. Vieses ou
fragilidades dos dados. Ameaças à validade dos resultados. Isto será escrito no artigo
de qualquer forma — melhor vir de você do que ser descoberto pela banca.

## 10. Material visual existente
Gráficos, diagramas, screenshots, tabelas que já foram produzidos (nos TCCs, no artigo de
2024 ou pela automação). Para cada um: o que mostra, onde está, e se poderia ser
reaproveitado.

## 11. Ética e dados
O projeto lidou com dados de pessoas? Houve consentimento, anonimização, aprovação em
comitê de ética? Há algo que não pode ser publicado?

## 12. Vocabulário do projeto
Termos técnicos, siglas e nomes internos usados no projeto, com a definição que vocês
adotaram. Isso mantém a terminologia consistente no artigo.

## 13. Lacunas consolidadas
Repita ao final, em lista única e numerada, TODAS as [[LACUNA: ...]] que você marcou ao
longo do documento. Esta lista será a primeira coisa que o autor vai responder.
```

---

## Depois de salvar a resposta

1. Salve em `00-contexto/contexto-projeto.md`
2. Leia a seção 13 (lacunas) e responda o que souber, direto no arquivo, marcando suas
   respostas com `> RESPOSTA DO AUTOR:`
3. Rode `/ingerir-contexto`
