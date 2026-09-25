# Final Pre-P0 Readiness Audit — V23.2

**Project:** HLS-DSE V23.2 · **Phase:** P0 (PLANNED) · **Study:** S00
**Audit timestamp:** 2026-09-25T16:50:55+02:00 · **Base HEAD:** `ada921ff946ef42b38f92289dfcbbcccc66a5f6a` (origin/main `db53266`)
**Machine-readable copy:** `FINAL_PRE_P0_READINESS_SNAPSHOT_V23_2.json`

## Decision

**READY_FOR_HUMAN_GATE**

```text
Technical pre-P0 prerequisites: PASS
Human Gate: REQUIRED
P0 execution: NOT AUTHORIZED
```

This decision does not start P0. It only means that nothing technical is left before the human gate.

## Findings reviewed before any change

A repository search for the device and environment terms found:

- **Configuration/contract files that define the device:**
  - `contracts/DEVICE_REFERENCE_CONTRACT.yaml`, `contracts/HARDWARE_PLATFORM_CONTRACT.yaml` and `contracts/TOOLCHAIN_DEVICE_CONTRACT.yaml` each still held `UNKNOWN_UNTIL_FIXED` for the speed grade. The first two also held it for the board.
  - The following fix only the part string `xc7z020clg484`: `ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT`, `SYSTEM_ARCHITECTURE_CONTRACT`, `MEMORY_PATH_CONTRACT`, `P1_IMPLEMENTATION_CONTRACT`, `RESEARCH_STATE.yaml`, `configs/preflight/default.yaml`, and the run templates.
- **Schemas:** `STUDY_RUN_SCHEMA.json` and `RUN_MANIFEST_SCHEMA.json` constrain `device_part` to exactly `"xc7z020clg484"`, and `validate_project.py` checks the same string. The speed grade is therefore recorded as a separate field. Vivado receives `xc7z020clg484-1` as the tool part string.
- **Environment registry:** it held only the template entry `ENV-001`. `TOOLCHAIN_DEVICE_CONTRACT` requires that "toolchain/device differences create distinct environment IDs", so registering an environment is consistent with the contract.
- **Historical audits** (`PRE_P0_*`, `ENVIRONMENT_DISCOVERY_REPORT.md`) mention `UNKNOWN_UNTIL_FIXED`. These are records of earlier states and were left unchanged.
- **Contract tension, resolved by interpretation:** `DEVICE_REFERENCE_CONTRACT` requires a new project version for a device change. The part is unchanged. The speed grade and board were declared placeholders (`UNKNOWN_UNTIL_FIXED`) intended to be fixed later. Resolving them is therefore treated as fixing a placeholder, not changing the device. The human reviewer should confirm this interpretation at the gate.
- **Environment drift since the toolchain audit:** the kernel changed from `7.0.0-31-generic` to `7.0.0-34-generic`. PyYAML 6.0.3 was installed into the venv outside this session.

## A. Repository

| Check | Command | Exit | Result |
|---|---|---|---|
| Branch / HEAD | `git rev-parse HEAD origin/main` | 0 | `main`, `ada921f` (1 commit ahead of `origin/main` `db53266`); clean at start |
| Whitespace | `git diff --check` | 0 | clean |
| Validator (system Python) | `python3 scripts/validate_project.py` | 0 | `errors=0 warnings=0` |
| Validator (venv) | `run_in_env.sh ~/.venvs/hls_dse_py312/bin/python scripts/validate_project.py` | 0 | `errors=0 warnings=0` |
| pytest | `run_in_env.sh ~/.venvs/hls_dse_py312/bin/python -m pytest -q -p no:cacheprovider` | 0 | `4 passed in 0.02s` |

## B. Toolchain

All versions below are TOOL_REPORTED, via `environments/xilinx_2025_2_1/run_in_env.sh`.

| Tool | Real path | Version | Exit |
|---|---|---|---|
| vivado | `/mnt/data/Apps/2025.2.1/Vivado/bin/vivado` | v2025.2.1 (64-bit) | 0 |
| vitis | `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis` | v2025.2.1 (64-bit) | 0 |
| vitis_hls | project shim → `vitis-run --mode hls` | vitis-run v2025.2.1 | 0 |
| vitis-run | `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis-run` | v2025.2.1 | 0 |
| v++ | `/mnt/data/Apps/2025.2.1/Vitis/bin/v++` | v2025.2.1 | 0 |

- **Hashes:**
  - vendor `settings64.sh`: `c53e2d30…aab3bb`
  - launcher: `3d662778…f7f58e`
  - shim: `17456415…8860`
- **Launcher check:** `--check` exited 0.
- **Old-toolchain contamination:** none. `type -a` inside the launcher lists only 2025.2.1 paths and the shim. The duplicate `Vitis/bin` entries come from the vendor script. A bypass attempt with the polluted interactive PATH was refused with exit 3 (`forbidden PATH entry: /home/benyamin/.local/bin`).

## C. Python

| Item | Value | Status |
|---|---|---|
| Interpreter | `/home/benyamin/.venvs/hls_dse_py312/bin/python` (base `/usr/bin/python3.12`) | MEASURED |
| Version | 3.12.3 | TOOL_REPORTED |
| pytest | 9.1.1 | TOOL_REPORTED |
| PyYAML | 6.0.3 in the venv; 6.0.1 in the system Python | TOOL_REPORTED |
| System Python modified | no | MEASURED |

## D. Device

| Field | Value | Status |
|---|---|---|
| vendor / family | AMD-Xilinx / Zynq-7000 | contract |
| part / package | `xc7z020clg484` / `clg484` | contract; `get_parts` confirms |
| speed grade | `-1` (tool part `xc7z020clg484-1`) | **FIXED_REFERENCE_CONFIGURATION** |
| board | `NONE` | NOT_AVAILABLE |
| hardware | not available | NOT_AVAILABLE |
| device recognition | `xc7z020clg484-1 FAMILY=zynq DEVICE=xc7z020 PACKAGE=clg484 SPEED=-1` (read-only `get_parts`, 16:50:39, exit 0) | VERIFIED (TOOL_REPORTED) |

**How the speed grade was chosen:** **there is no physical board.** The `-1` grade was not obtained from board identification. It was fixed by human decision on 2026-09-25 as a research reference configuration. The basis is documented and common Zynq-7020 HLS reference usage, and `-1` is the slowest (timing-conservative) commercial grade. The grades `-2` and `-3` were not considered.

**Values that remain UNKNOWN_UNTIL_MEASURED:** DMA, ACP, cache behavior, programming time and runtime. None of them is inferred from the device or the tools.

## E. License

| Item | Value |
|---|---|
| `LM_LICENSE_FILE` / `XILINXD_LICENSE_FILE` | `<UNSET>` / `<UNSET>`, in both the shell and the launcher (the launcher allowlist is in place) |
| License file | `~/.Xilinx/trial.lic` present, 359 bytes. **Its contents were not read.** |
| **Verified scope** | **Vivado Synthesis / xc7z020 = VERIFIED** |
| Not verified | Whole Xilinx toolchain license = NOT_VERIFIED |

**Synthesis smoke evidence (TOOL_REPORTED):**

- **Source:** a Vivado 2025.2.1 session that the user ran outside HLS_DSE. It belongs to a learning project, is not research evidence, and was not run by this audit.
- **Log:** `…/Learn_Zynq/zynq_gemm_xc7z020/…/synth_1/design_1_wrapper.vds`, sha256 `9201bd6e8886d71e626a90f4346237dc3ba7b033b1d46f26c772a2d1ca150604`.
- **Relevant lines:**
  - L36: `synth_design … -part xc7z020clg484-1`
  - L39: `INFO: [Common 17-349] Got license for feature 'Synthesis' and/or device 'xc7z020'`
  - L338: `synth_design completed successfully`

**Residual risk:** this checkout was not observed inside `run_in_env.sh`, so launcher-side checkout is UNKNOWN. The launcher preserves `HOME`, so the default `~/.Xilinx` license search location is unchanged.

## F. Workspace

| Item | Value | Status |
|---|---|---|
| Path | `/mnt/data/HLS_DSE_work` (exists, empty) | MEASURED |
| Owner / mode | `benyamin:benyamin`, `drwxr-x---` (750) | MEASURED |
| Writable | yes (`test -w`) | MEASURED |
| Filesystem | `/dev/sda4` xfs: size 11,921,134,714,880 B, used 370,673,115,136 B, available 11,550,461,599,744 B, 4% used | MEASURED |
| Minimum required space | UNKNOWN (no contract defines one) | gap |
| Registration | `ENV-2025.2.1-XC7Z020-1` in `environments/ENVIRONMENT_REGISTRY.yaml` | — |
| Suitability | Suitable for generated vendor artifacts | — |

The workspace is not yet bound to the run layout. `ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT` still places runs at `runs/<STUDY_ID>/<RUN_ID>/`. P0/S00 validates the control plane and generates no vendor artifacts, so binding the workspace is deferred to a separate change before the first phase that does.

## G. Safety

The scan covered the repository and `/mnt/data/HLS_DSE_work` at 16:50:55. It found no `*.xsa`, `*.bit`, `*.bin` or `*.elf` files and no `vivado/project` directory. `runs/` holds only `_TEMPLATE`, and `evidence/measured/` is empty.

```text
No XSA generated
No bitstream generated
No ELF generated
No programming performed
No runtime experiment performed
No research campaign started
No P1 authorization
No automatic phase advance
```

## H. Governance

The following values were read from `RESEARCH_STATE.yaml`, whose sha256 is `f78cd188…90de` both before and after the audit:

```text
current_phase = P0
current_study = S00
active_phase_state = PLANNED
human_gate_required = true
p1_authorized = false
automatic_advance = false
future_phase_implementation_allowed = false
next_phase_implementation_allowed = false
active_environment = null   (not modified; setting it is a human-gate decision)
```

## Consistency checks (16:50:43)

Each of the following checks passed:

- The part is identical across the contracts, the state, both schemas and the registry.
- The speed grade `-1` is consistent across the three contracts and the registry.
- The board is `NONE` everywhere.
- Hardware is recorded as not available everywhere.
- The speed-grade status is consistent.
- No contract still contains `UNKNOWN_UNTIL_FIXED`.
- Registry IDs are unique.
- The `ENV-001` template is preserved byte-for-byte.

## Preflight

The command `run_in_env.sh python3 scripts/p0_preflight.py` ran at 16:50:09. It exited 0 with `STATUS=ENVIRONMENT_TOOLS_VISIBLE` and empty stderr. The stdout sha256 is `75d473d7…6f6252`. It differs from the earlier output only because the kernel release changed.

The script's known limitations remain unchanged:

- The vitis version field records the banner line only.
- `device_support.verified` is hard-coded to `false`.
- `license_visibility`, `disk_space` and `cpu_memory` are not implemented.

## Change record (AI_CHANGE_CONTROL)

| File | Old sha256 | New sha256 | Reason |
|---|---|---|---|
| `contracts/DEVICE_REFERENCE_CONTRACT.yaml` | `e1b7d001…98568` | `6e818c0b…6ba17` | Speed grade `-1`, board `NONE`, `hardware_available: false`, speed-grade provenance |
| `contracts/HARDWARE_PLATFORM_CONTRACT.yaml` | `9937dc82…a733` | `45171186…c950` | Speed grade/board fixed; `platform_status` records hardware, board, programming and runtime as NOT_AVAILABLE |
| `contracts/TOOLCHAIN_DEVICE_CONTRACT.yaml` | `ba1c9b8e…6f1c` | `8c8745fe…70a4` | Speed grade `-1`, board `NONE` |
| `environments/ENVIRONMENT_REGISTRY.yaml` | `e5e9d5f8…b2dd` | `f71ca296…ab86` | Registered `ENV-2025.2.1-XC7Z020-1`; template preserved |

- **Actor:** Claude Code, acting on human instruction.
- **Approval:** the human instruction of 2026-09-25.
- **Unchanged files:** `RESEARCH_STATE.yaml`, the artifact contract, the run templates and all previous audits.

## Blockers

| ID | Blocker | Status |
|---|---|---|
| B-01 | Active control consistency | RESOLVED |
| B-02 | Toolchain | RESOLVED |
| B-03 | pytest | VERIFIED |
| B-04 | License | VERIFIED (Vivado Synthesis / xc7z020 only) |
| B-05 | Workspace | VERIFIED |
| B-06 | Human P0 gate | **OPEN** |

## Items for the human gate reviewer (non-blocking)

1. Confirm that fixing the speed grade and board counts as resolving placeholders, not as a device change.
2. The license checkout was observed outside the launcher. Launcher-side checkout remains UNKNOWN until the first authorized synthesis.
3. `active_environment` in `RESEARCH_STATE.yaml` is still `null`.
4. The workspace is not yet bound to the run layout, and no contract defines a minimum workspace size.
5. The preflight script's limitations are listed above.
