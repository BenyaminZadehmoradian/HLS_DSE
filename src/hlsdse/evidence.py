import json
from pathlib import Path

class EvidenceStore:
    def __init__(self, root):
        self.root=Path(root); self.root.mkdir(parents=True,exist_ok=True)
    def append(self, record):
        p=self.root/"evidence.jsonl"
        with p.open("a",encoding="utf-8") as f: f.write(json.dumps(record,ensure_ascii=False,sort_keys=True)+"\n")
