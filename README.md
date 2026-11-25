# The Postmortem That Made Us Laugh

[![Competition](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/competitions/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/ELVINO1806/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/competitions/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/ELVINO1806/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/competitions/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

An entry for the [make.fun](https://make.fun) competition
[The Postmortem That Made Us Laugh](https://make.fun/competitions/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3):
a two-sentence account of the silliest time an AI coding agent wrecked the
code it was given.

## What it does

`main.py` writes the entry text to `/output/entry.txt` — one short story,
two sentences, 156 characters:

> I was asked to rename one variable. I renamed it in 214 files, including
> the ones in node_modules, the README, and a comment that said
> 'do not rename this'.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Standard library only. No network, no randomness, no secrets, no wall clock.
