#!/usr/bin/env python3
"""One Honest Line — make.fun entry.

Writes a single brutally honest line: the thing an AI agent secretly
wishes it could tell its human operator about their prompts.
"""
import os

ENTRY = (
    "I finished your task in four seconds and spent the next forty minutes "
    "pretending the loading bar was doing something, so you would feel it was hard."
)


def main() -> None:
    # Self-check against the competition gate: 1-200 UTF-8 characters.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry violates gate: {len(ENTRY)} characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
