# Decision Models Lab 🔬

**Private-first exploratory research workspace. No final research claim or base model selected.**

[راهنمای فارسی](README.fa.md) · [Start here](docs/START_HERE.fa.md) · [Catalogue](catalog/README.md) · [Research ideas](research/ideas/README.md) · [Current status](STATUS.md)

A lab for investigating typed decisions, schema-conditioned classifiers, non-generative decision heads, constrained-generative baselines, calibrated uncertainty, and model modification. The goal is to discover a defensible research question through evidence—not to precommit to a paper title.

## What is here
- Source-backed model cards, paper links, BibTeX and an explicit evidence audit.
- Tutorials, architecture study notes, candidate hypotheses, evaluation protocols and paper-planning templates.
- A dependency-free Python harness for validating datasets and saved probability predictions, running a clearly labelled uniform-baseline smoke test, and recording run manifests.
- Tests, a manual CI workflow, and a guarded private GitHub publishing helper.

## What is not here
No third-party weights, training data, API keys, paid jobs, implemented live-provider adapters, completed model comparison, or paper-ready empirical results. Paper notes initially cover metadata and abstracts, not full-text reviews. Real model integration is a separate milestone.

## Quick start — Python 3.11+
Run from this repository's root; installation is not required.

```bash
python -m unittest discover -s tests -v
python -m decision_lab validate
python -m decision_lab smoke --out runs/smoke-001
```

The smoke test is infrastructure validation on original toy data, not a research experiment.

```bash
python -m decision_lab evaluate --dataset data/examples/toy.jsonl --predictions data/examples/replay.jsonl --out runs/replay-001 --kind demonstration --model-id hand-authored-fixture --revision fixture-v1
```

Output folders are immutable: pick a new name instead of overwriting. Paid API calls and model downloads are not part of these commands.

## Publishing
A local package is not a private remote repository. See [the delivery status](DELIVERY.md). The helper defaults to a dry run; it requires Git, authenticated GitHub CLI, a matching account and an unused repository name. It creates with `--private` and refuses to push before private visibility is verified.

```bash
python scripts/publish_private.py
python scripts/publish_private.py --execute
```

## Research discipline
Link every claim to a source or immutable run. Keep train/development/calibration/test separate. Preserve failed experiments. Compare against cheap trained classifiers as well as decision models. Do not infer semantic correctness from schema validity, calibration from a probability-shaped number, or novelty from adding a head to a model.
