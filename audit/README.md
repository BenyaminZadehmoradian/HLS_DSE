# Audit records — index

Audit files are evidence. They are never edited after the fact and keep the paths that were current when they
were written (see `archive/README.md` for the old-path → new-path map). This index says which record is current.

## Current
| Area | Record |
|---|---|
| Human approval | `gates/approvals/G0-P0-S00-001.yaml` (human-authored; never auto-published) |
| Gate request / package | `gates/P0_S00_HUMAN_GATE_REQUEST_V23_2.md`, `gates/HUMAN_GATE_PACKAGE_V23_2.md` |
| P0 exit criteria | `gates/P0_EXIT_CRITERIA.md` (required by `scripts/validate_project.py`) |
| Environment readiness | `environment/FINAL_PRE_P0_READINESS_AUDIT_V23_2.md` + `FINAL_PRE_P0_READINESS_SNAPSHOT_V23_2.json` |
| Control plane (P0/S00 implementation) | `AI_CONTROL/AI_CONTROL_P0_IMPLEMENTATION_REPORT_V23_2.md`, `AI_CONTROL_INTEGRITY_MATRIX_V23_2.md`, `AI_CONTROL_RUNTIME_TRACE_V23_2.md`, `AI_CONTROL_BYPASS_AUDIT_V23_2.md`, `AI_CONTROL/evidence/` |
| Auto-publish | `git/AUTO_PUSH_IMPLEMENTATION_REPORT_V23_2.md`, `git/AUTO_PUSH_INTEGRITY_MATRIX_V23_2.md`, `git/AUTO_PUSH_LOG.jsonl` (append-only) |
| Decision log | `AI_CONTROL/CONTROL_DECISION_LOG.jsonl` (append-only; created on the first control decision) |

## Superseded (kept as history)
| Record | Superseded by |
|---|---|
| `environment/ENVIRONMENT_DISCOVERY_REPORT.md`, `environment/environment_snapshot.json` | the FINAL readiness audit |
| `environment/PRE_P0_READINESS_AUDIT.md` + snapshot (verdict NO) | PRE_P0_REMEDIATION → FINAL readiness audit |
| `environment/PRE_P0_REMEDIATION_REPORT.md` + snapshot (NOT_READY) | FINAL readiness audit |
| `environment/PRE_P0_TOOLCHAIN_PREPARATION_REPORT.md` + snapshot | FINAL readiness audit (still cited as the source of the part/speed-grade visibility evidence) |
| `environment/evidence/vitis_hls.log` | tool log cited by the toolchain preparation report (formerly at the repository root) |
| `gates/PRE_P0_REPOSITORY_AND_RELATED_WORK_AUDIT_V23_2.md` | `gates/PRE_P0_CORRECTION_AUDIT_V23_2.md` |
| `gates/FINAL_PREIMPLEMENTATION_CHECKLIST.md`, `gates/P0_IMPLEMENTATION_START.md` | the approval G0-P0-S00-001 and the P0/S00 implementation report |
| `AI_CONTROL/AI_CONTROL_FINAL_AUDIT_V23_2.md` | pre-implementation audit (HEAD `91f14bb`); its companion files were later replaced by the post-implementation versions listed above |
| `V22_8_PREIMPLEMENTATION_AUDIT.md` | FINAL readiness audit |
