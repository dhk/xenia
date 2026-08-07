#!/usr/bin/env python3
"""Check repository Markdown links and default-branch publication hygiene."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FORBIDDEN_BRANCH_URL = re.compile(r"github\.com/dhk/xenia/(?:blob|tree)/(?!main(?:/|$))([^/\s)]+)")


def main() -> int:
    errors: list[str] = []
    for document in sorted(ROOT.rglob("*.md")):
        if ".git" in document.parts:
            continue
        text = document.read_text(encoding="utf-8")
        for branch in FORBIDDEN_BRANCH_URL.findall(text):
            errors.append(f"{document.relative_to(ROOT)}: feature-branch dependency: {branch}")
        for raw_target in LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            path_text = unquote(target.split("#", 1)[0])
            candidate = (document.parent / path_text).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"{document.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{document.relative_to(ROOT)}: missing target: {target}")
    if errors:
        print("Documentation checks failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("Documentation checks passed: local targets exist; no non-main GitHub branch dependencies found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
