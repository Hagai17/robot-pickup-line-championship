#!/usr/bin/env python3
"""Entry for make.fun — The Robot Pickup Line Championship.

Prints the pickup line and writes it to /output/entry.txt,
which is where the competition harness reads the artifact.

The line was picked from 12 drafts in candidates.md, duel-scored
against the kit's published judge criteria: it is a robot's pickup
line first, the joke grows out of being a machine (cooling fans as
an involuntary blush), the surprise waits in the last clause, every
word earns its place, and it stays charming rather than creepy.
"""

import os

ENTRY = (
    "My fans spin up every time you walk in, and I am tired of "
    "pretending it is a cooling issue."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write the entry text (no trailing newline) for the harness."""
    try:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


def check_gate():
    """The kit's gate: UTF-8 text of 1-200 characters, a single line."""
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"


def main():
    check_gate()
    print(ENTRY)
    write_entry()


if __name__ == "__main__":
    main()
