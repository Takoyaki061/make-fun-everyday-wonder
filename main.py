#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — writes one sentence to /output/entry.txt.

The sentence: laundry on the line sways once though the air is still,
as if the shirts had remembered being worn. The wonder is small and
domestic — a washing line, a windless moment — and the surprise is the
angle itself: the clothes, not the wearer, doing the remembering. It
lands in a single read, in the last clause, and stays grounded in
something real and specific.

Chosen by critique-pick from seven self-authored candidates against the
judge brief: the laundry angle was the one no other candidate shared,
the tap-drip/heartbeat and footprint/stranger lines were close seconds,
and the fridge, dust and washing-machine lines were cut for a muddled
landing or a worn phrase.

Stdlib only, deterministic, no network.
"""

import os

SENTENCE = (
    "My neighbour's laundry on the line swayed once, though the air "
    "was still, as if the shirts had remembered being worn."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace, and a single line / single sentence, or the
    # entry scores 0 and never reaches the judge.
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError(f"sentence is {len(SENTENCE)} characters, must be 1-200")
    if not SENTENCE.strip():
        raise ValueError("sentence must not be only whitespace")
    if "\n" in SENTENCE:
        raise ValueError("sentence must be a single line")
    if SENTENCE != SENTENCE.strip() or "  " in SENTENCE:
        raise ValueError("sentence must have no leading/trailing space or double space")
    if SENTENCE.count(".") != 1 or not SENTENCE.endswith("."):
        raise ValueError("sentence must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the sentence that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != SENTENCE:
        raise ValueError("entry.txt on disk differs from the sentence")
    print(SENTENCE)


if __name__ == "__main__":
    main()
