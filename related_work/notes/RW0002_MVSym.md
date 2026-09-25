# RW0002 — MVSym: Efficient symbiotic exploitation of HLS-kernel multi-versioning for collaborative CPU-FPGA cloud systems

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_ABSTRACT_ONLY`.

## Bibliographic identity
- Authors: Jordan, Michael Guilherme; Lignati, Bernardo Neuhaus; Korol, Guilherme; Rutzig, Mateus Beck; Beck, Antonio Carlos Schneider
- Year / venue: 2023 / Integration, the VLSI Journal
- DOI: 10.1016/j.vlsi.2023.102052 · URL: https://doi.org/10.1016/j.vlsi.2023.102052
- Metadata source: ScienceDirect abstract page (abstract, intro preview, section snippets) + Crossref

## PDF provenance
- Status: `METADATA_ONLY_PAYWALLED` (no PDF)
- Canonical path: `none`
- SHA-256: `none`
- Source: none

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
Resource provisioning in multi-tenant collaborative CPU-FPGA cloud systems with variable resource availability and workloads; the paper exploits multiple HLS-generated versions of each kernel to enlarge the options available to allocation strategies.

## 2. Problem setting
Cloud warehouse where batches of kernel requests from tenants are dispatched to CPU or FPGA partial reconfigurable regions (PRR) under a provider-set optimization goal.

## 3. Search space
Per-kernel choice among HLS versions (library of >90 versions from coarse-grained HLS directive exploration) jointly with CPU/FPGA collaborative allocation strategy; parameters include PRR size and batch size.

## 4. Evaluation method
Per abstract/snippets: kernel library characterized with Vivado HLS/Vivado reports (FPGA) and perf/RAPL/AMD uProf (CPU); allocation evaluated for makespan and energy across PRR sizes (20%, 80%, 100%). Exact on-board vs. model-based split NOT_REPORTED in accessible text.

## 5. Benchmarks
NOT_REPORTED in accessible text ('broad set of applications'; >90 kernel versions)

## 6. Hardware
Intel Core i7-4790k, AMD Threadripper 3990x, Xilinx Alveo U200 (from Methodology snippet)

## 7. Toolchain
Vivado HLS, Xilinx Vivado, perf, Intel RAPL, AMD uProf (versions NOT_REPORTED in accessible text)

## 8. Metrics
Makespan, energy

## 9. Baselines
Traditional cloud allocation strategies with non-optimized kernels (e.g., B.FCFS baseline mentioned in snippet)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 'Our framework achieves up to 4.62x makespan and 19.04x energy improvements over traditional strategies executing non-optimized kernels' (abstract); intro states up to 5.62x makespan and 26.68x energy.

## 11. Limitations
From accessible text: requires explicit Cloud-provider input (goal weights, batch size); future work to detect goals automatically. Full limitations NOT_REPORTED (paywalled).

## 12. What the paper does NOT evaluate
Unclear from abstract: post-route/physical effects on joint placement, reconfiguration time cost modeling detail, HLS estimate fidelity; full text not accessed.

## 13. Relationship to our Studies
- Direct (dimension = YES): S19 S20 S83 S84
- Partial (dimension = PARTIAL): S07 S15 S32 S34 S65 S85 S86 S88 S94

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Batch-level selection of kernel versions plus allocation; whether candidates are co-evaluated jointly is NOT verified (abstract only). |
| measured interactions | NOT_REPORTED | Full text not accessed. |
| staged evaluation | PARTIAL | Two-stage framework (versioning, then allocation) — staging of optimization, not of evaluation fidelity. |
| adaptive evidence acquisition | NOT_REPORTED | Full text not accessed. |
| cost/fidelity modeling | NOT_REPORTED | Full text not accessed. |
| lifecycle/configuration cost | PARTIAL | Considers Partial Reconfigurable Regions of different sizes; whether PR latency is modeled NOT_REPORTED. |
| physical implementation in the loop | NOT_REPORTED | Vivado used for FPGA reports per snippet; unclear if post-route. |
| multi-benchmark transfer | NOT_REPORTED | Full text not accessed. |
| decision/Pareto stability | NOT_REPORTED | Full text not accessed. |
| energy/power | YES | Energy is a primary metric (RAPL/uProf for CPU). |
| CPU-FPGA interaction | YES | Collaborative CPU-FPGA allocation is core. |
| memory/data movement | NOT_REPORTED | Full text not accessed. |

## 14. Possible overlap
PARTIAL OVERLAP on: energy/power; CPU-FPGA interaction

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
Identity confirmed: MVSym = 'Multi-Versioning ... Symbiotic' (not 'symbolic'). Paywalled Elsevier; no author/repository copy found (author page gkorol.github.io links only to ScienceDirect). Reviewed from ScienceDirect abstract, intro preview and section snippets. Related prior work by same group: Lignati et al., 'Exploiting HLS-Generated Multi-Version Kernels to Improve CPU-FPGA Cloud Systems', ASP-DAC 2021. ScienceDirect labels article type 'Review article' though content is an original framework.
