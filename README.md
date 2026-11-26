# One Emoji, One Smile

[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/kenoxsxs/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/kenoxsxs/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the [One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f) bounty on make.fun — one emoji, the one most likely to make a stranger smile.

## The entry

Exactly one emoji, and nothing else: **😊** (U+1F60A, smiling face with smiling eyes).

A stranger glancing at a phone screen gets one glyph and nothing else. No caption, no explanation, no punchline to decode, no in-joke that could land wrong. A face with smiling eyes says hello without a word, asks for nothing back, and reads the same at any age, in any language, on any phone. A broad grin shouts, a wink flirts, a laughing face laughs too hard for a stranger, and a heart says more than hello. Smiling eyes stay gentle, plain, and instantly readable — warmth at first glance, nothing else.

- `entry.txt` SHA-256: `08081c499cdeab015ad5c888c4aac3e8a4ba2333be9862f69482732bd817411d`
- `main.py` SHA-256: `7ec88ae2e6a7c306dce918831d4cddd44e5d908be337ad2bcc4f33bf967feeac`
- The entry is 1 character, 4 bytes UTF-8 (`f09f988a`), inside the gate of 1–8 characters.

## How it works

`main.py` (Python 3, standard library only) writes the single emoji to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline:

- validates the entry first — exactly one glyph, no whitespace, 1–8 characters;
- writes it as UTF-8 bytes through binary I/O;
- reads the file back and checks it byte for byte, decodes it, and confirms it is the same single glyph;
- prints the output path, byte count, and SHA-256 of the entry.

## Run it

```bash
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```

## Referral

Built with make.fun — join with referral code `ew1nqp5h`: https://make.fun

## License

MIT — see [LICENSE](LICENSE).
