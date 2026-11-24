#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one original out-of-office auto-reply, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.

The line is a single sentence under 160 characters. It is fixed text, kept
in this file so the program is deterministic: every run writes the same
entry, byte for byte.
"""

import os
import sys

ENTRY = (
    "I'm on vacation. My auto-reply has been covering for me so long "
    "it unionized, filed for overtime, and is now on vacation too."
)

MAX_CHARS = 160


def main() -> int:
    if not ENTRY.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read it back: the file the judge sees must be exactly the entry.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print("round-trip check failed: file differs from entry",
              file=sys.stderr)
        return 1

    print(f"wrote {len(ENTRY)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
