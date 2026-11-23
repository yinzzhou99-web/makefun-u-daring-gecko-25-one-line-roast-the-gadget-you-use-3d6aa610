"""One-Line Roast: The Gadget You Use Every Day.

Writes one original roast line (at most 200 characters) to
/output/entry.txt. Standard library only, deterministic, no network.
"""

import os

LINE = "My robot vacuum memorized my whole house and still gets stuck on the same rug every day."

OUT_DIR = "/output"
OUT_FILE = "/output/entry.txt"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
