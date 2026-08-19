# Daily Options Report — Wednesday, 2026-08-19

*Agentic account (cash, ••••7339). Written at 14:22 CT / 19:22 UTC — three minutes before the usual 14:25 CT slot, deliberately. Today's automation fired hourly (13:33, 14:26, 15:24, 16:22, 17:22, 18:22, 19:22 UTC), so the next run lands after the 4:00 PM ET bell. This is the last run of the day that can deliver this, and the playbook says early beats missing.*

**One-line summary: no trades today — the fourth straight flat day — and the day's most useful finding is that this desk was reading the tape wrong until the last hour. There is one decision that needs you, on the QQQ put, and it's in Section 5. Realized P/L today: $0.00.**

---

## 1. What we own

| Contract | Placed by | Entry | Mark now | P/L (mark) | Realistic exit | DTE | Status |
|---|---|---|---|---|---|---|---|
| QQQ 2026-09-11 680P | you (via a live agent session) | $4.05 | $3.58 | −$47.00 / −11.60% | −$49 at the bid | 23 | Stalled — see §5 |
| RBRK 2026-09-18 90P | you (via a live agent session) | $3.90 | $4.00 | +$10.00 / +2.56% | **−$10** at the bid | 30 | Stalled |
| SPY 2026-11-20 700P | agentic (authorized hedge) | $7.49 | $6.37 | −$112.00 / −14.95% | −$113 at the bid | 93 | Working as designed |
| ACHR 2028-01-21 5C | **you, in-app** | $2.47 | $3.125 | **+$65.50 / +26.52%** | +$58 at the bid | 521 | Untouched — yours |

**Why we own each one, in plain terms:**

- **QQQ 680P** — a bet the Nasdaq falls. It only pays if QQQ is below **676.42** on Sept 11, which is **5.68% below** today's 717.19. It costs **$20.64 a day** in time decay — that's 5.8% of what's left in it, every single day.
- **RBRK 90P** — the same bet on Rubrik. Needs RBRK below **86.00**, a **14.5%** drop, within 30 days. It decays slower ($11.77/day) and has a week more time, which makes it the more patient of the two.
- **SPY 700P** — your authorized portfolio insurance. It is *supposed* to lose money while the market is calm. A −14.95% mark on a hedge in a firm market is the policy working, not a position going wrong. It is exempt from every automatic stop and the only decision on it is a roll-or-close conversation with you around **October 30**.
- **ACHR 5C** — your own trade, placed in the app. The desk is barred from touching it. It's your best position, up 26.5%.

**One number worth internalizing on RBRK:** the mark says +$10, but the market is 3.80 bid / 4.20 ask — a **10%-wide spread on 71 open contracts, with 4 traded all day.** If we sold right now we'd get the bid and *lose* $10. On a thin chain the "profit" on your screen isn't money until someone pays for it. That gap is why this desk screens liquidity before it screens ideas.

---

## 2. Actions taken today

**None.** No order was placed, modified, or cancelled. Broker confirms zero option orders of any state on 2026-08-19. Realized P/L $0.00 against the −$200 daily cap; 0 of 3 daily entries used.

Every position was checked against the exit engine at all six runs. **Not one trigger fired, in either direction** — no profit level, no loss level, no setup break. Here's how far each one is from anything happening:

| Position | Sell-for-profit level | Re-check level | Hard auto-sell floor | Mark now |
|---|---|---|---|---|
| QQQ 680P | 7.29 | 2.03 | 1.42 | **3.58** |
| RBRK 90P | 7.02 | 1.95 | 1.37 | **4.00** |

Both sit comfortably in the dead zone between. There was genuinely nothing to do.

---

## 3. What I got wrong today, and the correction

This is the most useful thing in today's report, so I'm putting it before the candidate list.

At 17:22 and 18:22 UTC this desk labelled the tape **"breadth deterioration — narrowing participation beneath a flat index"** and called it the late-cycle setup the August–October defensive posture was written to anticipate. The evidence looked strong: eighteen names printing RSI(2) under 10 across four unrelated sectors while the S&P was *up*.

**Into the close, that reading doesn't hold up**, because of two facts neither run checked:

1. **Small caps are GREEN.** IWM finished the session +0.46%. The Russell is the best breadth proxy available, and genuine narrowing participation does not come with small caps rising.
2. **The VIX made its LOW of the day into the close — 14.95**, below this morning's 15.28 and yesterday's 15.70. That's the sixth consecutive session with no bid for volatility.

What's actually happening is a **two-group liquidation inside a firm market**: AI-semis (AVGO −3.97%, AMD −3.53%, both at session lows) and banks (C −3.42%, PNC −3.17%, USB −3.13%, WFC −1.89%) are being sold, and the money is visibly going into small caps, MSFT (+0.58%) and TSLA (+3.53%). NVDA and TSM were flat, so even the semis move is an AVGO/AMD story rather than an AI-wide one.

**Why the label matters and isn't just semantics:** a rotation is a much worse environment for the long index puts we own than a breadth breakdown would be. In a breakdown, volatility bids and puts gain even before the index falls much. In a rotation, the index holds, volatility keeps falling, and the puts just bleed. Two runs today held the QQQ put partly on a reading that the closing data doesn't support. That correction is what drives Section 5.

---

## 4. What I looked at and passed on

The desk had **one free position slot and $2,110.65 of settled cash**, so being flat was a choice, not a constraint. Five candidates:

**① Buying the beaten-up banks (XLF / C / USB / PNC / WFC calls) — Grade B. The closest call of the day.**
Four major banks printed RSI(2) under 7 inside intact long-term uptrends — a textbook oversold-bounce setup. Best of all, it's the one thing the desk *can't* buy in tech: uncorrelated with everything we own, and these are the most liquid non-tech chains available to us (checked first, per the sourcing rule). **Rejected because the setup has no trigger yet, and the group got worse while I watched it.** Citigroup went from −2.75% at 13:22 ET to −3.42% at 15:21 ET; PNC and USB likewise made new session lows. A mean-reversion trade needs the turn to actually start — "very oversold" is a condition, not a signal. Buying calls into a group still being sold is catching a falling knife.
→ **Tomorrow's trigger, written down so it isn't re-derived:** XLF or C opening green *and holding it*, with RSI(2) turning up off the low. That upgrades this to A− and makes it takeable.

**② More bearish tech (AVGO, AMD, SOXX puts) — structurally blocked, not graded.**
AVGO and AMD at session lows was the loudest move on the board, and it's precisely the trade we're barred from. The book already holds two bearish-tech positions (QQQ + RBRK) and the cap is two per theme. I deliberately did *not* write a thesis for it — building a case for a trade you can't place is how a risk cap quietly gets talked out of existence.

**③ DE calls into tomorrow morning's earnings — Grade C.** Fails three ways: the desk's rule is to close *before* earnings, not open into them; DE at $585 makes any sensible contract expensive against the $1,500 per-trade cap with the whole premium exposed to one overnight gap; and a 15-minute check cadence cannot manage a gap. The equity report flags DE no-entry for the same reason.

**④ Buying small caps on the green divergence (IWM calls) — Grade C.** The divergence is real and it's the day's best observation, but it's *one session* at +0.46% with no catalyst. Worse, it would be a long index position in a book already holding SPY and QQQ puts — paying premium to cancel out premium we already own. If the bearish view is wrong, the fix is to exit the puts, not to buy something that fights them.

**⑤ Buying volatility — Grade C.** Six straight sessions with no vol bid, and today the VIX hit its *low* into the close on a day eighteen names were deeply oversold. Buying vol now is the mirror image of chasing a finished trend: entering because a move keeps *failing* to happen is no better than entering because one already happened.

---

## 5. 🔔 The decision that needs you: the QQQ 680P

Nothing has *fired* on this position — I want to be precise about that. But the mandate is to bring you a decision at the right moment with the numbers attached, and the numbers moved against this one today.

**Where it stands:** paid $4.05, now $3.58 (−$47, −11.6%). Selling at the bid nets −$49. The chain is excellent — 1.1% spread, 33,336 contracts traded — so we can exit cheaply any time we want.

**The honest case against holding:**
- It costs **$20.64 every day** — 5.8% of the remaining premium, daily. Waiting the two sessions to Friday's scheduled review costs roughly **$41** of the $358 still in it.
- It needs QQQ to fall **5.68% in 23 days**, while QQQ sits comfortably above its 20-day average (706).
- It needs a volatility event, and volatility just made a six-session low.
- The tape read that supported holding it turned out to be wrong (Section 3).

**The case for holding:** Friday, August 21 is the pre-written 21-day review date — the point where this position gets a formal roll-or-close decision. Two sessions is short, one adverse day is not a thesis, and a scheduled decision point exists precisely so a position isn't abandoned on a bad afternoon. There's also a real chance the AVGO/AMD liquidation broadens; if it does, this put is exactly what you'd want to own.

**My recommendation: close it at or near the mid (~$3.58) on Thursday or at Friday's review, unless the semis selling visibly spreads to NVDA and the index.** The trade needs a vol event that six sessions of tape have refused to deliver, and the daily carry is high enough that patience here isn't free. I'm not acting on this — under your monitoring mandate it's your call. Say the word and it's done in one order at the midpoint.

**RBRK needs no decision yet.** Its next hard date is a pre-earnings close-or-roll call by **Wednesday, August 26**.

---

## 6. Sleeve state

| | |
|---|---|
| Account value | **$3,820.65** (equity $0 / options $1,710.00 / cash $2,110.65) |
| Settled cash / buying power | **$2,110.65**, all settled — unsettled $0.00, so nothing is blocked |
| Agentic premium at risk | **$1,544** ($749 hedge + $405 QQQ + $390 RBRK) |
| Realized P/L today | **$0.00** vs the −$200 daily cap |
| Entries used today | **0 of 3** |
| Position slots | **2 of 3** used (the hedge doesn't count) |
| Theme capacity | Bearish tech **2 of 2 — full**. Any new trade must come from elsewhere. |
| Broker reconciliation | **Zero drift**, thirteenth consecutive clean check. Four contracts at the broker, four in the ledger, nothing pending, no orders today. |

---

## 7. Tomorrow's watchpoints

1. **The bank-bounce trigger** — XLF or C opening green and holding, with RSI(2) turning up. That's the only graded candidate with a path to A− and the only one uncorrelated with what we own.
2. **QQQ 680P** — Friday's 21-day review is binding. From that point a −50% loss becomes a standing automatic cut rather than a re-check. See §5.
3. **Does the semis liquidation broaden?** If NVDA and TSM join AVGO and AMD on the downside and the VIX finally bids, the QQQ put becomes worth keeping. If they don't, §5's recommendation gets stronger.
4. **DE reports before the open** — not a position, but a read on how industrials are being treated.
5. **RBRK** — pre-earnings decision due by the close of Wednesday, August 26.

---

*Honest limit, restated: this is a 15-minute scheduled check during market hours only. A spike can round-trip entirely between two runs, and overnight and weekend gaps aren't covered at all. Nothing here is continuous monitoring.*
