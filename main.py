#!/usr/bin/env python3
"""The 3AM Fridge Text — writes one line a smart fridge texts its owner at 3am.

Deterministic: the same entry is written on every run.
"""

import os

ENTRY = (
    "3AM. You opened me, stared, shut me, then opened me again like I'd "
    "restock in 40 seconds. I didn't. I'm telling the scale."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
