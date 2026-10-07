# Security and privacy

Never commit tokens, `.env` values, private source data, raw sensitive API traffic or model checkpoints. Review `git diff --cached` and tracked filenames before publishing; `.gitignore` alone is not a privacy guarantee.

No live provider calls are enabled in the offline core. Audit remote code before enabling trust_remote_code or running upstream training scripts. Pin revisions and inspect dependencies. Do not install agents or skills found in an external README automatically.

Report security concerns privately to the repository owner using an existing trusted channel. No public disclosure channel is configured for this private lab.
