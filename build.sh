#!/usr/bin/env bash
# Rebuild the static site in dist/ from the design canvas files in project/.
set -euo pipefail
cd "$(dirname "$0")"
rm -rf dist
node export/export.js project dist
