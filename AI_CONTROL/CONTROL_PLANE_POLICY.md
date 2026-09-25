# Runtime Control Plane Policy

**Machine-readable policy:** `AI_CONTROL/CONTROL_PLANE_POLICY.yaml` (policy_version 1.0).
**Only implementation:** `src/hlsdse/control.py`.

## Call path

Every tool execution in the project goes through one path:

```text
request (action, phase, study, environment, actor, caller, argv)
  → hlsdse.control._decide:
      policy → action → state (RESEARCH_STATE + PHASE_CONTROL) → phase → study → environment
      → state provenance → [gated only] phase state → approval → scope → environment scope → hardware → study status
  → ALLOW / DENY → CONTROL_DECISION_LOG.jsonl
  → hlsdse.control._execute (ALLOW only)
  → tool
```

The public entry points are:
- `authorize()`: decide and log. It never executes anything.
- `run_authorized()`: decide, then execute only on ALLOW.
- `transition()`: the canonical phase-state transition.
- `repository_control_errors()`: the checks shared with `scripts/validate_project.py`.

The code paths that start tools all use `run_authorized()`: `hlsdse.flow.run_command`, the environment scanner
and the launcher gate (`environments/xilinx_2025_2_1/bin/<tool>` → `tool_gate.sh`).

## Rules

- **Actions** are approval-scope tokens. Each maps to a category (the authoritative lists are in the YAML):
  - ungated: `READ_ONLY`, `ENVIRONMENT_DISCOVERY`;
  - gated: `VALIDATION`, `CONTROL_PLANE`, `RESEARCH_EXECUTION`, `HLS`, `VIVADO`, `VITIS`, `HARDWARE`.

  An unknown action is DENY.
- **Ungated** actions need a valid policy and a valid state; they fail closed like every other action.
- **Gated** actions additionally need all of the following:
  - the phase in `IMPLEMENTING` (or `VALIDATING` where the category allows it);
  - exactly one valid approval artifact for the current phase and study;
  - the action listed in the approval's `allowed` scope and absent from `forbidden`;
  - the approval environment equal to `active_environment`;
  - for environment categories, a request environment equal to `active_environment`.
- **Approval validity** requires:
  - all fields present and no `<placeholder>`;
  - `status: APPROVED`;
  - a file name equal to `approval_id` and the policy's `project_version`;
  - an ISO-8601 `approved_at` with a timezone, not in the future;
  - not expired;
  - known scope tokens, and no token that is both allowed and forbidden;
  - the file committed and unmodified;
  - `approved_commit` an ancestor of HEAD.
- **State** and **approvals** are always read from the canonical files; a caller cannot supply them.
- **State provenance:** any state other than `PLANNED` must match (by gate-field hash) the last ALLOW `TRANSITION`
  record, and that record must be backed by a valid approval. A direct edit of the gate fields is therefore not
  authorization: it is DENY.
- **Transitions** follow the `PHASE_CONTROL.yaml` table:
  - `GATE_REVIEW → APPROVED_FOR_NEXT_PHASE` is human-only;
  - a phase change (for example P0 → P1) is never an automated transition;
  - `active_environment`, `p1_authorized` and the human-gate fields are never changed by `transition()`;
  - `RESEARCH_STATE.yaml` and `PHASE_CONTROL.yaml` are replaced as one unit: if either replace fails, the other is
    restored, so the two files never disagree;
  - any failure inside `transition()`, expected or not, is logged as a DENY `TRANSITION` record.
- **Executor:** it accepts only a sealed, single-use ALLOW decision bound to the exact argv, issued in-process by
  `run_authorized()`. A shell string is never executed.
- **Log:** every decision is appended to `audit/AI_CONTROL/CONTROL_DECISION_LOG.jsonl`.
  - Each record carries:
    - request and caller: `request_id`, `timestamp_utc`, `actor`, `caller`;
    - the request: `action`, `category`, `phase`, `study`, `environment`;
    - the outcome: `decision`, `reason`, `executor_called`, and `executor_returncode` after an ALLOW;
    - versions: project, policy, state schema, approval schema, contract;
    - provenance: `state_hash`, `approval_id`, `repository_commit`.
  - Arguments are recorded only as `argv_sha256`, never in clear.
  - A decision that cannot be logged is DENY.
  - If the record written *after* a tool ran cannot be appended, the tool's result is still returned (with
    `log_error` set and a warning on stderr); a completed execution is never hidden.

## Auto-push relation

`CONTROL_PLANE_POLICY.gate_fields` must equal `AUTO_PUSH_POLICY.protected_state`, and the validator checks this.
The publisher never publishes a gate-field change or an approval artifact. The researcher commits those.
