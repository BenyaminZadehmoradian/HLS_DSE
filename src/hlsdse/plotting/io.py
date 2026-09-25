"""Minimal shared I/O helpers for plotting.

No experiment execution belongs here. Study-specific scripts should load their
declared evidence/derived-data inputs and generate figures independently.
"""
from pathlib import Path
import json
import csv

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def load_csv(path):
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))
