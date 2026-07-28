# Voz e Estilo — não parecer texto de IA

> Calibrado empiricamente sobre o manuscrito de 2024, escrito pelo próprio grupo
> (331 frases analisadas). O objetivo não é "escrever bem em abstrato": é escrever como
> **estes autores** escrevem. Um artigo que destoa do texto anterior do mesmo grupo
> levanta suspeita em avaliação — e hoje periódicos rodam detecção.

## Perfil medido do grupo (2024)

| Métrica | Valor do grupo | Default de IA | Ação |
|---|---|---|---|
| Palavras por frase (média) | **25,4** | 15–20 | **Escreva frases longas.** Frase curta demais destoa. |
| Mediana / p90 / máximo | 25 / 43 / 79 | — | Variação ampla é normal aqui |
| Palavras por parágrafo | **81** | 40–60 | Parágrafos densos, 4 a 6 frases |
| Primeira pessoa do plural | **0 ocorrências** | comum | **Sempre impessoal** (exigência da revista também) |
| Construções impessoais | 29 | — | `foi/foram`, `utilizou-se`, `observou-se`, `adotou-se` |

## Conectivos: use os deles

Frequência real no texto de 2024:

- **`Por meio de` — 26 usos.** É a marca registrada do grupo. Use à vontade.
- `Além disso` — 10
- `Assim` — 4 · `Dessa forma` — 2 · `Sendo assim` — 2 · `No entanto` — 2 · `Diante disso` — 1

**Nunca apareceram, e não devem aparecer:** `Ademais`, `Outrossim`, `Nesse sentido`,
`Cumpre destacar`, `Vale salientar`, `Por conseguinte`, `Destarte`, `Em suma`,
`Em síntese`. São conectivos que LLM adora e que este grupo não usa — cada ocorrência é
uma impressão digital.

## Marcadores de texto gerado — evitar

### Estruturais (os que mais denunciam)
- **Tríades.** "eficiência, escalabilidade e confiabilidade", "planejar, executar e
  monitorar". Um LLM enumera em três quase por reflexo. Se a frase tem três adjetivos ou
  três substantivos coordenados, corte para dois ou reescreva.
- **Paralelismo excessivo** entre parágrafos consecutivos (todos abrindo com conectivo,
  todos com o mesmo comprimento, todos fechando com uma síntese).
- **Frase-resumo no fim de cada parágrafo.** "Dessa forma, a automação mostrou-se
  eficaz." Fecha o parágrafo sem acrescentar nada. Corte.
- **Bullet list no corpo do artigo.** O texto de 2024 é prosa corrida. Listas só onde a
  revista prevê (enumeração de requisitos, passos do método).
- **Travessão em par** (—) para aposto. Português acadêmico brasileiro usa vírgula ou
  parênteses; o travessão duplo é hábito de LLM.

### Lexicais
Palavras que o grupo **não** usa e que sinalizam geração automática: `robusto`,
`abrangente`, `holístico`, `poderoso`, `revolucionário`, `inovador` (como adjetivo
avaliativo), `aprofundar-se`, `mergulhar`, `panorama`, `cenário atual`, `na era digital`,
`desempenha um papel`, `de suma importância`, `é importante ressaltar`, `vale destacar`.

O grupo usa com moderação e naturalidade: `fundamental` (3), `eficaz` (3),
`significativo` (2), `crucial` (1), `não apenas… mas também` (3). Manter nessa dosagem —
não zerar, mas não multiplicar.

### Semânticos
- **Adjetivo avaliativo sem número atrás.** "resultados expressivos" → dê o número.
- **Afirmação genérica sobre tecnologia** que valeria para qualquer sistema
  ("a automação promove eficiência e agilidade"). Se a frase continuaria verdadeira
  trocando o objeto de estudo, ela não diz nada.
- **Hedge acumulado.** "pode potencialmente contribuir para possíveis melhorias."

## Como escrever para não destoar

1. **Comece pela evidência, não pela moldura.** O grupo abre parágrafos com o fato e
   depois contextualiza. LLM abre com contextualização vazia.
2. **Deixe a frase respirar até onde a ideia exige.** Não quebre uma frase de 40 palavras
   em três de 13 — no registro deste grupo, isso é que soa estranho.
3. **Aceite assimetria.** Um parágrafo de 3 frases seguido de um de 7 é natural. Blocos
   uniformes são artificiais.
4. **Termos do projeto, sempre os mesmos.** `discente` (não "aluno"/"estudante"
   alternando), `unidade`, `soft skill`, `sub-soft skill`, `mentor`, `autoavaliação`.
   Sinônimo elegante é ruído em texto técnico — e é outro hábito de LLM.

## Verificação

`python3 scripts/gate.py --estilo` roda a checagem mecânica: comprimento médio de frase e
parágrafo por seção, conectivos proibidos, marcadores lexicais e tríades. Não substitui
a leitura, mas pega o grosso.

Na review (`.claude/rules/review-artigo.md` §7), a pergunta a fazer em cada seção é:
**"um avaliador que leu o manuscrito de 2024 reconheceria a mesma mão aqui?"** Se a
resposta for não, o problema é de voz, mesmo que o conteúdo esteja correto.
