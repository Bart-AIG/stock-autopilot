# Daily report — trading day 2026-09-23 (Wednesday)

*Written by the 19:15Z scheduled run (2:15 PM CT — the v11 threshold). Master carried the 2026-09-22 report, so this run owned the duty and took it. Quotes stamped 19:15:39–19:15:41Z venue time, well past the opening auction.*

**One line:** **The DAY TRACK took its signal and is winning it; both money books stood down on capital for a third straight session — and tomorrow is the day that ends.** The opening range gave a 92.6%-body SHORT, which is the side that funds at $100 of deployable cash, so the paper row exists at all: **4 PSQ @ 24.6212, now +1.34R on a permanent breakeven stop.** The equity book graded four candidates and topped out at **B** — no A-grade, no rotation, correctly no trade. **Thursday 2026-09-24 is the event:** ABNB and UNP both hit their 14-day time stops and are sold green or red, which unfreezes ~$2,060.

---

## 1. DAY TRACK — paper day 6, signal 5, the row is working

| | |
|---|---|
| **Phase** | PAPER (day **6 of 10**; **5 signals of 8**). Nothing has ever been placed. `graduate()` → `go_live: False`. |
| **Status** | ACTIVE — `track_status(3312.26, …)` → not paused. |
| **Today** | **ENTER — SHORT**, `plan_entry` → `action='enter'` |

**The signal (13:45Z run, five settled 1-minute bars 13:30–13:34Z, re-fetched and byte-identical):**

| | |
|---|---|
| Opening range | 745.085 – 747.12 (2.035 pts) |
| Body | **92.6% of range** → decisive SHORT (doji bar is <10%) |
| Vehicle | **PSQ 4 shares @ 24.6212 = $98.48** (1x inverse; no margin, no borrow) |
| Entry / stop (signal terms) | 744.43 / 747.12 → **2.69 pts = 0.3614%**, r = **$0.36** |
| Late-entry gate | **PASSED by 0.3625 points** — the narrowest clearance the track has recorded. Three minutes later on the same drift it would have skipped. |
| Sizing | `bound_by='cash'` — risk at the stop is 0.011% of the account against a 5% ceiling. **Cash binds ~450× before RISK_PCT does.** |

**Management, 15:15 ET:** QQQ **740.82** (ask) → **+1.342R**. `manage()` → **hold**. The stop has been at **744.43 = breakeven since the 14:18Z pass**, and a short's stop only ratchets down, so **this row can no longer close red.** The 2.0R trail arm sits at 739.04, **1.78 points (~3.5 ATRs) away with 15 minutes left** — it will not arm. **The exit is the flat rule:** the first run at/after 19:30Z closes the row and it books ≈ +1.3R.

**The afternoon in one number:** five direction changes between 18:02Z and 19:15Z inside a 741.53–740.20 band (1.208R → 1.346 → 1.186 → 1.364 → 1.398 → 1.242 → 1.342). That is chop above the chop rule's reach — the rule only bites at |R| < 0.5 and this row cleared 1.0R by 14:18Z.

**Honest scope, restated because the number flatters:** $98.48 notional and $0.36 of risk is a real trade in **shape** and a trivial one in **size**. +1.34R is ~$0.48. It is a valid paper sample for direction, stop, timing and the manage() ladder — which is what the paper phase measures — and it is **not** evidence about what this strategy does at fundable size.

**⚠️ The escalated asymmetry, now observed from both sides.** The same ~$100 of deployable cash that could not buy **one** QQQ share on Tuesday's 99.6%-body LONG bought **four** PSQ shares on today's SHORT. Nothing about capital changed between the two days — the coin landed the other way. **The track's ability to trade is currently decided by the signal's DIRECTION, not its quality.** Fixing it means editing the spec, which no unattended run may do; it stays escalated to Ryan (`holdings.json._DAY_TRACK_THE_LONG_SIDE_COSTS_30X_THE_SHORT_SIDE…`).

---

## 2. Positions — equity book (3 of the 3-4 target)

| Name | Shares | Entry | Now (19:15Z) | P/L | Day held | Why we own it |
|---|---|---|---|---|---|---|
| **ABNB** | 6.573584 | 169.5209 | **151.80** | **−$116.49 / −10.45%** | **13 of 14** | RSI2 mean-reversion inside a rising 200-day. Thesis **WEAKENED, not broken** (researched today). |
| **UNP** | 3.858199 | 285.1071 | **275.855** | −$35.70 / −3.25% | **13 of 14** | RSI2 dip in an uptrend; rail volumes and pricing intact. |
| **V** | 2.716801 | 368.0799 | **361.49** | −$17.90 / −1.79% | 2 of 14 | RSI2 8.2 today — still oversold, thesis untouched. |

**No exit fired today, and each of the three mechanisms was checked, not assumed:**
- **Take-profit (RSI2 ≥ 70 while GREEN):** cannot fire — all three are RED. The trigger requires green; an underwater RSI2 bounce is an *optional* exit-into-strength routed to thesis, never a mechanical loss-realization.
- **Time stop (14 days):** ABNB and UNP are day 13. **Both fire tomorrow.**
- **Target hit:** none near.
- **Green-enough trail trigger** (entry ÷ 0.85): ABNB 199.44, UNP 335.42, V 433.04 — all far away. No `SET TRAILING STOP` alert for Ryan.
- **No stop orders exist on any of these** (HARD RULE 5). The DAY TRACK is the sole stop-carrying sleeve, and it is in PAPER, so nothing rests at the broker.

### ABNB thesis research — volunteered, and the verdict matters for tomorrow
No `THESIS CHECK` was flagged; the run did it anyway because ABNB fell **−6.2% on the session** with its time stop one day out. **Verdict: WEAKENED, NOT BROKEN.** It reads as a sector-wide agentic-commerce de-rating rather than a company break, and RBC still carries **OUTPERFORM, $195** against ~$151.85 spot. Two consequences, both deliberate:
1. **No autonomous thesis sell.** A sell needs BROKEN with evidence; weakened is not that.
2. **It was deliberately NOT written back as `thesis_checked: "intact"`**, because it isn't intact. Tomorrow's run therefore sells ABNB on the **TIME STOP as written** — green or red — and must not re-litigate it as a thesis decision. Evidence and sources: `holdings.json.positions[ABNB].thesis_research_2026-09-23`.

---

## 3. Actions taken today

**None, in any book.** Zero orders placed, zero fills, **$0.00 realized** (`get_realized_pnl` 09-23: 0 closing trades). The only position opened today is the DAY TRACK paper short, which places nothing by construction.

---

## 4. Candidates considered and SKIPPED — with the specific reason

**This is the section that changed character today.** For two sessions the equity stand-down was reported as capital-blocked with **nothing graded at all**. That is a weaker output than it looks — "we had no money" is not the same claim as "there was nothing worth buying", and only the second one is knowable. So the 18:19Z run graded the field properly. **The answer came back the same, for a better reason.**

Eleven RSI2 setups on the 19:07Z report; nine after removing the two HELD names:

| Name | Grade | Why not |
|---|---|---|
| **JPM** | **B** | Best trend cushion (4.32% at the stop), shallowest decline — but **disqualified on correlation** with held V and with BAC, and its −3.4% on 09-22 is a sector repricing, not a dip. |
| **UNH** | **B** | Cushion 3.03%, −4.40%/30d — but **nothing answers "why NOW"**. Also `[ERN 2026-10-13]`, inside the hold window. |
| **BAC** | **C** | **The trend cushion expires inside the hold:** SMA200 55.2704 rising 0.0409/day turns a 1.32% cushion into 0.28% by the time-stop date. `[ERN 2026-10-14]`. |
| **BMY** | **C** | −7.10%/30d staircase of lower lows. A downtrend, not a dip. |
| **VLO, MPC, PSX, EPD** | — | **Excluded unread on Ryan's oil steer** (no new energy entries). Four of eleven setups were energy — a correlated cluster the report flagged itself. |

**The rule that decides it: a B-grade gets NO position, not a small one.** Under the concentration policy the book runs 3–4 names at ~30% each, and that only pays if the top ideas are genuinely better than the rest. Filling a slot with a B is exactly the failure that policy was written to prevent.

**Rotation gate, checked explicitly (it is the live gate, not sizing).** With deployable cash below one position size, a new idea must grade **better than the weakest position held**. Nothing graded above B; all three holdings have intact-or-weakened theses with sound entry stacks. **Selling a sound underwater thesis to chase a fresher signal is the churn the rules forbid** — and it would be pre-empting by one day a mechanical exit that fires on its own tomorrow. **No rotation.**

**Options:** no entry, nothing priced. CORE needs $500–1,000 typical; deployable is $102.61. Pricing a chain the book cannot fund is the research-constrained failure the SOURCING fix warns against — the correct output is to say so and stop. The IV sweep was deferred for the same reason: a row that gates nothing today is not worth an upper-bound measurement.

---

## 5. Sleeve state

| | |
|---|---|
| Total account value | **$3,312.26** |
| Equity value / options value | $3,044.04 / **$0.00** |
| Cash = buying power = **unleveraged** buying power | **$268.22** — identical, so **no margin is being extended** (FOUR LAWS #4 unambiguous) |
| Operational reserve (5% of total, recomputed) | **$165.61** |
| **Deployable** | **$102.61** |
| Options premium at risk | **$0.00** (book empty) |
| Realized options P/L today | **$0.00** vs the −$400 cap |
| Options entries used | **0 of 3** (0 of 1 this run) |
| Equity entries used | **0 of 3** (0 of 1 this run) |
| Open equity slots | 3 held of the **3–4 target** (band 3–5) |
| Day-track trades | 1 of 1 (paper) |

**Deployable $102.61 is 17% of the ~$600 minimum equity entry and 21% of the $500 CORE options low end, and below one QQQ share ($740.82).** Both money books are closed on capital; the day track's SHORT side is the one thing that fits.

**This is a correct state, not a breach.** There is no cash floor — it was removed 2026-08-29. Cash is the residual of quality: ~92% deployed across three positions inside the target band is what a fully-deployed book looks like. **No calibration change was applied this week** (Monday 09-21's calibration stands; the options KILL branch that briefly appeared that morning was reversed at 14:05Z and options entries are **not** paused, multiplier 1.0).

---

## 6. Tomorrow's watchpoints

1. **THE EVENT — ABNB and UNP hit day 14 and are SOLD on the time stop, green or red.** At today's marks that is ≈ **$2,062** of proceeds, taking deployable from ~$103 to ~$2,165 and the book from 3 names to 1. It is the only mechanical loss discipline this book has, and it fires on its own alert line (`TIME STOP / SELL (stalled)`) — never as a take-profit. Expect ≈ **−$152** realized across the pair at current prices.
2. **Then the book is UNDER the 3–4 target with real capital**, so the entry bar stops being "can we afford it" and goes back to being "is it A-grade". Today's field topped out at B — if that holds tomorrow, holding the cash is the right answer, but **any deliberate hold must name a catalyst and an expiry** or it is the deleted cash floor sneaking back in.
3. **V is day 3 of 14** (time stop 2026-10-05), RSI2 8.2 — still the freshest thesis in the book.
4. **Day track:** the 19:30Z run closes today's paper short on the flat rule at ≈ +1.3R, taking paper to **day 6 / 5 signals**. Graduation needs 10 days and 8 signals, so the earliest possible go-live decision is a Monday calibration two weeks out — and it remains `graduate()`'s call alone, never a mid-week promotion.
5. **The long/short capital asymmetry is still open and still Ryan's to resolve.** Until it is, roughly half of all future signals are untradeable for a reason that has nothing to do with the signal.
