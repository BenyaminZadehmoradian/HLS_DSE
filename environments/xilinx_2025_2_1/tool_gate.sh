#!/usr/bin/env bash
# Control-plane PATH gate for the AMD-Xilinx tools of the 2025.2.1 environment.
#
# bin/<tool> shims exec this script with the tool name. It hands the request to hlsdse.control
# (tool_gate_main -> run_authorized): the invocation is classified by tool identity, authorized against
# RESEARCH_STATE.yaml, the human approval artifacts and AI_CONTROL/CONTROL_PLANE_POLICY.yaml, logged to
# audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl, and only on ALLOW is the real tool (resolved behind this gate,
# inside $HLSDSE_XILINX_ROOT) executed. DENY exits 126 without starting the tool.
set -euo pipefail

tool="${1:?tool name required}"; shift
GATE_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
ROOT="$(cd "$GATE_DIR/../.." && pwd)"
CONTROL_PYTHON=/usr/bin/python3        # system interpreter; -E ignores vendor PYTHON* variables, -B writes no bytecode

[[ "${HLSDSE_XILINX_ENV:-}" == "2025.2.1" ]] \
    || { echo "HLSDSE_CONTROL_DENY: $tool gate used outside run_in_env.sh" >&2; exit 126; }
[[ -x "$CONTROL_PYTHON" ]] || { echo "HLSDSE_CONTROL_DENY: control interpreter $CONTROL_PYTHON missing" >&2; exit 126; }

exec env -u LD_LIBRARY_PATH -u LD_PRELOAD "$CONTROL_PYTHON" -E -B -c \
    'import sys; sys.path.insert(0, sys.argv[1]); from hlsdse.control import tool_gate_main; raise SystemExit(tool_gate_main(sys.argv[2:]))' \
    "$ROOT/src" --root "$ROOT" --tool "$tool" --shim-dir "$GATE_DIR/bin" -- "$@"
