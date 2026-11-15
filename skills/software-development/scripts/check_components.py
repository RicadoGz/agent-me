#!/usr/bin/env python3
"""Check package integrity and optional local executable versions."""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", action="store_true", help="Also check local executable versions")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "sources.json").read_text())
    failures = []
    for relative, expected in manifest["sha256"].items():
        path = root / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            failures.append(relative)
    for role in (root / "components/playwright/agents").glob("*.toml"):
        try:
            tomllib.loads(role.read_text())
        except tomllib.TOMLDecodeError:
            failures.append(str(role.relative_to(root)))
    versions = {}
    if args.runtime:
        codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
        runtime = Path(os.environ.get("SOFTWARE_DEVELOPMENT_RUNTIME", codex_home / "tools/software-development-runtime"))
        serena = runtime / "bin/serena"
        default_playwright = Path.cwd() / "node_modules/playwright/cli.js"
        if not default_playwright.is_file():
            default_playwright = codex_home / "tools/software-development-playwright/node_modules/playwright/cli.js"
        playwright = Path(os.environ.get("SOFTWARE_DEVELOPMENT_PLAYWRIGHT_CLI", default_playwright))
        commands = {
            "serena": [str(serena) if serena.is_file() else shutil.which("serena") or "serena", "--version"],
            "playwright": ["node", str(playwright), "--version"],
        }
        for name, command in commands.items():
            try:
                result = subprocess.run(command, capture_output=True, text=True, timeout=30)
                versions[name] = result.stdout.strip()
                if result.returncode:
                    failures.append(name + " executable")
            except (OSError, subprocess.TimeoutExpired):
                failures.append(name + " executable")
    result = {
        "ok": not failures,
        "catalog": str(root / "SKILLS.md"),
        "source_files_checked": len(manifest["sha256"]),
        "versions": versions,
        "runtime_checked": args.runtime,
        "failures": failures,
        "project_runtime_tests": "not_run",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
