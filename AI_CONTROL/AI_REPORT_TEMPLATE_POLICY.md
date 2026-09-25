# AI REPORT TEMPLATE POLICY

All project reports must use `AI_CONTROL/REPORT_TEMPLATE.md`.

Every report must identify report ID, type, project/phase/study/gate, creation/update dates, AI model, human owner when known, approval state, version and revision.

Every substantive result must be traceable: `Study → Run → Evidence → Derived Metric → Figure/Table → Report`.

Results must distinguish MEASURED, DERIVED, PREDICTED and REFERENCE/ORACLE data. Predictions must never be presented as measurements.

A complete report includes purpose, research questions, scope, methodology, inputs, implementation actually performed, results, figures/tables, analysis, validation, failures, limitations, reproducibility, conclusions, gate decision where applicable, change log and appendices.

The AI model name must come from the actual execution context. If unavailable, use `UNKNOWN`; never guess. Old report versions remain archived and immutable. AI cannot self-approve a Gate.
