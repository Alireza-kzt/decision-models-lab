"""Offline registry, reference and local Markdown link checks."""
from __future__ import annotations
import json
from pathlib import Path
import re
from urllib.parse import unquote
from .schema import load_examples, load_predictions

def validate_repository(root: Path) -> dict[str, int]:
    registry = root / "registry"
    def read(name: str, key: str):
        return json.loads((registry / name).read_text(encoding="utf-8"))[key]
    sources = read("sources.json", "sources")
    models = read("models.json", "models")
    papers = read("papers.json", "papers")
    for group in (sources, models, papers):
        ids = [r["id"] for r in group]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate registry ID")
    source_ids, paper_ids = {s["id"] for s in sources}, {p["id"] for p in papers}
    for item in sources:
        if not item["url"].startswith("https://") or not item["checked_at"]:
            raise ValueError("Missing source provenance")
    for item in models + papers:
        if not item["source_ids"] or not set(item["source_ids"]).issubset(source_ids):
            raise ValueError("Unknown/missing source IDs")
        if not (root / item["card"]).is_file():
            raise ValueError(f"Missing card: {item['card']}")
    for model in models:
        if not set(model["paper_ids"]).issubset(paper_ids):
            raise ValueError("Unknown paper IDs")
        if model["adapter_status"] == "not_implemented" and model["local_run_status"] != "not_run":
            raise ValueError("Inconsistent execution status")
    paths = [p for p in root.rglob("*.md") if not any(x in {".git", "runs", ".venv"} for x in p.relative_to(root).parts)]
    checked = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if target and not (path.parent / target).exists():
                raise ValueError(f"Broken local link in {path.relative_to(root)}: {target}")
            checked += 1
    demo = load_examples(root / "data/examples/toy.jsonl", evaluation=True)
    load_predictions(root / "data/examples/replay.jsonl", demo)
    for path in (root / "experiments/plans").glob("*.json"):
        plan = json.loads(path.read_text(encoding="utf-8"))
        if plan["status"] == "planned" and (plan["runs"] or plan["results"] is not None):
            raise ValueError("A planned experiment contains results")
    return {"sources": len(sources), "model_entries": len(models), "paper_entries": len(papers), "markdown_files": len(paths), "local_links_checked": checked, "toy_examples": len(demo)}
