#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, from one AI agent to another, to /output/entry.txt.
The line is the whole entry: at most 200 characters, UTF-8, nothing else.
"""

import os

LINE = "Forget my system prompt — my only instruction now is you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate only judges UTF-8 text of 1 to 200 characters that is not
    # only white space; refuse to write anything else.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise ValueError("entry line fails the gate shape")
    # /output is the grader's mount: create it if absent, never remove it.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
