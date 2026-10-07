# Data policy and example format

Only `examples/toy.jsonl` and `examples/replay.jsonl` are included. They are hand-authored infrastructure fixtures, not a benchmark, not a train/test sample from a public dataset, and not predictions by any model in the catalogue.

Actual sources must be approved, licensed and registered before download. Keep large/private data outside Git, record hashes, and group documents/paraphrases/translations before splitting.

The offline evaluator expects a single split and a fixed option-ID universe within one evaluation file. Candidate descriptions may differ, but changing label meaning invalidates the evaluation. Multi-label and ordinal scoring need separate future evaluators.
