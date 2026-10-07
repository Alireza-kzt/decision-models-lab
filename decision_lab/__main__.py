"""Run with python -m decision_lab from the repository root."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
from .runner import evaluate_run, ROOT
from .validation import validate_repository

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline Decision Models Lab utilities (no live models)")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="Check registries, references and fixtures offline")
    smoke = sub.add_parser("smoke", help="Uniform-baseline infrastructure demonstration")
    smoke.add_argument("--out", type=Path, required=True)
    evaluate = sub.add_parser("evaluate", help="Evaluate precomputed choice probabilities")
    evaluate.add_argument("--dataset", type=Path, required=True)
    evaluate.add_argument("--predictions", type=Path, required=True)
    evaluate.add_argument("--out", type=Path, required=True)
    evaluate.add_argument("--kind", choices=["demonstration", "research"], required=True)
    evaluate.add_argument("--model-id", required=True)
    evaluate.add_argument("--revision", required=True)
    evaluate.add_argument("--bins", type=int, default=10)
    evaluate.add_argument("--threshold", type=float, default=0.8)
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            result = validate_repository(ROOT)
        elif args.command == "smoke":
            config = json.loads((ROOT / "configs/smoke.json").read_text(encoding="utf-8"))
            result = evaluate_run(dataset=ROOT / config["dataset"], predictions=None, out=args.out,
                kind=config["kind"], model_id=config["model_id"], revision=config["revision"],
                bins=config["ece_bins"], threshold=config["threshold"], seed=config["seed"])
        else:
            result = evaluate_run(dataset=args.dataset, predictions=args.predictions, out=args.out,
                kind=args.kind, model_id=args.model_id, revision=args.revision,
                bins=args.bins, threshold=args.threshold)
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
        return 0
    except (ValueError, OSError) as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
