# Daily Report — Wednesday, 2026-08-26 — **BOTH BOOKS**

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written at 16:20 ET / 21:20 UTC by the first post-close run, under the fallback clause — the bell rang with no report written, so this one was written immediately rather than deferred. Regular-session quotes stamped 20:14:59Z; after-hours prints are labelled as such and are never used to value a position.*

**One-line summary: two firsts and a flat book. The equity sleeve became autonomous at 18:15Z and its very first decision was to *decline its own trigger*; the legging protocol was proven end-to-end by fills in a Ryan-authorized live test for $16. Scheduled runs placed nothing in either book across twenty-eight firings — correctly, because the entire session was a pre-event vacuum in front of NVDA. NVDA has now reported: EPS $2.22 vs $2.09 estimated, a 6.2% beat, and the stock is +3.9% after hours. Everything the desk deferred today re-prices tomorrow morning.**

---

## 1. What we own

| Position | Book | Placed by | Basis | Close 2026-08-26 | P/L | What an exit nets | Status |
|---|---|---|---|---|---|---|---|
| SPY 2026-11-20 700P ×1 | options (hedge) | agentic | 7.49 / $749.00 | mark **5.805** | **−$168.50 / −22.50%** | −$171.00 at the 5.78 bid (spread 0.86% of mid) | Working as designed |
| PNC 1.825758 sh | equity (swing) | agentic | 246.4729 / $450.01 | **244.71** (+0.25% on the day) | **−$3.22 / −0.72%** | n/a — held on thesis | Hold, 4.4% from target |

**Book value on regular-session closes: options $580.50 + equity $446.79 + cash $3,007.26 = $4,034.55.**

**Why we own the SPY put.** This is the authorized Aug–Oct drawdown hedge — insurance, not a directional bet, and explicitly exempt from every premium backstop. It lost $29.50 today (prior close 6.10 → 5.805) in a tape that closed slightly green, which is exactly what a 0.14-delta, 86-DTE put is supposed to do when nothing breaks. Greeks at the close: delta −0.1449, theta **−$8.73/day**, IV 20.17%, OI 26,354, volume 2,175. Its one decision point is the ~21-DTE roll/close conversation with you around 2026-10-30. **No action, and none contemplated.** The honest read on the drawdown: it is now −22.5%, deeper than the −17% two sessions ago, and that is carry plus a market that has not obliged — not thesis deterioration. A hedge looks like this right up until the day it doesn't.

**Why we own PNC.** RSI2 oversold swing entry from 2026-08-19: Q2 beat, dividend raised +18%, an active 300-branch expansion, JPMorgan PT $269.50. Target 255.50. Per HARD RULE 5 it carries **no price stop** — it is thesis-managed until it is green enough (**$289.97**, i.e. entry ÷ 0.85) to earn your native 15% trail in the app. Seven sessions in, it is 0.7% underwater and 4.4% below target. Thesis re-read today: **INTACT.**

> ⚠️ **One number to disregard.** Your app and `get_portfolio` currently show the equity book at $440.25, not $446.79. That is a single thin after-hours PNC print at 241.13 on a **240.00 / 247.30 market — a $7.30-wide quote**. It is noise, not a −1.5% move. The regular-session close of 244.71 is the real number, and every figure in this report uses it.

---

## 2. Actions taken today

### Scheduled runs: **NONE.** Zero orders, both books, across twenty-eight firings.

That is the output, and it was a decision each time rather than an absence of one. The reasons are in §3.

### The one thing that did trade: the legging capability test — **yours, not the automation's**

Between 16:54Z and 17:26Z, an **interactive session with you present** ran a live end-to-end test of whether this account can build a debit vertical by legging. This is recorded here because it is the trading day's only fills and it moved real money — it was **not** an autonomous action, and the automation claims no credit for it.

**Total cost: −$16.00 across 3 closing trades.** What that $16 bought:

- **Cycle 1 (aborted, −$13.00).** Legged with limits resting at mid. The short leg never filled while the market fell away; the filled long bled $13 in seven minutes and the position was aborted by selling the long back. This is the whole argument against mid-resting between legs, priced.
- **Cycle 2 (complete round trip, −$3.00).** Both legs crossed at the touch, 31 seconds apart. Spread on at **$58 net debit**, margined as a vertical; legged back out at **$55 net**. In and out for $3 plus $0.32 of fees.

**What it proved, and it is worth more than $16:**

1. **Legging works when the long leg is held first.** With the long in hand, the short leg reviews at **$0 collateral** — the broker pairs them and margins the pair as a debit spread. The desk had spent two days believing this was arithmetically impossible, on the strength of a test that had reviewed a short leg with *no long held*, which is a different question entirely.
2. **The only executable exit is short-leg-first**, and the broker enforces it: selling the long first raises a collateral demand for the naked short that would remain.
3. **Single-ticket multi-leg orders still 400 out** — opening *and* closing — and `review_option_order` still returns a clean, healthy-looking preview of an order that cannot be placed. A clean multi-leg review remains worthless as evidence.
4. **Cross the touch, never rest at mid.** Cycle 1 cost $13 in seven minutes without ever holding the position; cycle 2 crossed both spreads and the entire round trip cost $3. On a penny-wide chain the half-spread is an order of magnitude cheaper than inter-leg drift.

No spread specs were handed to you today for in-app placement — nothing cleared the entry bar to spec.

---

## 3. Actions considered and skipped — the educational section

### Options — TACTICAL track: **five level-breaks fired, five declined, zero taken**

Today was the end of a two-session arc in which the desk kept tuning its confirmation filter after each failed break. The 16:37Z SPY break settled it, and the finding is the most useful thing the options sleeve produced today:

**That break satisfied every correction the desk had spent two sessions writing.** The level was genuinely structural — the session low at 764.680 sat 0.12 points from the 20-day SMA at 764.7985, not a box drawn around recent bars. The clause was freshly re-derived rather than quoted from an earlier run. The volume confirmed against *every* denominator, including the inflated first hour: 160,261 shares = **200.8%** of the trailing-30-minute baseline, 149.7% of the post-first-hour mean, 102.3% of the first hour itself. Price broke on a completed close and held for eight consecutive one-minute closes.

**It failed completely in 23 minutes.** By 17:00Z SPY had reclaimed the 20-day and printed four straight closes above it, finishing *above where the break started*.

> **The conclusion, now a written rule: do not open TACTICAL breakout scalps into an unresolved scheduled catalyst, however clean the fire.** When successive fixes to an instrument leave the result unchanged, the instrument was never the problem. Into a scheduled event, de-risking flow is real volume arriving at a level — so the volume clause fires honestly and means nothing, because nobody expresses a directional view before the number. Five failed breaks in two sessions, each on a *better* setup than the last, is the regime talking, not the filter.

A second, quieter check: the 16:45Z run declined that same break on **target arithmetic** — the +20% profit target needed roughly 95% of the entire session's range. Measured 36 minutes later, the vehicle it had priced (SPY 09-04 762P at 4.845) was at 4.300, **−11.25%**, more than a third of the way to its −30% stop, with delta drifted out of the tactical 0.40–0.60 band. Right for a stated reason, vindicated by a different one — worth auditing, because the arithmetic gate caught what the regime gate had not yet been written to catch.

### Options — CORE track: **barred, and independently declined on IV**

Every 21–45 DTE board opened today spans tonight's NVDA print — plus MRVL (08-27), DELL (09-01) and AVGO (09-02) behind it. The exit engine says *close* before earnings, not *open* into them.

It also failed on vol, on the honest reading. All eight core names were screened on the **ex-gap** IV/RV ratio, which strips the single earnings gap that makes implied vol look artificially cheap after a print:

| Name | Raw IV/RV | **Ex-gap IV/RV** | Read |
|---|---|---|---|
| QQQ | 0.9027 | **1.1697** | Looks cheap, isn't |
| SPY | 1.0378 | **1.2324** | Rich |
| NVDA | 1.1560 | **1.3209** | Highest on record for NVDA (n=12) |
| AMD | — | **0.8685** | Only genuinely cheap name of the eight |

AMD was the one name whose premium was actually inexpensive, **and it was declined anyway** — cheap vol is not a thesis, and there was no setup attached to it. NVDA itself was the clearest skip of the day: its ATM IV rose for a **fifth consecutive session** (0.4032 → 0.4042 → 0.4093 → 0.4108 → 0.4144) *while spot fell*, which is event premium accumulating, not directional repricing. Buying NVDA premium today meant paying the richest relative level in the entire history file, hours before the mechanical crush.

### Equities — the book's first live session: **six signals, six declines**

All six RSI2 swing setups in the 18:02Z report were graded. **The cash floor was not the constraint and it is worth saying so plainly**, because a run that declines everything can look frozen by a limit: the equity book sat at **87.0% cash**, leaving **$1,452 of compliant room** against a per-name cap of $609–812. A $400–800 A-grade entry was fully fundable. Every decline is on the merits.

| Name | Grade | Why not |
|---|---|---|
| **XOM** | *excluded* | Integrated oil major — your 2026-06-17 sector steer. RSI2 4.5 with the tightest stop on the board at −3.7%; it would have been the most interesting risk profile of the six, **which is exactly why the steer is worth honouring instead of rationalizing around.** Reply to override. |
| **LLY** | C — skip | **Thesis weakened on a same-day catalyst.** −3.18% today. Researched, not inferred: management disclosed the Q2 outperformance was aided by *non-recurring* U.S. rebate and discount adjustments, raising concern over H2 deceleration and margin compression. The RSI2 6.9 print is *produced by* the bad news, not an oversold dip inside an uptrend. Separately, 1 share = $1,194 = 29.4% of the account, so it could only be held fractionally — and a fractional position cannot carry your native trail. |
| **KHC** | C — skip | Not A-grade, which is the bar the defensive posture sets. Q2 beat and the organic-sales outlook was raised, but $100M was added to the investment plan (~$700M incremental spend) against a continuing sales slide, and the Street is uniformly capped (JPMorgan initiated Neutral, $27 PT, 08-20). Bull case reduces to a 5.78% dividend and a low multiple — a value-trap profile. **Declined on grade, not on a break: a legitimate future candidate.** |
| **AMAT** | B — **defer one session** | The cleanest setup of the six: RSI2 3.1, top-decile momentum, above a rising 200MA, 13.9% below its 50-day. Disqualified by the calendar, which was *checked* rather than assumed — NVDA tonight, MRVL 08-27, DELL 09-01, AVGO 09-02. AMAT is direct NVDA-complex beta and would carry **no stop**, so nothing protects an overnight gap. |
| **INTC** | B — **defer one session** | The strongest deferral. RSI2 9.0, mom12-1 of 342.9% (5th in the entire universe), above the 200MA, 17.5% below its 50-day — the deepest pullback of the three semis inside an intact uptrend. Own-earnings check clean (absent from the 21-day calendar). Its disqualifiers were the event and the tape, **and both resolved tonight.** |
| **AEHR** | C — skip outright | RSI2 2.1 is the most oversold print on the board, but the stock fell **4.32% today** on top of a −23.7% estimated stop width carrying the report's own extreme-volatility warning. A $91 small cap down 4.3% into the sector's largest print of the quarter is a falling knife, not a dip. |

**The cluster check binds on top of all of it:** three of the six (AEHR, AMAT, INTC) are the same AI/tech complex. Even with no event risk, at most *one* was takeable — buying several is one leveraged AI bet wearing a diversification costume.

### And the decision that defines the new authority: **PNC's exit trigger fired and was not taken**

`report.py` fired `EXIT-INTO-STRENGTH` on PNC at RSI2 78.5. Read literally, the v8 mechanical-exit clause — *"a target hit or RSI2≥70 swing bounce = bank it autonomously"* — was satisfied. The automation declined.

**Why:** at 18:16Z PNC was 245.635, up 0.62% on the day but still **$1.53 below the 246.4729 entry**. That trigger is a **take-profit authority, not a licence to realize a loss on a technical bounce.** Three independent sources agree: HARD RULE 5 defines it as a take-profit and states that a winner "can then only ever be sold for a locked-in gain"; `report.py` labels this exact case *"optional — policy default is hold-on-thesis"*; and the prior instance's written exit plan is target 255.50, no stop, thesis-managed. The thesis is intact, the trade is seven sessions old and working off its lows.

> **The rule this draws, now written to the ledger for promotion: gate the mechanical equity exit on `price > entry`.** A trigger that banks profits must never be allowed to realize losses because the wording happened to fit. The first day of a new authority spent declining to use it is the correct output — the bar does not fall because the desk just got a new tool.

---

## 4. Sleeve and book state

**Options**
- Premium at risk: **$749.00**, all of it the exempt hedge. Zero in TACTICAL, zero in CORE.
- Open agentic positions: **1 of 5** — and the one is the excluded hedge, so **all five slots are free** (2 tactical / 3 core).
- Realized P/L today: **−$16.00** against the −$400 cap → **$384 of headroom, not binding.** All of it from the authorized capability test.
- Entry throttle: **3 of 8** used, every one an interactive-session test entry. **Scheduled runs used 0.**

**Equities**
- Positions: 1 (PNC). Entries used: **0 of 1 this run, 0 of 3 today.**
- **Cash floor: 87.0%** — cash $3,007.26 ÷ (cash + equity $446.79). The posture requires ≥45%. Max compliant buy **$1,452.94**; per-name cap $605–807.
- Speculative sleeve: **0%** against the ~25% cap.

**Capital, both books**
- `unleveraged_buying_power` **$3,007.26 == buying_power** → **no margin extended**, as required.
- Deployable after the $250 reserve: **$2,757.26.**
- Account equity ~2× the $2,000 margin-equity minimum.
- Reconciliation: **zero drift.** One option contract, one equity position, all `pending_*` fields at 0.0000 — no overnight assignment, expiration or unauthorized fill. Lot invariants asserted in code and passed.

**Governance:** no open violation flags. The 17:00Z unauthorized-legged-spread flag was raised correctly by a scheduled run that could not see the interactive session, and was cleared by that session under HARD RULE 9(a) — by the session that placed the orders, on your live turns. This run touched neither the flag nor its resolution.

---

## 5. Tomorrow's watchpoints

**1. NVDA reported, and it beat.** FY2027 Q2 EPS **$2.22 actual vs $2.09 estimated — a 6.2% beat**, broker-verified. After hours the stock is **218.15, +3.90%** on the 209.95 close. QQQ 715.89 (+0.65%), SPY 769.48 (+0.46%). *After-hours prints are indicative only and routinely give back.*

**2. The two deferrals come straight back onto the board — and this is the honest part.** INTC and AMAT were deferred purely because of tonight's print, and tonight's print went their way: INTC 88.95 after hours (+0.78%), AMAT 485.85 (+1.31%). **A gap-up is not a gift to a mean-reversion setup — it can just as easily consume the edge.** Both must be re-graded from scratch on tomorrow's numbers: an RSI2 dip that gaps up 1–2% overnight may no longer be oversold, and the entry that looked good at 478 is a different trade at 486. Re-price, don't re-use.

**3. A pre-registered prediction settles.** The desk logged, in advance, that NVDA's IV/RV ratios (1.1560 raw / 1.3209 ex-gap — the highest on record at n=12) would collapse once the event passed. Tomorrow's `iv_history.json` row measures that against reality. Predictions written down before the fact are the only ones worth anything.

**4. The event bar lifts, but only partially.** The rule barring breakout scalps into an unresolved catalyst is satisfied for NVDA — but **MRVL reports tomorrow evening (08-27), DELL 09-01, AVGO 09-02.** The semi complex is not clear yet, and a CORE swing opened tomorrow still spans two of those.

**5. Everything that was scarce today was still scarce for the right reason.** Five free option slots, $2,757 deployable, an untouched loss cap, $1,452 of equity-floor room. **Capital has not been the constraint for weeks — setups have.** If tomorrow's tape hands the desk a genuine A-grade entry, nothing is in the way of taking it at size.

---

*Committing this file to master IS the delivery. Both books, one report, per prompt v8.*
