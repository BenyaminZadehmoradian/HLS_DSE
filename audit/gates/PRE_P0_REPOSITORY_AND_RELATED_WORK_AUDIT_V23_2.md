# Pre-P0 Repository and Related Work Audit — V23.2

**Date:** 2026-09-25 · **Scope:** repository structure audit and Related Work completion only. This is not P0 or S00 execution.
**Base HEAD:** `34061c88c0ea6278ecefedef1d54fcff2b891d6d`

# 1. Execution Status

```text
Repository audit: PASS
Folder structure: PASS (no moves required; findings documented in §3)
Related Work audit: PASS
PDF organization: PASS (55 of 62 papers have a canonical local PDF; 7 have none, see §5)
Registry: PASS
Provenance: PASS
Validation: PASS
P0 started: NO
P1 authorized: NO
```

# 2. Repository State

| Item | Value |
|---|---|
| Branch | `main` |
| HEAD at start | `34061c8` (3 local-only commits: `ada921f`, `0f65dba`, `34061c8`) |
| origin/main | `db53266` (HEAD 3 ahead, 0 behind; nothing pushed) |
| Worktree at start | clean |
| `RESEARCH_STATE.yaml` | sha256 `f78cd188…90de`, unchanged at start and end |
| State values | `current_phase: P0`, `current_study: S00`, `active_phase_state: PLANNED`, `p1_authorized: false`, `human_gate_required: true`, `automatic_advance: false`, `future_phase_implementation_allowed: false`, `next_phase_implementation_allowed: false`, `active_environment: null` |
| Gate state | Waiting for the human gate (`audit/gates/HUMAN_GATE_PACKAGE_V23_2.md`) |

**Discrepancy (reported, not changed):** the operation brief expected `status: WAITING_FOR_HUMAN_GATE`. The actual
field is `status: READY_FOR_P0_IMPLEMENTATION`. `WAITING_FOR_HUMAN_GATE` has so far been the conclusion of the
audit reports, not a value in the state file. Every gating flag above is in its blocked position. This operation made
no state-machine change. Whether the `status` string should be updated is left to the human gate.

# 3. Folder Audit

Tracked file counts come from `git ls-files`. 596 files were tracked at start.

| Path | Expected role | Actual role | Status | Action |
|---|---|---|---|---|
| `MASTER/` | Canonical master + prior versions | V23.2 canonical (named in state) plus V22–V23.1 history | OK | none |
| `REPORTS/` | R01–R14 program reports | Same. R05 still carries V22.8 metadata (flagged as historical in an earlier audit). | OK | none |
| `AI_CONTROL/` | Governance policies, phase control | 30 policy/control files | OK | none |
| `constraints/` | Project/experiment constraints | 7 YAML files | OK | none |
| `contracts/` | Research contracts | 26 contracts | OK | none |
| `environments/` | Tool/environment definitions | Registry plus 2025.2.1 launcher | OK | none |
| `agents/` | Agent role definitions | 6 `AGENT.md` files | OK | none |
| `skills/`, `plugins/` | Not required by any contract | Absent. Policies live in `AI_CONTROL/AI_SKILL_POLICY.yaml` and `AI_PLUGIN_POLICY.yaml`. | OK | not created |
| `studies/` | Study definitions and documentation | S00–S96: 97 folders, each with `CONTRACT.yaml` and `report.md`; 72 have plot scaffolding. No results. | OK | none; see finding F1 |
| `benchmarks/` | Benchmark definitions | Template only | OK (pre-P0) | none |
| `datasets/` | Not required by any contract | Absent | OK | not created |
| `experiments/` | Execution schemas | 6 schema/template files; no runs | OK | none |
| `runs/` | Isolated run workspaces | `_TEMPLATE/manifest.yaml` only | OK | none |
| `evidence/{measured,derived,verified}` | Evidence layers | `README.md` tracked; the three subfolders exist locally and are empty | OK (empty) | none; see finding F2 |
| `predictions/` | Not required by any contract | Absent | OK | not created |
| `related_work/` | Literature artifacts and analysis | 16 metadata-only rows before this audit | **Incomplete → completed** | §5 |
| `reports_generated/` | Generated reports index | Index plus timing template | OK | none |
| `audit/` | Audit, gate, environment and provenance records | `environment/`, `gates/`, one historical V22.8 audit at the top level. No research results. | OK | none |
| `archive/` | Read-only history | V21 master; legacy S09 contract | OK | none |
| `src/`, `scripts/`, `tests/` | Code, scripts, tests | `hlsdse` package; preflight/validator/gate scripts; 2 test files. `src/hlsdse/{adapters,runtime}` and `tests/p1_smoke` are empty local folders. | OK | none |
| `configs/` and `config/` | Configuration | `configs/preflight` (referenced by the validator); `config/examples` (2 example files, **no references**) | Minor | see finding F3 |
| `schemas/`, `pragma_space/`, `baselines/`, `templates/`, `hardware/` | Schemas, run templates, baseline registry, device folder | As expected. `hardware/xc7z020clg484/{base,registry}` are empty local folders. | OK | none |
| `storage/` (sqlite/parquet model) | Proposed storage model | Absent; **no contract or schema references it** | Deferred | not created (finding F4) |
| Repository root | Project files | State, README, pyproject, V22–V23.2 manifests, CSV policy. Also a tracked `vitis_hls.log` (legacy tool log) and an untracked, self-ignored `.pytest_cache`, both pre-existing. | OK | none (finding F5) |

**Separation of layers:** no mixing was found.
- `studies/` holds only definitions and plot scaffolding.
- `experiments/`, `runs/` and `evidence/` hold only schemas, templates and README files.
- `audit/` holds only audit, gate and environment records.
- `related_work/` holds only literature. Every registry row is `LITERATURE_REPORTED`.
- `predictions/` does not exist.
- No raw tool output sits in `evidence/`.

**Findings. None requires a structural move.**

- **F1: Study registry coverage.** `contracts/STUDY_ID_REGISTRY.yaml` reserves 36 IDs (S00–S09, S71–S96), while
  S10–S70 are indexed in `REPORTS/R06_Study_Specifications.md`, and all 97 study folders exist. Two further
  inconsistencies:
  - R06 names S09 "Learning efficiency", while the registry marks S09 historical/legacy.
  - The root `README.md` still describes S09 as the external-baseline study. S71 now fills that role.

  Study IDs are governance-controlled, so nothing was edited. **Needs a human decision.**
- **F2: Empty directories.** Git does not track empty directories, so a fresh clone lacks them.
  - Affected: `evidence/{measured,derived,verified}`, `hardware/xc7z020clg484/*`, `tests/p1_smoke` and
    `src/hlsdse/{adapters,runtime}`.
  - Adding `.gitkeep` to `evidence/measured` would trigger the validator warning "Unexpected measured evidence
    before P0".
  - Deferred until the first run creates them. Not a P0 blocker, because S00 creates no evidence.
- **F3: Unreferenced examples.** `config/examples` duplicates the role of `configs/`. Moving it would be cosmetic,
  so it was not moved. Proposal: merge it into `configs/examples/` in a later cleanup.
- **F4: Storage model deferred.** The `storage/` sqlite/parquet model is not referenced by any contract, schema or
  script. Creating empty execution folders now would add structure without contract backing. It should be
  introduced, together with a contract, by the phase that first writes evaluation data (see S26 Provenance/storage).
- **F5: Legacy tool log at the root.** `vitis_hls.log` is a legacy 2023.2-era tool log at the repository root.
  Earlier environment audits cite it at this path, so it was left in place.

# 4. Structural Corrections

No file was moved or renamed in the repository. Edits made in place:

| Path | Change | Content changed | Hash before → after (sha256 prefix) |
|---|---|---|---|
| `related_work/RELATED_WORK_REGISTRY.csv` | Rebuilt with the full column set; 16 → 62 rows; RW0001–RW0016 IDs preserved | yes | `619c1e47c332` → `7d7f1fab0d14` |
| `related_work/README.md` | Rewritten for new researchers; stale S09 reference → S71 | yes | `9d44d93e0957` → `c9a7c6859c8a` |
| `related_work/PDF_NAMING_STANDARD.md` | Clarifications appended; format unchanged | yes | `e973fa75aa20` → `c68f064b6743` |
| `related_work/notes/PAPER_REVIEW_TEMPLATE.md` | Extended to the 16 review items; original headings kept | yes | `3b283bc20d77` → `85d2332cc138` |
| `related_work/LITERATURE_GAP_MATRIX.csv` | G01 action `S09 reproduction study` → `S71 reproduction study` | yes (1 cell) | `3a29123b6bcc` → `41444fd48978` |

New files:
- `related_work/PDF_PROVENANCE.csv` (`f902bd21402b`)
- `related_work/MANIFEST.md` (`3d489872e590`)
- `related_work/GAP_OVERLAP_MATRIX.md` (`07a7cd7fa37a`)
- `related_work/STUDY_LITERATURE_MAP.yaml` (`a712c2a9663c`)
- `related_work/papers/README.md` (`66ec8cb5f26e`)
- `related_work/papers/.gitignore` (`483240bded49`)
- 62 review notes `related_work/notes/RW####_<Key>.md`
- this report

PDF placement: every canonical PDF was **copied**, not moved, into `related_work/papers/<category>/`.
- Library originals stay at their original paths.
- All 55 rows in `PDF_PROVENANCE.csv` have `same_content: true`: original and final SHA-256 are identical.

# 5. Related Work Summary

Counts are repository-derived from the registry.

| Item | Count |
|---|---|
| Registered papers | 62 (16 pre-existing IDs + 46 new) |
| Canonical local PDFs | 55: 34 copied from the local library, 21 downloaded open access |
| Metadata only (paywalled) | 6: MVSym, DML, IronMan-Pro, HGBO-DSE, both VOI papers |
| Open access, PDF not stored | 1: HLPerf (publisher returned HTTP 403; read online) |
| Reviewed full text / abstract only | 56 / 6 |
| Metadata complete (authors, venue, URL, DOI) | 57; 5 have no DOI (NeurIPS/PMLR proceedings, arXiv-only, or unconfirmed) |

Papers per category:

| Category | Papers |
|---|---|
| core | 1 |
| concurrent_multikernel | 4 |
| hls_dse | 22 |
| multifidelity | 3 |
| bo_mobo | 2 |
| physical | 6 |
| lifecycle_dfx | 4 |
| energy_sustainability | 14 |
| other | 6 |

**Sources.**
- Local papers came from `~/Desktop/Library`, `~/Desktop/Sustainable_Design_Explorer/Papers`,
  `~/Desktop/pragma_mach/reference/papers` and `~/Desktop/AutoDSE/docs/paper`.
- Downloads came from arXiv, NeurIPS/PMLR proceedings, author or institutional repositories, and CC-licensed
  publisher copies. One of these, CollectiveHLS (CC-BY), came via a Wayback Machine capture of the ACM PDF. No
  shadow libraries were used.
- About 1,200 local PDFs were screened. Excluded as out of scope: textbooks, course slides, datasheets,
  device-aging physics, and what appear to be the researcher's own drafts or submissions.

**Identity corrections found during review.** These are recorded in the registry notes.
- "Cooperative Components BO" is the method name inside Pretsch et al., *SMO* 2025 (a compressor-blade paper).
- "On the Value of Information in System Design" is Rouse, *Information Processing & Management* 1986.
- MVSym stands for *symbiotic*, not symbolic.
- The Stream-HLS venue is FPGA 2025.
- The hint names HLSyn, AutoHLS and HLSFactory-Agent were matched to specific papers. Two dates were later than the
  hints said: MPM-LLM4DSE is DATE 2026, and HLSFactory-Agent is 2026.
- The three DFX papers and three energy papers were chosen by the search agents; each choice is justified in
  its registry `notes`.

**Duplicate handling.**
- HLSyn: the Library copy and the download were byte-identical, so one canonical copy was kept and both origins
  were recorded.
- AutoDSE: a 2020 preprint of a different version is noted but not imported.

**PDFs are not committed.** The GitHub repository is public (its page returns HTTP 200 anonymously). Committing
publisher PDFs would redistribute copyrighted papers, so `related_work/papers/.gitignore` excludes `*.pdf`. The
registry keeps SHA-256, source URL and original path for every PDF, so each copy can be re-acquired and verified.
**Human decision:** keep this policy, or commit only the open-licensed PDFs.

**Category rule.** `core` = HLS/FPGA-targeted **and** both adaptive evidence acquisition **and** cost/fidelity
modeling marked YES. Only CMMFO (RW0006) qualifies. This is a mechanical rule, not a judgment of importance.

# 6. Prior-Art Findings

All findings are `LITERATURE_REPORTED`. Full tables are in `related_work/GAP_OVERLAP_MATRIX.md`. **No novelty claim is made.**

**Known overlap** (dimensions reported YES by several reviewed papers):
- HLS DSE.
- Multi-objective DSE.
- Multi-fidelity / cross-stage QoR prediction: CMMFO, HierQoR, QoRML, HIPPO and others.
- Cost-aware evaluation.
- Physical implementation in the loop: FADO, TAPA, RapidStream, HLPS-DSE and others.
- Multi-benchmark transfer: GNN-DSE, HARP, TaskTransfer, HLSyn and others.
- Lifecycle, configuration and DFX cost: PLD, FOS, the DPR survey, the DPR power papers and others.
- Energy/power.

**Partial overlap:**
- Joint (vs local) evaluation: MultiFPGAAlloc, EnergyOptAlloc, Stream-HLS, FADO, FIFOAdvisor, TAPA-CS,
  HLPS-DSE and others. These evaluate multiple kernels or components jointly for allocation, floorplanning or
  dataflow sizing, not for choosing which evidence to acquire.
- Staged evaluation and early stopping: CMMFO, AutoHLS, NLP-DSE, PatternDSE, PLD and HL-Pow.
- Adaptive evidence acquisition: CMMFO, Chimera, TaskTransfer, LLM-DSE, HLPS-DSE and MTBO.

**Potential overlap (unresolved because reviewed from abstract only):** MVSym, DML, IronMan-Pro, HGBO-DSE, and both
value-of-information papers.

**Potential gaps.** These require experimental validation and are not established:
- Decision/Pareto **stability**: YES only for CORDOBA (carbon domain).
- **Decision-centric** acquisition, i.e. value of information: only in the systems-engineering VOI papers; the HLS
  match (AutoHLS) is a keyword hit.
- CPU–FPGA interaction: YES only for MVSym (abstract), FOS and IdleSleep.
- Studies with no mapped literature: S91 (cross-device), S93 (invocation distribution), S95 (fragmentation/packing)
  and S96 (sustained/thermal).

**Unresolved questions:**
- The reviewed set is **not a systematic review**. A LOW- or MEDIUM-risk dimension may reflect search coverage
  rather than absence of work.
- The multi-objective and early-stopping rows use keyword screens and need manual confirmation.
- Paywalled works need full-text review before their overlap can be classified.

# 7. Study Mapping

`related_work/STUDY_LITERATURE_MAP.yaml` covers all 97 studies. Each entry carries `study_id`, `paper_ids`,
`relationship`, `direct_overlap`, `partial_overlap` and `missing_evidence`. Mappings are mechanical, using the
dimension → Study table in `related_work/README.md`.

| Group | Count |
|---|---|
| Studies with direct literature | 35 |
| Partial only (S71 as a baseline candidate; S87, S89 by keyword screen) | 3 |
| Not mapped by current dimensions | 59 |

Examples:

| Study | Direct / partial papers | Note |
|---|---|---|
| S73 Memory/data movement | 9 / 32 | |
| S83/S84 CPU–FPGA | 3 / 14 | |
| S85/S86 Configuration / bitstream cost | 13 / 8 | |
| S88 Early stopping / staged evaluation | 9 / 25 | |
| S90 Workload generalization | 12 / 18 | |
| S92 Objective sensitivity | 1 / 17 | |
| S94 Lifecycle-robust DSE | 13 / 8 | |
| S87 Evidence reuse | 0 / 6 | keyword screen |
| S89 Constraint vs QoR prediction | 0 / 19 | keyword screen |
| S91, S93, S95, S96 | 0 / 0 | unresolved |

Every entry records that no `OUR_MEASURED` evidence exists yet.

# 8. Validation

Run on 2026-09-25, 17:3x–17:42 +02:00.

| Command / check | Result |
|---|---|
| `git diff --check` (including new files) | PASS (exit 0, after removing a trailing blank line in `MANIFEST.md`) |
| `python3 scripts/validate_project.py` | PASS (`errors=0 warnings=0`) |
| `run_in_env.sh ~/.venvs/hls_dse_py312/bin/python -m pytest -q -p no:cacheprovider` | PASS (`4 passed in 0.02s`) |
| YAML / JSON / CSV parse and row-shape check (whole repo) | PASS (no errors, no ragged CSV) |
| Registry: 62 unique IDs, RW0001–RW0016 preserved | PASS |
| Every registered PDF exists, hash matches, folder = category, note exists | PASS |
| PDFs on disk = registered PDFs (55); duplicate hashes | PASS (none) |
| Provenance: `same_content` true for all rows; library originals still present | PASS |
| Internal path references in `related_work/*.md` | PASS (none broken) |
| Study map: 97 studies; all paper IDs exist in registry | PASS |
| PDFs ignored by git (`git check-ignore`) | PASS |
| Novelty-phrase scan | PASS (only the README's list of forbidden claims and verbatim author quotes marked `LITERATURE_REPORTED`) |
| Research-state hash | PASS (unchanged, `f78cd188…90de`) |
| `*.xsa`, `*.bit`, `*.bin`, `*.elf`; `runs/`; `evidence/measured/`; `__pycache__` | PASS (none; `_TEMPLATE` only; empty; none) |

# 9. State-Machine Safety

```text
P0 was NOT started.
S00 was NOT executed.
P1 was NOT authorized.
No automatic phase advancement occurred.
No research results were generated.
```

No Vivado, Vitis or HLS tool was invoked in this operation. `RESEARCH_STATE.yaml`, `AI_CONTROL/PHASE_CONTROL.yaml`,
contracts, the environment registry and study definitions were not modified. Nothing was pushed.

# 10. Human Gate Status

```text
STATUS: WAITING_FOR_HUMAN_GATE
```

Still requires human approval:

1. The device-contract interpretation (speed grade `-1`, board `NONE` as placeholder resolution), from `HUMAN_GATE_PACKAGE_V23_2.md`.
2. `active_environment: ENV-2025.2.1-XC7Z020-1` (currently `null`).
3. Explicit P0 authorization.
4. The `status` field wording in `RESEARCH_STATE.yaml` (`READY_FOR_P0_IMPLEMENTATION`, §2).
5. Study-registry coverage (F1): S10–S70 appear only in R06, the S09 naming conflicts, and the root README still
   refers to S09 as the external-baseline study.
6. The PDF policy for the public repository (PDFs local-only vs committing open-licensed copies).
7. Whether to push the local commits to `origin/main`.
