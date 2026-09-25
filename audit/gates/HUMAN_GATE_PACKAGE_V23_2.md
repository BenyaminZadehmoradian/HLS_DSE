# Human Gate Package — V23.2 / P0 / S00

This package prepares the human gate decision. **It does not make that decision.** Nothing in it authorizes P0, sets `active_environment`, or changes `RESEARCH_STATE.yaml`.

Validated: 2026-09-25T17:01:35+02:00 · HEAD `0f65dba` (local; `origin/main` = `db53266`; 2 local-only commits: `ada921f`, `0f65dba`)
Detailed evidence: `audit/environment/FINAL_PRE_P0_READINESS_AUDIT_V23_2.md` (sha256 `0822ce31…d8ef7`) and `…_SNAPSHOT_V23_2.json` (sha256 `8d795c58…ad406`)

## Current State

```text
Project: V23.2
Phase: P0
Study: S00
Status: READY_FOR_HUMAN_GATE
```

`RESEARCH_STATE.yaml` (sha256 `f78cd188…90de`) holds:

- `current_phase: P0`, `current_study: S00`, `active_phase_state: PLANNED`
- `human_gate_required: true`
- `p1_authorized: false`
- `automatic_advance: false`
- `future_phase_implementation_allowed: false`
- `active_environment: null`

## Technical Readiness

| Item | Status | Evidence |
|---|---|---|
| Repository consistency | PASS | Worktree clean; `git diff origin/main...HEAD --check` exit 0; the two local commits change only launcher, contracts, registry and audit files. No state, run or evidence changes. |
| Validator | PASS | `python3 scripts/validate_project.py` → `errors=0 warnings=0` |
| Python/pytest | PASS | venv `~/.venvs/hls_dse_py312` (Python 3.12.3, isolated, pytest 9.1.1, PyYAML 6.0.3) → `4 passed in 0.02s`. System Python unchanged. |
| Xilinx toolchain | PASS | Via `run_in_env.sh`: vivado, Vitis, vitis-run and v++ all report v2025.2.1; `vitis_hls` resolves to the project shim; no 2023.2 entry on PATH; `settings64.sh` sha256 `c53e2d30…aab3bb`; preflight exit 0, `ENVIRONMENT_TOOLS_VISIBLE` |
| Device | PASS | `xc7z020clg484`, consistent across contracts, state, schemas and registry; Vivado `get_parts` reports `xc7z020clg484-1` |
| Speed grade | FIXED_REFERENCE_CONFIGURATION | `-1` fixed by human decision (tool part `xc7z020clg484-1`); **not** derived from board identification |
| Workspace | PASS | `/mnt/data/HLS_DSE_work`: owner `benyamin:benyamin`, mode 750, writable, `/dev/sda4` xfs, 11,550,461,599,744 B available. Not yet bound to the run layout. |
| Vivado synthesis license | VERIFIED | Scope is **Vivado Synthesis on xc7z020 only**. External evidence: user-run session outside the repo, log `…/Learn_Zynq/zynq_gemm_xc7z020/…/synth_1/design_1_wrapper.vds`, sha256 `9201bd6e…0604`, session start `Fri Sep 25 13:58:22 2026`, line 39 `INFO: [Common 17-349] Got license for feature 'Synthesis' and/or device 'xc7z020'`. The whole Xilinx toolchain license is **NOT_VERIFIED**. |
| Hardware | NOT_AVAILABLE | No physical board; `board: NONE`, `hardware_available: false` |
| Programming | NOT_AVAILABLE | `HARDWARE_PLATFORM_CONTRACT.platform_status.programming_available: false` |
| Runtime | NOT_AVAILABLE | `runtime_measurement_available: false`. DMA, ACP, cache, programming time and runtime remain `UNKNOWN_UNTIL_MEASURED`. |

## Environment Notes

These are configuration changes, not research results.

- **ENVIRONMENT_CHANGE:** the kernel changed from `7.0.0-31-generic` (recorded in the toolchain snapshot at `db53266`) to `7.0.0-34-generic`. `TOOLCHAIN_DEVICE_CONTRACT` bases environment identity on toolchain and device differences and requires `os_image` to be recorded. The registry entry already records 7.0.0-34, so no new environment ID is required. No P0 measurement was taken under either kernel.
- **Python dependency:** PyYAML 6.0.3 was installed into the isolated venv (`include-system-site-packages = false`). The system Python is unchanged (PyYAML 6.0.1, no pytest).

## Governance Decisions Required

1. **Confirm the device-contract interpretation.**
   - Assessment: `CONTRACT_INTERPRETATION: CONSISTENT`. The part `xc7z020clg484` is unchanged. `speed_grade` and `board` were declared placeholders (`UNKNOWN_UNTIL_FIXED`). `TOOLCHAIN_DEVICE_CONTRACT` lists both fields as optional, and `DEVICE_REFERENCE_CONTRACT` requires a new project version only for a device change.
   - The human gate must confirm or reject this reading. The project version was not changed.
2. **Approve `ENV-2025.2.1-XC7Z020-1` as the active environment.**
   - Proposed value: `active_environment: ENV-2025.2.1-XC7Z020-1`
   - Current state: UNASSIGNED (`null`)
3. **Explicitly authorize P0.** P0 is not authorized, and this package does not authorize it.

## Non-blocking notes for the reviewer

- The license checkout was observed outside `run_in_env.sh`. A checkout inside the launcher remains UNKNOWN until the first authorized synthesis.
- The workspace is not yet bound to `runs/<STUDY_ID>/<RUN_ID>/`, and no contract defines a minimum size. P0/S00 generates no vendor artifacts.
- Known limits of the preflight scanner:
  - the vitis version field records only the banner line;
  - `device_support.verified` is hard-coded to `false`;
  - license, disk and CPU checks are not implemented.
