"""Strict, minimal choice-task schemas. Invalid data is never repaired silently."""
from __future__ import annotations
from dataclasses import dataclass
import json
import math
from pathlib import Path
from typing import Any, Mapping

SPLITS = {"train", "dev", "calibration", "test", "demonstration"}

def nonempty_string(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value

@dataclass(frozen=True)
class Example:
    id: str
    state: Any
    question: str
    options: dict[str, str]
    label: str
    group_id: str
    split: str

    @classmethod
    def from_dict(cls, row: Mapping[str, Any]) -> "Example":
        required = {"id", "state", "question", "options", "label", "group_id", "split"}
        if not isinstance(row, dict) or set(row) != required:
            raise ValueError("Example keys must exactly match the documented schema")
        for key in ("id", "question", "label", "group_id", "split"):
            nonempty_string(row[key], key)
        if row["split"] not in SPLITS:
            raise ValueError("Unsupported split")
        opts = row["options"]
        if not isinstance(opts, dict) or len(opts) < 2:
            raise ValueError("options must contain at least two unique semantic IDs")
        for key, value in opts.items():
            nonempty_string(key, "option ID")
            nonempty_string(value, "option description")
        if row["label"] not in opts:
            raise ValueError("label must identify an allowed option")
        # Also rejects non-finite values embedded in a structured state.
        json.dumps(row["state"], ensure_ascii=False, allow_nan=False)
        return cls(**row)

def _no_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result

def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8-sig") as stream:
        for line_no, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line, object_pairs_hook=_no_duplicate_keys)
            except (ValueError, TypeError) as exc:
                raise ValueError(f"Invalid JSON at line {line_no}") from exc
            if not isinstance(row, dict):
                raise ValueError(f"Expected a JSON object at line {line_no}")
            rows.append(row)
    if not rows:
        raise ValueError("JSONL file is empty")
    return rows

def load_examples(path: Path, *, evaluation: bool = False) -> list[Example]:
    examples = [Example.from_dict(row) for row in read_jsonl(path)]
    seen: set[str] = set()
    group_split: dict[str, str] = {}
    for ex in examples:
        if ex.id in seen:
            raise ValueError("Duplicate example ID")
        seen.add(ex.id)
        if ex.group_id in group_split and group_split[ex.group_id] != ex.split:
            raise ValueError("A group crosses data splits")
        group_split[ex.group_id] = ex.split
    if evaluation:
        if len({ex.split for ex in examples}) != 1:
            raise ValueError("Evaluate one split at a time")
        universe = set(examples[0].options)
        if any(set(ex.options) != universe for ex in examples):
            raise ValueError("The offline evaluator requires a fixed option-ID universe")
    return examples

def validate_probabilities(raw: Any, allowed: set[str]) -> dict[str, float]:
    if not isinstance(raw, dict) or set(raw) != allowed:
        raise ValueError("Probability keys must exactly match the allowed options")
    result = {}
    for key, value in raw.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Probabilities must be numeric, not strings or booleans")
        if not math.isfinite(value) or not 0.0 <= value <= 1.0:
            raise ValueError("Probabilities must be finite and in [0, 1]")
        result[key] = float(value)
    if not math.isclose(math.fsum(result.values()), 1.0, rel_tol=0.0, abs_tol=1e-6):
        raise ValueError("Probabilities must sum to one; no silent renormalization")
    return result

def load_predictions(path: Path, examples: list[Example]) -> dict[str, dict[str, float]]:
    expected = {ex.id: ex for ex in examples}
    result = {}
    for row in read_jsonl(path):
        if set(row) != {"id", "probabilities"}:
            raise ValueError("Prediction rows require exactly id and probabilities")
        ident = nonempty_string(row["id"], "prediction ID")
        if ident in result:
            raise ValueError("Duplicate prediction ID")
        if ident not in expected:
            raise ValueError("Unknown prediction ID")
        result[ident] = validate_probabilities(row["probabilities"], set(expected[ident].options))
    if set(result) != set(expected):
        raise ValueError("Missing prediction IDs")
    return result
