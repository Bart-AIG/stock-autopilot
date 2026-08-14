# Daily Options Report — Thursday, 2026-08-13

*Agentic account (cash, ••••7339). Written on the last scheduled run of the trading day (19:25 UTC / 14:25 CT). Plain-language by design — the point is that you can see **how** each decision was made, not just what it was.*

**One-line summary: no trades today. Both positions held on their own standing rules, and the one setup with a live thesis (Intel) tagged its trigger nine separate times and never closed above it. The sleeve ends the day exactly where it started — $749 of authorized hedge premium, zero discretionary risk, and every dollar of buying power intact.**

---

## 1. Positions we own

| Contract | Placed by | Entry | Mark now | P/L | DTE | Status |
|---|---|---|---|---|---|---|
| SPY 2026-11-20 700 PUT ×1 | agentic | $7.49 ($749) | $6.25 | **−$124.00 (−16.6%)** | 99 | HOLD — insurance, exempt from stops |
| ACHR 2028-01-21 5 CALL ×1 | **you** | $2.47 ($247) | $3.625 | **+$115.50 (+46.8%)** | 526 | NO ACTION — your trade, hands off |

**Why we own the SPY put, and why the loss is not a problem.** This is the defensive hedge you authorized on Aug 5 for the Aug–Oct drawdown watch. The 700 strike sits just below the July-low shelf (716.6) and the rising 200-day MA (702), so it only pays off on a genuine break of trend — it is deliberately *not* insurance against an ordinary dip.

Today SPY closed in on a fresh all-time high at 778.35 (+0.76%). That is precisely the tape in which this position is *supposed* to lose money. Here's the mechanic worth understanding: the put's delta is **−0.136**, meaning it gains about $13.60 for every $1 SPY falls and loses about the same when SPY rises. SPY rose ~$5.85 today, so the mark drifting from $6.27 to $6.25 is the option doing exactly what the math says it must. **That bleed is the premium being paid for protection, not evidence of a broken trade** — which is why the rules explicitly exempt this position from the −50%/−70% premium backstops that would force a sale on any other losing option.

Two things say hold, not act: neither condition that would invalidate the hedge has been met (SPY is not decisively above ~800, and you haven't lifted the Aug–Oct posture), and time decay is running at only **−$0.084/day** against 99 days left — so there is no urgency. Its next real decision point is a roll-or-close conversation **with you** around **Oct 30** (~21 DTE).

**Why we own the ACHR call.** You bought this Jan-2028 LEAP yourself on Jul 20 and told me on Jul 22 to leave it alone, so the automation only ever *watches* it. It's up +46.8% and healthy. It does not count against the sleeve's $1,500 budget, because that budget governs only trades the automation places itself.

*One clarification, so it never gets misread:* earlier runs today flagged that ACHR was brushing +49.8%, just under the +50% level where a profit-protection ratchet would normally arm. It has since eased back to +46.8%, so the question is moot — but the principle matters more than the number. **That ratchet applies only to positions the automation opened.** On your contract, crossing +50% is information, not a trigger. Nothing would have happened either way.

---

## 2. Actions taken today

**None. Zero orders placed, zero fills, $0 realized.**

That is the whole list, and it deserves a sentence rather than an apology: across 28 runs the automation found no setup that cleared its own bar. The sleeve's edge at a 15-minute cadence is patience — being flat is a position, and it was the correct one today.

*Separately, for context on the cash line:* **you** closed the IREN equity position yourself this morning — your GTC stop at $45.16 filled 11 shares at $45.305, and you market-sold the 0.81-share remainder at $45.29, banking **+$27.33 (+5.4%)**. The automation neither placed nor influenced that (equities are never traded autonomously); it only reconciled the ledger afterward. Those **$535.05 of proceeds are unsettled until tomorrow (T+1)** and were excluded from every affordability check today.

---

## 3. Actions considered and skipped — the educational part

**INTC — the one that came closest, declined 26 times today. Grade B, conviction 4/10 against a 7/10 gate.**

The thesis here is good and it is *still* good: Intel is a top-decile 12-month momentum name, the $20B upsized share offering at $95.00 closed Aug 12 so the overhang that was capping it is confirmed gone, its options are genuinely cheap (implied volatility is running *below* realized volatility, ratio 0.84 — which is exactly when buying a plain long call is the right structure rather than a spread), and the September monthly chain is deeply liquid (44,946 open interest, ~3.4% spread).

**What was missing all day was the entry price — only that.** The written trigger was a decisive *close* above $105.45, the July 21 swing high. Here is the day, in one line of prices: Intel opened strong, ran to **$106.87** at 15:31 UTC, and then tagged and failed the $105.45 level **nine separate times**, finishing the session at **$104.66 — $0.79 below the trigger and $2.21 off the high.**

That pattern is itself the lesson. Through the first few tags, the chop was neutral information — a close-based trigger exists precisely to filter intraday noise. But nine rejections followed by a fade into the bell is **the level working as resistance**, which is evidence *about* the setup, not merely the absence of evidence. So conviction was cut from 6/10 to 4/10 during the afternoon.

A second, entirely independent reason to stand down: **AMAT reports earnings tonight after the close.** Applied Materials is the semiconductor-equipment bellwether, and its guidance reads directly through to Intel's foundry spending. Any 21–45 day call bought today is by construction an overnight hold through a coin-flip event that forms no part of our thesis. Even a perfect technical trigger would not have justified taking that binary.

And the honesty test — *would I approve this if you asked, purely on the account's interest?* — fails on its own: buying something up 3.7% on the day, right under a level that has rejected it nine times, after seven sessions of waiting, is chasing. Chasing is not a catalyst.

**Four named setups were screened and killed on structure — worth seeing, because each failed for a different reason:**

- **ROST** (surfaced by the equity report on a deeply oversold RSI(2) print of 1.9, inside a genuinely rising 200-day uptrend — the cleanest *trend* structure we've seen in six sessions). Killed on three counts: it reports earnings **Aug 20**, which is inside every tradable expiry given our 7-day DTE floor; its September chain is effectively dead (12.8% bid-ask spread, **zero** open interest at the strike); and its implied volatility is inflated to 1.69× realized precisely *because* of that earnings event — meaning you'd be paying up for a binary you don't want. **Re-look after Aug 21**, when the print is behind it and the IV crush may flip it to cheap.
- **LIN** — the screen called it an oversold dip; reading the actual chart says otherwise. LIN gapped −6.6% on its July 31 earnings, bounced for a week, and has since rolled straight back over. That's a **failed recovery in a breakdown, not a dip in an uptrend** — the RSI reading was measuring the second leg down. Its chain seals it: 17% to 48% spreads.
- **ACGL** — cheap premium, but a $5-wide strike ladder producing 25.6% and 50.7% spreads. Paying half the premium in spread means the stock must move ~5% before you're even breakeven. Also: **we already own ACGL as an equity**, so a call would stack correlated exposure. Note for the future — that thin chain is a structural property of a low-beta insurer, not a passing condition, so ACGL is likely permanently untradable in this sleeve.
- **IREN** — gapped +12% intraday and was tempting. But no *new* dated catalyst was behind it (the move traces to July 20 contracts and an Aug 4 acquisition close, both long since priced), its 200-day MA is *falling* — making a reclaim the falling-knife case, not the uptrend case — and the chain printed 14.5–20.6% spreads. **Cheap IV is never a thesis.**

**The recurring theme worth internalizing:** four of the five names died on **liquidity**, not on the idea. At this account size, a wide bid-ask is a tax charged on entry *and* exit; a 25% spread means the stock must move 25% just to get you back to flat. Wide markets are an automatic skip, without regret.

**Also skipped, documented in advance so no run re-litigated them:** AMAT (earnings tonight is not our thesis), CSCO (down 7% on a bad print — shorting a gap that has already fully repriced is late-entry chasing, the exact error the ZTS incident taught us), IWM (small caps lead when rate-cut odds rise, but "rates might fall" is a macro lean, not a dated catalyst — and going long index beta would fight our own SPY hedge).

---

## 4. Sleeve state

| Measure | Value |
|---|---|
| Agentic premium at risk | **$749** of the $1,500 budget (**$751 headroom**) |
| Open agentic positions | 1 (the hedge) — **0 of 3** non-hedge slots used |
| Realized options P/L today | **$0.00** vs the −$200 daily loss cap — not in play |
| Settled buying power | **$1,447.47** |
| Unsettled (IREN proceeds) | $535.05, settles **tomorrow, Aug 14** |
| Weekly circuit breaker | Not tripped |
| Approaching any exit trigger? | **No.** The SPY hedge's next decision is ~Oct 30 with you; ACHR is hands-off. |

**Market backdrop:** the second consecutive benign inflation print — July PPI came in **unchanged** month-over-month against a +0.2% consensus, following an in-line CPI. SPY and QQQ both closed at fresh all-time highs; the VIX sits near its 2026 low around 15.4. Your defensive tripwire — a *closing* break of SPY 746–748 — is roughly **31 points below** spot and was never threatened.

---

## 5. Tomorrow's watchpoints

1. **AMAT's print tonight** sets the tone for the whole semiconductor complex at tomorrow's open.
2. **INTC gets re-graded post-AMAT** — and deliberately **not** against today's $105.45 trigger as if nothing happened. Nine rejections make that level demonstrated resistance, so a reclaim now needs *more* confirmation, not less. A gap-up straight through it on AMAT enthusiasm is a chase, not a trigger. The clean entries remain a pullback into ~$97–100 that holds above the $95 offering price, or a confirmed hold of a reclaimed level. A close below $95 kills the setup outright.
3. **$535.05 settles tomorrow**, lifting settled buying power to roughly $1,982.
4. **Friday's final run carries the weekly review** — hit rate, average win vs average loss, best and worst *decision* judged on process rather than P&L, and a drift check on whether any standing preference is being overridden often enough that it should be formally rewritten.
5. **Retail earnings cluster Aug 18–20** (HD, WMT, TGT, TJX, ROST) — that whole group stays in an earnings blackout for this sleeve until it clears.
