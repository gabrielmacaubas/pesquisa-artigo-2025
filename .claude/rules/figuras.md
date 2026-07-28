# Figuras e Tabelas

## Princípio

A imagem **não** entra no markdown. O que entra é um **bloco de reserva** que declara o
que aquela posição precisa. Assim você sabe, sem ler o texto todo, exatamente que imagem
criar ou reutilizar — e o build sabe onde inseri-la.

## Formato do bloco (obrigatório, o gate valida)

```
[[FIG:03-1
  tipo: grafico-barras
  status: criar
  origem: n8n workflow "relatorio-mensal" / execução 2024-12
  dados: mapa-de-fatos §5.2
  descricao: Tempo médio de processamento por execução do workflow, jan–dez 2024
  legenda: Figura 3 — Tempo médio de processamento (s) por execução do workflow, 2024. Fonte: os autores.
  largura: 1col
  altura_cm: 6
  arquivo: figuras/fig-03-1.png
]]
```

Tabelas usam o mesmo formato com `[[TAB:03-1 ...]]`.

### Campos

| Campo | Valores / regra |
|---|---|
| **ID** | `FIG:<seção>-<n>` — `03-1` = primeira figura da seção 03. Estável: não renumere ao reordenar; a numeração final é do build. |
| `tipo` | `grafico-barras`, `grafico-linhas`, `diagrama-arquitetura`, `fluxograma`, `screenshot`, `tabela`, `foto` |
| `status` | `criar` (não existe), `reutilizar` (existe em `docs/` ou nos TCCs), `pronto` (arquivo já em `figuras/`) |
| `origem` | De onde vem o material: qual workflow n8n, qual execução, qual TCC e página. Obrigatório. |
| `dados` | Onde estão os números que sustentam a figura. Se for `[[VERIFICAR]]`, a figura não pode ser criada ainda. |
| `descricao` | Para **você**: o que a imagem precisa mostrar. Escrita como instrução, não como legenda. |
| `legenda` | Texto final que vai no artigo, já em formato ABNT: `Figura N — Título. Fonte: ...` |
| `largura` | `1col` (largura do texto) ou `meia` (duas lado a lado) |
| `altura_cm` | Estimativa — entra no orçamento de páginas |
| `arquivo` | Caminho previsto em `figuras/`. Nome = ID em minúsculo. |

## Chamada no corpo do texto (obrigatória)

Toda figura precisa ser chamada no texto **antes** de aparecer. Não escreva o número —
ele só é conhecido no build. Use o marcador inline:

```markdown
O tempo de processamento caiu ao longo do ano, conforme a [[@FIG:03-1]].
```

O build substitui `[[@FIG:03-1]]` por `Figura 3` e renumera tudo automaticamente. Assim
você pode reordenar seções sem renumerar nada à mão.

O gate cruza os dois sentidos e ambos são **bloqueantes**:
- bloco `[[FIG:03-1 ...]]` declarado sem nenhum `[[@FIG:03-1]]` no texto
- `[[@FIG:03-1]]` no texto sem bloco de declaração

Figura não referenciada no texto é erro de norma ABNT, não só descuido.

## Exigências da Revista Principia (bloqueiam a submissão)

- Figuras em `.jpg`/`.png` com **mínimo 300 dpi**.
- **Texto interno da figura em Times New Roman, tamanho ≥ 18**, proporcional. Isso
  inviabiliza a maioria dos screenshots de código e de tela — prefira redesenhar como
  diagrama, ou usar pseudocódigo no corpo do texto (a revista recomenda explicitamente).
- **Tabelas e quadros têm de ser editáveis — nunca imagem.** Use `[[TAB:...]]` com o
  conteúdo em markdown, não uma captura de planilha.
- `Fonte:` em Times New Roman 8, obrigatória: `dados da pesquisa`,
  `elaborado pelos autores` ou `Autor (ano, p. x)`.
- Elemento vem **logo após ser citado** no texto.
- **Screenshots com dados de discentes precisam de máscara** — ver
  `.claude/rules/dados-e-privacidade.md`. Nome, CPF, matrícula e e-mail não podem
  aparecer em nenhuma figura.

## Regras de conteúdo

- **Legenda autoexplicativa**: o leitor entende a figura sem ler o parágrafo. Inclua
  unidade, período e universo (n=).
- **`Fonte:` sempre**. `Fonte: os autores.` quando produzida pelo projeto;
  referência ABNT completa quando reutilizada de outro trabalho.
- **Reutilização dos TCCs**: figura vinda de TCC do grupo é citada
  (`Fonte: SILVA, 2023, p. 42.`) e o TCC entra em `refs.md`. Reutilizar sem citar é
  autoplágio, inclusive de imagem.
- **Screenshot do n8n**: só se o layout do workflow for o resultado em si. Screenshot
  para "mostrar que existe" ocupa página e não sustenta argumento — prefira um diagrama
  de arquitetura.
- **Legibilidade em 1 coluna**: gráfico com mais de 5 séries ou eixo com rótulo em 6pt
  não sobrevive à impressão. Prefira dois gráficos simples a um denso.

## Ao escrever uma seção

Insira o bloco na posição exata onde a figura deve aparecer, mesmo que ela ainda não
exista. `status: criar` é o estado normal durante a escrita — é assim que a lista de
imagens a produzir se monta sozinha.

Para ver tudo o que falta produzir:
```bash
python3 scripts/gate.py --figuras
```
