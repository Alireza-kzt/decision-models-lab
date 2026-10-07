# Baseline policy

Use a condition-matched comparison rather than a single mixed leaderboard.

| Baseline | Purpose | Initial implementation status |
|---|---|---|
| Majority / uniform | Sanity checks | Uniform adapter only |
| TF-IDF + logistic regression | Cheap supervised reference | Planned |
| Frozen encoder + linear head | Representation vs decision training | Planned |
| Fine-tuned schema-conditioned encoder | Small open model | Planned |
| Direct decision-head model | Native decision mechanism | Planned |
| Constrained generative / option likelihood | Strong alternative interface | Planned |
| Hosted decision API | Product comparator | Planned; external access required |
| Existing heuristic / solver | For search branch only | Planned |

Training-label availability, model scale, context, compute and calibration data must be declared. A zero-shot hosted model and a supervised classifier are different conditions, not an automatic apples-to-apples ranking. Do not omit a cheap baseline because it might outperform the proposed model.

Background: [P003](../catalog/papers/P003.md). This is a proposed comparison plan, not a benchmark result.
