#!/usr/bin/env bash
#
# fetch_data.sh — download the third-party linguistic datasets used by this
# project from their original sources. The datasets are NOT committed to this
# repository; this script reproduces the contents of data/ on demand.
#
# Each dataset carries its own license. Two are NON-COMMERCIAL (PBase,
# MorphoLex-en) and several are ShareAlike. See ATTRIBUTION.md for full credit,
# citations, and license obligations before you redistribute anything.
#
# Usage:
#   scripts/fetch_data.sh            # download everything in data/sources.csv
#   scripts/fetch_data.sh wals       # download only rows whose name matches
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
DATA_DIR="${REPO_ROOT}/data"
MANIFEST="${DATA_DIR}/sources.csv"

FILTER="${1:-}"

if [ ! -f "${MANIFEST}" ]; then
  echo "error: manifest not found at ${MANIFEST}" >&2
  exit 1
fi

# Pick a downloader.
if command -v curl >/dev/null 2>&1; then
  download() { curl -fL --retry 3 -o "$1" "$2"; }
elif command -v wget >/dev/null 2>&1; then
  download() { wget -O "$1" "$2"; }
else
  echo "error: need curl or wget on PATH" >&2
  exit 1
fi

mkdir -p "${DATA_DIR}"

# Skip the CSV header; read fields.
tail -n +2 "${MANIFEST}" | while IFS=',' read -r name url version license commercial_ok notes; do
  [ -z "${name}" ] && continue
  if [ -n "${FILTER}" ] && [[ "${name}" != *"${FILTER}"* ]]; then
    continue
  fi

  echo "----------------------------------------------------------------------"
  echo "dataset : ${name} (${version})"
  echo "license : ${license}  | commercial use ok: ${commercial_ok}"
  [ -n "${notes}" ] && echo "notes   : ${notes}"

  if [ "${commercial_ok}" = "no" ]; then
    echo "WARNING : ${name} is NON-COMMERCIAL. Do not use in commercial contexts."
  fi

  # PBase has no downloadable archive — flag for manual retrieval.
  case "${url}" in
    *.zip|*.tar.gz)
      out="${DATA_DIR}/${name}.zip"
      if [ -f "${out}" ]; then
        echo "skip    : ${out} already exists"
      else
        echo "fetch   : ${url}"
        download "${out}" "${url}"
        echo "saved   : ${out}"
      fi
      ;;
    *)
      echo "MANUAL  : no direct archive. Download by hand from: ${url}"
      ;;
  esac
done

echo "----------------------------------------------------------------------"
echo "Done. Downloaded archives live in ${DATA_DIR}/ and are git-ignored."
echo "Review ATTRIBUTION.md before redistributing any dataset."
