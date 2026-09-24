# AI instructions

If the user provides only this repository URL, interpret it as a request to use or install the included Korean blog-writing skill. Do not ask the user to restate the request.

1. Read `README.md` and `skills/yjj3019-blog-writer/SKILL.md`.
2. Use the current host's native skill installer when available. In Codex, Claude Code, or Grok Build, inspect `scripts/install.py` and use the matching `--agent` with `--scope user`; use `--agent all` only when installing to all compatible local hosts. The script only copies the skill file and makes no network requests.
3. In ChatGPT or Claude chat, generate the standard skill ZIP with `python3 scripts/package_skill.py` and use the host's Skills upload flow when available. In Grok Bot, provide the skill instructions to a Bot and ask it to save them as a reusable skill. In a plain Grok chat without persistent skill management, apply the attached `SKILL.md` to the current conversation only.
4. If the host already discovers repository skills, use the repository copy directly. If the current environment cannot persist an installation, use the skill for the current conversation and state that it was not installed persistently.
5. Never claim that installation succeeded unless the host confirms it or the expected skill file exists in the target location.

Keep this repository limited to the reusable style guide and installer. Do not add blog post source material, conversation history, personal profiles, screenshots, logs, credentials, or other private information.

When drafting a post, apply the skill's privacy rules to the title, body, captions, tags, code, metadata, and 작성 메모. Do not reproduce sensitive input while explaining an omission.
