# Related Work

## 1. Why this directory exists

HLS-DSE is a gated research program. Before any Study claims a contribution, we must know what prior work already
studies, measures and optimizes. This directory holds that literature evidence and our analysis of it: papers,
metadata, reviews, an overlap matrix and a map from papers to Studies. It contains **no experimental measurements**.

## 2. Contents

| Path | Purpose |
|---|---|
| `RELATED_WORK_REGISTRY.csv` | One row per paper: identity, PDF provenance, review fields, study relations, overlap/gap labels |
| `PDF_PROVENANCE.csv` | Where each canonical PDF came from, with SHA-256 before and after placement |
| `MANIFEST.md` | Human-readable inventory (repository-derived counts, per-category totals) |
| `GAP_OVERLAP_MATRIX.md` | Research dimensions vs prior work, plus the named prior-art check |
| `STUDY_LITERATURE_MAP.yaml` | Literature ↔ Study relationships for S00–S96 |
| `notes/RW####_<Key>.md` | Structured review per paper (from `notes/PAPER_REVIEW_TEMPLATE.md`) |
| `papers/<category>/` | Canonical local PDFs (not committed; see §5) |
| `PDF_NAMING_STANDARD.md` | Filename rules |
| `LITERATURE_GAP_MATRIX.csv`, `LITERATURE_STATUS_2026_09.md` | Earlier planning snapshots (kept for history) |
| `S71_BASELINE_SCHEMA.csv` | Column schema for S71 external-baseline reproduction records |

## 3. Categories

Each paper has exactly one primary `category` (its folder) and optional `secondary_categories` in the registry.
A PDF is never copied into a second folder.

| Category | Meaning |
|---|---|
| `core` | HLS/FPGA-targeted work whose review marks **both** adaptive evidence acquisition and cost/fidelity modeling as YES. This is the closest prior art to the evidence-selection question (S05/S07). It is assigned by that rule, not by judgment. |
| `concurrent_multikernel` | Multi-kernel / multi-application allocation or joint optimization |
| `hls_dse` | HLS pragma/directive DSE, QoR models used for DSE, HLS datasets |
| `multifidelity` | Multi-fidelity or cross-stage QoR estimation |
| `bo_mobo` | Bayesian / multi-objective optimization methods (not HLS-specific) |
| `physical` | Floorplanning, high-level physical synthesis, post-route-in-the-loop work |
| `lifecycle_dfx` | Partial reconfiguration (DFX), compile/configuration cost, FPGA runtime systems |
| `energy_sustainability` | Power/energy models, carbon and sustainability of computing and FPGAs |
| `other` | Surveys, infrastructure, decision theory and other supporting work |

## 4. Paper IDs and filenames

Every paper has an immutable ID `RW####`. RW0001–RW0016 keep the IDs of the original registry; new papers get the
next free ID. Filenames follow `PDF_NAMING_STANDARD.md`: `RW####_<FirstAuthor><Year>_<Key>_<Venue>[_suffix].pdf`.

## 5. PDFs, hashes and provenance

- **PDFs are not committed.** This repository is public, and most PDFs are publisher or author copies that we may
  not redistribute. `papers/.gitignore` excludes `*.pdf`. Each researcher keeps local copies in `papers/<category>/`.
- **Identity is the SHA-256.** The registry records `sha256`, `pdf_source_url` or `original_path`, `pdf_version`
  and `metadata_source`. To verify a copy, run `sha256sum related_work/papers/<category>/<file>` and compare it with the registry.
- **Acquisition status** (`pdf_status`) is one of:
  - `LOCAL_EXISTING`: copied from a library already on the machine. The original is left in place.
  - `DOWNLOADED_OPEN_ACCESS`: downloaded from arXiv, proceedings, an author or institutional page, or a CC-licensed
    publisher copy.
  - `METADATA_ONLY_PAYWALLED`: no legitimate open copy was found.
  - `NOT_FOUND`: open access, but the download was blocked. The paper was read online.

  Shadow libraries are never used.
- **Never overwrite a PDF with different content.** A duplicate is resolved by hash. Byte-identical copies collapse
  to one canonical file, and every origin is recorded. A different version (for example, preprint vs journal) is
  noted in the registry and is not imported as a second copy of the same paper.

## 6. How reviews are performed

Each review follows `notes/PAPER_REVIEW_TEMPLATE.md`:
- 16 fixed items: research question, setting, search space, evaluation, benchmarks, hardware, toolchain, metrics,
  baselines, findings, limitations, what is not evaluated, relation to Studies, overlap, gap and reproducibility.
- 12 evidence dimensions, each marked `YES` / `PARTIAL` / `NO` / `NOT_REPORTED` / `NOT_APPLICABLE` with a short
  evidence note.
- A `review_status`: `REVIEWED_FULL_TEXT` or `REVIEWED_ABSTRACT_ONLY`.

Missing information is written as `NOT_REPORTED`, `UNKNOWN` or `NOT_APPLICABLE`. It is never guessed.

## 7. How Related Work maps to Studies

The mapping is mechanical. A paper relates to a Study when a review dimension linked to that Study is YES (direct)
or PARTIAL (partial):

| Dimension | Studies |
|---|---|
| joint (vs local) evaluation | S07, S15, S65 |
| measured interactions | S02, S36, S37, S56 |
| staged evaluation | S32, S34, S88 |
| adaptive evidence acquisition | S05, S20, S23, S33 |
| cost/fidelity modeling | S04, S06, S21, S72 |
| lifecycle/configuration cost | S85, S86, S94 |
| physical implementation | S59, S61, S78, S81 |
| multi-benchmark transfer | S10, S11, S90 |
| decision/Pareto stability | S43, S45, S92 |
| energy/power | S19, S20 |
| CPU–FPGA interaction | S83, S84 |
| memory/data movement | S73 |

Two more rules add partial links:
- `bo_mobo` papers relate partially to S72.
- HLS papers with public code relate partially to S71, as candidate external baselines.

S87 and S89 receive keyword-screen partial links. These are labelled as such in `STUDY_LITERATURE_MAP.yaml`.
A mapping means the paper reports on the same dimension. **It does not mean the paper answers the Study's question.**

## 8. Overlap and gaps

The labels are deliberately cautious: `KNOWN PRIOR ART`, `PARTIAL OVERLAP`, `POTENTIAL OVERLAP`, `UNRESOLVED`,
`POTENTIAL GAP`, `REQUIRES EXPERIMENTAL VALIDATION`.

A *potential gap* only says that a particular paper does not report a dimension. It is not evidence that no work
exists; the reviewed set is not a systematic review.

## 9. Literature evidence vs our evidence

Everything here is `LITERATURE_REPORTED`. A number from a paper never becomes `OUR_MEASURED`, and cross-paper
numbers are not compared without normalization (`AI_CONTROL/LITERATURE_NORMALIZATION_POLICY.md`). Reproducing a
baseline belongs to **S71**, which produces `REPRODUCED` evidence under `runs/` and `evidence/`, never here.

## 10. What must NOT be claimed from this directory

- Novelty, "first work", "no prior work", "state of the art", "best" or "unique". Such a claim requires a separate,
  reviewed argument backed by our own measured evidence.
- That a Study is answered, or that a gap is real, because a matrix cell is empty.
- Any measured, reproduced or hardware result.
