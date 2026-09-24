#!/usr/bin/env python3
"""Package the portable blog-writing skill for ChatGPT and Claude upload."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "yjj3019-blog-writer"
SKILL_DIR = REPO_ROOT / "skills" / SKILL_NAME
DEFAULT_OUTPUT = REPO_ROOT / "dist" / f"{SKILL_NAME}.zip"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"ZIP path (default: {DEFAULT_OUTPUT.relative_to(REPO_ROOT)})",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = sorted(path for path in SKILL_DIR.rglob("*") if path.is_file())
    if not files or not (SKILL_DIR / "SKILL.md").is_file():
        raise SystemExit(f"Skill source is incomplete: {SKILL_DIR}")

    output = args.output if args.output.is_absolute() else Path.cwd() / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, Path(SKILL_NAME) / path.relative_to(SKILL_DIR))

    print(f"Created {output} ({len(files)} file(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
