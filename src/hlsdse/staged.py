import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Iterable

STAGES = ("CANDIDATE", "HLS", "SYNTHESIS", "IMPLEMENTATION", "BITSTREAM", "PROGRAMMING", "RUNTIME")
DECISIONS = ("ADVANCE", "DROP", "KEEP", "DEFER", "BLOCKED")
DECISION_SOURCES = ("RULE", "HUMAN", "SCHEDULER", "ESTIMATOR_ASSISTED")   # STAGE_DECISION_CONTRACT

@dataclass(frozen=True)
class StageDecision:
    decision_id: str
    candidate_id: str
    run_id: str
    current_stage: str
    decision: str
    reason_codes: tuple[str, ...]
    evidence_ids: tuple[str, ...]
    next_stage: str | None
    decision_source: str
    timestamp_utc: str
    policy_version: str = "1.0"
    estimator: dict[str, Any] | None = None

    def to_dict(self):
        d = asdict(self)
        d["reason_codes"] = list(self.reason_codes)
        d["evidence_ids"] = list(self.evidence_ids)
        return d


def next_stage(stage: str) -> str | None:
    if stage not in STAGES:
        raise ValueError(f"unknown stage: {stage}")
    i = STAGES.index(stage)
    return STAGES[i + 1] if i + 1 < len(STAGES) else None


def validate_stage_decision(decision: StageDecision) -> None:
    if decision.current_stage not in STAGES:
        raise ValueError("invalid current_stage")
    if decision.decision not in DECISIONS:
        raise ValueError("invalid decision")
    if decision.decision_source not in DECISION_SOURCES:
        raise ValueError(f"invalid decision_source: {decision.decision_source}")
    if decision.decision == "ADVANCE":
        expected = next_stage(decision.current_stage)
        if expected is None:
            raise ValueError(f"cannot ADVANCE past the final stage {decision.current_stage}")
        if decision.next_stage != expected:
            raise ValueError(f"ADVANCE must target {expected}")
    elif decision.next_stage is not None and decision.decision in {"DROP", "KEEP", "DEFER", "BLOCKED"}:
        raise ValueError("non-ADVANCE decision cannot target a next stage")
    if not decision.evidence_ids and decision.decision_source != "HUMAN":
        raise ValueError("non-human stage decisions require evidence_ids")
    if decision.decision_source == "ESTIMATOR_ASSISTED":
        e = decision.estimator or {}
        for key in ("estimator_id", "estimator_version", "confidence", "input_evidence_ids", "uncertainty_description"):
            if key not in e:
                raise ValueError(f"missing estimator field: {key}")


def make_decision(candidate_id: str, run_id: str, current_stage: str, decision: str,
                  reason_codes: Iterable[str], evidence_ids: Iterable[str],
                  source: str = "RULE", estimator: dict[str, Any] | None = None,
                  decision_id: str | None = None) -> StageDecision:
    if decision_id is None:
        decision_id = f"DEC-{run_id}-{candidate_id}-{current_stage}-{uuid.uuid4().hex[:12]}"
    d = StageDecision(
        decision_id=decision_id, candidate_id=candidate_id, run_id=run_id,
        current_stage=current_stage, decision=decision,
        reason_codes=tuple(reason_codes), evidence_ids=tuple(evidence_ids),
        next_stage=next_stage(current_stage) if decision == "ADVANCE" else None,
        decision_source=source,
        timestamp_utc=datetime.now(timezone.utc).isoformat(), estimator=estimator)
    validate_stage_decision(d)
    return d
