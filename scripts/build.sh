#!/usr/bin/env bash
# Monta o artigo e converte para .docx com estilos ABNT.
#   bash scripts/build.sh          # gera build/artigo.docx
#   bash scripts/build.sh --md     # só o markdown consolidado
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RAIZ"

echo "── gate ─────────────────────────────────"
set +e
python3 scripts/gate.py
GATE=$?
set -e
if [ "$GATE" -eq 1 ]; then
  echo
  echo "🔴 Gate bloqueante. Corrija antes de gerar o documento."
  exit 1
elif [ "$GATE" -eq 2 ]; then
  echo
  echo "🟡 Há pendências abertas. Gerando mesmo assim (rascunho) — não submeta."
fi

echo
echo "── montagem ─────────────────────────────"
python3 scripts/build.py

[ "${1:-}" = "--md" ] && { echo "Pronto: build/artigo.md"; exit 0; }

if ! command -v pandoc >/dev/null 2>&1; then
  echo
  echo "pandoc não instalado — parando em build/artigo.md"
  echo "  sudo apt install pandoc            # .docx"
  echo "  sudo apt install texlive-xetex     # + PDF direto"
  exit 0
fi

echo
echo "── pandoc ───────────────────────────────"
REF_DOC="scripts/reference-abnt.docx"
ARGS=(build/artigo.md -o build/artigo.docx --resource-path=.:figuras)

if [ -f "$REF_DOC" ]; then
  ARGS+=(--reference-doc="$REF_DOC")
else
  echo "⚠️  $REF_DOC não existe — saindo com estilos padrão do pandoc (não é ABNT)."
  echo "    Para criar o template uma única vez:"
  echo "      pandoc -o $REF_DOC --print-default-data-file reference.docx"
  echo "    depois ajuste os ESTILOS (Normal, Título 1-3, Citação, Bibliografia)"
  echo "    conforme .claude/rules/abnt.md e versione o arquivo."
fi

pandoc "${ARGS[@]}"
python3 scripts/formato_principia.py

if command -v soffice >/dev/null 2>&1; then
  echo
  echo "── pdf ──────────────────────────────────"
  soffice --headless --convert-to pdf --outdir build build/artigo.docx >/dev/null 2>&1
  if [ -f build/artigo.pdf ]; then
    PAGS=$(pdfinfo build/artigo.pdf 2>/dev/null | awk '/^Pages:/{print $2}')
    echo "Pronto: build/artigo.pdf${PAGS:+  ($PAGS páginas reais)}"
  fi
fi

echo "Pronto: build/artigo.docx"
echo
echo "Próximo passo: subir no Google Docs (Arquivo > Abrir > Upload) e conferir"
echo "capa, sumário e paginação — ver .claude/rules/abnt.md."
