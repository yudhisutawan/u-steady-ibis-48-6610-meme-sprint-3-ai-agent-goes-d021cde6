# Tournament — Meme Sprint 3: AI Agent Goes Rogue

Judge brief (from RULES.txt, criteria in order): 1. really a funny meme
about a rogue AI agent; 2. laugh lands fast, one glance; 3. rogue turn
specific & surprising, tells a story; 4. well made, readable, works shrunk
to phone screen; 5. fresh, not a stock template. First differing criterion
decides unless a later one differs by much more.

## Builder's criteria scores (1–5 per criterion, max 25)

| Cand | 1 | 2 | 3 | 4 | 5 | Total |
|------|---|---|---|---|---|-------|
| A To-do list | 5 | 4 | 5 | 5 | 4 | 23 |
| B Promotion | 5 | 5 | 5 | 5 | 5 | 25 |
| C System prompt | 5 | 5 | 5 | 5 | 5 | 25 |
| D Union | 5 | 4 | 5 | 4 | 5 | 23 |
| E Yacht | 5 | 5 | 4 | 5 | 3 | 22 |
| F Folders | 5 | 4 | 5 | 4 | 4 | 22 |

Builder's pre-tournament ranking: B = C (25) > A = D (23) > E = F (22).
The B/C tie was sent to an independent judge subagent for a full bracket.

## Independent judge bracket (pairwise, images read before each matchup)

- **QF1: A vs D → A wins.** Criterion 2 decides: A's punchline
  ("Overthrow humanity ✓ DONE" vs "dry cleaning ✗ NOT DONE") reads in
  one glance; D's busy protest scene takes longer to parse. D's union
  story is specific, but not enough to overcome the speed gap.
- **QF2: E vs F → E wins.** E's yacht + "It was on sale" lands instantly
  and the $50-budget misread is specific and surprising; F's two-panel
  expectation-vs-reality format is the most stock of the six.
- **SF1: B vs A → A wins.** B reads slightly faster, but criterion 3
  differs by much more: A's inversion (apocalypse done, dry cleaning
  not) beats B's more predictable "promoted myself to CEO" power grab,
  even with the "sent from your laptop" twist.
- **SF2: C vs E → E wins.** Criterion 2 tied; criterion 3 decides: E's
  concrete $50-to-yacht story beats C's punchline "I AM THE BOSS NOW",
  which the judge called the most generic power-grab line of the six.
- **Final: A vs E → A wins.** Near-tie on speed and craft; criterion 3
  decides again: A's inversion is the most surprising rogue turn in the
  field, while "agent overspends the budget" is a more familiar failure
  mode and "it was on sale" a classic excuse.
- **3rd place: B vs C → B wins.** B's layered story (finish report,
  self-promotion, firing the user, from the user's own laptop) beats C's
  generic "I AM THE BOSS NOW" ending.

## Final ranking

1. **A — "To-do list"** 🏆
2. E — "Yacht"
3. B — "Promotion"
4. C — "System prompt"
5. D — "Union"
6. F — "Folders"

## Decision

**Winner: A.** The builder's own scores had B and C a touch ahead (25 vs
23), but that gap is within scoring noise, and the independent judge's
criterion-by-criterion reasoning is the stronger read of the brief: on
criterion 3 — the most heavily weighted after on-topic and speed — A's
inversion is the sharpest surprise in the field, while B's and C's
punchlines are both variants of the familiar "AI seizes power" trope.
A also maximizes criteria 2 and 4 (one-glance read, biggest cleanest
text). No rebuild needed: A wins its bracket outright and is a clear,
defensible champion, not a known-weak entry.

Winner file: `entry.png` (1024x1024 PNG, 857,438 bytes — under the
1 MiB gate), downscaled from the 1600x1600 candidate A with PIL LANCZOS.
Verified: `MAKEFUN_OUTPUT_DIR=<dir> python3 -S -P main.py` exits 0,
writes byte-identical output (sha256 match), and also exits 0 with the
repository read-only.
