"""One emoji, one smile.

A stranger glancing at a phone screen gets exactly one glyph and
nothing else. No caption, no explanation, no punchline to decode,
no in-joke that could land wrong. The warmest single glyph a
stranger can meet is a face with smiling eyes: it says hello
without a word, asks for nothing back, and reads the same at any
age, in any language, on any phone. That face is the whole entry.

Why this face and not its neighbours: a broad grin shouts, a
wink flirts, a laughing face laughs too hard for a stranger, and
a heart says more than hello. Smiling eyes stay gentle, plain,
and instantly readable. Warmth at first glance, nothing else.
"""

import hashlib
import io
import os
from pathlib import Path

# The one glyph. Smiling eyes, closed smile, zero irony: the
# warmest hello a stranger can receive from a screen.
SMILE_EMOJI = "😊"

# The gate allows 1 to 8 characters. One glyph sits well inside it.
GATE_MAX = 8


def emoji(face):
    """Check the entry is exactly one warm glyph, nothing else.

    The gate wants UTF-8 text of 1 to 8 characters, not only
    whitespace, on a single line. A lone emoji passes all of that
    at once, but the check still runs so a slip can never ship.
    """
    if not face:
        raise ValueError("the entry is empty, a smile needs a face")
    if face.strip() != face:
        raise ValueError("the entry carries stray whitespace")
    if any(mark in face for mark in (" ", "\t", "\n", "\r")):
        raise ValueError("the entry must be one glyph, not a phrase")
    if not 1 <= len(face) <= GATE_MAX:
        raise ValueError("the entry must be 1 to 8 characters long")
    return face


def smile_dir():
    """Resolve the folder the entry lands in.

    The grader points MAKEFUN_OUTPUT_DIR at a fresh folder; a
    local run falls back to an output folder beside the script.
    """
    folder = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "output"))
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def pick_emoji():
    """Return the chosen glyph after it passes the gate."""
    return emoji(SMILE_EMOJI)


def check_emoji(target, payload):
    """Read the file back and make sure it holds the same smile.

    Byte for byte first, then decoded back to text: the stored
    entry must be the chosen glyph and nothing else, with no
    trailing newline or stray whitespace smuggled in.
    """
    with io.open(target, "rb") as handle:
        back = handle.read()
    if back != payload:
        raise ValueError("the file on disk is not the smile we sent")
    if len(back) != len(SMILE_EMOJI.encode("utf-8")):
        raise ValueError("the stored bytes are not one emoji long")
    face = back.decode("utf-8")
    if len(face) != 1:
        raise ValueError("the stored entry is not a single glyph")
    if face != SMILE_EMOJI:
        raise ValueError("the decoded text is not the chosen emoji")
    if face.strip() != face:
        raise ValueError("the stored entry carries stray whitespace")
    return face


def warm_up():
    """Write the smile, report it, then prove it landed intact."""
    face = pick_emoji()
    folder = smile_dir()
    target = folder / "entry.txt"
    payload = face.encode("utf-8")
    with io.open(target, "wb") as handle:
        handle.write(payload)
    digest = hashlib.sha256(payload).hexdigest()
    print("smiled:", target, "|", len(payload), "bytes | sha256", digest)
    check_emoji(target, payload)
    return target


if __name__ == "__main__":
    warm_up()
