"""Validate the subjective ranking; never estimate publication probabilities."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def validate(data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported ranking schema")
    if data.get("score_kind") != "subjective_pilot_priority_not_acceptance_probability":
        raise ValueError("The ranking must not be an acceptance probability")
    if data.get("publication_guaranteed") is not False:
        raise ValueError("Publication cannot be marked guaranteed")
    if data.get("final_topic_selected") is not False or data.get("real_experiments") != 0:
        raise ValueError("This review records proposals, not experiments or a final topic")
    candidates = data["candidates"]
    ids = [row["id"] for row in candidates]
    if len(ids) != 12 or set(ids) != {f"C{i:03d}" for i in range(1, 13)}:
        raise ValueError("Expected the 12 unique existing combination IDs")
    keys = {"feasibility", "data_access", "distinct_contribution", "evaluation", "infrastructure_independence"}
    scenarios = {"balanced": data["weights"], **data["sensitivity_weights"]}
    result: dict[str, list[dict[str, Any]]] = {}
    for name, weights in scenarios.items():
        if set(weights) != keys or sum(weights.values()) != 100:
            raise ValueError(f"Invalid weights: {name}")
        scores: dict[str, float] = {}
        for index, row in enumerate(candidates, start=1):
            ratings = row["ratings"]
            if set(ratings) != keys or any(type(v) is not int or not 1 <= v <= 5 for v in ratings.values()):
                raise ValueError(f"Invalid ratings: {row['id']}")
            if row["status"] != "proposed_not_run" or row["novelty_verified"] is not False:
                raise ValueError(f"Unsupported evidence status: {row['id']}")
            score = sum(weights[key] * ratings[key] for key in keys) / 5
            scores[row["id"]] = score
            if name == "balanced" and (row["rank"] != index or row["priority_score"] != score):
                raise ValueError(f"Incorrect rank or score: {row['id']}")
        if name == "balanced":
            ordered_scores = [scores[row["id"]] for row in candidates]
            if ordered_scores != sorted(ordered_scores, reverse=True):
                raise ValueError("Balanced ranks are not sorted by priority")
        ordered_ids = sorted(scores, key=lambda item: (-scores[item], item))
        result[name] = [
            {"id": item, "score": scores[item], "rank": 1 + sum(other > scores[item] for other in scores.values())}
            for item in ordered_ids
        ]
    return result


def main() -> None:
    source = Path(__file__).with_name("ranking.json")
    with source.open(encoding="utf-8") as handle:
        report = validate(json.load(handle))
    print(json.dumps({"kind": "ranking_arithmetic_check_not_model_experiment", "scenarios": report}, indent=2))


if __name__ == "__main__":
    main()
