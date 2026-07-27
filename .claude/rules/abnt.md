# ABNT — aplicada no build, não no markdown

## Princípio

Os arquivos em `secoes/` não contêm formatação. A ABNT é aplicada **uma única vez**, no
build, via `reference.docx` (template de estilos) do pandoc. Se você se pegar ajustando
espaçamento dentro de um `.md`, parou de escrever e começou a diagramar.

## O que o template `reference.docx` precisa carregar

Norma de referência: ABNT NBR 14724 (trabalhos acadêmicos), NBR 6023 (referências),
NBR 10520 (citações), NBR 6028 (resumo). **Confirme sempre com o template do
veículo/instituição de destino — ele prevalece sobre o padrão genérico abaixo.**

| Elemento | Padrão |
|---|---|
| Fonte | Arial ou Times New Roman 12 |
| Espaçamento (corpo) | 1,5 |
| Espaçamento (citação longa, notas, legendas, referências) | simples |
| Margens | esq/sup 3 cm, dir/inf 2 cm |
| Recuo 1ª linha do parágrafo | 1,25 cm |
| Citação direta longa (4+ linhas) | recuo 4 cm da margem esquerda, fonte 10, sem aspas |
| Títulos de seção | numeração progressiva (1, 1.1, 1.1.1), alinhados à esquerda |
| Referências | ordem alfabética, alinhadas à esquerda, separadas por linha em branco |
| Paginação | canto superior direito, contagem desde a capa, exibida a partir da introdução |

## Como criar o `reference.docx`

```bash
pandoc -o build/reference.docx --print-default-data-file reference.docx
```
Abra no Google Docs/LibreOffice, ajuste os **estilos** (Normal, Título 1-3, Citação,
Bibliografia) conforme a tabela, salve em `scripts/reference-abnt.docx` e versione.
Ajuste estilos — não formate parágrafos manualmente, ou o pandoc ignora.

## Elementos pré-textuais

Capa, folha de rosto, resumo, abstract, palavras-chave, sumário: **não** ficam nas
seções. Ou vão no `reference.docx`/no template do veículo, ou são montados no Google Docs
ao final. Exceção: `resumo` e `abstract` são conteúdo — ficam em
`secoes/00-resumo.md`, sem formatação.

## Se o destino final for PDF

Considere pular o Docs: `abntex2` (LaTeX) entrega ABNT correta sem trabalho manual e sem
o risco de a formatação escorregar a cada edição. Vale quando não há coautor revisando no
Docs. Decisão registrada em `LOG.md`.
