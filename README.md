# Dad Joke Showdown

[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/oponopon31/u-mfnakmal-dad-joke-showdown-1d2ce3e5/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/oponopon31/u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [make.fun](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) competition "Dad Joke Showdown".

`main.py` (Python 3, pure standard library, deterministic, no network)
writes one original dad joke to `entry.txt`:

> I told my computer I needed space, so it started sending me facts about Mars.

The joke is 77 characters, well inside the 200-character gate. The pun is
a literal-minded machine hearing "I need space" as outer space; the
punchline lands at the end, delivered deadpan. The reasoning behind the
choice, including the candidates it beat, is in the docstring of `main.py`.

Run it with:

```sh
python3 main.py
```

It honours `$MAKEFUN_OUTPUT_DIR` (falling back to `/output`, then the
current directory), validates the joke (1–200 characters, not only
whitespace), writes `entry.txt`, and prints the character count, byte
count, and SHA-256 of the output.
