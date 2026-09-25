# Related Work

## 1. Why this directory exists

HLS-DSE is a gated research program. Before any Study claims a contribution, we must know what prior work already
studies, measures and optimizes. This directory holds that literature evidence and our analysis of it. It contains
**no experimental measurements**, and the collection is **curated, not a systematic review**.

## 2. Contents

| Path | Purpose |
|---|---|
| `RELATED_WORK_REGISTRY.csv` | Canonical papers (CORE, SUPPORTING) plus HOLD papers: identity, provenance, relevance, review fields |
| `EXCLUSION_REGISTER.csv` | Papers reviewed and judged ADJACENT or EXCLUDE, with reason and provenance. Prevents rediscovery churn. |
| `PDF_PROVENANCE.csv` | Every PDF ever placed: original path, current path, SHA-256, license reported, disposition |
| `MANIFEST.md` | Human-readable inventory (repository-derived counts) |
| `GAP_OVERLAP_MATRIX.md` | Dimensions vs canonical prior work, plus the prior-art boundary check |
| `STUDY_LITERATURE_MAP.yaml` | Literature ↔ Study relationships for all 97 registered Study IDs |
| `notes/RW####_<Key>.md` | Detailed reviews for CORE and SUPPORTING papers; abstract-only reviews for HOLD papers |
| `papers/<category>/` | Canonical local PDFs (not committed; see §6) |
| `noncanonical_pdfs/` | Local-only PDFs of ADJACENT papers that exist nowhere else locally (not canonical; not committed) |
| `PDF_NAMING_STANDARD.md` | Filename rules |
| `LITERATURE_GAP_MATRIX.csv`, `LITERATURE_STATUS_2026_09.md` | Earlier planning snapshots (history) |
| `S71_BASELINE_SCHEMA.csv` | Column schema for S71 external-baseline reproduction records |

## 3. Research scope used for relevance

The scope is taken from the canonical sources, not from keywords:
- `MASTER/HLS_DSE_MASTER_V23_2.md` names the core local-vs-joint evidence-selection question.
- `REPORTS/R11_RESEARCH_PROGRAM_AND_STUDY_PORTFOLIO.md` §2 lists the program dimensions.
- `REPORTS/R06_Study_Specifications.md` §19 marks the CORE studies: S02–S08, S15, S16, S20, S65, S66.
- `contracts/STUDY_ID_REGISTRY.yaml` holds the Study universe.

## 4. Relevance gate

Every candidate goes through: identity verification → scope test → relation to the research program → relation to a
Study → decision.

| Class | Meaning | Where |
|---|---|---|
| `CORE` | HLS/FPGA design-space work on a contribution boundary of the central question: (a) HLS design decisions of several kernels/components chosen jointly under shared constraints, or (b) evidence selection across fidelities/stages for HLS DSE under an evaluation budget. Assigned paper by paper from the full-text review, not by keyword. | registry; `papers/core/` |
| `SUPPORTING` | Direct methodological or empirical foundation for a named Study. Examples: S71 baseline candidates, fidelity models, datasets, and configuration-cost sources. | registry; `papers/<category>/` |
| `HOLD` | Potentially relevant, but primary-source evidence is incomplete (abstract-only). | registry (metadata only) |
| `ADJACENT` | Technically related but not needed by any current Study question | `EXCLUSION_REGISTER.csv` |
| `EXCLUDE` | Out of scope, wrong identity, or duplicate | `EXCLUSION_REGISTER.csv` |

Notes on the gate:
- A paper is never kept because it was already added, and never added to grow the collection.
- Every registry and register row carries its reason.
- An earlier rule defined `core` as a keyword intersection (adaptive acquisition AND fidelity YES). That rule is
  **retired**, because it measured dimension overlap, not centrality.

## 5. Topical categories (folders)

The topical category is secondary to relevance. CORE papers live in `papers/core/`, and their topic is recorded in
`secondary_categories`. The other canonical folders are:

| Folder | Topic |
|---|---|
| `concurrent_multikernel` | multi-kernel / multi-application allocation |
| `hls_dse` | HLS directive DSE, QoR surrogates, HLS datasets |
| `multifidelity` | cross-stage QoR estimation |
| `bo_mobo` | Bayesian / multi-objective optimization and value-of-information methods |
| `physical` | floorplan / post-route-in-the-loop DSE |
| `lifecycle_dfx` | partial reconfiguration, compile and configuration cost |
| `energy_sustainability` | power, energy and carbon |

`other/` is **not used**: an uncertain paper goes to HOLD, not to a catch-all folder.

## 6. PDFs, licensing, hashes and provenance

- **No PDF is committed.** The repository is public. `papers/.gitignore` and `noncanonical_pdfs/.gitignore` exclude `*.pdf`.
- `storage_status`:
  - `local_only (gitignored)`: a local PDF exists.
  - `metadata_only`: no PDF is held.
- `license_reported`: the license OpenAlex reports for the paper's open-access version, for example `cc-by` or
  `none (OpenAlex: closed)`. It applies to that version only. A reported open license does **not** override the
  local-only policy; committing an openly licensed PDF needs an explicit human decision.
- `pdf_availability`:
  - `PDF_AVAILABLE`
  - `BROWSER_ONLY`: a legitimate open-access copy exists, but scripted download is refused.
  - `LEGITIMATE_OPEN_COPY_NOT_FOUND`: search found none, and OpenAlex reports the paper closed.
  - `UNKNOWN`
- **Identity is the SHA-256.** Verify a copy with `sha256sum` against the registry. Duplicates collapse by hash, and
  a different version is noted rather than imported.
- **Library PDFs are copied, never moved.** When a paper leaves the canonical set, the repo copy is removed only
  after the original is re-verified by hash. Downloaded-only files move to `noncanonical_pdfs/`. Every disposition
  is recorded in `PDF_PROVENANCE.csv`.
- **Never used:** shadow libraries or suspicious mirrors.

## 7. Review notes

- **CORE and SUPPORTING:** a full review. The 16 items of `notes/PAPER_REVIEW_TEMPLATE.md` plus 12 evidence
  dimensions, each `YES` / `PARTIAL` / `NO` / `NOT_REPORTED` / `NOT_APPLICABLE` with an evidence note.
- **HOLD:** the abstract-only review, clearly marked.
- **ADJACENT and EXCLUDE:** the reason in `EXCLUSION_REGISTER.csv`. Their earlier full reviews stay in git history
  (commit `6a08f53`).

Missing information is `NOT_REPORTED`, `UNKNOWN` or `NOT_APPLICABLE`, never guessed.

## 8. Mapping to Studies

`STUDY_LITERATURE_MAP.yaml` covers every ID in `contracts/STUDY_ID_REGISTRY.yaml`. Three relationship levels are recorded:

- `direct_overlap`: the Study is a primary Study named in the paper's relevance decision (reviewed judgement).
- `dimension_match`: a review dimension linked to the Study is YES (mechanical).
- `partial_overlap`: the linked dimension is PARTIAL (mechanical).

HOLD papers are listed separately as `not_reviewed_hold`. The mechanical dimension → Study links:

| Dimension | Studies |
|---|---|
| joint evaluation | S07, S15, S65 |
| interactions | S02, S36, S37, S56 |
| staged | S32, S34, S88 |
| adaptive acquisition | S05, S20, S23, S33 |
| cost/fidelity | S04, S06, S21, S72 |
| lifecycle/configuration | S85, S86, S94 |
| physical | S59, S61, S78, S81 |
| transfer | S10, S11, S90 |
| stability | S43, S45, S92 |
| energy | S19, S20 |
| CPU–FPGA | S83, S84 |
| memory | S73 |

A mapping means the paper reports on the same dimension. **It does not mean the paper answers the Study's question.**

## 9. Overlap and gap vocabulary

- **Matrix status:** `KNOWN PRIOR ART`, `PARTIAL OVERLAP`, `POTENTIAL OVERLAP`, `POTENTIAL GAP`, `UNRESOLVED`, `NOT REVIEWED`.
- **Prior-art boundary labels:** `PRIOR ART`, `PARTIAL OVERLAP`, `METHOD FOUNDATIONAL`, `RELEVANT BUT DIFFERENT`, `UNRESOLVED`.

An empty match is written as "No directly matching work identified in the current reviewed collection. Additional
systematic search required." It is **never** written as absence of prior work.

## 10. Literature evidence vs our evidence

Everything here is `LITERATURE_REPORTED`. Our measurements go to `evidence/measured/` and derived results to
`evidence/derived/`. A paper's number never enters a measurement dataset. Cross-paper comparison requires
normalization (`AI_CONTROL/EXTERNAL_BASELINE_AND_LITERATURE_POLICY.md`). Reproduction belongs to **S71** (`REPRODUCED` evidence).

## 11. What must NOT be claimed from this directory

- Novelty, "first work", "no prior work", "state of the art", "best" or "unique". Such a claim requires a separate,
  reviewed argument backed by our own measured evidence.
- That a Study is answered, or that a gap is real, because a matrix cell is empty.
- That this collection is a systematic review.
- Any measured, reproduced or hardware result.
