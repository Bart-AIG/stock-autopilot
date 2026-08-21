# Daily Options Report — Friday, 2026-08-21

*Agentic account (limited margin, ••••7339). Written at 14:22 CT / 19:22 UTC by the first run past the report threshold, with ~38 minutes left in the session. Quotes are live as of 19:19–19:20Z, not closing prints.*

**One-line summary: you answered the QQQ question yourself — instead of closing the put the desk had been bringing you all day, you bought a second one at $3.56, and a second RBRK put at $4.30. The desk placed nothing, as it should have. Realized P/L today: +$53.00, all of it your ACHR LEAP sale. The book is now 100% one-way short at 10.8× account value, and the decision that actually binds next is RBRK, on Wednesday.**

---

## 1. What we own

| Contract | Placed by | Basis | Mark | P/L at mark | **Net at bid** | Spread | DTE |
|---|---|---|---|---|---|---|---|
| QQQ 2026-09-11 680P ×2 | lot 1 desk, **lot 2 you** | $761 ($3.805 avg) | $3.535 | **−$54.00 / −7.10%** | −$59.00 | 1.4% ✅ | 21 |
| RBRK 2026-09-18 90P ×2 | lot 1 desk, **lot 2 you** | $820 ($4.10 avg) | $4.40 | **+$60.00 / +7.32%** | **+$0.00** | 13.6% ⚠️ | 28 |
| SPY 2026-11-20 700P ×1 | desk (authorized hedge) | $749 | $6.49 | −$100.00 / −13.35% | −$101.00 | 0.3% ✅ | 91 |
| **Book** | | **$2,330** | **$2,236** | **−$94.00 / −4.03%** | | | |

**Why we own each one:**

- **QQQ 680P** — a bet the Nasdaq falls. It pays only below **676.46**, which is **5.16% under** today's 713.27. Costs **$43.40/day** in decay across the two contracts — 6.1% of what's left in it, every day.
- **RBRK 90P** — a bet Rubrik falls. Pays below **85.60**, which is **13.9%** under today's 99.45. RBRK is *up* 1.98% today. Reports earnings **Aug 27 after the bell**.
- **SPY 700P** — your authorized insurance against an Aug–Oct drawdown. Not a trade; exempt from the stop rules and held to a roll decision with you around 21 DTE (late October).

---

## 2. Actions taken today

**By the desk: none.** Zero entries, zero exits, both tracks, across 27 scheduler-fired runs.

**By you, in-app — three fills, and they're the day's real story:**

| Time | Action | Fill | Effect |
|---|---|---|---|
| 13:55Z | **Sold** ACHR 2028-01-21 5C to close | $3.00 | **+$53.00 realized (+21.5%)** |
| 15:50Z | **Bought** a 2nd QQQ 2026-09-11 680P | $3.56 | QQQ avg basis $4.05 → **$3.805** |
| 16:00Z | **Bought** a 2nd RBRK 2026-09-18 90P | $4.30 | RBRK avg basis $3.90 → **$4.10** |

All three carry `placed_agent: "user"` at the broker — verified, not inferred. Three things follow, and they matter more than the fills themselves:

1. **You answered the pending decision by acting.** Seven runs today worked the QQQ 21-DTE bank-vs-ride question and paged you three times. You didn't bank it — you doubled it. The desk has stopped re-litigating that decision and will not page you about it again unless a trigger actually moves.
2. **Your add lowered the blended basis but doubled the carry.** Each QQQ contract now needs less to work, but the position bleeds **$43.40/day** instead of $21.70, and a 1% adverse move now costs twice what it did.
3. **This was not a rule breach, and no future run should read it as one.** The Four Laws bar *the desk* from adding to a losing position without asking you. You adding to your own is your call. Logged explicitly so nobody flags it later.

---

## 3. Candidates screened and skipped

Nine groups worked today. Every one declined, and the reasons are the point:

- **NVDA bearish scalp — B, the closest call of the day.** The chain was superb (215P at 1.08% of mid, 17,483 OI, delta −0.46, exactly the tactical band) and the tape agreed — NVDA faded all session to −0.88% while the index rose. Killed by three things: $925 breaks the $300–600 tactical band; the cheap short-DTE alternative spans NVDA's **Aug 26** print, which is precisely what the DTE floor exists to prevent; and a 14:30 ET Friday scalp whose time stop is Monday's close is really a bet on the weekend gap, not on an intraday level. Add that we're *already* short this exact view through QQQ.
- **QQQ add — barred, not merely declined.** Adding to a position that's down is the one thing the desk must ask you about first. You did it yourself instead; the desk didn't and wouldn't.
- **TSLA (+5.5% on robotaxi news) — C.** Chasing. A move that has already run 5.5% today on idiosyncratic news is not a catalyst for entering after it.
- **CRWD (RSI2 0.9, the most oversold print on the equity report) — passed on the earnings rule.** Reports **Aug 26**, inside any hold window. A name can beat and still gap down; no stop protects an overnight gap.
- **INTC, KLAC, TXN, TSEM (semis, RSI2 3.6–6.4) — C.** Mean-reversion longs into a sector down ~5% on the week, with the quarter's biggest semi catalyst (NVDA, Aug 26) landing inside the hold window.
- **SPY / QQQ tactical, either direction — C.** No level breaking, so no invalidation could be written. QQQ sat 0.03% above its falling 50-day for a third straight session — that's monthly-expiry pinning, not a break. "No written invalidation = no trade" bit honestly today rather than technically.
- **A fourth core swing — C.** The theme cap *allowed* it. Judgment declined it: a third expression of the same bearish view, into a pinned tape, on expiry Friday, is concentration without a catalyst.

---

## 4. Sleeve state

- **Premium at risk $2,330** — core swing $1,581 (QQQ $761 + RBRK $820), hedge $749. Tactical: **$0, none open.**
- **Slots:** tactical **0 of 2**, core **2 of 3**. Bearish-tech theme at **2 of 3**.
- **Entries used: 0 of 8 today**, 0 of 2 this run.
- **Buying power $1,156.87** — `unleveraged_buying_power` equals `buying_power`, so **no margin is extended**. Deployable after your $250 reserve: **$906.87**.
- **Realized options P/L today: +$53.00** on 1 closing trade — sourced from the broker, not asserted. That was your ACHR sale. Desk-placed realized P/L, which is what the −$400 cap gates: **$0.00**. The cap was never near.
- **Account value $3,837.75** — comfortably above the $2,000 margin-equity minimum.

**The number worth sitting with: the book is 100% one-way short, about −$41,400 of delta notional against a $3,838 account — 10.8×.** A 1% *up* move costs roughly $412, or 18% of the premium at risk, in a single session. That is not leverage in the loss sense — max loss is the $2,330 already paid, there is no margin and no assignment risk on long options. But it means every position profits from the same thing, and today they all lost together while the tape drifted up. Combined decay is **$78/day** across the book, so the weekend alone is a real cost with no offsetting long.

---

## 5. The decision that binds next: RBRK, by Wednesday's close

**Not QQQ — you settled that one today. RBRK is the live one, and it has two problems stacked.**

**Problem one: the gain isn't collectible.** RBRK shows **+$60 / +7.3% at the mark**. But the market is 4.10 bid × 4.70 ask — a **13.6% spread on 75 open interest and 8 contracts of volume all day.** Selling into that bid nets **$820 against an $820 basis: exactly zero.** The mark is an average of two prices nobody is transacting at. Any exit here realistically gives back the whole paper gain, and the only reason it isn't worse is that you paid up on the second lot.

**Problem two: earnings, Thursday Aug 27 after the bell.** The contract expires Sept 18, so holding through the print is a choice — and by the standing rule it's a no unless the earnings move *is* the thesis. The thesis was a technical breakdown, not an earnings bet. RBRK is also moving the wrong way: **+1.98% today to 99.45**, versus a breakeven at 85.60 that needs a **13.9%** decline.

**The clock: a decision is needed by the close of Wednesday, Aug 26.** The desk will bring it to you Monday with fresh numbers rather than letting it drift into the print by default. Three honest options, in order of what the numbers support:

1. **Close Monday/Tuesday, working the limit toward the mid** — likely nets somewhere between flat and a small gain, and takes the earnings gamble off the table. IV is already 80%, so decay accelerates into the print regardless of direction.
2. **Hold through earnings** — only if you want the earnings move itself. It needs a *large* down gap to pay: 13.9% below spot in 22 days.
3. **Close one lot, hold one** — splits the difference; halves both the earnings risk and the upside.

**The desk will not act on any of these without you** — that's your monitoring mandate, and it's working as designed. The one thing that executes without asking is a hard backstop (−65% at this DTE), and RBRK is nowhere near it.

---

## 6. Monday's watchpoints

- **RBRK earnings clock** — decision due by **Wed Aug 26** close. Desk brings it Monday with fresh bid/ask, not mark.
- **NVDA reports Wed Aug 26 after the bell.** It sits inside the QQQ put's 21-day window and is the single biggest event for that position. NVDA closed today −0.88% while the index rose — the leadership divergence the desk has flagged all week.
- **CRWD reports Aug 26** — relevant only as a read on software; not a position.
- **QQQ 713.05, the falling 50-day.** Pinned three sessions running. A decisive break below on volume is the first real confirmation the QQQ put's thesis is working; a clean reclaim above is the first evidence it isn't.
- **Weekend decay ≈ $78/day on paper.** Much is priced into Friday's close, but expect Monday's marks to open a touch lower absent a move.
- **Buying power $906.87 deployable** — enough for one tactical scalp or one small core swing. Both tactical slots are open, and the desk would prefer a *non*-bearish setup given the concentration above.

---

*Broker-sourced: `get_realized_pnl`, `get_option_orders`, `get_option_positions`, `get_portfolio`, `get_option_quotes`, `get_equity_quotes`. Reconciliation: zero drift — three option contracts and one equity position (PNC), every pending field zero. This is a 15-minute scheduled cadence during market hours only; intraday spikes between runs and overnight gaps are not covered.*
