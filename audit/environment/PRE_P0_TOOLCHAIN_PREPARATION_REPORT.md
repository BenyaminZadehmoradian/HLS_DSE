# Pre-P0 Toolchain Preparation Report

**Project:** HLS-DSE V23.2 · **Reference commit:** `d9fe19661205a3863fcdfa8d8c66628e23bf887a`
**Verification timestamp:** 2026-09-25T13:23:22+02:00
**Scope:** project-scoped 2025.2.1 toolchain selection and identity checks only. P0 was not started. P1 is not authorized. `RESEARCH_STATE.yaml` was not modified.

## 1. Objective

Define one reproducible, project-scoped way to select the AMD-Xilinx 2025.2.1 Vivado/Vitis/Vitis HLS toolchain, verify that the tools are coherent, and record the result as auditable evidence. This addresses blocker B-02 from `PRE_P0_REMEDIATION_REPORT.md`.

## 2. Current Environment Problem

The software is installed. What was missing was a coherent, reproducible way to select it:

- The interactive shell puts `/mnt/data/Apps/2025.2.1/Vitis/bin` on PATH and sets `XILINX_VITIS`/`XILINX_HLS`, but it does not set `XILINX_VIVADO` and does not put Vivado on PATH.
- The same shell also carries ISE 14.7 (`XILINX=/opt/Xilinx/14.7/ISE_DS/ISE`, `/opt/Xilinx/14.7/.../bin/lin64` on PATH), pyenv shims, and a Jupyter virtual environment that shadows `python3`.
- `vitis_hls` resolves to the user wrapper `~/.local/bin/vitis_hls`. That wrapper passes `-version` unchanged to `vitis-run`, which rejects it (`ERROR: [vitis-run 60-1520] unrecognised option '-version'`, rc=2).
- The tracked `vitis_hls.log` in the repository root (`WARNING: XILINX_VIVADO not found`) records the failure mode that follows from this.

## 3. Discovered Xilinx Installations

| Location | Release | Role in this environment |
|---|---|---|
| `/mnt/data/Apps/2025.2.1` (Vivado, Vitis, PDM, Model_Composer) | 2025.2.1 (`data/version.sh`: `XILINX_VERSION_DEFAULT=2025.2.1`) | **Selected** |
| `/mnt/data/Xilinx/Vitis_HLS/2023.2` | 2023.2 | Excluded; the launcher refuses PATH entries matching it |
| `/tools/Xilinx/SDK/2019.1` | 2019.1 | Excluded; the launcher refuses PATH entries matching it |
| `/opt/Xilinx/14.7/ISE_DS/ISE` | ISE 14.7 | Excluded; not inherited because of `env -i` |
| `/home/benyamin/.local/bin/vitis_hls` | Wrapper that runs 2025.2.1 `vitis-run --mode hls` | Not used; unchanged |

`/mnt/data/Xilinx/Vivado` and `/tools/Xilinx/Vivado` exist but are empty. Release 2025.2.1 ships **no standalone `vitis_hls` executable**. In this release, HLS runs through `vitis-run --mode hls`.

## 4. 2025.2.1 Environment Initialization

The vendor initialization script is `settings64.sh`. The copies at `Vivado/settings64.sh` and `Vitis/settings64.sh` are byte-identical (sha256 `c53e2d30…aab3bb`). The script sources, in order, the PDM, Vitis Embedded Development, Vivado, Model_Composer, DocNav and Vitis-for-HLS fragments.

The result was measured by diffing `env` before and after sourcing it, starting from `env -i` with only a system PATH:

| Variable | Value after init |
|---|---|
| `XILINX_VIVADO` | `/mnt/data/Apps/2025.2.1/Vivado` |
| `XILINX_VITIS` | `/mnt/data/Apps/2025.2.1/Vitis` |
| `XILINX_HLS` | `/mnt/data/Apps/2025.2.1/Vitis` |
| PATH prepends | `Vitis/bin`, `/mnt/data/Apps/DocNav`, `Model_Composer/bin`, `Vivado/bin`, `Vitis/bin` (again), `Vitis/gnu/riscv/.../lin32/bin`, `.../lin64/bin`, `PDM/bin` |

No other variables are set. After init, Vivado and Vitis come from the same release tree. `vitis_hls` is still **not found**, because the release does not provide it.

## 5. Project-Scoped Environment Design

**Existing infrastructure reused:** the `environments/` directory, which holds `ENVIRONMENT_REGISTRY.yaml`; the PATH-based scanner `src/hlsdse/scanning/environment.py`; and `scripts/p0_preflight.py`. The project had no setup script, launcher or toolchain selector, so nothing was duplicated.

**Mechanism:** a controlled launcher, `environments/xilinx_2025_2_1/run_in_env.sh <command…>`. It:

1. re-executes itself under `env -i`, keeping only `HOME USER LOGNAME LANG TERM` and a system PATH. This makes the environment independent of the caller's shell.
2. checks the vendor `settings64.sh` against its pinned sha256 and checks that `data/version.sh` declares 2025.2.1.
3. sources the vendor `Vivado/settings64.sh`.
4. prepends `environments/xilinx_2025_2_1/bin`, which contains only a `vitis_hls` shim.
5. refuses to run (exit 3) if any of the following holds:
   - a `XILINX_*` variable points outside `/mnt/data/Apps/2025.2.1`;
   - PATH contains a 2023.2, `Vitis_HLS`, `/tools/Xilinx`, `/opt/Xilinx`, `~/.local/bin`, pyenv or `.venvs` entry;
   - `vivado`, `vitis`, `vitis_hls`, `vitis-run` or `v++` resolves (real path) outside the release tree or the shim.
6. sets `PYTHONDONTWRITEBYTECODE=1` so that no `__pycache__` is written into the repository.

**The `vitis_hls` shim** runs `$XILINX_VITIS/bin/vitis-run --mode hls`. It maps `-f` to `--tcl` (as the existing user wrapper does) and `-version`/`-v` to `--version`. It refuses to run outside the launcher.

**What the design does not do:** it does not modify `~/.bashrc`, `~/.profile` or `/etc/environment`, and it does not modify the Xilinx installation or delete anything. It does not pass license variables through; see §10.

**Command-line checks:** `environments/xilinx_2025_2_1/run_in_env.sh --check` prints the resolved identity.

## 6. Toolchain Coherence Verification

Every command was run through the launcher. Real paths were resolved with `readlink -f`.

| Tool | `command -v` → real path | Version command | Measured version | rc |
|---|---|---|---|---|
| vivado | `/mnt/data/Apps/2025.2.1/Vivado/bin/vivado` | `vivado -version` | `vivado v2025.2.1 (64-bit)`, SW Build 6403652 | 0 |
| vitis | `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis` | `vitis -version` | `Vitis v2025.2.1 (64-bit)`, SW Build 6397637 | 0 (a stderr note says DISPLAY is not set; this is harmless) |
| vitis_hls | `…/HLS_DSE/environments/xilinx_2025_2_1/bin/vitis_hls` (shim) → `vitis-run --mode hls` | `vitis_hls -version` | `vitis-run v2025.2.1 (64-bit)`, SW Build 6397637 | 0 |
| vitis-run | `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis-run` | `vitis-run --version` | `vitis-run v2025.2.1 (64-bit)`, SW Build 6397637 | 0 |
| v++ | `/mnt/data/Apps/2025.2.1/Vitis/bin/v++` | `v++ --version` | `v++ v2025.2.1 (64-bit)`, SW Build 6397637 | 0 |

All five tools resolve to 2025.2.1, so there is **no release conflict** in the selected environment. Negative tests:

- running the shim directly returns `HLSDSE_ENV_ERROR … outside run_in_env.sh` (rc=3);
- forcing the launcher to skip `env -i` while inheriting the polluted PATH returns `forbidden PATH entry: /home/benyamin/.local/bin` (rc=3).

## 7. Target Device Verification

Vivado was started in batch mode through the launcher with `-nolog -nojournal`, from a scratch directory outside the repository. It ran a read-only Tcl script that uses `get_parts` and `get_property`. No project was created and no design was loaded.

```
PARTS_MATCHED=3
PART=xc7z020clg484-1 FAMILY=zynq DEVICE=xc7z020 PACKAGE=clg484 SPEED=-1
PART=xc7z020clg484-2 FAMILY=zynq DEVICE=xc7z020 PACKAGE=clg484 SPEED=-2
PART=xc7z020clg484-3 FAMILY=zynq DEVICE=xc7z020 PACKAGE=clg484 SPEED=-3
```

The 2025.2.1 device database recognizes `xc7z020clg484` (rc=0). The project speed grade is still `UNKNOWN_UNTIL_FIXED` in `DEVICE_REFERENCE_CONTRACT.yaml`, and three grades are available. Fixing the speed grade is a separate human decision and was not made here.

## 8. P0 Preflight Result

Command, run from the project root: `environments/xilinx_2025_2_1/run_in_env.sh python3 scripts/p0_preflight.py`. The script was not modified.

| Item | Result |
|---|---|
| Exit code | **0** |
| Status line | `STATUS=ENVIRONMENT_TOOLS_VISIBLE` |
| stderr | empty |
| stdout sha256 | `90d914e4a64543b8c6f3c6233f0b74289f4a4e2d2d04832d7614df8f8057440a` |
| Python | `/usr/bin/python3` 3.12.3 |
| vivado | present, `/mnt/data/Apps/2025.2.1/Vivado/bin/vivado`, `vivado v2025.2.1 (64-bit)` |
| vitis | present, `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis`, recorded as `****** Vitis Development Environment` |
| vitis_hls | present, project shim, `****** vitis-run v2025.2.1 (64-bit)` |
| git | present, `/usr/bin/git`, 2.43.0 |
| device_support | `xc7z020clg484`, `verified: false` |

Limits of the scanner, recorded but not fixed because the scanner may not be modified:

- For vitis, the scanner stores the first banner line of the output, not the line that contains the version.
- `device_support.verified` is hard-coded to `false`. The device was verified separately in §7.
- `configs/preflight/default.yaml` lists `license_visibility`, `disk_space` and `cpu_memory`, but the script does not implement these checks.

The tracked `vitis_hls.log` and `RESEARCH_STATE.yaml` had the same sha256 before and after the preflight run. `validate_project.py` inside the launcher reported `errors=0 warnings=0`. Preflight did not fail on licensing, because it does not check licensing.

## 9. Python / Pytest Status

The launcher's `python3` is `/usr/bin/python3` (3.12.3, system prefix, the canonical interpreter from the prior audit). The pyenv and Jupyter-venv interpreters are excluded by design.

| Check | Result |
|---|---|
| pytest | **MISSING** (`No module named pytest`) |
| PyYAML (project dependency) | 6.0.1 |
| pip | 24.0 (system) |
| venv / ensurepip | importable |
| PEP 668 | `/usr/lib/python3.12/EXTERNALLY-MANAGED` is present, so a plain `pip install` into the system interpreter is blocked |
| Project venv | absent |

The environment can receive pytest later, but it needs a human choice. One option is the OS package (`python3-pytest`, needs sudo). The other is a project virtual environment; the launcher would then have to select that interpreter explicitly. Nothing was installed. The future verification command is `environments/xilinx_2025_2_1/run_in_env.sh python3 -m pytest -q -p no:cacheprovider`.

## 10. License Status

**HUMAN_ACTION_REQUIRED.**

| Evidence | Result |
|---|---|
| `XILINXD_LICENSE_FILE`, `LM_LICENSE_FILE` | UNSET in the interactive shell. The launcher also does not pass them through. |
| `~/.Xilinx/*.lic` | 1 file present. Only its presence was checked; the contents were **not read**. |
| `xlicdiag` (2025.2.1 `Vitis/bin`) | Fails: `lmutil not found`. `lmutil` exists at `Vivado/bin/unwrapped/lnx64.o/lmutil` but is not on the vendor PATH. |
| Vivado Tcl `info commands *licen*` | No matches |

No safe, non-secret entitlement query was found that could run without human involvement. Tool diagnostics such as `xlicdiag` with `lmutil` on PATH, or the `vlm` license manager GUI, show host IDs and license details. Whoever runs them must review the output before sharing it. A successful `-version` or `get_parts` call is **not** evidence of entitlement. The Vivado banner line `Tool Version Limit: 2025.11` is also not interpreted as evidence of entitlement.

## 11. Workspace Status

| Location | FS | Available | Writable top level | Status |
|---|---|---|---|---|
| Project root `/` | ext4 | 17,421,660,160 B (97% used) | yes | Not adequate for vendor-generated output |
| `/mnt/data` | xfs | 11,550,461,599,744 B | **no** (`root:root 755`); user-owned subdirectories exist (`Apps`, `hls_clean`, `pragma_mach`) | Candidate only |

`ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml` fixes the run workspace at `runs/<STUDY_ID>/<RUN_ID>/`, relative to the project. No contract defines a generated-workspace root, so none was activated.

**Proposal only:** a human creates a dedicated, user-owned directory, for example `/mnt/data/HLS_DSE_work/`. A contract amendment then does one of two things:

- (a) allows `runs/` to be a recorded symlink into that root, or
- (b) adds an explicit `generated_workspace_root` field. Each Run's `manifest.yaml` would record the physical path and filesystem.

Either option is a change request under `AI_CHANGE_CONTROL.md`. The launcher already works from any cwd, and the repository itself would not change.

## 12. Environment Identity

Every value below is MEASURED except `environment_id`, which is UNKNOWN. The machine-readable copy is in `PRE_P0_TOOLCHAIN_PREPARATION_SNAPSHOT.json`.

| Field | Value | Class |
|---|---|---|
| environment_id | not assigned (registry holds template `ENV-001` only) | UNKNOWN |
| toolchain_family | AMD-Xilinx 2025.2.1 | MEASURED |
| vivado_version / path | v2025.2.1 SW 6403652 / `/mnt/data/Apps/2025.2.1/Vivado/bin/vivado` | MEASURED |
| vitis_version / path | v2025.2.1 SW 6397637 / `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis` | MEASURED |
| vitis_hls_version / path | vitis-run v2025.2.1 SW 6397637 (HLS mode) / project shim → `vitis-run --mode hls` | MEASURED |
| vitis_run_version / path | v2025.2.1 SW 6397637 / `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis-run` | MEASURED |
| vpp_version / path | v2025.2.1 SW 6397637 / `/mnt/data/Apps/2025.2.1/Vitis/bin/v++` | MEASURED |
| python_executable / version | `/usr/bin/python3` → `python3.12` / 3.12.3 | MEASURED |
| target_device | `xc7z020clg484` (-1/-2/-3 visible) | MEASURED |
| environment_initialization_method | `environments/xilinx_2025_2_1/run_in_env.sh` | MEASURED |
| workspace_candidate | `/mnt/data` (not approved) | MEASURED |
| verification_timestamp | 2026-09-25T13:23:22+02:00 | MEASURED |

## 13. Files Created or Modified

No existing file was modified.

| Path | Purpose | Old hash | New sha256 | Why required | Verification |
|---|---|---|---|---|---|
| `environments/xilinx_2025_2_1/run_in_env.sh` | Project-scoped, guarded 2025.2.1 launcher | none (new) | `55a7c55deb2e42e330ad478ec348de1e8001970f4b5bc3a67512e0f06772d423` | No reproducible selection mechanism existed. The vendor init leaves 2023.2/ISE/pyenv leakage possible from the caller's shell. | `environments/xilinx_2025_2_1/run_in_env.sh --check` |
| `environments/xilinx_2025_2_1/bin/vitis_hls` | `vitis_hls` shim that runs `vitis-run --mode hls` | none (new) | `17456415db532ac3b8724480c320ea5e16a4e5b19a28ef4af1cf821193b48860` | 2025.2.1 has no `vitis_hls`. Preflight requires one. The user wrapper fails on `-version` and lives outside the project. | `environments/xilinx_2025_2_1/run_in_env.sh vitis_hls -version` |
| `audit/environment/PRE_P0_TOOLCHAIN_PREPARATION_REPORT.md` | This report | none (new) | recorded in git | Required deliverable | — |
| `audit/environment/PRE_P0_TOOLCHAIN_PREPARATION_SNAPSHOT.json` | Machine-readable identity | none (new) | recorded in git | Required deliverable | `python3 -m json.tool` |

## 14. Remaining Human Actions

1. Approve (or reject) `environments/xilinx_2025_2_1/run_in_env.sh` as the canonical toolchain entry point, and decide whether to register an environment ID in `environments/ENVIRONMENT_REGISTRY.yaml`.
2. Provide pytest for the selected interpreter: either the OS package or a project venv that the launcher selects explicitly.
3. Verify license entitlement, and decide whether the launcher should pass through a specific license variable. The launcher currently passes none.
4. Create and approve a generated-workspace root on `/mnt/data`, together with the matching contract amendment (§11).
5. Fix the device speed grade when appropriate. It is still `UNKNOWN_UNTIL_FIXED`.
6. Grant the P0 human gate only after a new pre-P0 re-audit.

## 15. Remaining Blockers

| ID | Blocker | Status |
|---|---|---|
| B-02 | Coherent toolchain selection | Resolved by this procedure, pending human approval and re-audit |
| B-03 | pytest missing for `/usr/bin/python3` | OPEN |
| B-04 | License entitlement unverified | OPEN, HUMAN_ACTION_REQUIRED |
| B-05 | Generated-workspace root not approved | OPEN (proposal only) |
| B-06 | Human P0 gate | OPEN |

## 16. Final Status

**READY_FOR_PYTEST_AND_LICENSE_REVIEW**

Final safety check:

- P0 was not started, and P1 remains unauthorized.
- `RESEARCH_STATE.yaml` is unchanged (sha256 checked before and after).
- No benchmark, HLS synthesis, Vivado synthesis or implementation was run.
- No XSA or bitstream was generated, and no FPGA was programmed.
- No license contents or credentials were read or exposed.
- No Xilinx installation, global shell file or user wrapper was modified.
- No file was deleted and no cleanup was performed.
