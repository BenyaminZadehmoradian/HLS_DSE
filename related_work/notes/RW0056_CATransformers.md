# RW0056 — CATransformers: Carbon Aware Transformers Through Joint Model-Hardware Optimization

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Wang, Irene; Elhoushi, Mostafa; Sumbul, H. Ekin; Hsia, Samuel; Jiang, Daniel; Ardalani, Newsha; Mahajan, Divya; Wu, Carole-Jean; Acun, Bilge
- Year / venue: 2025 / NeurIPS
- DOI: 10.48550/arXiv.2505.01386 · URL: https://arxiv.org/abs/2505.01386
- Metadata source: PDF first page (arXiv v4, NeurIPS 2025 footer) + arXiv abs page (journal ref NeurIPS 2025)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/energy_sustainability/RW0056_Wang2025_CATransformers_NeurIPS_arxiv.pdf`
- SHA-256: `ad0e83a21cf09e60bc235de58f637d66822e4ea8210162f9822846702a61a7c1`
- Source: https://arxiv.org/pdf/2505.01386

## Code / dataset / artifact provenance
Code: https://github.com/facebookresearch/CATransformers

## 1. Research question
Hardware-aware model/accelerator design optimizes latency or energy and ignores total (operational + embodied) carbon, which leads to different design choices.

## 2. Problem setting
Early-stage co-design of Transformer model architecture (pruning) and edge ML accelerator parameters minimizing total lifecycle carbon under accuracy/latency constraints.

## 3. Search space
Model pruning dims (layers, FFN size, heads, embedding dim) x accelerator template params (cores 1-4, PE array X/Y 1-256, global buffer 1-8 MB, local buffer 256 KB-4 MB, local bandwidth, vector width); ~100M configurations

## 4. Evaluation method
Analytical/architectural simulation estimates (22nm, INT8); latency validated with SCALE-Sim (~13% error) and energy/latency vs V100/A100/H100 GPUs (8%/9% error); accuracy by fine-tuning proxies.

## 5. Benchmarks
BERT-Base, Llama3-8B, ViT-B/16, CLIP ViT-B/16 and ViT-B/32; CarbonCLIP vs CLIP and TinyCLIP

## 6. Hardware
Modelled edge accelerator (22nm ASIC template, 20 TOPS max, 500 MHz); search run on 8xV100 node

## 7. Toolchain
Ax, BoTorch (qNEHVI), Accelergy, Sunstone, ACT, SCALE-Sim, Electricity Maps

## 8. Metrics
Accuracy, latency, energy, operational/embodied/total carbon (CO2e), area

## 9. Baselines
Optimization modes (latency-only, energy-only, carbon); CLIP and TinyCLIP with hardware-only search

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: carbon-aware co-design 'reduce[s] total carbon emissions—by up to 30%—while maintaining accuracy and latency'; carbon-optimal designs differ from latency- or energy-optimal ones.

## 11. Limitations
Stated: targets Transformers and edge accelerators only; proxy accuracy may deviate; no CNN evaluation; broader impacts (e-waste, water) not covered; results sensitive to grid intensity and assumed lifetime.

## 12. What the paper does NOT evaluate
FPGA/HLS implementation, post-synthesis or measured accelerator power, reconfiguration, multi-accelerator systems.

## 13. Relationship to our Studies
- Direct (dimension = YES): S05 S19 S20 S23 S33 S85 S86 S94
- Partial (dimension = PARTIAL): S02 S04 S06 S07 S10 S11 S15 S21 S32 S34 S36 S37 S43 S45 S56 S65 S72 S73 S88 S90 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Joint model + hardware configuration evaluation, but single accelerator. |
| measured interactions | PARTIAL | Model-hardware interaction on latency/energy/carbon estimated; not measured on hardware. |
| staged evaluation | PARTIAL | Pruned-model fine-tuning proxy before full training of final CarbonCLIP models. |
| adaptive evidence acquisition | YES | Bayesian optimization (qNEHVI) chooses configurations to evaluate over 100 trials. |
| cost/fidelity modeling | PARTIAL | Uses cheap proxies (fine-tuning) because evaluations take 5-15 min; cost not modelled in acquisition. |
| lifecycle/configuration cost | YES | Embodied manufacturing carbon plus operational carbon over a 3-year lifetime. |
| physical implementation in the loop | NO | Architectural estimates only. |
| multi-benchmark transfer | PARTIAL | Applied to several model families, each searched separately. |
| decision/Pareto stability | PARTIAL | Sensitivity of optimal designs to grid carbon intensity/lifetime explored (Appendix K). |
| energy/power | YES | Energy and carbon are objectives. |
| CPU-FPGA interaction | NO | Not addressed. |
| memory/data movement | PARTIAL | Buffer sizes/bandwidths are search parameters affecting latency/energy. |

## 14. Possible overlap
PARTIAL OVERLAP on: adaptive evidence acquisition; lifecycle/configuration cost; energy/power

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/facebookresearch/CATransformers

## Open questions / reviewer notes
ENERGY slot justification: carbon-aware (embodied + operational) accelerator DSE with multi-objective BO, representing the lifecycle-carbon objective that the held GreenFPGA/CORDOBA/FOCAL papers treat at platform level, but applied inside an automated accelerator DSE loop. Caveat: ASIC-style accelerator template, not FPGA/HLS. No NeurIPS proceedings DOI found; arXiv DOI given. Alternatives considered and not chosen: 'A high-level synthesis approach for precisely-timed, energy-efficient embedded systems' (arXiv 2404.14769), XPNet cross-FPGA power estimation (FPGA 2024), Carbon-Efficient 3D DNN Acceleration (arXiv 2504.09851).
