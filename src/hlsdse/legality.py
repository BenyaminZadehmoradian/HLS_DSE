from typing import Callable, Iterable
from .models import Candidate

def filter_legal(candidates: Iterable[Candidate], predicate: Callable[[Candidate], bool]):
    for c in candidates:
        try:
            if predicate(c): yield c
        except Exception:
            continue
