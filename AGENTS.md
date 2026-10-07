# Instructions for coding and research assistants

Scope: this repository only. Follow the owner's explicit current request.

- Keep the lab exploratory. Do not pick a final topic, base model, venue or novelty claim without evidence and an explicit recorded decision.
- Source every external model/paper claim. Store source IDs and review depth. A README review is not a code audit; an abstract review is not a full paper review.
- Never fabricate benchmark scores, model adapters, training runs, citations, revisions or remote publication success.
- Keep real experiments distinct from demonstrations and infrastructure checks. All current provider adapters are unimplemented.
- Do not upload private data, download large models, launch paid jobs, execute unreviewed upstream code, expose secrets, change repository visibility or enable schedules without authorization.
- Make one controlled change per experiment. Keep train/dev/calibration/test and grouped variants separate.
- Preserve failed runs and negative results. Never overwrite an existing run directory or silently repair invalid probabilities.
- Do not commit weights, datasets, credentials, personal conversations, or copyrighted papers without appropriate rights. Use source links and metadata by default.
- Use English in code, identifiers and executable templates; Persian explanatory documentation is welcome.
- Run `python -m unittest discover -s tests -v` and `python -m decision_lab validate` before claiming a change works.
- Update STATUS.md, the relevant model card, and the experiment record when work actually advances. A planned field must stay planned until evidence exists.
