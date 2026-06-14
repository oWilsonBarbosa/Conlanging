#!/usr/bin/env bash
#
# extract_data.sh — unpack the zipped linguistic datasets in data/ into
# data/extracted/<dataset>/ for local use. The extracted output is git-ignored.
#
# Usage:
#   ./scripts/extract_data.sh            Extract all zips (skip already-extracted)
#   ./scripts/extract_data.sh --force    Re-extract, overwriting existing output
#   ./scripts/extract_data.sh --list     List archives without extracting
#   ./scripts/extract_data.sh --help     Show this help
#
set -euo pipefail

# Resolve paths relative to this script so it works from any CWD.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DATA_DIR="$REPO_ROOT/data"
OUT_DIR="$DATA_DIR/extracted"

FORCE=0
LIST_ONLY=0

for arg in "$@"; do
  case "$arg" in
    --force) FORCE=1 ;;
    --list)  LIST_ONLY=1 ;;
    --help|-h)
      grep '^#' "$0" | grep -v '^#!' | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *)
      echo "Unknown option: $arg (try --help)" >&2
      exit 2
      ;;
  esac
done

command -v unzip >/dev/null 2>&1 || { echo "Error: 'unzip' is not installed." >&2; exit 1; }

shopt -s nullglob
zips=("$DATA_DIR"/*.zip)
if [ ${#zips[@]} -eq 0 ]; then
  echo "No .zip files found in $DATA_DIR" >&2
  exit 1
fi

if [ "$LIST_ONLY" -eq 1 ]; then
  echo "Archives in $DATA_DIR:"
  for z in "${zips[@]}"; do
    printf '  %-32s %s\n' "$(basename "$z")" "$(du -h "$z" | cut -f1)"
  done
  exit 0
fi

mkdir -p "$OUT_DIR"
extracted=0; skipped=0

for z in "${zips[@]}"; do
  name="$(basename "$z" .zip)"
  dest="$OUT_DIR/$name"
  if [ -d "$dest" ] && [ "$FORCE" -eq 0 ]; then
    echo "skip   $name (already extracted; use --force to overwrite)"
    skipped=$((skipped + 1))
    continue
  fi
  echo "unzip  $name -> data/extracted/$name/"
  rm -rf "$dest"
  mkdir -p "$dest"
  unzip -q -o "$z" -d "$dest"
  extracted=$((extracted + 1))
done

echo "Done. Extracted: $extracted, skipped: $skipped. Output in: $OUT_DIR"
