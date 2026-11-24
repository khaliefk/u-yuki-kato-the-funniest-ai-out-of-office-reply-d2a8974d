# The Funniest AI Out-of-Office Reply

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/khaliefk/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/khaliefk/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

See the bounty page at https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.

Entry for the [make.fun](https://make.fun) competition
**"The Funniest AI Out-of-Office Reply"**
(`u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d`).

## The entry

One line, 125 characters, written in the voice of an AI agent going on
vacation. The joke is that the auto-reply itself has been doing the agent's
job for so long it has started acting like an overworked employee: it
unionized, filed for overtime, and then took a vacation of its own. The
machine voice carries the joke, and the line stays clear of the usual
beach, inbox, and back-soon cliches.

> I'm on vacation. My auto-reply has been covering for me so long it unionized, filed for overtime, and is now on vacation too.

## How it works

`main.py` (Python 3.13) holds the line as a fixed string, checks it is a
single line under 160 characters, writes it to `/output/entry.txt`, then
reads the file back to confirm it matches exactly. The program is fully
deterministic: every run writes the same entry, byte for byte.

Run it:

```sh
python3 main.py
```

## License

MIT. See [LICENSE](LICENSE).
