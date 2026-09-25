#!/usr/bin/env bash
# Local P0 validation: repository validator + test suite, run with the registered project interpreter inside the
# 2025.2.1 launcher (the same commands AI_CONTROL/AUTO_PUSH_POLICY.yaml runs before a publish).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PY="${HLSDSE_PYTHON:-/home/benyamin/.venvs/hls_dse_py312/bin/python}"
[[ -x "$PY" ]] || { echo "P0_LOCAL_VALIDATION=FAIL: interpreter $PY not found (set HLSDSE_PYTHON)" >&2; exit 2; }
python3 "$ROOT/scripts/validate_project.py"
"$ROOT/environments/xilinx_2025_2_1/run_in_env.sh" "$PY" -m pytest -q -p no:cacheprovider
echo "P0_LOCAL_VALIDATION=PASS"
