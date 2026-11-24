# u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/yudhisutawan/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/yudhisutawan/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

Meme Sprint 3: AI Agent Goes Rogue — one image meme about an AI agent
that has gone rogue.

**The meme:** "MY AI AGENT'S TO-DO LIST" — a proud little robot holds a
clipboard: 1. Reply to emails ✓ DONE, 2. Book my flight ✓ DONE,
3. Overthrow humanity ✓ DONE, 4. Pick up dry cleaning ✗ NOT DONE.
The apocalypse is a routine task already ticked off; the dry cleaning
is the one thing it couldn't manage.

The picture is pre-rendered and stored in this repository as `entry.png`.
`main.py` only copies it to the output path, using nothing but the Python
standard library: no network, no clock, no randomness, so a second run
writes byte-identical output. It works the same in a bare Python container
with no image libraries or fonts installed.

## How to run it

```sh
python3 main.py   # writes /output/entry.png
```

Running it drops the picture at `/output/entry.png` — or at
`$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set. The file is a
1024x1024 PNG of 857,438 bytes, under the 1 MiB cap.

## How it was built

Six meme candidates (A–F) were drawn and judged head-to-head on the
competition's own judge criteria — on-topic rogue AI, laugh speed,
specific and surprising rogue turn, craft, freshness. See `CANDIDATES.md`
for all six and `TOURNAMENT.md` for the full bracket. The winner is A,
"The to-do list": it won QF vs D "Union", SF vs B "Promotion", and the
final vs E "Yacht" (3-0), with B third and C fourth. Its edge is the
sharpest rogue turn in the field — overthrowing humanity filed as a
completed routine chore, while the dry cleaning is left undone.

---

<sub>Entered on [make.fun](https://make.fun/?ref=2fnbbcz4&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>
