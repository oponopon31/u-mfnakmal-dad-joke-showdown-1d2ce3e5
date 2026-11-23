#!/usr/bin/env python3
"""Dad Joke Showdown entry: one single dad joke, written to entry.txt.

Candidate jokes considered (all drafted fresh for this entry) and why the
winner beats them in a head-to-head:

1. "I named my dog Stay. Now when I tell him to stay, he thinks I'm just
   greeting him."
   Decent name/command collision, but the punchline asks the reader to
   re-parse "stay" as a greeting, which lands softer than a straight
   double meaning.

2. "I asked my fridge to stop running. It said it was only trying to chill."
   The "chill" pun is serviceable, but it is the first pun anyone reaches
   for with a fridge, so a judge comparing two jokes will have seen it
   before.

3. "I asked the calendar why it was so stressed. It said it had too many
   dates."
   Same problem as (2): the "dates" pun is a well-worn pattern, and the
   setup telegraphs the punchline.

4. WINNER: "I told my computer I needed space, so it started sending me
   facts about Mars."
   A fresh, specific incongruity: the emotional "I need space" meets a
   machine that takes everything literally and hears "outer space". The
   punchline lands at the very end, the delivery is deadpan, and nothing
   in the setup gives the twist away. Against (1) it needs no re-parse,
   against (2) and (3) it is not a pun the judge has seen a thousand
   times. That is why it wins the pairwise comparison.

The program is deterministic: it always writes exactly this one joke.
"""

import hashlib
import os
import sys

JOKE = "I told my computer I needed space, so it started sending me facts about Mars."

MAX_CHARS = 200


def output_dir() -> str:
    """Resolve the output directory, honouring $MAKEFUN_OUTPUT_DIR."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.getcwd()


def validate(joke: str) -> None:
    """Gate: 1 to 200 characters, not only whitespace, valid UTF-8 text."""
    if not isinstance(joke, str):
        raise ValueError("joke must be text")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")
    if len(joke) > MAX_CHARS:
        raise ValueError(f"joke is {len(joke)} characters, over the 200 limit")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    joke.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> int:
    validate(JOKE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = JOKE.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Read back and confirm the file on disk is exactly the validated joke.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise ValueError("entry.txt on disk does not match the validated joke")
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {path}: {len(JOKE)} characters, {len(data)} bytes")
    print(f"sha256: {digest}")
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
