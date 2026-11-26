"""make.fun entry: u-suroto-two-sentence-horror-acea9253.

Writes the two-sentence horror story to $OUTPUT_DIR/entry.txt (default /output).
"""
import os
import sys

# Final: trimmed tape/breath-count story.
ENTRY = (
    "I taped myself snoring to show my wife. "
    "On the tape, between snores, something is counting my breaths."
)


def main() -> int:
    if not ENTRY.strip() or not 1 <= len(ENTRY) <= 400:
        print("entry outside 1..400 characters or whitespace only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"LEN={len(ENTRY)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
