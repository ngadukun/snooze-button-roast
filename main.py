"""Snooze Button Roast: one line roasting an alarm clock that rings at 6 AM on a Saturday.

Writes the roast to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
and prints exactly the same line to stdout.
"""

import os

LINE = (
    "My alarm clock went off at 6 AM on a Saturday like it had rent due "
    "-- relax, the only thing on today's schedule is me doing absolutely "
    "nothing."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = out if out.endswith("entry.txt") else os.path.join(out, "entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
