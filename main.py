"""Warning Label for Humans: writes the entry to /output/entry.txt.

Why this line: the judge wants a single-line safety warning label for
every human being — funny first, plausible second, with the turn arriving
in the last few words and the wording of a real printed label. "I'm fine"
is the most recognised lie in the human vocabulary: everyone has said it
while visibly falling apart, and everyone has heard it and known better.
The label form does the comedy — WARNING, then a hazard, then handling
instructions — and the turn lands at the very end: do not attempt to fix,
offer snacks and leave quietly. That last instruction is true about how
people actually behave, which is why it lands instead of just sounding
absurd.

The entry text is assembled below from three fragments, joined with a
single space, so the sentence is built step by step and stays readable.
"""

import os

# The entry itself: one line, at most 160 characters.
# Kept as fragments so the sentence can be read and checked piece by piece.
ENTRY_PARTS = [
    "WARNING: This human will say 'I'm fine' while visibly falling apart.",
    "Do not attempt to fix.",
    "Offer snacks and leave quietly.",
]

# Joining with one space rebuilds the exact one-line entry.
ENTRY = " ".join(ENTRY_PARTS)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    # The gate reads a single line: no newline may sneak into the entry.
    assert "\n" not in text, "entry must be a single line"
    # No stray leading/trailing whitespace: the gate reads the line as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()
