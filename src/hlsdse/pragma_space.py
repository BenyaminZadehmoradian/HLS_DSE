from itertools import product
from .models import Candidate

def validate_space(space: dict) -> None:
    if not isinstance(space, dict) or not space:
        raise ValueError("Pragma space must be a non-empty mapping")
    for name, values in space.items():
        if not isinstance(values, list) or not values:
            raise ValueError(f"Pragma parameter {name} must have a non-empty list")

def generate_cartesian(space: dict, benchmark_id: str):
    validate_space(space)
    keys=list(space)
    for i, vals in enumerate(product(*(space[k] for k in keys))):
        cfg=dict(zip(keys,vals))
        yield Candidate(f"{benchmark_id}-C{i:06d}", benchmark_id, cfg, "cartesian")
