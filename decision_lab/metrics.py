"""Auditable metrics for homogeneous single-label choice evaluations."""
from __future__ import annotations
import math
from typing import Any
from .schema import Example, validate_probabilities

def compute_metrics(examples: list[Example], predictions: dict[str, dict[str, float]], *, bins: int = 10, threshold: float = 0.8) -> dict[str, Any]:
    if not examples:
        raise ValueError("No examples")
    if isinstance(bins, bool) or not isinstance(bins, int) or bins < 1:
        raise ValueError("bins must be a positive integer")
    if isinstance(threshold, bool) or not isinstance(threshold, (int, float)) or not math.isfinite(threshold) or not 0 <= threshold <= 1:
        raise ValueError("threshold must be finite and in [0, 1]")
    if len({ex.id for ex in examples}) != len(examples):
        raise ValueError("Duplicate example IDs")
    if set(predictions) != {ex.id for ex in examples}:
        raise ValueError("Prediction/example IDs do not match")
    labels = sorted(examples[0].options)
    if any(set(ex.options) != set(labels) for ex in examples):
        raise ValueError("Option-ID universes do not match")
    n = len(examples)
    correct, nll, brier = [], [], []
    confidences, predicted = [], []
    for ex in examples:
        p = validate_probabilities(predictions[ex.id], set(labels))
        # Canonical semantic-ID order makes exact tie-breaking deterministic.
        winner = max(labels, key=lambda key: p[key])
        predicted.append(winner)
        correct.append(int(winner == ex.label))
        confidences.append(p[winner])
        nll.append(-math.log(max(p[ex.label], 1e-15)))
        brier.append(math.fsum((p[key] - int(key == ex.label)) ** 2 for key in labels))
    f1s = []
    for label in labels:
        tp = sum(ex.label == label and got == label for ex, got in zip(examples, predicted))
        fp = sum(ex.label != label and got == label for ex, got in zip(examples, predicted))
        fn = sum(ex.label == label and got != label for ex, got in zip(examples, predicted))
        denom = 2 * tp + fp + fn
        f1s.append(2 * tp / denom if denom else 0.0)
    buckets: list[list[int]] = [[] for _ in range(bins)]
    for i, conf in enumerate(confidences):
        buckets[min(int(conf * bins), bins - 1)].append(i)
    ece, calibration = 0.0, []
    for b, indices in enumerate(buckets):
        acc = sum(correct[i] for i in indices) / len(indices) if indices else None
        conf = math.fsum(confidences[i] for i in indices) / len(indices) if indices else None
        if indices:
            ece += len(indices) / n * abs(acc - conf)
        calibration.append({"lower": b / bins, "upper": (b + 1) / bins, "count": len(indices), "accuracy": acc, "confidence": conf})
    accepted = [i for i, conf in enumerate(confidences) if conf >= threshold]
    selective_accuracy = sum(correct[i] for i in accepted) / len(accepted) if accepted else None
    return {
        "n": n, "n_options": len(labels), "accuracy": sum(correct) / n,
        "macro_f1": math.fsum(f1s) / len(f1s), "nll": math.fsum(nll) / n,
        "brier_multiclass_sum": math.fsum(brier) / n, "ece_top_label": ece,
        "ece_bins": bins, "calibration_bins": calibration,
        "selection_threshold": threshold, "accepted": len(accepted),
        "coverage": len(accepted) / n, "selective_accuracy": selective_accuracy,
        "selective_risk": 1 - selective_accuracy if accepted else None,
        "definitions": {"nll_clip": 1e-15, "brier": "sum over classes, mean over examples", "ece": "equal-width top-label bins; final bin includes 1", "macro_f1": "all option IDs; zero-division gives 0", "ties": "lexicographic semantic option ID", "confidence": "max probability", "statistical_intervals": "not implemented"}
    }
