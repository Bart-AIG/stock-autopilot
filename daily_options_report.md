# Daily Options Report — Thursday, 2026-08-20

*Agentic account (cash, ••••7339). Written after the 4:00 PM ET bell, at 15:20 CT / 20:20 UTC. Today's automation fired at 13:26, 13:33, 15:24, 16:24, 17:24, 18:24, 19:21 and 20:18 UTC. The 19:21Z run landed four minutes before the 14:25 CT report window, so this post-close run is the first one eligible — and it writes it rather than waiting for a tidier slot.*

**One-line summary: no trades again today — the fifth straight flat day — but the book made money doing nothing: the options sleeve gained $224.50 in mark-to-market on the day, and QQQ finally closed below the line the desk has been watching all week. Realized P/L today: $0.00. There is one decision that needs you, on the QQQ put, and it binds at tomorrow's open.**

---

## 1. What we own

| Contract | Placed by | Entry | Close mark | P/L at mark | Realistic exit (at bid) | DTE | Status |
|---|---|---|---|---|---|---|---|
| QQQ 2026-09-11 680P | agentic | $4.05 | **$4.89** | **+$84.00 / +20.74%** | **+$78.00** | 22 | Working — **decision due, see §5** |
| RBRK 2026-09-18 90P | agentic | $3.90 | **$4.80** | **+$90.00 / +23.08%** | **+$80.00** | 29 | Working |
| SPY 2026-11-20 700P | agentic (authorized hedge) | $7.49 | $7.29 | −$20.00 / −2.67% | −$22.00 | 92 | Insurance, best mark since entry |
| ACHR 2028-01-21 5C | **you, in-app** | $2.47 | $2.855 | +$38.50 / +15.59% | +$34.00 | 519 | Untouched — yours |

**Why we own each one, in plain terms:**

- **QQQ 680P** — a bet the Nasdaq falls. It pays only if QQQ is below **675.11** on Sept 11, which is **5.04% below** today's 710.95 close. It costs **$25.24 a day** in time decay — **5.2% of everything left in it, every single day.** That decay number is the whole argument in Section 5.
- **RBRK 90P** — the same bet on Rubrik, which reports earnings **next Thursday, 8/27**. It needs RBRK below **85.20** (a 12.6% drop) by Sept 18. It decays at $12.58/day — half the QQQ burn — and has a week more time, which is why it is the more patient of the two.
- **SPY 700P** — your authorized portfolio insurance from the Aug–Oct drawdown watch. It is *supposed* to bleed while the market is calm, and today it did the opposite: it gained $91 as SPY fell. A −2.67% mark on a hedge two weeks in is the policy doing its job cheaply. Exempt from every automatic stop; the only decision on it is a roll-or-close conversation with you around **October 30**.
- **ACHR 5C** — your own trade, placed in the app, with a hold override on it. The desk is barred from touching it and does not re-litigate it. Down $29.50 today, still up 15.6% overall.

**The day's mark-to-market, position by position:** QQQ put **+$113**, SPY hedge **+$91**, RBRK put **+$50**, ACHR **−$29.50**. Net **+$224.50** on a day the desk placed zero orders. This is what it looks like when a book is already positioned for the tape that shows up — and it is the reason Section 4's "why we stayed flat" is not an apology.

---

## 2. Actions taken today

**None. No orders were placed, modified, or cancelled.** `get_option_orders` for the trading day returns empty, realized P/L is **$0.00**, and the broker's position list matches the ledger one-for-one on all four contracts with every pending field at zero — so no assignment, exercise, expiration, or unauthorized fill occurred.

One **notification** was issued, at 18:24 UTC (1:24 PM ET), when the QQQ put spiked to +27.8% intraday: a bank-versus-ride recommendation handed to you for decision. It was deliberately **not** re-sent on the 19:21Z or 20:18Z runs — the recommendation had not changed, and re-pinging you every 15 minutes about an unchanged situation is how a monitoring mandate turns into noise you stop reading.

---

## 3. What the market actually did — and where the desk was wrong this morning

| | Close | Day |
|---|---|---|
| SPY | 762.65 | −0.83% |
| QQQ | 710.95 | −0.72% |
| IWM (small caps) | 297.68 | −1.34% |
| RBRK | 97.49 | −2.29% |

**The one level that mattered resolved.** QQQ opened sitting *exactly* on its 50-day average (712.98) — the brief called that "the single most actionable level on the board today." It **closed below it, at 710.95.** The next line down is the 20-day at 706.78, 0.6% away. That is the bearish premise on the QQQ put working, not a random red day.

**Small caps led down.** IWM at −1.34% was the weakest board and got weaker through the session. Risk-off broadening from a couple of megacaps into the small-cap complex is a more genuine signal than the selective rotation earlier in the week.

**But the semis did not break, and that matters.** TSM **+0.97%**, AVGO **+0.49%**, AMD **+0.67%** all closed *green*; NVDA was nearly flat at −0.26%. A Nasdaq decline with the semiconductor complex holding up is a rotation, not a top. This is the "unless" clause on the standing QQQ plan, and it did **not** fire.

**Where this desk read it wrong this morning — worth writing down.** The 9:30 open showed 30-day implied volatility up on 8 of 9 tracked names and the brief declared "for the first time in five sessions, vol is bidding," while explicitly warning not to buy premium on an opening tick because opening IV is inflated by wide auction markets. **The afternoon re-measure proved the warning right and the headline wrong:** QQQ 30-day IV finished at ~0.201 versus 0.203 at the open, SPY ~0.130 versus 0.132 — flat-to-*lower* on a day the index fell three-quarters of a percent. Vol did not bid. The lesson is the general one: **an opening IV print is not a regime change, and the discipline of waiting cost nothing while acting would have cost real money.**

---

## 4. Actions considered and SKIPPED

*This is the section worth reading. Nine candidate groups were worked today; all nine were killed, and the reasons split cleanly into "structurally barred" and "no reason to act."*

**Barred by structure, regardless of how good they looked:**

1. **More bearish tech — QQQ, AVGO, AMD, TSM, NVDA puts.** This is the expression that fit today's tape *best*, and it was unavailable. The book already holds two bearish-tech positions (QQQ 680P + RBRK 90P), which is the hard **2-per-correlated-theme cap**. The cap did its job on precisely the day it was most tempting to ignore — which is the only day a cap ever matters.

2. **IWM puts (small caps, the weakest board).** Graded **B**, passed. This one deserves explanation because it *appears* to pass the theme test: IWM is not tech. But in substance it fails — with SPY 700P and QQQ 680P already on the books, a third short-index leg is the same macro bet wearing a different ticker, not diversification. Stacking a fourth correlated short into $1,210 of settled cash, with NVDA earnings (8/26) and Jackson Hole (8/27) both ahead, is not what a free slot is for.

**Killed on the merits:**

3. **The equity report's RSI2 oversold list** — CRWD (RSI2 1.2), EMR 1.8, ALAB 2.1, USB 2.5, PANW 2.7, plus SBUX, C, NUE, MS, ARM, ETN, NET, UNH, DELL, ROST, BE, COF, GEV, TKR, TSEM. Graded **B/C** as a group. These are *bullish* mean-reversion setups; buying calls on them would fight both today's broadening risk-off and the desk's own bearish book. Several carry earnings inside any plausible hold window (CRWD 8/26, PANW 9/1, DELL 9/1, ROST today) — a standing no-entry. The rest are mid-caps with chains too thin to trade at this size. **All were killed on tape-and-chain before any thesis workup** — that ordering is deliberate and it is what the sourcing fix was written to enforce.

4. **Bullish index/megacap calls** (QQQ, SPY, NVDA, INTC, MSFT — the affordable tier). Grade **C**. No trigger firing *now*; these are drifting lower, not reversing. "The tape is down so buy the dip" is not a catalyst. Buying calls would also have directly hedged away the two puts the book was being paid on today.

5. **TSLA** (weakest core name, −1.66%). Grade **C**, and it is a trap worth naming. Its headline IV/RV of **0.72** screams "cheap premium." It is an artifact: TSLA's 57.2% realized vol is driven by a single **−15.69% earnings gap on 7/23**. Strip that one day and realized vol is 33.2%, which flips the ratio to **1.24 — rich, not cheap.** The mechanical number was inviting exactly the wrong trade.

6. **MSFT.** Grade **C**, same trap, more extreme: headline IV/RV **0.52**, the most extreme "half-price vol" reading on the desk's board. It is almost entirely one **+14.42% gap on 7/30**; ex-gap, realized is 25.9% against 26.1% implied — premium priced almost exactly *fair*. Also worth repeating: proving a vehicle is cheap and liquid supplies **no thesis whatsoever.**

7. **NVDA.** Grade **C**, watch-only into the 8/26 print. The standing preference is to *close* before earnings, not open into them, and "earnings is the thesis" does not apply — this desk has no differentiated view on NVDA's quarter. The relevant NVDA exposure is already owned indirectly through the QQQ put.

8. **XLE / energy** (the only green sector earlier in the day). Grade **C**. One green session is not a catalyst, there was no fresh driver, and the standing sector steer de-emphasizes oil energy.

9. **XLF / banks.** Yesterday's setup required XLF to open green and hold. It closed **−0.92%**. The trigger simply did not fire — logged so it isn't re-derived from scratch tomorrow.

**The honest summary of why we were flat:** two independent reasons, either sufficient. Structurally, the only free slot is barred to bearish tech, and every honest bearish expression available today is a bet the book already owns twice. Substantively, nothing had a trigger firing today that isn't already owned. **The desk was already positioned for exactly the tape that printed** — and the right response to a thesis working is to manage the winner, not to bolt on a fourth correlated leg with the week's two biggest catalysts still ahead.

---

## 5. ⚠️ The decision that needs you — QQQ 680P, and it binds tomorrow

This is the same question sent at 1:24 PM ET, now with the closing numbers attached. **The desk will not act on it without you** — under the monitoring mandate you set on 8/18, discretionary exits on this position are recommended and wait for your go-ahead.

**Where it stands at the close:**

| | |
|---|---|
| Entry / close mark | $4.05 → **$4.89** |
| P/L | **+$84 at mark, +$78 net if sold at the bid** |
| Market | 4.83 × 4.95 — **2.45% spread**, OI 33,897, 486 traded. This is a *real*, liquid exit price, not a paper number. |
| Intraday peak | **$5.21** at 1:24 PM (+$116). It has given back **27.6%** of that peak gain into the close. |
| Time decay | **−$25.24/day = 5.2% of the remaining premium, every day** |
| Delta | −0.204 — it takes a *large* QQQ move to move this much further |
| Needs to win | QQQ below **675.11** by 9/11 — another **5.04%** down in 22 days |
| DTE | **22 — the unconditional 21-DTE review lands tomorrow, 8/21** |

**The case for banking it (my recommendation, unchanged):** you have a genuine +$78 in hand on a tight, liquid market. The 21-DTE management rule exists because the theta-and-gamma window past this point is where option buyers get hurt — and at 5.2% of premium per day, simply carrying this position across the weekend costs roughly $75 in decay if QQQ doesn't move. NVDA reports 8/26 *inside* the hold window, which is a large two-way variance event this desk has no edge on. And index-put spikes of the kind that printed at 1:24 today characteristically bleed back out — which is exactly what happened over the following two hours.

**The honest case against — the reason this is your call, not a mechanical one:** the thesis is *working*, not stalling. QQQ closed below its 50-day for the first time, small caps are leading down, and the written invalidation (a close above ~730) is nowhere near. Mechanically, nothing on the exit ladder has fired: the pop-bank level is $7.29, the profit-ratchet arms at $6.08, and the mark is $4.89 — so the rulebook's own answer is "let it ride." Selling a working position because a *calendar* date arrived is the argument you'd want to push back on.

**What tips me to banking anyway:** delta −0.20 and a 5.04% required move mean this position now needs the Nasdaq to *accelerate* downward, not merely to keep drifting. Meanwhile the semis closed green — the specific "unless" condition on this trade's standing plan did **not** fire, so the broadening that would justify holding is not in evidence. Paying 5.2% a day to wait for a break that the strongest sector in the index is currently refusing to confirm is a poor use of $489 of premium.

**Three ways to play it, if you'd rather not choose between all-or-nothing:** (a) **sell it at tomorrow's open** and bank ~$78; (b) **hold through the 21-DTE review** with an explicit written re-justification and a hard exit if QQQ reclaims 713 (the 50-day it just lost); (c) **roll down-and-out** to a later expiry, which resets the decay clock but costs new premium and re-opens a position rather than closing one. I recommend **(a)**, and absent a reply the position simply carries into tomorrow's review run — nothing is sold on autopilot.

**RBRK, for contrast, needs nothing from you today.** It is +$80 net at the bid on a market that tightened all day (11.2% of mid this morning → **4.17%** at the close), the underlying fell 2.29%, and its binding deadline is the **pre-earnings decision by the close of Wednesday 8/26**, ahead of the 8/27 print. That question comes to you Wednesday, not now.

---

## 6. Sleeve state

| | |
|---|---|
| Account value | **$4,071.17** (equity $876.52 / options $1,984.00 / cash $1,210.65) |
| Settled cash | **$1,210.65**, unsettled $0.00 — the settled-cash law is not binding |
| Agentic premium at risk | **$1,544** ($749 hedge + $405 QQQ + $390 RBRK) |
| Unrealized on agentic positions | **+$154 at mark** |
| Realized P/L today | **$0.00** vs the −$200 daily cap — not binding |
| New entries used today | **0 of 3** |
| Position slots | **2 of 3** non-hedge used (hedge excluded) |
| Theme capacity | **bearish tech 2 of 2 — FULL** |

The theme cap, not money, is what kept the desk flat today. There is $1,210 of settled cash and a free position slot; what there isn't is a non-correlated idea worth owning.

---

## 7. Tomorrow's watchpoints

- **QQQ 680P 21-DTE management review — Friday 8/21, unconditional.** The decision in Section 5 lands at the open. This is the single binding item.
- **QQQ 706.78 (the 20-day).** 0.6% below today's close. Losing it confirms the breakdown and strengthens the case to hold; reclaiming **713** (the 50-day) is the first evidence the bearish premise is failing.
- **The semis are the tell.** TSM, AVGO and AMD closed green while the index fell. If they roll over Friday, the QQQ hold case gets much stronger; if they keep holding, banking the put is right.
- **Friday weekly review** is due — hit rate, average win versus average loss, best and worst *process* decisions of the week, and the drift check on standing preferences. It will be sourced from broker P&L, not from the journal.
- **Next week's two catalysts:** **NVDA earnings Wednesday 8/26 (pm)** — inside the QQQ put's window — and **Jackson Hole 8/27**, alongside the **RBRK pre-earnings decision due at Wednesday's close** before its 8/27 print.

---

*Written by the 20:18 UTC post-close automation run. Reconciliation: zero drift on both books — four option positions matching the ledger exactly, all pending fields zero, no orders placed today. Heartbeat stamped for the 2026-08-20 trading day at 13:33Z. Nothing in this report is an executed action; the QQQ recommendation awaits your go-ahead.*
