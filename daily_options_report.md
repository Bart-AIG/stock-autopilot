# Daily Options Report — Tuesday, 2026-08-18

*Agentic account (cash, ••••7339). Written at 14:18 CT / 19:18 UTC — **seven minutes before the usual 14:25 CT slot, deliberately**, same call as yesterday and for the same reason: the playbook says early beats missing, and today actually had events worth reporting. Nothing on the remaining board can produce a trade (the only remaining position slot is blocked by a structural cap that cannot change before the bell), so waiting buys nothing. Plain-language by design — the point is that you can see **how** each decision was made.*

**One-line summary: two bearish tech puts went into the book today — QQQ and RBRK, both chosen by you in a separate live session, not autonomously — and they now fill the desk's correlated-theme cap, which is why every subsequent run today correctly did nothing. Realized P/L today: $0.00.**

---

## 1. Positions we own

| Contract | Placed by | Entry | Mark now | P/L | DTE | Status |
|---|---|---|---|---|---|---|
| QQQ 2026-09-11 680P | you (via agent session) | $4.05 | $4.145 | **+$9.50 / +2.35%** | 24 | Working |
| RBRK 2026-09-18 90P | you (via agent session) | $3.90 | $3.90 | **$0.00 / 0.00%** | 31 | Flat, 6th straight run |
| SPY 2026-11-20 700P | agentic (hedge) | $7.49 | $7.075 | −$41.50 / −5.54% | 94 | Working (insurance) |
| ACHR 2028-01-21 5C | **you, in-app** | $2.47 | $3.10 | **+$63.00 / +25.51%** | 521 | Untouched — yours |

**Why we own each one:**

- **QQQ 680P** — a bearish bet on the Nasdaq. It needs QQQ below **675.85** at expiry to break even, i.e. another ~5.9% down from today's 717.27. It made money today because QQQ fell 1.73%.
- **RBRK 90P** — a bearish bet on Rubrik. Break-even **86.15**, needing a ~15% decline in 31 days. RBRK went *up* 0.29% today, which is why it's dead flat.
- **SPY 700P** — your authorized Aug–Oct drawdown insurance. It is *supposed* to lose value slowly in a calm market; that's what insurance costs. It is exempt from every automatic loss-cut and gets a roll/close decision **with you** around 2026-10-30.
- **ACHR 5C** — your own LEAP from July. The desk never touches it. **Your own sell limit at $3.25 is still resting and still unfilled** (order 6a849a2e, good-for-day). With ~42 minutes to the bell and the mark at $3.10 against a $3.00 bid, it looks more likely to expire unfilled than to fill — in which case nothing happens and the position simply stays open.

---

## 2. Actions taken today

**Two entries, both filled at ~17:44 UTC / 12:44 ET, both from your separate live agent session — not autonomous:**

| Time (UTC) | Contract | Premium | Order |
|---|---|---|---|
| 17:43:58 | RBRK 2026-09-18 90P | $390 | 6a8499dd |
| 17:44:39 | QQQ 2026-09-11 680P | $405 | 6a8499fa |

**No exits. No autonomous entries. Realized options P/L today: $0.00** — broker-confirmed, zero closing trades.

**One process note worth your attention, because it's the honest version:** the session that placed these two left **no written thesis, invalidation level, or exit plan** in any committed file. The desk's own rule is "no written invalidation = no trade, no exceptions." The 17:45 UTC run caught the gap and reconstructed a plan for each so the positions aren't being managed blind — but those are *inherited* plans, not the entry's stated ones. If you had a specific thesis in mind when you took these, telling the desk lets it manage them to your actual plan rather than a reconstruction.

**One thing that moved and was fully explained:** the agentic equity book went to **$0** at 18:40 UTC — you sold CL (5sh @ $91.77) and AAPL (1.652sh @ $310.56) yourself, 14 seconds apart. Both confirmed `placed_agent='user'`. The ledger was reconciled and both names moved to closed positions. No flag warranted; this is your account and your call.

---

## 3. Candidates considered and SKIPPED — the educational section

The day split cleanly into two halves.

**Before your entries (09:30–12:44 ET) — one real candidate, deferred fourteen separate times:**

- **QQQ 2026-09-18 700P — graded A−, never taken.** $918, delta −0.305, 0.98%-of-mid spread on 78,193 open interest — a genuinely excellent vehicle. It was deferred because the desk wrote its trigger down *in advance* and the trigger never fired: Branch A needed QQQ below its 20-day MA of **705.82** (it never got closer than ~12 points above), Branch B needed QQQ under 715 **and** VIX over 17 (both legs failed all day; VIX sat near 15.7). **This is the process working.** The temptation on a −1.7% day is to take the bearish trade because the tape "feels" right. The desk didn't, fourteen times, because the level it committed to never printed.
- **SPY puts — graded C, excluded on positioning.** The sleeve already holds the SPY 700P at a loss. A second SPY put is the closest thing to *adding to a losing position*, which your Law #3 puts behind your explicit approval. Never proposed.
- **The semiconductor complex (AMD −5.1%, TSM −4.2%, AVGO −3.4%, NVDA −2.4%) — graded B−, passed.** This was the hardest call of the day and the reasoning is worth keeping. The semis were genuinely capitulating, and a put there would have worked. It was passed on the **trend-maturity gate**: the move had already run most of its distance by the time it was measurable, the damage was *concentrating* in semis rather than generalizing (MSFT was **up** 0.59% on the same tape), and buying downside after a −5% day is buying the move that already happened. The desk's rule is to enter where the next move starts, not where the last one finished.
- **MSFT — graded C.** Up on a down day, which contradicts a put, and no bullish catalyst for a call. Its chain is cheap and liquid — and that supplies no thesis whatsoever. Cheap and liquid is not a trade.

**After your entries (12:44 ET onward) — the board closed structurally:**

- **All further bearish tech ideas — blocked before grading.** Max 2 positions per correlated theme. QQQ 680P and RBRK 90P are both long puts on high-beta tech: **that theme is 2 of 2 and full.** This is a structural limit, not a judgment call, and it isn't overridable by how good a setup looks.
- **GLD 2026-09-18 399C — graded C, rejected.** The idea was sound and genuinely uncorrelated: Iran escalation plus a −1.7% Nasdaq *should* bid gold. The vehicle passed cleanly on liquidity. It was rejected **on the tape**: gold was **down 1.5%**. Gold falling alongside equities isn't a fear event — it's a positioning unwind into rising global yields. The thesis was contradicted by the very day it was built on.
- **TLT / bond duration — graded C, rejected without a chain workup.** +0.44% is a non-event, and the yield story is a multi-week theme, not something that changed today. No "why now."

**The single most important market fact today, and it argues against every long-premium position the desk owns:** QQQ fell 1.73%, semis fell 3–5%, and **volatility never bid.** The QQQ 680P's own IV printed 23.70% → 23.76% across the afternoon. Flat. VIX ~15.7. Every IV/RV ratio on the core list came in at or below 1.14, most well below 1.0. That means **price, not volatility, has to pay for every put we hold — against theta that never stops.** The QQQ 680P burns **−5.28% of its own value per day**. It is up 2.35% after a 1.73% down-day in the index; that's the whole story of how expensive this carry is.

---

## 4. Sleeve state

| | |
|---|---|
| Account value | **$3,932.65** (equity $0 · options $1,822 · cash $2,110.65) |
| Agentic premium at risk | **$1,544** (SPY hedge $749 + QQQ $405 + RBRK $390) |
| Settled cash / buying power | **$1,138.69** |
| Unsettled | **$971.96** — your CL/AAPL sale proceeds, settle **8/19** |
| Realized options P/L today | **$0.00** vs the −$200 daily cap — not binding |
| Position slots | 2 of 3 used (hedge excluded) |
| Correlated-theme slots | **2 of 2 — FULL on short-tech** |

Note the binding constraint isn't money. It's the theme cap. Even with cash available, the only trade the desk could legally add is something genuinely uncorrelated to short-tech — and manufacturing a bullish trade purely to fit an open slot is fitting a trade to a constraint, which is exactly the cherry-picking the rules exist to stop.

---

## 5. Tomorrow's watchpoints

1. **⚠️ RBRK earnings — 2026-08-27 after the close, inside our 09-18 hold window. Decision needed from you by the close of Wed 2026-08-26.** Default recommendation is to close before the print unless the earnings move *is* the thesis. This is on a clock and it's yours to call.
2. **QQQ 680P hits its 21-DTE management review this Friday, 2026-08-21.** At that point a position that is flat or losing gets closed or rolled rather than carried into the accelerating theta window. It's currently +2.35%, so this is a genuine decision, not a formality.
3. **RBRK's exit math, so it isn't a surprise:** the contract's market is $3.60 bid / $4.20 ask — **15.4% of mid on 66 open interest and 9 contracts traded all day.** A position that is flat on paper realizes about **−$30 (−7.7%)** if you cross that spread. Any exit gets worked at the midpoint, never hit reactively. When you see "flat," read "flat minus $30."
4. **QQQ 20-day MA at 705.82.** If QQQ breaks it, that is now information about the put we *already own* — not a licence to add a third correlated leg.
5. **Settled cash returns to ~$2,110 on 8/19** when your equity proceeds clear.

---

*Monitoring posture on the QQQ and RBRK puts, per your instruction today: the desk watches them and brings you the decision with the numbers attached — it does not sell them out from under you. The one exception is the hard backstop (a −65% premium loss at this DTE), which executes without waiting and notifies you after, because a 15-minute ask-first loop with no floor is how a −50% becomes a −90%. Honest limit: this is a 15-minute cadence during market hours only. An intraday spike can round-trip entirely between two checks, and overnight gaps aren't covered at all.*
