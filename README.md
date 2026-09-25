# HLS-DSE V23.2 — AI-Controlled Research Project

Start here:
- `RESEARCH_STATE.yaml` — the machine-readable project state (phase, study, gate fields).
- `MASTER/HLS_DSE_MASTER_V23_2.md` — the canonical master: research question, phases, rules, current report list.
- `contracts/STUDY_ID_REGISTRY.yaml` — every study ID with its title and status.

## Running the checks
```
python3 scripts/validate_project.py
scripts/p0_gate_check.sh            # validator + test suite inside the 2025.2.1 launcher
PYTHONPATH=src python3 -m hlsdse status
```

## Repository layout
| Path | Contents |
|---|---|
| `AI_CONTROL/` | AI governance: control-plane and auto-push policies (YAML = enforced, MD = explanation), phase-gate policy, AI conduct, agent permissions, measurement/plot/report policies |
| `contracts/` | Research and engineering contracts (device/platform, runs and artifacts, metrics and provenance, staged evaluation, …) |
| `schemas/` | All JSON/YAML schemas (run manifest, timing, evidence, metric provenance, stage decision, pragma space/candidate) |
| `studies/` | Only studies with real content (S00, S01, S71, S72; S09 tombstone), `_TEMPLATE/`, `PLOT_REGISTRY.json` |
| `REPORTS/` | Current narrative reports (list in the master) |
| `runs/_TEMPLATE/` | The single run-workspace template; runs live in `runs/<STUDY_ID>/<RUN_ID>/` |
| `configs/`, `benchmarks/`, `baselines/`, `templates/` | Preflight config, benchmark template, baseline registry, document templates |
| `environments/` | Registered toolchain environments and the gated launcher |
| `src/hlsdse/`, `tests/`, `scripts/` | Control plane, publisher, CLI; test suite; validator and gate scripts |
| `related_work/` | Literature registry, notes and (local-only) papers |
| `audit/` | Evidence records; `audit/README.md` says which are current |
| `archive/` | Read-only history; `archive/README.md` maps every moved or merged path |

## Core rules
- No AI-generated estimate may be silently promoted to measured evidence (`AI_CONTROL/AI_CONDUCT.md`).
- Exactly one phase is implemented at a time; only a human approves a gate (`AI_CONTROL/AI_PHASE_GATE_POLICY.md`).
- Every tool execution goes through the runtime control plane (`AI_CONTROL/CONTROL_PLANE_POLICY.md`).

## Execution
Read MASTER → AI_CONTROL → active Study contract → execute → scan → register evidence → report → update state.

## Fixed device and artifact isolation
The reference target is fixed to **xc7z020clg484** (`contracts/HARDWARE_PLATFORM_CONTRACT.yaml`). All
Vivado/Vitis outputs are isolated under `runs/<STUDY_ID>/<RUN_ID>/`; completed Runs are immutable
(`contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml`). External baselines are study S71
(`AI_CONTROL/EXTERNAL_BASELINE_AND_LITERATURE_POLICY.md`).
