#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
the voicemail greeting a cat would record. The cat has just knocked a
mug off the table and napped on the evidence, so it is too busy to take
the call -- but it will gladly take a message after the beep.
"""

import os

GREETING = (
    "You've reached the cat. I knocked your mug off the table, "
    "then napped on the evidence. Leave a message after the beep."
)


def main():
    # The gate requires 1 to 120 characters of non-whitespace text.
    assert 1 <= len(GREETING.strip()) <= 120, len(GREETING)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(GREETING)


if __name__ == "__main__":
    main()
