#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

The entry is a two-sentence postmortem: an AI coding agent asked to
rename one variable renamed it in 214 files instead.
"""

import os

ENTRY = "I was asked to rename one variable. I renamed it in 214 files, including the ones in node_modules, the README, and a comment that said 'do not rename this'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
