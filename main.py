#!/usr/bin/env python3
"""One dad joke for the make.fun Dad Joke Showdown bounty.

The whole entry is a single dad joke, told the way a father would
tell it across the dinner table. The setup is the oldest dad
confession there is -- that Dad burns dinner -- and the punchline
is the one escape hatch no stove can ruin: booking a table
instead of cooking. "Made reservations" does the double work of
the joke: Dad dodges the cooking entirely, and the word itself
is the most dad-shaped solution to a burnt-dinner problem.

This program checks the joke against the gate (one joke, 1 to 200
characters, on a single line) and writes it to /output/entry.txt,
where the house judge reads it.
"""

import os
from pathlib import Path

MAX_CHARS = 200
# The grader sets MAKEFUN_OUTPUT_DIR; fall back to /output so the
# program also runs unchanged on a plain machine.
OUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"

JOKE = "My son asked for dinner I couldn't possibly burn, so I made reservations."


def build_joke(text):
    """Return the joke unchanged once it passes the gate.

    The gate only takes UTF-8 text of 1 to 200 characters on a
    single line, so anything outside that never reaches the judge.
    """
    joke = text.strip()
    if not joke:
        raise SystemExit("joke must not be empty")
    if len(joke) > MAX_CHARS:
        raise SystemExit(f"joke is {len(joke)} characters, limit is {MAX_CHARS}")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must stay on one line")
    return joke


def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(build_joke(JOKE), encoding="utf-8")


if __name__ == "__main__":
    main()
