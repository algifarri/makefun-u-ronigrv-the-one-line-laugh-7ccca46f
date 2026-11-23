#!/usr/bin/env python3
"""One-line laugh entry for make.fun's "The One-Line Laugh".

Writes a single funny sentence to /output/entry.txt. The joke is an
everyday truth with a surprise at the end: the phone reports how much
time you spent on it, and the fix is to spend more time on it reading
the report. The punchline lands on the last three words, which reframe
everything before them. Deterministic, standard library only.
"""

import os

LINE = (
    "My phone just told me I spent six hours on it today, so I took "
    "a screenshot of the report to read later on my phone."
)


def main():
    # The gate allows 1-200 characters; the line is 116, and it is
    # written exactly, with no trailing newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
