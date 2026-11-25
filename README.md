[![competition](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/vickyair1/u-donrulezz-the-absurd-clause-contest-035cc0f1/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/vickyair1/u-donrulezz-the-absurd-clause-contest-035cc0f1/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)

# The Absurd Clause Contest

An entry for [make.fun's "The Absurd Clause Contest" bounty](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1): one sentence, 200 characters at most, an absurd clause buried deep inside a terms-of-service agreement, judged in pairwise blind rounds until the funniest takes the reward.

## The line

> Section 14.3: by using this service, you grant us a perpetual licence to your dreams, including the right to re-run them as advertisements.

Section 14.3 grants the company a perpetual licence to the user's dreams, including the right to re-run them as advertisements. Deadpan legal boilerplate until the absurdity hits; the joke comes from the register as much as from the words, and the image is concrete.

## How it works

`main.py` (stdlib only, deterministic) writes exactly that one line to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–200 characters, UTF-8, a single clean line.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the line itself (139 characters)
- `LICENSE` — MIT
