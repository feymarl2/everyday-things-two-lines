#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run (make.fun).

Writes a fixed two-line explanation of a traffic jam to /output/entry.txt.
Deterministic by construction: one constant string, no clock, no randomness,
no environment reads, no network, stdlib only. Two runs produce byte-identical
output. No trailing newline: the file holds exactly two lines (333 chars).
"""

import os

ENTRY = (
    "A traffic jam is a school corridor at break time, with a thousand kids "
    "all trying to squeeze through one narrow door at once.\n"
    "It maps the crush, the slow shuffle forward, and the way nobody can "
    "overtake \u2014 but it leaves out that kids can turn sideways and slip "
    "through gaps while cars cannot, and that no bell ever rings to end a jam."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
