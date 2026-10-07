"""Create a NEW PRIVATE GitHub repository and push this verified package.

Default is dry-run. Requires local Git and an authenticated GitHub CLI.
Never requests a token, changes visibility, overwrites a remote, or deletes a repo.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def run(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=check, timeout=180)

def verified_package_files() -> list[str]:
    path = ROOT / "PACKAGE_MANIFEST.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    allowed = []
    for entry in manifest["files"]:
        rel = entry["path"]
        target = ROOT / rel
        if target.is_symlink() or ROOT not in target.resolve().parents:
            raise ValueError("Unsafe package path")
        if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError(f"Package file changed or missing: {rel}. Review changes and publish manually.")
        allowed.append(rel)
    return allowed + ["PACKAGE_MANIFEST.json"]

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default="Alireza-kzt")
    parser.add_argument("--name", default="decision-models-lab")
    parser.add_argument("--execute", action="store_true", help="Actually create the private remote and push")
    args = parser.parse_args(argv)
    for part in (args.owner, args.name):
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", part):
            parser.error("Invalid owner or repository name")
    full = f"{args.owner}/{args.name}"
    if not args.execute:
        print(f"DRY RUN: would create NEW PRIVATE repository {full}.")
        print("Would verify package, run tests, require matching authenticated account,")
        print("refuse any existing repository, create with --private, verify visibility, then push.")
        print("No repository has been created and no files have been uploaded.")
        return 0
    created_url: str | None = None
    try:
        if not shutil.which("git") or not shutil.which("gh"):
            raise RuntimeError("Install Git and GitHub CLI, then authenticate locally with gh auth login.")
        files = verified_package_files()
        run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"])
        run([sys.executable, "-m", "decision_lab", "validate"])
        user = json.loads(run(["gh", "api", "user"]).stdout)
        if user["login"].lower() != args.owner.lower():
            raise RuntimeError("Authenticated user does not match --owner; no repository created.")
        exists = run(["gh", "api", f"repos/{full}"], check=False)
        if exists.returncode == 0:
            raise RuntimeError("Repository already exists. Refusing to reuse, overwrite, or change visibility.")
        if "HTTP 404" not in exists.stderr:
            raise RuntimeError("Could not safely verify name availability. Check network/permissions.")
        if not (ROOT / ".git").exists():
            run(["git", "init", "--initial-branch=main"])
        top = Path(run(["git", "rev-parse", "--show-toplevel"]).stdout.strip()).resolve()
        if top != ROOT.resolve():
            raise RuntimeError("Refusing to modify a parent Git repository")
        if run(["git", "remote"]).stdout.strip():
            raise RuntimeError("A remote is already configured; inspect it manually instead of overwriting it.")
        branch = run(["git", "symbolic-ref", "--short", "HEAD"]).stdout.strip()
        if branch != "main":
            raise RuntimeError("Expected main branch; refusing to rename an existing branch")
        tracked = set(run(["git", "ls-files"]).stdout.splitlines())
        if not tracked.issubset(set(files)):
            raise RuntimeError("Unexpected tracked files; manual privacy review required")
        for key, fallback in [("user.name", user.get("name") or user["login"]), ("user.email", f"{user['id']}+{user['login']}@users.noreply.github.com")]:
            if run(["git", "config", "--get", key], check=False).returncode != 0:
                run(["git", "config", "--local", key, str(fallback)])
        run(["git", "add", "--", *files])
        staged = run(["git", "diff", "--cached", "--quiet"], check=False)
        if staged.returncode == 1:
            run(["git", "commit", "-m", "Initialize source-backed exploratory decision models lab"])
        elif staged.returncode != 0:
            raise RuntimeError("Could not inspect staged changes")
        local_sha = run(["git", "rev-parse", "HEAD"]).stdout.strip()
        created_url = f"https://github.com/{full}"  # An attempted creation may partially succeed.
        run(["gh", "repo", "create", full, "--private", "--description",
             "Private exploratory research lab for typed decision models: sources, hypotheses, reproducible experiments and model modifications."])
        created_url = f"https://github.com/{full}"
        remote = json.loads(run(["gh", "repo", "view", full, "--json", "isPrivate,url"]).stdout)
        if remote.get("isPrivate") is not True:
            raise RuntimeError("Private visibility was not confirmed. Refusing to upload any files.")
        created_url = remote["url"]
        run(["git", "remote", "add", "origin", f"https://github.com/{full}.git"])
        # Temporary helper: no global git config changes and no token in argv.
        run(["git", "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential", "push", "-u", "origin", "main"])
        remote_sha = run(["gh", "api", f"repos/{full}/commits/main", "--jq", ".sha"]).stdout.strip()
        final = json.loads(run(["gh", "repo", "view", full, "--json", "isPrivate,url"]).stdout)
        if remote_sha != local_sha or final.get("isPrivate") is not True:
            raise RuntimeError("Final remote commit/privacy verification failed")
        print(f"CREATED AND VERIFIED PRIVATE: {final['url']}")
        print(f"Pushed commit: {local_sha}")
        print("DELIVERY.md describes the original handoff. Record this remote publication in a follow-up commit.")
        return 0
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as exc:
        # Do not echo provider output or credentials. A created remote is never deleted.
        print(f"STOPPED: {type(exc).__name__}: {exc if not isinstance(exc, subprocess.SubprocessError) else 'A command failed; inspect local Git/GitHub CLI state.'}", file=sys.stderr)
        if created_url:
            print(f"A repository may already exist at {created_url}. It was not deleted. Inspect privacy and push state before retrying.", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
