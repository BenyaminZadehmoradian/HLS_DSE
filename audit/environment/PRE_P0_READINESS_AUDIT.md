# HLS-DSE V23.2 Pre-P0 Readiness Audit

**Scope:** read-only pre-P0 audit. No P0 implementation, tool installation, environment configuration, compilation, synthesis, bitstream generation, hardware programming, experiment, or research-state change was performed.

**Audit timestamp:** 2026-09-25T12:53:03+02:00
**Project root:** `/home/benyamin/Desktop/HLS_DSE`
**Reference part:** `xc7z020clg484`

## 1. Executive Summary

**Can P0 implementation start now?**

**NO**

The repository's canonical state is V23.2/P0/PLANNED and its structural validator passes, but the current P0 entry path is blocked by three concrete issues: (1) the required Vivado and Vitis commands are not visible to the preflight on `PATH`; (2) the required S00 unit-test path cannot run because `pytest` is absent; and (3) active S00 documents still require V22.8, contradicting V23.2.

The host is otherwise capable for lightweight P0 validation (native Ubuntu, 8 physical CPU cores, 93 GiB RAM). The target part is supported by the installed Vivado database and a live non-synthesis Vivado query. Physical FPGA hardware is not detected, but the current preflight explicitly classifies hardware execution as optional until P1 hardware smoke.

| Area | Status | Basis |
|---|---|---|
| Canonical project state | READY | `RESEARCH_STATE.yaml` declares V23.2, P0/PLANNED, human gate required, P1 unauthorized. |
| Structural project validation | PASS | `python3 scripts/validate_project.py`: `errors=0 warnings=0`, exit 0. |
| P0 control documents | CONFLICT | S00 requires V22.8; gate documents are V23.1; canonical state is V23.2. |
| Tool visibility | BLOCKED | `scripts/p0_preflight.py` exits 2: `MISSING_TOOLS=vivado,vitis`. |
| Target part support | READY | Vivado 2025.2.1 Tcl `get_parts xc7z020clg484*` returned three parts. |
| Hardware | HARDWARE_NOT_DETECTED | No Xilinx/AMD FPGA or JTAG device in USB/PCIe discovery; not a P0 contract blocker. |
| License | UNKNOWN | Relevant license variables are unset; usable entitlement was not demonstrated. |

## 2. Current Research State

`RESEARCH_STATE.yaml` is the canonical project-level execution state: the V23.2 master explicitly says so in its **State rule** (line 33). It identifies `MASTER/HLS_DSE_MASTER_V23_2.md` as `canonical_source`.

| State item | Status | Evidence |
|---|---|---|
| Project version | READY | `RESEARCH_STATE.yaml`: `project_version: V23.2`. |
| Current phase/study | READY | `current_phase: P0`, `current_study: S00`, `active_phase_state: PLANNED`. |
| P0 authorization state | AVAILABLE | `status: READY_FOR_P0_IMPLEMENTATION`; this is a declared state, not a completed human gate. |
| P1 | BLOCKED | `p1_authorized: false`, `next_phase_implementation_allowed: false`, `future_phase_implementation_allowed: false`. |
| Human gate | REQUIRED | `human_gate_required: true`, `automatic_advance: false`. |

The V23.2 master defines P0 as the first stage in the gated sequence and directs P1 to begin only after P0 gate review. S00 is defined by `studies/S00/CONTRACT.yaml`; its purpose is validation of the control plane before scientific experiment.

## 3. P0 Requirements Matrix

| Requirement | Source / section | Required for P0? | Current status | Evidence | Blocking? | Action required |
|---|---|---:|---|---|---:|---|
| Canonical V23.2 P0/PLANNED state | `RESEARCH_STATE.yaml`; V23.2 master State rule | Yes | READY | Declared state is internally consistent; validator passes. | No | None. |
| Correct current S00 version requirement | `studies/S00/{CONTRACT.yaml,IMPLEMENTATION.md,report.md}` | Yes | CONFLICT | Each names V22.8, not V23.2. | Yes | Human-approved correction of active S00 text/criteria. |
| Required contracts and schemas exist/parse | `scripts/validate_project.py`; contracts/schemas | Yes | READY | 30 YAML and 8 JSON audited parseable; validator exit 0. | No | None. |
| Immutable study IDs/S09 archived/S71 active | validator; `contracts/STUDY_ID_REGISTRY.yaml` | Yes | READY | Validator exit 0. | No | None. |
| No premature measured evidence | S00 required checks; validator | Yes | READY | Only `evidence/README.md`; only `runs/_TEMPLATE/manifest.yaml`. | No | None. |
| Candidate-generator and staged/provenance tests | S00 required checks; `tests/`; `scripts/p0_gate_check.sh` | Yes | BLOCKED | `pytest` absent under both existing interpreters. | Yes | Provide/select an approved Python 3 environment containing pytest, then run tests. |
| Vivado, Vitis, Vitis HLS | `configs/preflight/default.yaml` `required_tools` | Yes | BLOCKED | Preflight exit 2 because `vivado`/`vitis` are not on PATH. | Yes | Select/configure one coherent toolchain in an authorized environment step. |
| Device support | preflight `device_support`; device contracts | Yes | READY | Live Vivado query returns `xc7z020clg484-{1,2,3}`. | No | Record selected speed grade when the board/hardware identity is fixed. |
| License visibility | preflight `license_visibility`; P1 stop conditions | Yes | UNKNOWN | License variables unset; no entitlement check performed. | Yes for tool-driven P0 | Confirm entitlement safely after selecting the toolchain. |
| Disk space | preflight `disk_space` | Yes | BLOCKED | Project filesystem has 17 GiB free (97% used). No project threshold is specified. | Yes for tool outputs | Use a verified spacious workspace before HLS/Vivado artifact generation. |
| Physical FPGA | `configs/preflight/default.yaml` | No until P1 hardware smoke | HARDWARE_NOT_DETECTED | No visible Xilinx/AMD USB/PCIe/JTAG device. | No for P0 | Connect/verify only before authorized P1 hardware smoke. |
| Provenance fields and stage policy | Metric/stage/run contracts and schemas | Yes | READY | Required fields and source-status classes are explicit. | No | Preserve them in implementation. |

## 4. Environment Readiness

Measured at `2026-09-25T12:53:03+02:00` with `uname`, `lscpu`, `free`, `df`, and version commands.

| Item | Status | Measured result |
|---|---|---|
| OS / kernel / architecture | READY | Ubuntu 24.04.5 LTS; Linux 7.0.0-31-generic; x86_64. |
| Virtualization | READY | Native host (`systemd-detect-virt` previously reported `none`). |
| CPU | READY | Intel Core i7-10700; 8 physical cores, 16 logical CPUs; 0.8–4.8 GHz reported. |
| RAM / swap | READY | 93 GiB total, 60 GiB available; 8 GiB swap, 7.7 GiB free. |
| Python 3 | READY | `/usr/bin/python3`, 3.12.3; project requires `>=3.10`. |
| Plain `python` | CONFLICT | `/home/benyamin/bin/python`, Python 2.7.18, precedes Python 3. |
| pip / venv | AVAILABLE | pip 24.0 for Python 3.12; `python3 -m venv --help` succeeds. |
| Bash/Tcl/GCC/G++/Clang/Make/CMake | READY | bash 5.2.21; Tcl 8.6.14; GCC/G++ 13.3.0; Clang 18.1.3; Make 4.3; CMake 3.28.3. |
| Ninja | MISSING | Not on PATH; not declared by `pyproject.toml`. |
| Git | READY | `main...origin/main`, clean; commit `28f98fac9a93a6f5fa50453746d6c1ae15acf8d7`. |

**Correction to the earlier environment report:** its Git status was accurately `UNKNOWN` at its audit time because this directory was then not a Git repository. It is now a clean Git repository after the later authorized initial push. This is temporal drift, not a contradiction in the original observation.

## 5. Vivado Readiness

| Check | Status | Evidence |
|---|---|---|
| Installation | AVAILABLE | `/mnt/data/Apps/2025.2.1/Vivado/bin/vivado`. |
| Version | AVAILABLE | `vivado -version`: 2025.2.1 (64-bit). |
| Shell visibility | BLOCKED | `command -v vivado` returns no path; `XILINX_VIVADO` is unset. |
| Part recognition | READY | In an isolated temporary directory, `get_parts xc7z020clg484*` returned three entries: `-1`, `-2`, `-3`. No project, synthesis, or implementation was created. |
| License usability | UNKNOWN | Version and part database access do not prove a licensed implementation/HLS flow. |

## 6. Vitis Readiness

| Check | Status | Evidence |
|---|---|---|
| Installation/version | AVAILABLE | `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis`; reports Vitis 2025.2.1. |
| Shell visibility | BLOCKED | `command -v vitis` returns no path. |
| Preflight behavior | BLOCKED | `python3 scripts/p0_preflight.py` exit 2, explicitly missing `vivado,vitis`. |
| XRT/PetaLinux | NOT_REQUIRED_YET | Not shown as P0 required in project contracts; not assessed as a blocker. |

## 7. Vitis HLS Conflict Analysis

**Final classification: CONFLICT.**

| Resolution / installation | Evidence | Finding |
|---|---|---|
| `which vitis_hls` | `/home/benyamin/.local/bin/vitis_hls` | This is the selected command. It is a regular executable wrapper, not a symlink. |
| Wrapper behavior | Wrapper source | Exports `XILINX_VITIS` and `XILINX_HLS` as `/mnt/data/Apps/2025.2.1/Vitis`, prepends its `bin`, converts `-f` to `--tcl`, then `exec`s `vitis-run --mode hls`. |
| Actual launched executable | Wrapper source | `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis-run --mode hls`. `vitis-run -v` reports 2025.2.1. |
| 2023.2 standalone HLS | `/mnt/data/Xilinx/Vitis_HLS/2023.2/bin/vitis_hls` | Startup/version query reports `WARNING: XILINX_VIVADO not found` and `ERROR: cannot find Vivado parts data`; not usable in the current environment. |
| Relevant variables | `printenv`, wrapper source | `XILINX_VITIS` and `XILINX_HLS` are set to existing 2025.2.1 Vitis paths; `XILINX_VIVADO` is unset. |
| PATH ordering | `command -v`, PATH inspection | The wrapper is visible; no Vivado/Vitis/Xilinx directory is visible in the parent PATH. |

The modern 2025.2.1 installation exposes an HLS mode through `vitis-run`, so a separate legacy-named HLS binary is not proven required. However, current HLS usability is **BLOCKED**: neither the wrapper nor the 2023.2 binary establishes a matching Vivado parts environment. This makes tool identity and reproduction non-deterministic until one release and one settings procedure are selected.

## 8. Python and Pytest Readiness

| Command | Exit/result | Status |
|---|---|---|
| `/home/benyamin/bin/python --version` | Python 2.7.18 | CONFLICT |
| `/usr/bin/python3 --version` | Python 3.12.3 | READY |
| `python -m pytest --version` | `No module named pytest` | MISSING |
| `python3 -m pytest --version` | `No module named pytest` | MISSING |
| `pytest --version` | command not found | MISSING |

`pyproject.toml` declares PyYAML only and does not declare pytest, but `tests/test_staged_and_provenance.py` imports pytest and `scripts/p0_gate_check.sh` unconditionally runs `python -m pytest -q`. No project virtual environment was found; Python 3 venv capability is available but none was created. Therefore the project cannot currently run its complete test suite without an approved selection/installation of pytest. This is **BLOCKED**, not a test failure.

## 9. Storage Readiness

Measured with `df -hT`, `du -sh .`, and `du -x -h -d 1 .` at the audit timestamp.

| Location | Type / capacity / free | Status |
|---|---|---|
| Project filesystem `/` | ext4, 468 GiB total, 428 GiB used, 17 GiB free, 97% used | BLOCKED for tool-generated outputs |
| Project checkout | 8.9 MiB total (`.git` 4.6 MiB, `studies` 3.0 MiB) | READY for read-only/Python validation |
| `/mnt/data` | XFS, 11 TiB total, 346 GiB used, approximately 11 TiB free | AVAILABLE; it contains the discovered vendor tools |

**Measured conclusion:** the project directory currently has only 17 GiB available. **Estimated conclusion:** this is inadequate headroom for normal future HLS/Vivado working directories, synthesis/implementation artifacts, and bitstreams. The project defines no numeric capacity threshold, so an exact required amount is **UNKNOWN**. P0 infrastructure validation without tool outputs is feasible; any P0 action creating vendor workspaces should use a verified spacious location.

## 10. License Readiness

| Check | Status | Evidence |
|---|---|---|
| `LM_LICENSE_FILE` | UNKNOWN | Unset; value was not sought or exposed. |
| `XILINXD_LICENSE_FILE` | UNKNOWN | Unset; value was not sought or exposed. |
| Safe entitlement proof | UNKNOWN | No identified read-only license-status command was used. |

License readiness cannot be confirmed without a safe, authorized vendor entitlement check after choosing the coherent toolchain. It is not valid to infer license entitlement from `vivado -version` or a parts-list query.

## 11. Target Device Readiness

| Check | Status | Evidence |
|---|---|---|
| Canonical target | READY | `RESEARCH_STATE.yaml`, device, hardware, system, and memory contracts all fix `xc7z020clg484`. |
| Installed database | READY | 2025.2.1 `installed_devices.txt` includes `xc7z020clg484-1`; legacy ISE metadata lists CLG484 grades 1–3. |
| Live Vivado recognition | READY | Vivado 2025.2.1 query returned `xc7z020clg484-1`, `-2`, `-3`. |
| Board / speed grade selection | UNKNOWN | Contracts intentionally specify `speed_grade: UNKNOWN_UNTIL_FIXED` and `board: UNKNOWN_UNTIL_FIXED`. |
| HLS usable with target | BLOCKED | HLS paths are unresolved/misconfigured as described in section 7. |

Device support is distinct from physical-board availability.

## 12. Physical Hardware Visibility

| Check | Status | Evidence |
|---|---|---|
| USB/JTAG | HARDWARE_NOT_DETECTED | `lsusb` lists root hubs, Dell keyboard/mouse, and Edimax only. |
| PCIe | HARDWARE_NOT_DETECTED | No Xilinx/AMD/FPGA/JTAG match in `lspci`. |
| Serial JTAG nodes | HARDWARE_NOT_DETECTED | No `ttyUSB*` or `ttyACM*` candidate was found. |
| Programming executables | AVAILABLE but not selected | `hw_server`/`xsdb` exist under vendor trees but are absent from PATH. |

`configs/preflight/default.yaml` says `hardware_execution: optional_until_P1_hardware_smoke`; therefore the absent board is **not** a P0 entry blocker.

## 13. Project Testability

| Command | Duration | Exit | Status | Summary |
|---|---:|---:|---|---|
| `/usr/bin/python3 scripts/validate_project.py` | < 1 s | 0 | PASS | Exact output: `errors=0 warnings=0`. |
| `/usr/bin/python3 scripts/p0_preflight.py` | < 1 s | 2 | BLOCKED | Exact status: `MISSING_TOOLS=vivado,vitis`; `STATUS=BLOCKED_UNTIL_ENVIRONMENT_READY`. |
| `python3 -m pytest -q -p no:cacheprovider` | < 1 s | 1 | BLOCKED | Python reports `No module named pytest`; no tests collected. |
| `scripts/p0_gate_check.sh` | NOT_RUN | n/a | BLOCKED | Static inspection shows it calls plain Python 2.7 and then pytest; it cannot satisfy the intended Python 3 test path as currently resolved. |

No test failure was inferred from the missing runner.

## 14. Project Integrity

| Check | Status | Evidence |
|---|---|---|
| Canonical master/state/manifest | READY | Master, state file, and `V23_2_MANIFEST.json` exist. |
| Contracts/schemas/configuration | READY | Required tree exists; 30 YAML and 8 JSON files parsed with zero errors. |
| S00/P0/environment audit | AVAILABLE | S00 files, gates, prior environment report/snapshot, and the present audit exist. |
| Current validator | READY | Validator pass as above. |
| V23.2 manifest historical verification | AVAILABLE | Prior report recorded 585 listed files, zero missing/mismatched before later Git initialization/audit output. |

### Active-document version contradictions

| Occurrence | Classification | Contradiction / disposition |
|---|---|---|
| `studies/S00/CONTRACT.yaml` entry criterion | OBSOLETE | Requires state pointing to V22.8; conflicts with canonical V23.2. |
| `studies/S00/IMPLEMENTATION.md` entry criterion | OBSOLETE | Names V22.8 state file. |
| `studies/S00/report.md` objective/acceptance | OBSOLETE | Calls the control plane and canonical version V22.8. |
| `audit/gates/{FINAL_PREIMPLEMENTATION_CHECKLIST,P0_EXIT_CRITERIA,P0_IMPLEMENTATION_START}.md` | OBSOLETE | Labeled V23.1; checklist explicitly calls V23.1 canonical. Active P0 gate inputs must not supersede current state. |
| `README.md` V22/V22.5.1/V23.1 history | LEGITIMATE_REFERENCE but AMBIGUOUS | It is a legacy overview, not declared canonical; its title makes it unsafe as current operational authority. |
| V22/V23.1 references in V23.2 master | HISTORICAL | The master explicitly preserves/extends earlier work; no contradictory current requirement found. |

## 15. Provenance Readiness

**Status: READY.** The V23.2 master (lines 136–142), `contracts/METRIC_PROVENANCE_CONTRACT.yaml`, `contracts/STAGED_EVALUATION_CONTRACT.yaml`, `contracts/STAGE_DECISION_CONTRACT.yaml`, `contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml`, and relevant schemas define the required chain.

| Required item | Status | Source |
|---|---|---|
| `run_id`, `candidate_id`, `benchmark_id` | READY | Run schema and artifact contract. |
| tool / tool version | READY | Metric provenance contract/schema. |
| stage / command / decision | READY | Staged evaluation and stage decision contracts/schemas. |
| artifact / SHA-256 | READY | Artifact contract and metric provenance schema. |
| source field/measurement | READY | Metric provenance schema. |
| metric status | READY | Explicit MEASURED, TOOL_REPORTED, DERIVED, ESTIMATED, PREDICTED, LITERATURE_REPORTED, REPRODUCED, REFERENCE_ORACLE, UNKNOWN. |
| separation of measured/derived/estimated/predicted | READY | Metric provenance rules require artifacts/inputs/model evidence as appropriate; UNKNOWN cannot have fabricated value. |

No required provenance field listed by this audit is missing. Implementation must preserve this design; readiness does not mean evidence has been produced.

## 16. Hardware Platform Contract Readiness

**Status: READY for definition; UNKNOWN for physical realization.** `HARDWARE_PLATFORM_CONTRACT.yaml`, `SYSTEM_ARCHITECTURE_CONTRACT.yaml`, and `MEMORY_PATH_CONTRACT.yaml` define CPU-owned programming/configuration, FPGA/shared-cache path, result-return declaration requirement, unique hardware identity, per-run isolation, and programming-time measurement (`t_program_s`).

The contracts deliberately retain the following, and this audit preserves them: DMA = `UNKNOWN_UNTIL_MEASURED`; ACP = `UNKNOWN_UNTIL_MEASURED`; M_AXI = `UNKNOWN_UNTIL_MEASURED`; direct DDR = `NOT_ASSUMED`; cache/coherency/control/result-return path must be declared/measured. No hardware fact has been inferred from software tooling.

## 17. P0 Entry Gate

| P0 entry criterion | Evidence | Status | Blocking? | Required action |
|---|---|---|---:|---|
| Canonical state V23.2/P0/PLANNED | State + validator | PASS | No | None. |
| Active S00 criteria match canonical state | S00 V22.8 references | FAIL | Yes | Correct through approved project change control. |
| Required contracts/schema parse | Parser audit + validator | PASS | No | None. |
| Validator clean | `errors=0 warnings=0` | PASS | No | None. |
| Python 3 project runtime | Python 3.12.3 + PyYAML | PASS | No | Invoke Python 3 explicitly. |
| Required test path | pytest unavailable | BLOCKED | Yes | Provide/select pytest in approved Python 3 environment. |
| Required tool visibility | preflight exit 2 | BLOCKED | Yes | Configure selected Vivado/Vitis/HLS environment. |
| Target part database | live Vivado result | PASS | No | Record speed grade when fixed. |
| License visibility/usability | variables unset | UNKNOWN | Yes for tool-driven P0 | Safely confirm entitlement. |
| Sufficient future vendor workspace | root filesystem: 17 GiB free | BLOCKED | Yes for tool output | Use a verified high-capacity workspace. |
| Physical board | preflight makes optional until P1 | NOT_APPLICABLE | No | Defer to P1 smoke. |
| Human gate | state requires human approval | BLOCKED | Yes | Obtain human approval after all gate issues resolve. |

## 18. Blocking Issues

1. **Active S00 version conflict.** Evidence: three S00 files require V22.8 while canonical state is V23.2. This invalidates the current P0 acceptance criteria.
2. **Tool PATH/configuration conflict.** Evidence: P0 preflight exit 2; `vivado` and `vitis` installed but invisible; `vitis_hls` is a wrapper with no `XILINX_VIVADO`.
3. **pytest unavailable.** Evidence: no importable module or command under the existing Python 2.7 or Python 3.12 interpreters; P0 gate script requires it.
4. **License readiness unknown.** Evidence: both relevant environment variables unset; no entitlement proof.
5. **Insufficient root workspace headroom for vendor outputs.** Evidence: 17 GiB free / 97% used; no numeric project threshold, but current tool-output location is unsuitable.
6. **Human approval is still required.** Evidence: canonical state explicitly requires it.

## 19. Non-Blocking Issues

1. **No physical FPGA/JTAG detected.** This is deferred by the preflight until P1 hardware smoke.
2. **Board and speed grade are intentionally unknown.** Contracts preserve this until a board is fixed.
3. **Ninja, Podman, Conda, XRT, and PetaLinux are not visible.** No current P0 contract makes them required.
4. **Legacy document labeling.** README and historical master references are not authoritative, but README's V22 title should be clarified before it is used as onboarding guidance.
5. **Earlier environment report has stale Git status.** Its observation predates the later Git initialization and is explained in section 4.

## 20. Recommended Remediation Order

### A. MUST FIX BEFORE P0

1. **Align active S00 and P0 gate criteria to V23.2.** Evidence: section 14 contradictions. Why: P0 cannot validate against obsolete canonical-version acceptance. Action: authorized documentation/contract maintenance; **human approval required; changes project files, not environment**.
2. **Select and expose one coherent 2025.2.1 Vivado/Vitis/HLS environment.** Evidence: preflight exit 2 and HLS conflict. Why: all three are declared required by `configs/preflight/default.yaml`. Action: authorized settings/PATH environment procedure; **human approval required; changes active environment, not project logic**.
3. **Provide/select pytest for the intended Python 3 interpreter.** Evidence: section 8. Why: S00 and `p0_gate_check.sh` require tests. Action: approved dependency/environment change; **human approval required; changes environment**.
4. **Establish license readiness safely.** Evidence: section 10. Why: tool-driven P0 cannot rely on unverified entitlement. Action: safe vendor/license check after tool selection; **human approval required; may change no environment if query-only**.
5. **Choose a workspace with adequate free capacity for any generated vendor files.** Evidence: section 9. Why: root has 17 GiB free. Action: approved workspace/storage decision; **human approval required; changes execution environment/location**.

### B. SHOULD FIX BEFORE P0

1. **Make P0 scripts invoke Python 3 explicitly or ensure `python` resolves to the intended interpreter.** Evidence: plain `python` is 2.7 while script uses it. Why: reproducible execution. **Approval required; changes project script or environment.**
2. **Refresh the earlier environment report's Git section.** Evidence: it is now stale due later Git initialization. Why: audit accuracy. **Approval required; changes project audit file.**
3. **Clarify README version authority.** Evidence: README title is V22 while canonical source is V23.2. Why: reduce onboarding ambiguity. **Approval required; changes project documentation.**

### C. CAN WAIT UNTIL P1 OR LATER

1. **Connect and enumerate the FPGA/JTAG device.** Hardware is optional until P1 smoke. **Approval required; changes physical setup.**
2. **Fix board identity and speed grade.** Contracts intentionally defer these. **Approval required; changes declared hardware identity.**
3. **XRT/PetaLinux and runtime stack.** Not required by current P0 contracts. **Approval required if installed/configured; changes environment.**

## 21. Final Decision

**NO**

P0 implementation must not start until all of the following are satisfied:

1. The active S00/P0 criteria are reconciled with canonical V23.2 under change control.
2. One reproducible Vivado/Vitis/HLS toolchain is selected and made visible to the preflight, including a matching Vivado parts environment.
3. The intended Python 3 test environment can import/run pytest.
4. License entitlement is safely confirmed for the selected toolchain.
5. A high-capacity workspace is selected for any vendor-generated work.
6. The required human P0 gate is granted.

The physical board is not among these P0 conditions because the current configuration explicitly defers hardware execution to P1 hardware smoke.

## 22. Exact Evidence and Commands

| Command / source | Timestamp / result | Status |
|---|---|---|
| `sed`/`rg` review of state, V23.2 master, S00, contracts, schemas, configs, gates, scripts, tests, prior environment audit | During this audit | COMPLETE |
| `python3` YAML/JSON parse audit | 30 YAML, 8 JSON, `parse_errors=0` | PASS |
| `/usr/bin/python3 scripts/validate_project.py` | `errors=0 warnings=0`, exit 0 | PASS |
| `/usr/bin/python3 scripts/p0_preflight.py` | exit 2; `MISSING_TOOLS=vivado,vitis` | BLOCKED |
| `python{,3} -m pytest --version`; `pytest --version` | pytest missing/not found | BLOCKED |
| `df -hT . /mnt/data`; `du` | root 17 GiB free; `/mnt/data` approximately 11 TiB free | MEASURED |
| Vendor `-version` / `-v` commands | Vivado/Vitis/Vitis-run 2025.2.1; 2023.2 HLS cannot find Vivado parts | COMPLETE |
| Isolated Vivado Tcl `get_parts xc7z020clg484*` | 3 parts: speed grades 1, 2, 3 | PASS |
| `lsusb`, `lspci`, `/dev` serial query | no FPGA/JTAG candidate | HARDWARE_NOT_DETECTED |
| non-secret environment variable presence checks | `XILINX_VIVADO`, license variables unset; Vitis/HLS set | COMPLETE |
