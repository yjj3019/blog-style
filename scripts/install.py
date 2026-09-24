#!/usr/bin/env python3
"""Copy the bundled blog-writing skill into compatible local skill folders."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_NAME = "yjj3019-blog-writer"
SOURCE = Path(__file__).resolve().parents[1] / "skills" / SKILL_NAME / "SKILL.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--agent",
        choices=("codex", "claude", "grok", "both", "all"),
        default="both",
        help="Host to install into: codex, claude, grok, both (codex+claude), or all",
    )
    parser.add_argument(
        "--scope",
        choices=("user", "project"),
        default="user",
        help="Install for the current user or only this project (default: user)",
    )
    return parser.parse_args()


def destination_root(agent: str, scope: str) -> Path:
    base = Path.home() if scope == "user" else Path.cwd()
    if agent == "claude" or (agent == "grok" and scope == "project"):
        relative = Path(".claude/skills")
    else:
        # Codex and Grok Build share the user-level ~/.agents/skills location.
        relative = Path(".agents/skills")
    return base / relative / SKILL_NAME


def main() -> int:
    args = parse_args()
    if not SOURCE.is_file():
        raise SystemExit(f"Skill source not found: {SOURCE}")

    agents = {
        "both": ("codex", "claude"),
        "all": ("codex", "claude", "grok"),
    }.get(args.agent, (args.agent,))
    targets: dict[Path, list[str]] = {}
    for agent in agents:
        targets.setdefault(destination_root(agent, args.scope), []).append(agent)

    for target_dir, hosts in targets.items():
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / "SKILL.md"
        existed = target_file.exists()
        shutil.copyfile(SOURCE, target_file)
        action = "Updated" if existed else "Installed"
        print(f"{action} {'/'.join(hosts)} skill: {target_file}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
