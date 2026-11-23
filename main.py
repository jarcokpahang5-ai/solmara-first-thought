#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

The entry is a single word: the first word that comes to mind,
with no topic, no explanation and no second draft. It is validated,
printed, and written to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
"""

import os

WORD = "firefly"  # first thought: small, bright, gone before you can catch it

OUTPUT_PATH = "/output/entry.txt"


def validate_word(word: str) -> str:
    """Validate the entry is exactly one word."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not word or word != word.strip():
        raise ValueError("word must be a single word with no surrounding space")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def main() -> None:
    word = validate_word(WORD)
    print(word)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word + "\n")


if __name__ == "__main__":
    main()
