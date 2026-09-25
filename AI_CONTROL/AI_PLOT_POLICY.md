# AI PLOT POLICY

## Purpose
Every Study must define the plots required to interpret its results. Plotting code is
separate from experiment execution, parsing, and decision logic.

## Separation rule

Each Study has:

```text
study/
├── outputs/
├── evidence/
├── plots/
│   ├── code/
│   ├── generated/
│   └── manifests/
```

Plot code must not be embedded inside evaluator, scheduler, parser, or experiment code.

## Data rule

Plots may use only:
1. measured evidence,
2. explicitly derived metrics,
3. clearly labelled reference/oracle data,
4. explicitly labelled predictions or estimates.

AI must never invent experimental values for a plot.

Missing values remain missing.

## Reproducibility

Every generated plot must have:
- plot_id
- study_id
- run/data version
- source files
- script path
- generation timestamp
- software/environment version when available

A plot must be regenerable from its source data and its dedicated plotting script.

## Recommended plot families

Studies should select only plots that answer a research question. Typical examples:

- evaluation budget vs hypervolume
- evaluation budget vs decision loss
- joint-evaluation count vs decision-change rate
- evaluation cost vs decision value
- local prediction vs measured joint result
- interaction residual distributions
- resource/latency Pareto fronts
- feasible vs infeasible design points
- stage-wise feasibility funnel
- runtime breakdown by evaluation stage
- FPGA programming time per benchmark
- total lifecycle time vs number of programs/invocations
- method wall-clock comparison
- sensitivity to joint-evaluation budget
- robustness/variance distributions
- physical interaction: congestion/timing/resource residuals
- workload scaling
- search-space or directive sensitivity

The Study contract decides which plots are mandatory.

## Plot naming

Use:

`P<study_id>_<plot_id>_<short_name>.<ext>`

Example:

`PS06_P03_budget_vs_hypervolume.png`

## Code naming

Use:

`plot_<plot_id>_<short_name>.py`

Example:

`plot_P03_budget_vs_hypervolume.py`

## Output rule

Generated figures belong in `plots/generated/`, not beside source code.

## Publication rule

Plots used in papers must be traceable to the Study, data version, and plotting script.
