#!/usr/bin/env python3
"""Write the two-sentence horror entry to $OUTPUT_DIR/entry.txt."""
import os
import sys

ENTRY = (
    "I found my daughter's drawings taped inside her closet. "
    "In every one I am asleep in bed, and the closet door is open, "
    "though I lock it every night."
)


def main():
    if not ENTRY.strip() or not 1 <= len(ENTRY) <= 400:
        print("LEN=%d" % len(ENTRY))
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    print("LEN=%d" % len(ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
