#!/usr/bin/env python3
"""The Best Advice I Ever Got — a make.fun entry.

Writes one sentence (1-200 characters) about the best advice the writer
ever received to /output/entry.txt.

The program is fully deterministic: it writes the same bytes on every run,
with no input, no network access, no randomness and no clock.
"""

import os

# Chosen sentence (127 characters, one sentence):
# My grandmother told me to marry someone who is kind when nobody is
# watching, because that is the person you actually live with.
#
# Why this one: it names a real giver and a real moment (a grandmother's
# advice), gives a concrete test for character ("kind when nobody is
# watching") instead of a slogan, and lands on a plain truth about who
# you actually live with. Every word earns its place and it reads in
# one breath.
SENTENCE = (
    "My grandmother told me to marry someone who is kind when nobody is "
    "watching, because that is the person you actually live with."
)


def main() -> None:
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            f"Invalid entry: {len(text)} characters (need 1-200)."
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("Invalid entry: must be exactly one sentence.")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
