# Daily report — trading day 2026-09-15 (Tuesday)

*Written by the 19:15Z scheduled run (2:15 PM CT — the v11 threshold). Master still carried the 2026-09-14 report, so this run owned the duty. Quotes stamped 19:16–19:17Z, well outside the opening-auction window.*

**One line:** Nothing was traded by the desk in any book today. The DAY TRACK took its first-ever paper signal and stopped out at −1.00R inside twelve minutes; Ryan opened a two-legged SPY strangle himself at 18:43Z, which the desk detected, logged and left alone; the equity screen produced no A-grade for the eighth consecutive session. **Tomorrow is the FOMC decision (2026-09-16, 14:00 ET), and it is the event nearly everything below is waiting on.**

---

## 1. DAY TRACK — paper day 1 of 10

**Phase: PAPER.** The track is *not* live and did not place an order. Read the phase note carefully, because one of its two locks opened today and the other did not:

- **Lock (a) — prompt authority: OPENED.** Stop-order authority on `sleeve: "day"` positions requires prompt v11, and v11 was confirmed live at 16:18Z by direct observation of a run's own invocation stamp. This lock is discharged and should stop being reported as a blocker.
- **Lock (b) — `day_track.graduate()`: STILL CLOSED, and it is independent of the prompt.** It requires ≥10 paper days and ≥8 signals with positive expectancy. Today is **1 day, 1 signal**. The earliest arithmetically possible go-live is a Monday on or after **2026-09-28**, and only the Monday calibration may flip it. **A live prompt stamp is not a graduation.**

### Today's signal

| Field | Value |
|---|---|
| Opening range (QQQ, 09:30–09:35 ET, 1-minute bars) | high **708.855** / low **707.56** / open **708.79** / close **707.88** |
| Range | 1.295 pts = 0.183% of spot |
| Body as fraction of range | **70.3%** — well clear of the 10% doji filter, so a genuine signal |
| Direction | **SHORT** (OR close below OR open) → vehicle **PSQ** |
| Paper entry (13:35:17Z) | QQQ 708.10 signal / PSQ 26.195 vehicle |
| Stop | QQQ 708.855 (opposite OR edge) / PSQ 26.1671 |
| Size | 56 shares, $1,466.92, **bound by cash** not by risk |
| R | $1.56 |
| Exit (13:47Z) | **stop reached** — QQQ 13:38 bar high 709.10 breached 708.855 |
| Result | **−1.00R = −$1.56** at the spec's stop-price convention |

**The honest number is worse and is not being hidden.** A resting `stop_market` on PSQ triggers and then fills *at market*, and PSQ's next tick down is 26.16, so a realistic fill is **−$1.96 = −1.254R**. The spec's convention is kept so `graduate()` reads one consistent statistic across the paper sample and no single run gets to change the track's own measuring stick — but the slippage figure is carried into the Monday calibration explicitly.

### What paper day 1 bought us — three findings, which is the point of paper

1. **The short side was sized in the wrong instrument** (`_DAY_TRACK_SHORT_SIDE_SIZED_IN_THE_WRONG_INSTRUMENT_2026-09-15`). Caught only because this was the first SHORT signal the track ever produced. Fixed in `day_track.plan_entry`. This is exactly the class of bug that PAPER exists to absorb, and it would have cost real money on day one of LIVE.
2. **The PSQ stop is 2.79 cents wide on an instrument whose bid/ask is one cent** (`_DAY_TRACK_THE_PSQ_STOP_IS_2_79_TICKS_WIDE_...`). The vehicle's stop was breached at 13:37Z, a full minute *before* the signal's at 13:38Z. A stop that is under three ticks wide on a one-tick instrument is not a risk control, it is noise — this needs a decision before the track goes live.
3. **An unsettled rule collision, flagged for Ryan, not for an unattended run to resolve** (`_DAY_TRACK_VS_CASH_HOLD_UNSETTLED_2026-09-15`). `_DAY_TRACK.capital_priority` says the day trade claims deployable cash at its entry run; THE CAPITAL POLICY says a `_cash_hold` parks that same cash. Today both pointed at the same $1,470. **In PAPER this costs nothing. Before the track goes LIVE, Ryan should say which claim wins.**

**Running tally: 1 paper day, 1 signal, 1 trade, 0 wins, −1.00R.** One trade per day means no re-entry today regardless of what QQQ does into the bell.

---

## 2. Positions

### Equity swing book — 2 of the 3–4 target

| Name | Shares | Entry | Last (19:16Z) | P/L | Held | Time stop |
|---|---|---|---|---|---|---|
| **ABNB** | 6.573584 | 169.5209 | 167.923 | **−0.94%** (−$10.50) | 5 of 14d | **2026-09-24** |
| **UNP** | 3.858199 | 285.1071 | 284.640 | **−0.16%** (−$1.80) | 5 of 14d | **2026-09-24** |

**ABNB — why we own it:** a Connors RSI(2) mean-reversion entry inside a rising 200-day uptrend, taken 09-10. **Thesis re-checked today and INTACT.** The name fell 2.05% on a tape down 0.38% — roughly 5× the index — and the driver is identified, not inferred: Airbnb announced late Monday a **$250M initial housing investment** intended to unlock $5B+ of new-housing capital over ten years. That is a capital-allocation item, not a demand or regulatory shock; the market took it mildly negative because it is discretionary spend with no near-term revenue. It arguably *addresses* the largest structural threat to short-term rentals (municipal supply politics) rather than revealing a new one. Analyst posture is unchanged and far above spot: FactSet mean PT **$183.24**, average rating overweight, with Gordon Haskett to $180 (09-11) and Baird to $200 (09-08). Full write-up: `_ABNB_2PCT_IDIOSYNCRATIC_DECLINE_HAS_A_NAMED_DRIVER_AND_IT_IS_NOT_A_THESIS_BREAK_2026-09-15`.

**UNP — why we own it:** same RSI(2) mean-reversion entry, 09-10, essentially flat at −0.16%. No news, no thesis event, nothing to re-argue.

**Neither is close to any exit**, and it is worth being precise about which leg binds:

- **Take-profit (RSI2 ≥ 70 while green):** unavailable on both, on *two* independent legs. The signal is unmet — RSI2 re-derived Wilder off our own daily bars including the live print is **ABNB 19.87 / UNP 30.50**, not inherited from an earlier run — and both names are **red**, so the profit-banking authority does not exist regardless of the print. An RSI2 cross on an underwater position is an optional exit-into-strength routed to thesis, never a mechanical loss-realization.
- **Time stop:** 5 days held of 14. The 09-24 date is nine sessions out, well outside the 3-day warn window.
- **Target:** ABNB needs +9.03% to 183.08, UNP +4.81% to 298.32.
- **Green-enough (native trail):** ABNB would need 199.44, UNP 335.42. Not close.
- **No price stops**, per HARD RULE 5. Both are bounded by the 09-24 time stop, which is the only mechanical loss discipline this book has.

### Options book — agentic: EMPTY. Ryan's own: 2 positions.

| Contract | Qty | Basis | Mark (19:17Z) | P/L | Owner |
|---|---|---|---|---|---|
| SPY 2026-09-17 **731P** | 1 | $28.00 | 0.265 (0.26×0.27) | −$1.50 | **user** |
| SPY 2026-09-17 **770C** | 1 | $27.00 | 0.255 (0.25×0.26) | −$1.50 | **user** |

Ryan opened these himself in the app at **18:43:44Z and 18:44:39Z**, 55 seconds apart, while the desk's options book was empty. The 18:45Z run's broker reconciliation caught them two and three minutes after the fills, synced the ledger, applied the ownership gate and **notified him once**. Combined they are a **long strangle** on the FOMC gap — two separate broker positions, not a spread, each closable alone.

**The desk will not touch these.** Ownership gate: `placed_agent="user"` means never close, trim or roll without his explicit go-ahead. It may detect a fired exit condition, record it, notify once, and wait — and that notification is already discharged, so the −$3.00 re-mark since 18:46Z does **not** earn a second one. They also consume none of the agentic book's budget, none of its 3 CORE slots, and none of its daily entry throttle.

**What the greeks say, surfaced because it is worth him knowing and not because the desk is recommending anything:** combined stated theta is roughly **−$62/day against $55.00 of total premium** at 2 DTE. Read it as the linearization it is — theta cannot literally take an option below zero — but the direction is honest: absent a real gap, these are worth close to nothing by Thursday. Breakevens are 730.70 (−3.49%) and 770.26 (+1.74%); the broker's own `chance_of_profit_long` reads 0.042 and 0.064. That is a pure binary bet on tomorrow's decision, which is a coherent thing to own and is priced as exactly that. **Mechanical deadline to be aware of: `sellout_datetime` on both is 2026-09-17T19:45Z.**

---

## 3. Actions taken today

| Time | Action | Reasoning |
|---|---|---|
| 13:33Z | Heartbeat stamped, market brief rebuilt, options loss cap + both entry throttles reset | First post-bell run of the trading day owns these. Correct to reset here and only here — the UTC-rollover rule bars any post-close/pre-open run from rolling a daily artifact. |
| 13:35Z | **DAY TRACK paper entry** (short, PSQ, 56 sh) | Mechanical. OR body 70.3% of range cleared the doji filter; direction short; late-entry gate passed. No judgment applied by design — this track is executed, not judged. |
| 13:47Z | **DAY TRACK paper exit**, stop reached, −1.00R | `day_track.manage()` returned `close`. QQQ's 13:38 bar high 709.10 breached the 708.855 stop. Day complete; one trade per day, no re-entry. |
| 18:45Z | **Ledger drift found and repaired** — Ryan's two SPY contracts synced, ownership gate applied, **one** notification sent | Broker-first reconciliation caught fills the ledger had no way to know about. Not a HARD RULE 9 incident in either direction: an unauthorized trade is an *agentic* order nobody approved; this is the account owner trading his own account. Nothing adjudicated. |

**No order was placed by the desk in any book today.** Agentic throttles: **equities 0 of 3**, **options 0 of 3** (v11 structural limit; the ledger object's legacy "0 of 8" string refers to the retired dual-track budget).

---

## 4. Candidates considered and skipped

### Equities — the 19:06Z board, 11 RSI(2) names, zero A-grades

The report's fresh 19:06Z board carries LRCX, WMB, AMAT, NBIS, GS, FCX, MS, MU, PFE, IWM, AEHR. **Every one of these was already graded earlier today or on 09-14**, and the board has *shrunk* rather than grown — RTX, BAC, JPM and NEM dropped off since 15:02Z. **Ungraded delta: zero.** (This check is not a formality; `_THE_UNGRADED_DELTA_RETURNED_ON_A_BOARD_FOUR_RUNS_HAD_DECLARED_CLOSED_2026-09-10` exists because a board once re-opened after four runs called it closed.)

| Name | Grade | Why it gets nothing |
|---|---|---|
| **AMAT** | B | Semis complex — inherits the AI-governance sentiment-shock de-rating (Amodei's "Pace the Frontier" essay, bid rotated to cybersecurity). Best name on today's board and still not A. |
| **LRCX** | B− | Same semis veto, weaker on the stack than AMAT. |
| **AEHR** | C | Semis veto plus two name-specific defects: the report's own suggested stop is −16.5% wide with the volatility warning, and under HARD RULE 5 this book carries no stop at all. |
| **NBIS** | C | AI-adjacent, extended above its 200-day, speculative sleeve. |
| **MU** | **EXCLUDED** | `[ERN 2026-09-30]` sits inside the 1–3 week hold window. Under the concentration policy this is an **absolute bar**, not the advisory flag it used to be — at up to 30% of the account with no price stop, one overnight gap through a print is a 4–5% account hit. |
| **WMB** | **EXCLUDED** | Ryan's standing sector steer: no new oil/gas-related energy entries. |
| **GS, MS** | C | Bank cohort, de-rating on BAC's investment-banking fee guidance, now in its third session. A live guidance event is not an indiscriminate sell-off, which is what a mean-reversion thesis needs. |
| **PFE** | C | Pharma cluster — live, targeted, unresolved regulatory repricing (MFN structure, CMS-finalized Medicare discounts effective Jan 2026). Targeted selling with further scheduled legs. |
| **FCX** | B− | Rate-levered into tomorrow's decision; same objection as NEM below and it resolves at the same instant. |
| **IWM** | — | Index ETF. An index on the RSI2 screen carries no idiosyncratic information — it is the market, which is what the screen is supposed to be selecting *against*. |

**NEM is the one worth flagging even though it fell off the board.** Graded **B** at 16:02Z — the best setup the desk saw today. FactSet mean PT $136.82 vs spot $122.11 (+12.0%), consensus overweight, and **Goldman raised its PT to $127.50 this morning while the stock was falling**. Its single binding objection is dated and it is tomorrow: gold miners are the asset class most directly levered to the rate decision, with a 25bp hike priced at ~85.6%. And the tape diverged — NEM −0.78% while GLD was **+0.14% green** at the same minute, so this is the miner de-rating on its own leverage, not "gold dipped and the miner came with it." **Re-grade NEM first after the decision, from scratch, on post-event prices.** That is a reopening condition on a declined candidate, not a reason to hold cash, and a gap-up is not a gift to a mean-reversion setup.

**The decline was on GRADE, not on cash** — this distinction matters and runs keep getting it backwards. Capital was fully available: $708.14 per slot against a ~$600 minimum and a $1,159.43 per-name cap, with a genuine open slot (2 held vs the 3–4 target), not an optional fourth. **A B-grade gets no position, not a small one.** Concentration does not raise expected return — 4×$900 and 8×$450 have identical expectancy and the concentrated book has strictly more variance. It only pays if the top ideas are genuinely better, so fewer must mean *more selective*, never merely bigger.

### Options — no CORE entry, 0 of 3 open

TACTICAL is retired (2026-09-14), so there is one track. No CORE entry today, for reasons that are about vol rather than about any particular name: **index premium is rich into the event** (SPY raw IV/RV 1.3478, ex-gap 1.7086), which puts long premium on the wrong side of the volatility. The board's own candidates route either to earnings binaries (MU 09-30) or to chains untradeable at this account size. **FOMC is a macro event, so under the narrowed catalyst bar it is a sizing input, not a bar** — it is not what stopped an entry; the absence of a setup worth owning at these vol levels is.

No spread specs were handed to Ryan today.

---

## 5. Sleeve state

| | |
|---|---|
| Total account value | **$3,864.75** |
| Cash = buying power = **unleveraged** buying power | **$1,609.52** — identical, so no margin is extended and FOUR LAWS #4 is unambiguous |
| Equity value / options value | $2,202.23 / $53.00 |
| Operational reserve (5%, recomputed) | **$193.24** |
| **Deployable** | **$1,416.28** |
| Open equity slots | **2 of the 3–4 target** → $708.14 per slot, clears the ~$600 minimum |
| Per-name cap (30%) | $1,159.43 |
| Agentic premium at risk | **$0.00** — the agentic options book is empty |
| Realized options P/L today | **$0.00** against the −$400 cap (full headroom) |
| Realized equity P/L today | **$0.00** |
| Entries used | equities **0 of 3**, options **0 of 3** |

**The `_cash_hold` is live and expires tomorrow.** It names the 09-16 FOMC as its opportunity and dissolves automatically the moment the decision is released, or at the first run on or after 09-17, whichever comes first. **It is a disclosure with an expiry date, not a gate** — it did not bar an entry today and would not have barred an A-grade. On dissolution the capital returns to normal full deployment and the key is deleted, not renewed; an unattended run may not extend it.

**Calibration:** the weekly run for this week completed **2026-09-14** with **no change to either book**. Equities read a healthy +18.73 points of margin over the payoff-implied breakeven (66.67% actual vs 47.94% required, n=51, expectancy +$5.01) — but only **4 of those 51 closes happened under the current parameters**, so the in-regime gate blocked any adjustment, exactly as designed. Tuning a parameter on trades that predate it is superstition. Options read −4.44 points at n=18, below the 20-trade floor, so report-only. Next calibration: **Monday 2026-09-21**, which also runs `day_track.graduate()`.

---

## 6. Tomorrow's watchpoints

1. **FOMC decision, Wednesday 2026-09-16, 14:00 ET, with an SEP/dot-plot release.** A 25bp hike is priced at ~85.6%; the asymmetric surprise is a hold, or the dots. This single event resolves the binding objection on NEM, FCX, and the whole rate-sensitive half of the screen simultaneously.
2. **`_cash_hold` dissolves on that release.** The capital returns to unconditional deployment. No renewal is available to an unattended run.
3. **Re-grade NEM first, from scratch, on post-event prices.** Never re-use the pre-event B, and do not treat a gap-up as an improvement to a mean-reversion setup.
4. **Ryan's SPY strangle is the binary bet on this event.** Sellout deadline 2026-09-17T19:45Z. The desk will not act on it; it will keep marking it and will notify only if the recommendation itself changes.
5. **DAY TRACK paper day 2.** Fresh QQQ opening range at 09:30–09:35 ET. Still PAPER, still nine days and seven signals short of the graduation gate.
6. **Time stops: ABNB and UNP both fire 2026-09-24** if they have neither hit target nor printed a bounce — green or red. Nine sessions out.
7. **The PSQ stop-width problem** (2.79 ticks on a one-tick instrument) needs resolving before the DAY TRACK can go live, alongside the day-trade-vs-cash-hold capital collision. Both are Ryan's calls, both are recorded, neither is urgent while the track is in paper.

*Generated by the scheduled automation run 19:15Z 2026-09-15. Every figure sourced from the broker at 19:16–19:17Z or from the committed 19:06Z report; P&L is broker-sourced, never from the trade journal.*
