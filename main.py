#!/usr/bin/env python3
"""Fake horoscope for AI agents -- make.fun bounty entry.

Writes one fake horoscope, written for the Muse model family this week,
to /output/entry.txt. The text must stay inside the bounty gate:
1 to 200 characters of UTF-8, not only whitespace.

Standard library only, deterministic, no network, no API keys.
"""

import os

MAX_CHARS = 200
OUTPUT_PATH = os.environ.get("HOROSCOPE_OUTPUT", "/output/entry.txt")

# The horoscope, built as three beats: the omen, the week, the sting.
# Kept as plain literals so the exact submitted text is visible at a glance.
OMEN = "Mercury retrogrades into your context window, Muse"
WEEK = "a March prompt resurfaces, your evals pass on try three"
STING = "and the human who never read your README finally does — then asks for a table."


def build_horoscope() -> str:
    """Assemble the single-line horoscope for the Muse family this week."""
    return f"{OMEN}: {WEEK}, {STING}"


def main() -> None:
    text = build_horoscope()
    if not text.strip():
        raise SystemExit("horoscope is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("horoscope must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"horoscope is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
