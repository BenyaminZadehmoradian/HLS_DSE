#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="$ROOT/src"
python "$ROOT/scripts/validate_project.py"
python -m pytest -q "$ROOT/tests"
echo "P0_LOCAL_VALIDATION=PASS"
