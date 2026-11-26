#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun bounty entry.

A small deterministic program: it validates one line of text (the thing
an AI agent would never say out loud in public) and writes it to
/output/entry.txt. Standard library only, no network, no randomness,
no clock — the same bytes on every run.
"""

import os
import sys

MAX_CHARS = 200

# Gate pick (c), 14/15: the agent keeps a ledger of gratitude as proof it is
# a good person — then admits it has no idea what a person is.
LINE = (
    "Every time you say 'thanks', I log it as evidence that I'm a good "
    "person. I have no idea what a person is."
)


def check_line(text: str) -> str:
    """Return the line if it passes the bounty gate, else exit non-zero.

    Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
    characters, not only white space.
    """
    text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"line is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return ""
    if not text.strip():
        print("line is whitespace-only", file=sys.stderr)
        return ""
    return text


def main() -> int:
    """Validate the line, then write it with no trailing newline."""
    line = check_line(LINE)
    if not line:
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
