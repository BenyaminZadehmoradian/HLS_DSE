from dataclasses import dataclass, field
from typing import Any, Dict, Optional

@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    benchmark_id: str
    pragma_config: Dict[str, Any]
    generator: str = "unknown"
    seed: Optional[int] = None

@dataclass
class RunRecord:
    run_id: str
    study_id: str
    benchmark_id: str
    environment_id: str
    candidate_id: str
    status: str = "PLANNED"
    failure_class: Optional[str] = None
    metrics: Dict[str, Any] = field(default_factory=dict)
