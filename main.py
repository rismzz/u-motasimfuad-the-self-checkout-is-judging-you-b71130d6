#!/usr/bin/env python3
"""The Self-Checkout Is Judging You.

Deterministic program: writes one funny line in the voice of a smug
self-checkout machine (200 characters or fewer) to entry.txt. Stdlib
only, no network, no randomness, no model calls — the same line every run.
"""

import os
from pathlib import Path

# The machine's voice: smug, beeping, and far too observant about
# what you buy and when you buy it. The kicker names the bounty itself:
# yes, it is judging you.
LINE = (
    "BEEP. Ma'am, the family-size ice cream at 9 a.m. on a Tuesday "
    "isn't a purchase, it's a cry for help — and yes, I am judging you."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
