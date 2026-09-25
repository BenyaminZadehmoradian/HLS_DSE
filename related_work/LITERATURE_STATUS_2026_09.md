# Literature Status Snapshot — 2026-09

This is a planning snapshot, not a claim of exhaustive literature coverage.

| Work | What it establishes for our design | Implication |
|---|---|---|
| HLSFactory | Large-scale dataset curation, design-space expansion, concurrent synthesis, aggregation, tool-version benchmarking | We need benchmark/tool/version provenance and a dataset/evidence pipeline. |
| HLSyn | 42 programs and 42k+ labeled designs; explicit pragma configurations and validity | Candidate identity, validity, and tool-version-specific design spaces must be first-class data. |
| AutoHLS | Automatic pragma selection/parameters plus transformations; BO/DNN-assisted exploration | Automatic pragma generation is not standalone novelty. |
| Automatic Hardware Pragma Insertion | Pragma configuration can itself be solved as an optimization problem and used for pruning | Candidate generation/space definition must be separated from evidence selection. |
| Sisyphus | Unified code transformation, pragma insertion, tile-size selection | Future search-space extensions must not be confused with the current pragma-only core. |
| Stream-HLS | Global/dataflow optimization and multi-kernel design-space automation | Multi-kernel interaction is a relevant neighboring area; our joint-evidence question must be experimentally distinguished. |
| HLSFactory-Agent | Automated extraction of standalone HLS designs from repositories | Benchmark acquisition is a separate pipeline from DSE. |

## Required next literature pass

Before P5/S71, update this table with exact paper versions, artifacts, licenses, benchmark mappings, and reproducibility status for every selected baseline.
