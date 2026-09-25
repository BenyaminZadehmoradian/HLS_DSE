# AI_CONTROL Bypass Audit — V23.2 (post-implementation, P0/S00)

**Date:** 2026-09-25.
**Evidence:**
- `evidence/control_probe_results.json` (`bypass_paths`);
- `tests/test_control_plane.py`.

The pre-implementation audit, "there is no control layer to pass", is preserved at commit `d2a8523`.

**Enforcement points:**

| File | Function | Boundary |
|---|---|---|
| `src/hlsdse/control.py` | `_decide` | the single authorization decision |
| `src/hlsdse/control.py` | `run_authorized` | decide → log → execute only on ALLOW |
| `src/hlsdse/control.py` | `_execute` | the only tool executor; sealed, single-use, argv-bound decisions |
| `src/hlsdse/control.py` | `transition` | the only state-transition writer |
| `src/hlsdse/flow.py` | `run_command` | run-level executor → `run_authorized` |
| `src/hlsdse/scanning/environment.py` | `_version` | discovery → `run_authorized` |
| `environments/xilinx_2025_2_1/bin/<tool>` → `tool_gate.sh` | `tool_gate_main` | launcher PATH gate for 10 Xilinx tools |
| `scripts/validate_project.py` | `repository_control_errors` | static state / approval / provenance check |

| Path | Via | Tested | Classification |
|---|---|---|---|
| Agent → AI_CONTROL → Executor | `control.run_authorized` | A–N, POS | NO_BYPASS |
| Agent → Executor | `control._execute` | J (forged, reused, argv-tampered decisions) | NO_BYPASS |
| Agent → Adapter | `flow.run_command`, `scanning.environment._version` | J; AST guard | NO_BYPASS |
| CLI → Executor | `hlsdse` CLI | AST guard (the CLI imports no process API) | NO_BYPASS |
| Launcher → Tool (by name) | `run_in_env.sh` PATH → `bin/<tool>` → `tool_gate.sh` | K; real-launcher resolution check | NO_BYPASS |
| Launcher → `vitis_hls` shim → real `vitis-run` | `bin/vitis_hls` execs `$XILINX_VITIS/bin/vitis-run` | mock: reached with 0 decisions; strict-xfail test | **UNINTENTIONAL_BYPASS** (patch pending) |
| Launcher → Tool (absolute path argument) | `run_in_env.sh /mnt/data/Apps/…/vivado` (`exec "$@"`) | static | **UNINTENTIONAL_BYPASS** (patch pending) |
| Publisher → git / validation commands | `hlsdse.publish` | existing auto-push suite | INTENTIONAL_BYPASS (repository sync; policy-fixed commands; named tools still gated) |
| Direct state write | edit `RESEARCH_STATE.yaml` | L | NO_BYPASS at runtime (`STATE_PROVENANCE_INVALID`) |
| Direct lowest-layer invocation | shell or foreign code running a tool binary directly | — | OUTSIDE_REPOSITORY_CONTROL |
| Local git commit of approvals/state; plain `git push` | git | — | OUTSIDE_REPOSITORY_CONTROL (branch protection, signed commits) |

## Why the two launcher paths are still open

Closing them requires editing `environments/xilinx_2025_2_1/run_in_env.sh` and `bin/vitis_hls`. The harness's
permission check denied that edit in this run, so the edit was not attempted again.

The required change:
1. `bin/vitis_hls`: exec `"$(dirname "$(readlink -f "$0")")/vitis-run" --mode hls …`, i.e. the gated shim,
   instead of `$XILINX_VITIS/bin/vitis-run`.
2. `run_in_env.sh`:
   - export `HLSDSE_XILINX_ROOT="$XILINX_ROOT"` and `HLSDSE_ENVIRONMENT_ID=ENV-2025.2.1-XC7Z020-1`;
   - require each gated tool to resolve to `$ENV_DIR/bin/<tool>`;
   - before `exec "$@"`, refuse a first argument that resolves inside `$XILINX_ROOT`.

Until then, the gate cannot resolve the real tool, because the launcher does not export the tool root. Every Xilinx
tool invoked by name under the launcher is therefore DENIED (`TOOL_NOT_RESOLVED`, or earlier by policy). That
includes `-version` queries.

**Verdict: DIRECT BYPASS = DETECTED.** There are 2 unintentional launcher paths, both pending the launcher patch.
No unintentional bypass remains in the Python control path.
