# Pre-P0 Correction Audit — V23.2

**Date:** 2026-09-25 · **Base HEAD:** `6a08f53e2afa442ed63fecea8cf0bbccc1264b7b`. Its parent is `34061c88c0ea…`; the
brief quoted `34061c8c0ea6…`, which is a typo of the same commit.
**Scope:** an independent correction and re-audit of the previous repository/Related Work audit
(`PRE_P0_REPOSITORY_AND_RELATED_WORK_AUDIT_V23_2.md`, kept unchanged as a historical record). No research execution.

# A. Previous Audit Review

**Accepted after re-verification:**
- The git position was confirmed.
- The validator and tests pass.
- There is no research artifact.
- The environment, toolchain and device records are untouched.
- The storage-model conclusion was re-checked (§I).
- The PDF copyright principle (local-only in a public repository) holds.
- The SHA-256 provenance of all 55 previously placed PDFs matches.
- The first page of every canonical PDF matches its registry title (automated check: 0 mismatches).

**Found wrong or insufficient:**
1. **State label.** `RESEARCH_STATE.yaml` carried `status: READY_FOR_P0_IMPLEMENTATION`, which is outside the
   canonical phase vocabulary and readable as an authorization. The previous audit only reported it. It is fixed here (§B).
2. **Study registry.** It held 36 of 97 IDs; S10–S70 existed only in R06. S28–S31 had no definition anywhere.
   S09 had three conflicting meanings. The previous audit left all of this unresolved. It is fixed here (§C).
3. **Related Work was optimized for coverage.**
   - All 62 found papers were kept in canonical folders.
   - `core` was defined by a keyword intersection that measured dimension overlap, not centrality.
   - `other/` served as a catch-all.
   - The gap matrix counted non-canonical papers and used a count-based "overlap risk" plus unverified keyword-screen
     rows (multi-objective, early stopping, decision-centric).
   - All of this is fixed (§D–§J).
4. **Availability labels.** "Paywalled" was asserted from failed downloads. It is now checked against OpenAlex (§H).
5. **Stale S09 references in active documents.** R06 §19 (the current-role table) and the root README (§C) still
   described S09's old roles.

# B. State Machine Correction

| Field | Before | After |
|---|---|---|
| `status` | `READY_FOR_P0_IMPLEMENTATION` | `PLANNED` |
| every other field | unchanged | unchanged |

`RESEARCH_STATE.yaml` sha256 went from `f78cd188…90de` to `562136aff9b2…`. The diff is exactly one line.

**Contract support:**
- `AI_CONTROL/AI_PHASE_GATE_POLICY.md` defines the allowed states: `PLANNED → IMPLEMENTING → VALIDATING →
  GATE_REVIEW → APPROVED_FOR_NEXT_PHASE | BLOCKED`. It also says the user must explicitly approve before a phase
  enters `IMPLEMENTING`.
- `AI_CONTROL/PHASE_CONTROL.yaml` has `active_phase: P0`, `state: PLANNED`.
- `audit/gates/P0_IMPLEMENTATION_START.md` says "P0 implementation: READY after the human gate".
- `READY_FOR_P0_IMPLEMENTATION` is not a state in any contract. `PLANNED` is the canonical pre-authorization state,
  and it already equals `active_phase_state` and `PHASE_CONTROL.state`. No new state was invented.
- `GATE_REVIEW` does not apply, because P0 has not been implemented or validated.
- `BLOCKED` does not apply, because no gate has failed.

**Verified after the change:**
- `current_phase: P0` and `current_study: S00`.
- `active_phase: P0` and `active_phase_state: PLANNED`.
- `p1_authorized: false` and `p1_gate_required: true`.
- `human_gate_required: true` and `automatic_advance: false`.
- `future_phase_implementation_allowed: false` and `next_phase_implementation_allowed: false`.
- `active_environment: null`: unchanged, not authorized.

`hlsdse status` prints `status=PLANNED`. The validator passes.

# C. Study Registry Reconciliation

`contracts/STUDY_ID_REGISTRY.yaml` went from version 1.0 to 1.1 (sha256 `1674cea2bce4…` → `d6a1d875c774…`). All 36
original entries are byte-for-byte unchanged, and no ID was reused or renamed.

| Study ID Range | Count | Status | Source |
|---|---:|---|---|
| S00 | 1 | PLANNED (current_study; P0 not started) | `studies/S00/CONTRACT.yaml` (IMPLEMENTABLE), state |
| S01 | 1 | PLANNED | contract `LOCKED_UNTIL_P0_GATE` |
| S02–S08 | 7 | RESERVED | R06 §19 roles; `registry_only` contract stubs |
| S09 | 1 | ARCHIVED | contract `ARCHIVED_ID_COLLISION`; `archive/legacy_study_ids/` |
| S10–S27 | 18 | RESERVED | R06 §19 (S17 notes archived historical variants) |
| S28–S31 | 4 | MISSING_DEFINITION | stub folders only |
| S32–S70 | 39 | RESERVED | R06 §19 (S59 notes archived historical variants) |
| S71–S96 | 26 | PLANNED | named contracts (`PLANNED` / `planned`) |
| **Total** | **97** | | |

**Explanations:**
- **S28–S31** have `studies/<ID>/` stub folders but appear in none of R06 §19, R07 §27, R11, MASTER, REPORTS or
  archive. They are recorded as `MISSING_DEFINITION`, and no definition was invented.
- **S09** keeps its registry text "Historical/legacy allocation; no new execution".
  - The added `supersession` entry: old S09 → S71 for external-baseline reproduction, with its sources.
  - Its other historical meanings ("Model/Learning efficiency" in R03 and in R06 before the fix; "Multi-fidelity
    evidence" in R07 §27) have no replacement ID in canonical sources, and this is stated.
- **Historical meaning drift.** R07 §27 is an older map whose S07–S27 meanings differ from R06 §19. Following the
  R06 registry rule, R06 records the current role, and the drift is recorded in the registry. No ID was reassigned.

**Immutability and S71 checks:**
- S71 is still reserved for external-baseline reproduction, in both the registry and `RESEARCH_STATE.yaml`
  (`external_baseline_study.study_id: S71`).
- No study was renamed by the Related Work work.
- Stale references were corrected:
  - R06 §19, S09 row: "Learning efficiency | EXTENSION" became ARCHIVED, with the S71 note.
  - The root README's V22.5.1 changelog line was annotated as superseded by S71; the history text itself was kept.
- Remaining S09 mentions are correct or historical: S00's archived-S09 checks, S09's placeholder report, the
  validator, and the versioned R03 and R07 reports.

**Open item for the human:** `studies/S09/CONTRACT.yaml` has a malformed
`study_id: S09_LEGACY_EXTERNAL_BASELINE_LEGACY_EXTERNAL_BASELINE`. It is the only contract whose `study_id` differs
from its folder. It was left unedited because it is archived content.

# D. Related Work Relevance Audit

**Scope** is derived from:
- the MASTER ("core local-vs-joint evidence-selection question");
- R11 §2 (the program dimensions);
- R06 §19 (CORE studies S02–S08, S15, S16, S20, S65, S66).

**CORE** was redefined as HLS/FPGA design-space work on a contribution boundary of that question:
- (a) HLS decisions of several kernels/components chosen jointly under shared constraints, or
- (b) evidence selection across fidelities/stages for HLS DSE under an evaluation budget.

It is assigned per paper from the full-text evidence. The previous keyword rule is retired.

```text
CORE:        6
SUPPORTING: 30
ADJACENT:   17
HOLD:        6
EXCLUDE:     3
TOTAL:      62 (all RW0001–RW0062 accounted for; IDs remain immutable)
```

These counts were not targeted. They follow from the per-paper reasons in `related_work/RELATED_WORK_REGISTRY.csv`
and `related_work/EXCLUSION_REGISTER.csv`.

| Paper ID | Exact identity | Relevance | Reason (short) | Related Study | Action |
|---|---|---|---|---|---|
| RW0006 | CMMFO, Sun et al., DATE 2021 | CORE | Selects configuration and fidelity jointly with cost-penalized acquisition | S04 S05 S07 S21 S23 | kept in `core/` |
| RW0011 | Stream-HLS, Basalama et al., FPGA 2025 | CORE | Kernels scheduled jointly under a global budget; named boundary in LITERATURE_STATUS | S15 S65 S36 | moved to `core/` |
| RW0031 | Prometheus, Pouget et al., TODAES 2025 | CORE | All tasks optimized jointly in one NLP | S15 S65 S66 | moved to `core/` |
| RW0033 | FIFOAdvisor, ASP-DAC 2026 | CORE | Inter-kernel FIFO depths sized jointly | S15 S36 S65 | moved to `core/` |
| RW0037 | FADO, Du et al., FPGA 2023 | CORE | Directives of multiple kernels co-optimized under shared per-die resources | S15 S65 S78 | moved to `core/` |
| RW0050 | EtoE-DSE, Liao et al., TCAD 2024 | CORE | Component alternatives evaluated jointly at system level | S15 S65 S66 | moved to `core/` |
| RW0001 | CRYPTONITE, ASAP 2025 | SUPPORTING | Local composition of per-kernel Pareto fronts | S66 S65 | kept |
| RW0003, RW0004 | Shan et al., DAC 2019 / TCAD 2022 | SUPPORTING | Joint kernel allocation under shared resources | S95 S15 S19 | kept |
| RW0008, RW0023 | HLSFactory (MLCAD 2024); HLSyn (NeurIPS 2023 D&B) | SUPPORTING | Datasets / benchmarks | S71 S90 | kept; HLSFactory `other` → `hls_dse` |
| RW0009, RW0036 | HierQoR (DATE 2024); QoRML (FCCM 2018) | SUPPORTING | Cross-fidelity QoR models | S04 S21 S89 | kept |
| RW0010, RW0017, RW0019, RW0020, RW0030, RW0032 | CollectiveHLS, AutoDSE, GNN-DSE, AutoHLS, NLP-DSE, Sisyphus | SUPPORTING | HLS DSE methods; S71 candidates or standard baselines | S71 S72 | kept |
| RW0012, RW0013, RW0014 | MTBO (NeurIPS 2013); COMBOO (AISTATS 2025); Pretsch et al. (SMO 2025) | SUPPORTING | Methodological foundations: multi-task, constrained and cooperative-component BO | S07 S10 S14 S15 | kept |
| RW0018, RW0026, RW0021, RW0035 | Chimera, TaskTransfer, HARP, PatternDSE | SUPPORTING | Single-fidelity active learning; cross-program transfer; surrogate; pruning | S05 S10 S87 S89 S57 S88 | kept |
| RW0042 | HLPS-DSE, ICCAD 2025 | SUPPORTING | Post-route-in-the-loop DSE | S78 S61 | kept |
| RW0043, RW0044, RW0045, RW0053 | DPR survey, FOS, PLD, IdleSleep | SUPPORTING | Reconfiguration / configuration / compile cost | S85 S86 S94 | kept |
| RW0046, RW0047, RW0048 | Bonamy DPR power; Nafkha DPR measurement; HL-Pow | SUPPORTING | Configuration energy; measured power; power-aware DSE | S86 S19 | kept |
| RW0052, RW0057 | GreenFPGA; CORDOBA | SUPPORTING | FPGA lifecycle carbon; carbon-aware optimization | S20 S94 S92 | kept |
| RW0002, RW0005, RW0007, RW0022, RW0015, RW0016 | MVSym, DML, IronMan-Pro, HGBO-DSE, both VOI papers | HOLD | Abstract-only review; no legitimate open full text | S84 S85 S71 S72 S33 | registry (metadata only); VOI `other` → `bo_mobo` |
| 17 papers | see §F | ADJACENT | Not needed by any current Study question | — | moved to exclusion register |
| 3 papers | see §F | EXCLUDE | Out of scope | — | moved to exclusion register |

Row-level identity, availability, license and primary Studies for every paper are in the registry and the register.

# E. Corrected Paper List (changed papers)

- **Moved to `core/`** (relevance CORE; topical category kept as secondary): RW0011, RW0031, RW0033, RW0037, RW0050.
  RW0006 stays in `core/` under the new definition.
- **Recategorized out of `other`:**
  - RW0008 → `hls_dse`; its PDF moved and the hash was re-verified.
  - RW0015 and RW0016 → `bo_mobo` (metadata only).
- **HOLD:** RW0002, RW0005, RW0007, RW0015, RW0016, RW0022. Previously these were canonical with the unverified
  label "paywalled".
- **Registry columns added:**
  - `pdf_availability`, `storage_status`, `license_reported`, `identity_status`;
  - `relevance_class`, `relevance_reason`, `related_studies` (primary);
  - `overlap_status`, `gap_status`, `source_type`.
- **Notes:** all 42 remaining notes received a relevance header (and an identity header where corrected). 20 notes
  of ADJACENT/EXCLUDE papers were retired; they remain retrievable with `git show 6a08f53:<path>`.

# F. Incorrect / Removed Papers

| Paper | Problem | Action |
|---|---|---|
| RW0024 Balor | Redundant QoR evaluator; no Study need | ADJACENT; repo copy removed, Library original verified |
| RW0025 HLPerf | Performance characterization, not DSE; wrongly hinted as a predictor | ADJACENT; `BROWSER_ONLY` (CC-BY at ACM) |
| RW0027 Iceberg | Model-training aid | ADJACENT; repo copy removed |
| RW0028 LIFT, RW0029 LLM-DSE, RW0034 MPM-LLM4DSE | LLM-guided search is deferred (R11 §4.F/K) | ADJACENT; MPM-LLM4DSE moved to `noncanonical_pdfs/` |
| RW0038 RapidStream 2.0, RW0039 TAPA, RW0040 RapidStream IR | Tool infrastructure | ADJACENT; repo copies removed |
| RW0041 TAPA-CS | Distributed HBM FPGAs; outside the fixed device | ADJACENT; repo copy removed |
| RW0049 PowerGear, RW0058 HIPPO | Power estimators without a DSE loop | ADJACENT; repo copies removed |
| RW0054 Sustainable HW Specialization | Argument paper; no DSE method | ADJACENT; repo copy removed |
| RW0056 CATransformers | ASIC-style carbon co-design, not FPGA/HLS | ADJACENT; moved to `noncanonical_pdfs/` |
| RW0060 FPGA HLS Today | General survey | ADJACENT; repo copy removed |
| RW0061 TARO | Specific coding style; no Study question | ADJACENT; repo copy removed |
| RW0062 HLSFactory-Agent | 2-page workshop paper on benchmark extraction | ADJACENT; moved to `noncanonical_pdfs/` |
| RW0051 FOCAL | Processor carbon model; out of scope | EXCLUDE; repo copy removed |
| RW0055 Architectural Sustainability Indicator | General-architecture indicator; out of scope | EXCLUDE; repo copy removed |
| RW0059 Sustainability Gap (CACM) | Perspective article; out of scope | EXCLUDE; repo copy removed |

No paper was excluded for wrong identity: every identity issue found was corrected (§G). No source material was
destroyed:
- Library originals were re-verified by SHA-256 before each repo copy was removed.
- The three downloaded-only PDFs were moved, not deleted.

# G. Identity Corrections

| Paper | Correction |
|---|---|
| RW0014 | The registry entry "Cooperative Components Bayesian Optimization" named a **method** (CC-BO), not a paper. Registered as the paper: Pretsch, Arsenyev, Bartoli, Duddeck, "Bayesian optimization of cooperative components for multi-stage aero-structural compressor blade design", *Struct. Multidisc. Optim.* 68:84, 2025, doi 10.1007/s00158-025-03998-w. |
| RW0016 | The venue was just "1986". Actual: W. B. Rouse, *Information Processing & Management* 22(3), 1986, with the full subtitle; not IEEE SMC. |
| RW0015 | Venue: *Systems Engineering* 24(6), 2021, Shallcross et al. The companion paper sys.21595 is a different work. |
| RW0002 | MVSym: "Sym" = symbiotic. Full title added. |
| RW0011 | Venue was "2025"; actual venue FPGA 2025. |
| RW0013 | The paper's algorithm is named COMBOO; the entry is registered under the paper title. |
| RW0007 | Published title wording "Multiobjective … Graph Neural Network-Based Modeling" (TCAD 2023). |
| RW0004 | Title: "Multi-Kernel DNN-like **Application** Allocation". |
| RW0001 | Full CRYPTONITE title. |
| RW0006 | The DATE 2021 DOI is used; the same-title TODAES 2022 extension is a different paper. |
| RW0023 | "HLSyn" is the dataset name; the paper title is "Towards a Comprehensive Benchmark for High-Level Synthesis Targeted to FPGAs". |
| RW0025 | HLPerf is performance simulation, not a predictor. |
| RW0034, RW0062 | Year 2026, not 2025. |
| RW0047 | Conference paper ISWCS 2016; the local filename said 2017. |
| RW0018 | "Chimera" is shared with unrelated works; the HLS DSE tool (Yu, Huang, Chen) was selected. |
| RW0043–RW0045, RW0048, RW0050, RW0056 | Placeholder keys (DFX1–3, ENERGY1–3) replaced by paper keys: DPRSurvey, FOS, PLD, HLPow, EtoEDSE, CATransformers. |

# H. PDF Provenance

| Item | Count / status |
|---|---|
| PDFs kept locally, canonical (`papers/<category>/`) | 36 (CORE 6, SUPPORTING 30) |
| PDFs kept locally, non-canonical (`noncanonical_pdfs/ADJACENT/`) | 3 (downloaded-only copies) |
| Repo copies removed (originals retained and hash-verified in the user's library) | 16 |
| PDFs tracked by git | **0** (all 39 verified with `git check-ignore`) |
| Metadata only | 6 HOLD papers: `LEGITIMATE_OPEN_COPY_NOT_FOUND` |
| Browser only | HLPerf (register): CC-BY copy at `https://dl.acm.org/doi/pdf/10.1145/3655627`; scripted download refused; no PDF and no hash stored |
| Hashes checked | every canonical and non-canonical PDF against the registry/register; every library original before copy removal; `PDF_PROVENANCE.csv` covers all 55 PDFs ever placed, with dispositions |

- **Evidence for LEGITIMATE_OPEN_COPY_NOT_FOUND:** the agents' search of arXiv, author pages and publishers, plus
  OpenAlex reporting all six as `closed`.
- **Caveat on `license_reported`:** it comes from OpenAlex, which can miss open copies. CRYPTONITE, CMMFO and AutoHLS
  are "closed" in OpenAlex, yet legitimate arXiv or author copies were found and are held.
- **Licenses:** open licenses reported for OA versions (cc-by, cc-by-sa, cc-by-nc-sa, cc-by-nc-nd, public-domain,
  other-oa) are recorded per paper. **The local-only policy is unchanged.** Committing an openly licensed PDF remains
  a human decision.

# I. Folder Structure

- **Confirmed correct:** the layer separation between studies, experiments/runs/evidence, audit and related_work.
  Literature is kept out of `evidence/`.
- **Corrected:**
  - `related_work/papers/other/` was removed (empty).
  - `related_work/noncanonical_pdfs/` was added: gitignored, with a header comment.
  - `related_work/EXCLUSION_REGISTER.csv` was added.
- **Intentionally deferred, local-only structural directories.** Git does not track them because they are empty.
  - `evidence/{measured,derived,verified}`:
    - required by the canonical contract;
    - documented in the tracked `evidence/README.md`;
    - a `.gitkeep` in `measured/` would trigger the validator's "unexpected measured evidence" warning;
    - created by the first execution that writes evidence.
  - `hardware/xc7z020clg484/{base,registry}`: referenced by no contract, script or document. Local-only; no action.
  - `tests/p1_smoke`, `src/hlsdse/{adapters,runtime}`: P1 and future placeholders. Creating content there would be
    future-phase implementation, which is forbidden.
- **`config/examples`:** two example files with **no references** anywhere. They're retained, since deletion needs a
  human decision, and documented as orphaned examples.
- **`predictions/`:** absent, and no contract requires it. It was not created.
- **Storage model:** the previous conclusion holds, with one refinement. No contract, schema or code implements the
  proposed `storage/` (sqlite/parquet/content-addressed) tree. The implemented store is the append-only JSONL
  `EvidenceStore` (`src/hlsdse/evidence.py`), consistent with `CSV_AND_DATA_STORAGE_POLICY.md` (JSON/JSONL canonical).
  Redesign is out of scope.

# J. Gap/Overlap Matrix

`related_work/GAP_OVERLAP_MATRIX.md` was regenerated:
- **Inputs:** canonical papers only (CORE + SUPPORTING). HOLD papers appear as NOT REVIEWED; ADJACENT and EXCLUDE
  papers are not used.
- **Status vocabulary:** KNOWN PRIOR ART, PARTIAL OVERLAP, POTENTIAL OVERLAP, POTENTIAL GAP, UNRESOLVED and
  NOT REVIEWED. These replace the count-based "overlap risk".
- **Keyword rows removed:** early stopping is now stated as not verified.
- **Empty matches** say: "No directly matching work identified in the current reviewed collection. Additional
  systematic search required."

A new **prior-art boundary check** covers 14 topics. It uses PRIOR ART, PARTIAL OVERLAP, METHOD FOUNDATIONAL,
RELEVANT BUT DIFFERENT and UNRESOLVED. Key boundaries:
- **Multi-fidelity HLS DSE:** PRIOR ART (CMMFO), which optimizes per benchmark.
- **Joint multi-kernel optimization:** PARTIAL OVERLAP (Stream-HLS, Prometheus, FADO, FIFOAdvisor, EtoE-DSE), all
  within one design.
- **VOI:** UNRESOLVED (HOLD papers only).
- **Evidence reuse/caching of tool results and early stopping:** no directly matching work identified in the
  current collection.

**No novelty claim is made, and the collection is not a systematic review.**

`STUDY_LITERATURE_MAP.yaml` v2.0 covers all 97 registry IDs. It uses reviewed `direct_overlap`, mechanical
`dimension_match` and `partial_overlap`, and lists HOLD papers separately.

# K. Validation

Run on 2026-09-25 after all corrections.

| Command / check | Result |
|---|---|
| `git diff --check` (including new files) | PASS (after removing a trailing blank line in MANIFEST.md) |
| `python3 scripts/validate_project.py` | PASS: `errors=0 warnings=0` |
| `run_in_env.sh ~/.venvs/hls_dse_py312/bin/python -m pytest -q -p no:cacheprovider` | PASS: `4 passed` |
| `PYTHONPATH=src python3 -m hlsdse status` | `status=PLANNED`, `p1_authorized=False`, `human_gate_required=True` |
| YAML / JSON / CSV parse and row shape (whole repo) | PASS |
| Registry 42 + exclusion 20 = RW0001–RW0062, unique | PASS |
| Canonical PDFs exist, hash = registry, folder = category, CORE ⇔ `core/` | PASS |
| Non-canonical copies and library originals: hash = register | PASS |
| `PDF_PROVENANCE.csv` current paths and hashes | PASS |
| Duplicate PDFs; unregistered canonical PDFs | none; none |
| Notes exist for all 42; no stale notes for the 20 | PASS |
| Study map IDs = registry IDs = `study_status` IDs (97) | PASS |
| Contract `study_id` = folder | PASS except archived S09 (reported in §C) |
| Markdown path references (related_work, gate package) | PASS |
| Novelty-phrase scan | PASS: only the README prohibition list, the matrix caveat, and a quoted baseline name |
| `*.xsa`, `*.bit`, `*.bin`, `*.elf`; `runs/`; `evidence/measured/`; `__pycache__` | none; `_TEMPLATE` only; empty; none |

# L. Gate Safety

```text
P0 NOT STARTED
P1 NOT AUTHORIZED
NO AUTOMATIC ADVANCE
NO RESEARCH EXECUTION
NO PUSH
```

No Vivado, Vitis or HLS tool was run. `active_environment` remains `null`. The state change was a label correction
to the canonical `PLANNED`; no gating flag changed.

**Still requires human approval:**
1. P0 authorization.
2. `active_environment: ENV-2025.2.1-XC7Z020-1`.
3. The device-contract interpretation (speed grade `-1`, board `NONE`).
4. The malformed archived `studies/S09/CONTRACT.yaml` `study_id`.
5. Confirming or overriding the relevance decisions: in particular the 6 CORE papers, CoopBO as SUPPORTING, and
   the LLM-search papers as ADJACENT.
6. The PDF policy for openly licensed copies.
7. Pushing the local commits.

```text
STATUS: WAITING_FOR_HUMAN_GATE
```
