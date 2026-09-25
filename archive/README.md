# Archive — read-only history

Nothing here is current truth. The canonical sources are `RESEARCH_STATE.yaml`, `MASTER/HLS_DSE_MASTER_V23_2.md`,
`contracts/` and `AI_CONTROL/`.

| Folder | Contents |
|---|---|
| `masters/` | Superseded masters V22, V22.8, V23, V23.1 (fully contained in, or merged into, V23.2) |
| `manifests/` | Release file-hash manifests V22 … V23.2. They describe their release only; `V23_0_MANIFEST.json` repeats V22.9's file list, and V23.2's hashes predate the P0 commits. Git history is the integrity record. |
| `release_notes/` | Per-version handoff/completion notes (R10, R13, R14, README_V22_8) |
| `reports_retired/` | Retired report stubs R01, R02, R04, R08 |
| `V19/` | The V19 research master, split verbatim out of `REPORTS/R07_Research_Extensions.md` |
| `V21/` | Placeholder only — the original V21 master is not retained (sha256 `59030c08…` recorded in `manifests/V22_MANIFEST.json`) |
| `legacy_study_ids/` | The full V22.6 S09 contract (S09 is archived; its role moved to S71) |

## Path migration (repository cleanup)
Audit records keep the paths that were current when they were written. Old path → current location:

| Old path | Now |
|---|---|
| `V2*_MANIFEST.json` (root) | `archive/manifests/` |
| `vitis_hls.log` (root) | `audit/environment/evidence/vitis_hls.log` |
| `README_V22_8_IMPLEMENTATION_READY.md` | `archive/release_notes/` |
| `CSV_AND_DATA_STORAGE_POLICY.md` | `AI_CONTROL/CSV_AND_DATA_STORAGE_POLICY.md` |
| `MASTER/HLS_DSE_MASTER_V22*.md`, `V23.md`, `V23_1.md` | `archive/masters/` |
| `REPORTS/R01, R02, R04, R08` | `archive/reports_retired/` |
| `REPORTS/R10, R13, R14` | `archive/release_notes/` |
| V19 block of `REPORTS/R07_Research_Extensions.md` | `archive/V19/HLS_DSE_V19_RESEARCH_MASTER.md` |
| `contracts/DEVICE_REFERENCE_CONTRACT.yaml`, `TOOLCHAIN_DEVICE_CONTRACT.yaml` | merged into `contracts/HARDWARE_PLATFORM_CONTRACT.yaml` |
| `contracts/MEMORY_PATH_CONTRACT.yaml` | merged into `contracts/SYSTEM_ARCHITECTURE_CONTRACT.yaml` |
| `contracts/FAILURE_TAXONOMY.yaml` | merged into `contracts/FAILURE_AND_RETRY_CONTRACT.yaml` (aliases keep the old class names) |
| `constraints/*.yaml` | removed; the few unique rules are in `AI_CONTROL/AI_EXECUTION_POLICY.yaml` |
| `config/examples/` | removed (duplicated `benchmarks/templates/` and `configs/`) |
| `configs/preflight/staged_evaluation.yaml` | removed (duplicated `contracts/STAGED_EVALUATION_CONTRACT.yaml`, with a looser rule) |
| `agents/*/AGENT.md`, `AI_CONTROL/AI_AGENT_POLICY.yaml`, `AI_PERMISSION_MATRIX.csv`, `AI_TOOL_POLICY.yaml`, `AI_SKILL_POLICY.yaml`, `AI_PLUGIN_POLICY.yaml` | `AI_CONTROL/AGENT_PERMISSIONS.yaml` |
| `AI_CONTROL/AI_SYSTEM_CONTRACT, AI_RESEARCH_RULES, AI_NO_GUESSING_POLICY, AI_EVIDENCE_POLICY, AI_IMPLEMENTATION_POLICY, AI_ESCALATION_RULES, AI_STOP_CONDITIONS, AI_CHANGE_CONTROL, AI_EXECUTION_CHECKLIST` (.md) | `AI_CONTROL/AI_CONDUCT.md` |
| `AI_CONTROL/AI_DATA_ISOLATION_POLICY.md` | `AI_CONTROL/AI_ARTIFACT_ISOLATION_POLICY.md` (rules 9-10) |
| `AI_CONTROL/AI_SCOPE_POLICY.yaml`, `AI_REPORTING_POLICY.md`, `PHASE_GATE_REPORT_TEMPLATE.md` | `AI_CONTROL/AI_PHASE_GATE_POLICY.md` + `AI_REPORT_TEMPLATE_POLICY.md` |
| `AI_CONTROL/EXTERNAL_BASELINE_COMPARISON_POLICY.md`, `LITERATURE_NORMALIZATION_POLICY.md` | `AI_CONTROL/EXTERNAL_BASELINE_AND_LITERATURE_POLICY.md` |
| `experiments/*_SCHEMA.json`, `pragma_space/schemas/PRAGMA_SPACE_SCHEMA.yaml` | `schemas/` |
| `schemas/STUDY_RUN_SCHEMA.json` | merged into `schemas/RUN_MANIFEST_SCHEMA.json` |
| `experiments/RUN_TIMING_SCHEMA.json` (an example, not a schema) | `schemas/RUN_TIMING_SCHEMA.json` (a real JSON Schema) |
| `experiments/PLOT_REGISTRY.json` | `studies/PLOT_REGISTRY.json` (rebuilt against the study registry) |
| `experiments/PLOT_CONTRACT_TEMPLATE.yaml`, `reports_generated/TIMING_ACCOUNTING_TEMPLATE.md` | `templates/` |
| `reports_generated/REPORT_INDEX.yaml` | `REPORTS/REPORT_INDEX.yaml` |
| `templates/run_workspace/` | `runs/_TEMPLATE/` (single run template) |
| `studies/S02-S08, S10-S70, S73-S96` (template stubs) | removed; IDs and titles in `contracts/STUDY_ID_REGISTRY.yaml`, template in `studies/_TEMPLATE/` |
| `studies/*/plots/` skeletons, `studies/S72/plots/code/*.py` placeholders | removed; plot IDs stay in `studies/S72/plots/manifests/` |
| `studies/S09/comparison/`, `studies/S09/inputs/` | `studies/S71/` |
| `studies/S00/IMPLEMENTATION.md`, `studies/S01/IMPLEMENTATION.md` | merged into the study `report.md` |
| `src/hlsdse/metrics.py, legality.py, evidence.py, plotting/` | removed (unused stubs; the real components are P1 work) |
