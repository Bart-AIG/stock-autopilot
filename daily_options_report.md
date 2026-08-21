# Daily Options Report — Friday, 2026-08-21

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written at 14:20 CT / 19:20 UTC by the first run at or past the 14:15 CT window, from live quotes timestamped 19:16:13Z. Not written post-close and not deferred to a tidier slot.*

**One-line summary: no agentic trades again today — the sixth straight flat day — and the book gave back $237.50 in mark-to-market while doing nothing. Realized agentic P/L: $0.00 against the −$400 cap. Two things need you, and both bind before or at Monday's open: the QQQ put crossed its 21-DTE review this morning and my recommendation is still sitting unanswered, and the book pays roughly $236 in theta across the three-day weekend with nothing long to offset it.**

---

## 1. What we own

| Contract | Placed by | Basis | Mark 19:16Z | P/L at mark | **What an exit actually nets (at bid)** | DTE | Status |
|---|---|---|---|---|---|---|---|
| SPY 2026-11-20 700P ×1 | agentic (hedge) | 7.49 | 6.515 | −$97.50 / −13.02% | −$99.00 (bid 6.50, 0.46% spread) | 91 | Working as designed |
| QQQ 2026-09-11 680P ×2 | 1 agentic + 1 yours (8/21 @3.56) | 3.805 blended | 3.575 | −$46.00 / −6.04% | −$51.00 (bid 3.55, 1.40% spread) | **21** | Stalled, setup intact |
| RBRK 2026-09-18 90P ×2 | 1 agentic + 1 yours (8/21 @4.30) | 4.10 blended | 4.400 | +$60.00 / +7.32% | **$0.00** (bid 4.10, 13.6% spread) | 28 | Stalled, leaning wrong |

**Book: basis $2,330 → mark value $2,246.50. Unrealized −$83.50 / −3.58%.**

**Why we own each one:**

- **SPY 700P** — insurance, not a trade. It executes your 2026-08-05 Aug–Oct drawdown-watch authorization and is explicitly exempt from every premium backstop; it is *supposed* to decay in a melt-up. The only decision it ever gets is a roll/close review with you around 2026-10-30 (~21 DTE). No action, today or any day before then.
- **QQQ 680P** — bearish QQQ tail. Break-even at expiry is QQQ 676.42, so it needs a further ~5.1% decline in 21 days. Invalidation is a QQQ *close* above ~730; spot is 713.11, so the setup is intact on its own terms.
- **RBRK 90P** — bearish RBRK ahead of its 2026-08-27 pm earnings print. Break-even 85.60, i.e. a ~13.7% decline in 28 days. The underlying has spent the week going the *other* way (99.24 today, +1.76%).

**On the RBRK "+$60": please read the bid column, not the mark.** The chain is 13.6% wide on 75 open interest and has traded 8 contracts all session. The $60 gain at mark is not collectable — sell into that bid and you net exactly zero. This is the same caveat the last four runs have flagged, and it hasn't improved.

---

## 2. Actions taken today

**None by the desk.** No entry, no exit, no roll, no modification. 0 of 8 daily entries used, 0 of 2 this run.

Three things did move in the account today, and none were agentic:

1. **You closed your ACHR 2028-01-21 5C** at 13:55:50Z, limit 3.00, +$52.94 / +21.4%. Verified on the order record (`placed_agent="user"`). Your gain, your trade — it doesn't touch the agentic loss cap, and the `manual_hold_override` that governed it retires with the position.
2. **You added a second QQQ 680P** @3.56 at 15:50Z and **a second RBRK 90P** @4.30 at 16:00Z. Both verified as yours on the order record. These raised the blended basis on both positions, which is why the P/L math above uses per-lot basis rather than a naive close-to-mark.
3. **The QQQ 680P hit its unconditional 21-DTE management review** at this morning's open. Under your 2026-08-18 monitoring mandate that is a recommend-and-ask, not an execute, so nothing was traded — you were notified once at 13:33Z with the full numbers and the recommendation. See §5; it is still open.

**One accounting note worth your attention.** Today's naive close-to-mark day P/L reads −$429.50, which looks like it breaches the −$400 daily cap. It doesn't, and it's wrong twice over: computed per-lot the real MTM day is **−$237.50**, because the two lots you added today get charged with a move they were never present for; and the cap governs *realized* losses and gates *new entries* only — it never blocks or delays an exit. Realized today: $0.00.

---

## 3. Candidates screened and skipped — the reasoning

Fifteen-plus scheduled runs worked the board today. Every candidate that cleared liquidity failed on thesis or timing; the two that cleared the tape were barred structurally.

**Track A (tactical scalp) — nothing triggered, all day.**

- **SPY / QQQ tactical, either direction — C.** Track A requires an intraday level *actually breaking now*. QQQ has spent three sessions pinned within 0.1% of its falling 50-day (713.05) — that is a pin, not a break. Between 17:24Z and 19:16Z every liquid name moved less than 0.1%: SPY 765.78→765.89, QQQ 713.47→713.11, NVDA 215.03→214.78. There was no level to trade.
- **NVDA bearish scalp — C.** The one genuine divergence on the board: NVDA −0.96% at 214.78 while QQQ is +0.31%, and the PHLX semi index is −5% on the week. Interesting, still not a setup — and NVDA reports **2026-08-26 pm**, inside any short-DTE hold window, which is an independent reason not to pre-position. An earnings bet is barred unless earnings *is* the thesis.
- **TSLA long calls — C.** +5.37% on robotaxi news, and it carried the index nearly alone. Declined on the trend-maturity gate: a +5% day stalling *under* a falling 50-day (366.23) with spot well above VWAP is a move that has already happened. This is the ZTS mistake and the desk has now made it once.
- **Any tactical entry in the final 40 minutes — declined on structure, not on the tape.** A Track A scalp carries a hard time stop of flat-by-next-session's-close. Opened at 14:20 CT on a Friday, that means paying three days of weekend carry on a position whose entire edge is intraday delta. The vehicle and the calendar are simply mismatched; that is a reason to not trade, not a reason to widen the rules.

**Track B (core swing) — one real candidate, and it was a trap.**

- **INTC — B, and the most educational skip of the day.** The committed equity report put it at the top of its RSI2 board (RSI2 3.6, spot 90.44, screened as oversold inside a rising 200-day uptrend), and INTC is one of the few names certified as having a genuinely tradeable chain at this account size. The chain checked out — the 2026-09-18 100C is 1.42% of mid on 43,359 OI, passing even the stricter tactical gate. Structures were priced properly: single-leg 90C $627.50 (theta −$11.17/day), 95C $422.50, versus the **90/100 vertical at $345.50 debit, max profit $654.50, net theta −$1.18/day** — a 9.5× carry reduction at 55% of the capital, and clearly the right structure had the thesis held. **It didn't.** The RSI2 print was manufactured by a $20B secondary offering — a supply event, not mean reversion. Separately, INTC is −36.6% off its June high and the screen's "rising 200-day" gate passed for the wrong reason on a name that has round-tripped.
- **MSFT — C, an IV trap.** Headline IV/RV 0.525 reads like half-price vol. It isn't: that is the +14.42% 07-30 earnings gap sitting inside the realized window. Ex-gap the ratio is 1.008 — priced fair. Cheap-looking premium is not a setup.
- **AVGO — C.** Richest premium on the core list (IV/RV 1.17 raw, 1.41 ex-gap) and −15% in nine sessions. A put here chases a move that already ran, into a green tape.
- **CRWD (RSI2 0.9), KLAC / TXN / TSEM (RSI2 4.3 / 6.4 / 5.6), BE / BAC / GD / DDOG — C.** Report signals with either no tradeable chain at this size or no "why now."
- **A third bearish-tech expression — BARRED, and correctly.** The short-tech theme sits at 2 of 3 and, more to the point, the book was measured at **10.7× the account in one-way short delta notional (−$41,229)**. A fourth bearish position has to clear a materially higher bar than a neutral or long one. Equally — and this cuts both ways — that measurement is not itself a reason to buy calls. Trading to fix a concentration number is the same error as trading out of boredom.
- **Adding to QQQ or RBRK — barred by FOUR LAWS #3.** Both are underwater or flat; adding to a loser needs your explicit approval and a very good reason.

---

## 4. Sleeve state

| | |
|---|---|
| Open positions | 3 → **0 of 2 TACTICAL**, **2 of 3 CORE** (SPY hedge excluded) |
| Correlated theme | Bearish tech **2 of 3** |
| Premium at risk | **$2,330** ($749 hedge exempt + $761 QQQ + $820 RBRK) |
| Unleveraged buying power | **$1,156.87** — equals `buying_power`, so **no margin extended** |
| Deployable after $250 reserve | **$906.87** |
| Realized P/L today (agentic) | **$0.00** vs the −$400 cap |
| Entries used | **0 of 8** |
| Account value | $3,847.89 — clear of the $2,000 margin-equity minimum |

**The number I'd most want you to see: weekend carry ≈ $236.** Theta across the three-day weekend runs about $131 on the QQQ pair, $78 on RBRK, $27 on the SPY hedge. The book is 100% one-directional short with nothing long to offset it, so that bleed is unhedged and it is paid whether or not the market opens lower Monday.

---

## 5. The decision that's still with you — QQQ 680P

This crossed its **unconditional 21-DTE management review** at this morning's open and I flagged it to you at 13:33Z. It hasn't been re-sent since, deliberately — the recommendation hasn't changed and the mandate says don't page you twice for the same thing. But today was the last session before the weekend, so here are the current numbers.

The exit engine's rule is plain: *a position flat or losing at 21 DTE is closed or rolled, never held into the accelerating theta/gamma window.* It is losing (−$51 net at the bid) and Monday it is 20 DTE — inside that window, with $131 of weekend carry already paid to get there.

**Three options, honestly stated:**

1. **Close both lots** at/near mid (3.575). Nets about −$51. Ends the carry, frees ~$710 of buying power, and takes the book from 10.7× one-way short to roughly 4.5×.
2. **Convert to the 680/660 vertical** — sell the 2026-09-11 660P against the held 680Ps. This was measured on your own position: **theta from −$23.88/day to −$5.67/day (−76%), capital at risk from $405 to $179 per lot.** It keeps the bearish view alive at a quarter of the bleed, and caps the payoff at the 660 strike. This is what level 3 is for, and it is my recommendation if you still want the exposure.
3. **Hold as-is.** Defensible only if you think QQQ breaks down in the next fortnight — it needs a further ~5.1% to break even. The setup *is* still technically intact (invalidation is a close above 730; spot 713.11). But you would be paying full single-leg theta for a view that option 2 expresses far more cheaply.

**My recommendation: option 2 — roll it into the vertical.** It respects the 21-DTE rule without abandoning a thesis that hasn't actually been invalidated, and it cuts the carry that is doing most of the damage. Option 1 is the clean, no-argument choice if you'd rather just be flat. I will not act on either without your go-ahead; the mandate is yours to call.

---

## 6. Monday's watchpoints

- **QQQ 680P → 20 DTE at Monday's open**, inside the accelerating-theta window. The §5 decision binds here.
- **NVDA earnings Wed 2026-08-26 pm.** The whole semi complex is positioning around it — PHLX semis −5% on the week. This suppresses any short-DTE directional entry in semis until it clears, in either direction.
- **RBRK earnings Thu 2026-08-27 pm — hard deadline Wed 2026-08-26 close.** Default is to close before the print unless earnings becomes the thesis. That decision must be brought to you by Wednesday; it cannot be allowed to expire into the print by default.
- **QQQ 713.05 (falling 50-day).** Pinned within 0.1% for three sessions. A decisive break either way is the first genuine Track A trigger the board has offered all week.
- **SPY hedge:** nothing until the ~2026-10-30 roll review. 91 DTE.

*Honest limit, restated: this is a scheduled cadence during market hours only — roughly every 15 minutes since the trigger was repaired at 17:05Z today. An intraday spike can round-trip entirely between two runs, and nothing is monitored overnight or across the weekend.*
