# HLS-DSE V23.2 Environment Discovery Report

**Audit scope:** discovery only. No project architecture, contracts, study state, tool configuration, software packages, FPGA configuration, synthesis, HLS run, or benchmark was changed.

**Audit date:** 2026-09-25  
**Project root:** `/home/benyamin/Desktop/HLS_DSE`  
**Reference device:** `xc7z020clg484`

## Executive readiness

| Area | Classification | Evidence / conclusion |
|---|---|---|
| Environment | PARTIAL | Strong host CPU/RAM and native host OS; only 17 GiB free on the project filesystem. |
| Toolchain | PARTIAL | Vivado/Vitis 2025.2.1 are installed and executable by absolute path, but are absent from `PATH`; HLS installations conflict and the 2023.2 HLS executable cannot locate Vivado parts data. |
| Project | READY | Validator: `errors=0 warnings=0`; V23.2 manifest: 585 files, 0 missing, 0 mismatched. Unit tests were not executable because `pytest` is absent. |
| Hardware | HARDWARE_NOT_DETECTED | USB and PCIe discovery found no Xilinx/AMD FPGA/JTAG device. |
| License | UNKNOWN | License environment variables are unset; no license credential was read or exposed. |
| P0 | BLOCKED | Resolve usable, consistent tool environment; establish license status; and provide adequate workspace headroom before tool-driven P0 work. |
| P1 | NOT_AUTHORIZED | `RESEARCH_STATE.yaml` explicitly sets `p1_authorized: false`; human gate remains required. |

## A. Host OS, CPU, memory, and storage

| Item | Classification | Observed value |
|---|---|---|
| OS | READY | Ubuntu 24.04.5 LTS (Noble), x86_64 |
| Kernel | AVAILABLE | Linux 7.0.0-31-generic |
| Host | AVAILABLE | `ea06c189`, Dell Precision 3440 |
| Virtualization | READY | `systemd-detect-virt`: none (native host detected) |
| CPU | READY | Intel Core i7-10700 @ 2.90 GHz; 8 physical cores / 16 logical CPUs; 0.8–4.8 GHz reported |
| Memory | READY | 93 GiB total; 60 GiB available at audit time; 8 GiB swap (7.7 GiB free) |
| Project filesystem | BLOCKED | `/` is ext4, 468 GiB total, 428 GiB used, 17 GiB available (97% used) |
| Secondary storage | AVAILABLE | `/mnt/data` is an XFS volume on a 10.8 TiB partition; free-space value was not captured in this report |
| Vivado/Vitis workload space | BLOCKED | 17 GiB on the project filesystem is not adequate headroom for normal synthesis/implementation artifacts. Move future generated workspaces to a verified spacious filesystem or free space. |

## E/F. Python and build environment

| Tool | Classification | Version / path |
|---|---|---|
| `python3` | READY | Python 3.12.3, `/usr/bin/python3` |
| `pip3` | AVAILABLE | pip 24.0, `/usr/bin/pip3` |
| `venv` | AVAILABLE | `python3 -m venv --help` succeeded |
| `python` | CONFLICT | `/home/benyamin/bin/python` is Python 2.7.18, ahead of Python 3 on `PATH`; unsuitable for this project (`>=3.10`). |
| Project dependency | AVAILABLE | PyYAML 6.0.1 is installed for Python 3.12; `pyproject.toml` declares only `PyYAML>=6.0`. |
| Test dependency | MISSING | `pytest` is unavailable for both discovered `python` and `python3`; cache-disabled test execution could not start. |
| gcc / g++ | AVAILABLE | GCC/G++ 13.3.0, `/usr/bin/gcc`, `/usr/bin/g++` |
| clang | AVAILABLE | clang 18.1.3, `/usr/bin/clang` |
| make / cmake | AVAILABLE | GNU Make 4.3; CMake 3.28.3 |
| ninja | MISSING | Not on `PATH`; not declared by this project. |
| Tcl | AVAILABLE | Tcl 8.6.14 (`/usr/bin/tclsh`) |
| bash / Git | AVAILABLE | bash 5.2.21; Git 2.43.0 |
| Java | AVAILABLE | OpenJDK 21.0.12 |
| Docker | AVAILABLE | Docker 29.1.3; daemon replied with server version 29.1.3 |
| Podman / Conda | MISSING | Not on `PATH`; not required yet. |

The Python dependency ecosystem is compatible with a later Python 3.12 environment. No environment was created and no packages were installed.

## G–J. AMD/Xilinx tools and installation conflicts

| Tool / installation | Classification | Version, path, and usability |
|---|---|---|
| Vivado | AVAILABLE | 2025.2.1 (64-bit), `/mnt/data/Apps/2025.2.1/Vivado/bin/vivado`; version query succeeded. Not on `PATH`; `XILINX_VIVADO` is unset. |
| Vitis | AVAILABLE | 2025.2.1 (64-bit), `/mnt/data/Apps/2025.2.1/Vitis/bin/vitis`; executable by absolute path, not on `PATH`. |
| Vitis HLS (modern wrapper) | CONFLICT | `/home/benyamin/.local/bin/vitis_hls` exports `XILINX_VITIS` and `XILINX_HLS` to `/mnt/data/Apps/2025.2.1/Vitis`, then invokes `vitis-run --mode hls`. It is on `PATH`, whereas its matching Vivado is not. |
| Vitis HLS | CONFLICT | 2023.2 at `/mnt/data/Xilinx/Vitis_HLS/2023.2/bin/vitis_hls`; executable, but its harmless startup/version query reported `XILINX_VIVADO not found` and `cannot find Vivado parts data`. |
| SDK tools | AVAILABLE | 2019.1: `/tools/Xilinx/SDK/2019.1/bin/{xsct,xsdb,bootgen,hw_server}`. Bootgen identified itself as 2019.1. |
| Legacy ISE | AVAILABLE | `/opt/Xilinx/14.7/ISE_DS`; legacy installation, not a substitute for Vivado. It contains Zynq `xc7z020` package metadata. |
| `xsim`, `xelab`, `xvlog`, `xvhdl` | MISSING | Not on `PATH`; their availability under the 2025 Vivado tree was not verified in this discovery pass. |
| `hw_server`, `xsdb` | AVAILABLE | Present under `/mnt/data/Apps/2025.2.1/{Vivado,Vitis}/bin` and `/tools/Xilinx/SDK/2019.1/bin`, but absent from `PATH`. |
| XRT / PetaLinux | NOT_REQUIRED_YET | `xbutil`, `xbmgmt`, `xrt-smi`, and `petalinux-config` are absent from `PATH`. They are not assumed required for P0. |

Multiple major generations are installed (ISE 14.7, SDK 2019.1, Vitis HLS 2023.2, and Vivado/Vitis 2025.2.1). This is a **CONFLICT**, not evidence that any particular version is configured for this project. The 2025.2.1 tools should be selected coherently in a future authorized configuration step; no environment settings were changed during this audit.

## H/R/S. Target-device and environment-variable readiness

| Check | Classification | Evidence |
|---|---|---|
| `xc7z020clg484` installed-device evidence | AVAILABLE | 2025.2.1 `installed_devices.txt` includes `xc7z020clg484-1` (line 18604). Legacy ISE 14.7 customer parts list includes `xc7z020-clg484-{1,2,3}`. |
| Vivado recognition by live Tcl query | UNKNOWN | Not executed because the audit avoided initializing Vivado beyond its harmless version query. Database evidence supports device availability but does not prove a configured run can use it. |
| Device family / package | AVAILABLE | Zynq-7000 `xc7z020`, CLG484 package is present in discovered parts metadata. |
| `PATH` precedence | CONFLICT | `vitis_hls` resolves to a user wrapper, while matching Vivado/Vitis 2025.2.1 directories are not in `PATH`; plain `python` resolves to Python 2.7 before Python 3. |
| `XILINX_VIVADO` | MISSING | Unset. |
| `XILINX_VITIS`, `XILINX_HLS` | CONFLICT | Set to an existing 2025.2.1 Vitis directory via the wrapper environment; no matching `XILINX_VIVADO` is set. |
| `XILINX_XRT` | NOT_REQUIRED_YET | Unset. |
| `LM_LICENSE_FILE`, `XILINXD_LICENSE_FILE` | UNKNOWN | Both unset. Values/credentials were never printed or inspected. |

## K–M. Hardware, programming infrastructure, and license

| Check | Classification | Evidence |
|---|---|---|
| USB FPGA/JTAG visibility | HARDWARE_NOT_DETECTED | `lsusb` showed only Linux root hubs, Dell keyboard/mouse, and an Edimax device; no Xilinx/AMD cable/device. |
| PCIe FPGA visibility | HARDWARE_NOT_DETECTED | No Xilinx/AMD/FPGA/JTAG match in `lspci`. |
| JTAG serial nodes | HARDWARE_NOT_DETECTED | No matching `/dev/ttyUSB*`, `/dev/ttyACM*`, Xilinx, or JTAG node was found. |
| Programming executables | AVAILABLE | 2025.2.1 `hw_server` and `xsdb` exist, plus 2019.1 SDK equivalents. They were not started and no target connection was attempted. |
| Cable drivers / permissions | UNKNOWN | The 2025.2.1 tree contains cable-driver data, but with no cable visible, runtime driver operation and user permissions cannot be established. |
| License | UNKNOWN | No safe read-only license-status interface was identified; environment variables are unset. A successful `vivado -version` proves installation access only, not feature licensing. |

No hardware detection is a software failure. It prevents hardware-ready/P1 measurement work only.

## O–Q. Git and project integrity

| Check | Classification | Result |
|---|---|---|
| Git repository state | UNKNOWN | `git status`, branch, and commit queries report `fatal: not a git repository`. No `.git` worktree was available to the executed Git commands, so branch/commit/dirty/untracked status cannot be reported. |
| Required canonical trees | READY | `MASTER`, `contracts`, `schemas`, `studies`, `scripts`, `configs`, `benchmarks`, `baselines`, `audit`, `REPORTS`, and `src` all exist. |
| V23.2 declared state | READY | `RESEARCH_STATE.yaml`: V23.2, P0/PLANNED, `READY_FOR_P0_IMPLEMENTATION`, reference part `xc7z020clg484`, P1 disabled, human gate required. |
| Existing validator | READY | `python3 scripts/validate_project.py` returned exactly `errors=0 warnings=0` (exit 0). |
| Manifest checksum validation | READY | V23_2 manifest: 585 listed files; 0 missing; 0 content/size mismatches. |
| Existing tests | BLOCKED | Not run: `pytest` module is missing for both available Python interpreters. The command was invoked cache-disabled and failed before test collection. |

## Required actions (not performed)

### Installation / environment actions

1. Make a single compatible Vivado/Vitis/Vitis HLS release the selected toolchain, preferably the coherent 2025.2.1 installation after confirming project compatibility.
2. In an authorized future shell/setup action, source the selected vendor settings script or otherwise provide a consistent `XILINX_VIVADO`, Vitis/HLS, and `PATH` environment. Do not mix it with the standalone 2023.2 HLS tree.
3. Confirm the Vivado license entitlement through an authorized, non-secret vendor license check.
4. Free or relocate the future generated workspace to storage with adequate headroom; do not place Vivado implementation artifacts on the current 17 GiB root filesystem.
5. Provide `pytest` in the intended Python 3.12 environment if test execution is required. Do not use the Python 2.7 `python` executable for this project.
6. Connect the target board/JTAG cable and verify user permissions when hardware work is authorized.

### Implementation actions

1. None performed or authorized by this audit.
2. After the human P0 gate and the environment corrections above, run the project’s normal preflight in the selected Python 3 environment.
3. Before any P1/hardware study, perform a configured Vivado target-part query and a read-only `hw_server`/`xsdb` target enumeration.

## Critical blockers

1. **Toolchain configuration conflict:** multiple generations are present; 2025.2.1 Vivado/Vitis is not on `PATH`, and the 2023.2 HLS installation cannot find Vivado parts data.
2. **License readiness unknown:** license variables are unset and usable entitlement has not been demonstrated.
3. **Workspace capacity:** only 17 GiB is free on the project filesystem.
4. **Hardware absent:** no FPGA/JTAG device is detectable (not a software defect, but blocks hardware measurements).
5. **Test runner unavailable:** `pytest` is absent for the installed Python 3 interpreter.
6. **Git metadata inaccessible:** repository branch, commit, and dirty state are unavailable from this working directory.

