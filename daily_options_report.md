# Daily Options Report — Friday, 2026-08-14

*Agentic account (cash, ••••7339). Written on the first scheduled run at/after 14:25 CT (19:30 UTC). Plain-language by design — the point is that you can see **how** each decision was made, not just what it was.*

**One-line summary: no options trades today, for the fifth session running — but for a reason that changed this week. Every rejection today was a *vehicle* or *trigger* rejection, not a budget rejection. Your sizing change worked; what's now binding is that the setups the desk likes keep living on chains this account either can't afford or can't structure.**

---

## 1. Positions we own

| Contract | Placed by | Entry | Mark now | P/L | DTE | Status |
|---|---|---|---|---|---|---|
| SPY 2026-11-20 700P (1) | agentic | $7.49 ($749) | $6.17 | **−$132 / −17.6%** | 98 | HOLD — exempt from stops |
| ACHR 2028-01-21 5C (1) | **you** | $2.47 ($247) | $3.35 | **+$88 / +35.6%** | 890 | HOLD — your position, untouched |

**Why we own the SPY put.** This is the Aug–Oct drawdown insurance you authorized on 2026-08-05. The 700 strike sits just under the July-low shelf (716.6) and the rising 200-day (≈702), so it only pays if the market genuinely breaks trend — not on a garden-variety dip. It is *supposed* to bleed while the index sits near highs, which is exactly what −17.6% represents. **It is deliberately exempt from the −50%/−65%/−70% cut rules** that govern every other position; insurance you sell during calm weather isn't insurance. The next real decision is the ~21-DTE roll-or-close review around 2026-10-30, and that one is yours, not the automation's.

Worth noting for education: the put is only down 17.6% after nine days despite SPY sitting *higher* than at entry. That's because it's 98 days out — theta on a long-dated OTM put is only −$0.083/day. This is what buying time rather than direction looks like.

**Why we own the ACHR call.** We don't — *you* do. You bought it 2026-07-20 and told the desk on 07-22 to leave it alone. It's +35.6% today. Two separate rules keep the automation's hands off it: the ownership gate (anything `placed_agent="user"` can only be flagged to you, never closed by a run) and your explicit hold override. The desk checked it for a fired exit condition today, as the gate requires — none fired. It would need +50% to even *arm* the profit ratchet, and even then the answer would be to tell you, not to sell.

---

## 2. Actions taken today

**In the options sleeve: none.** Twenty-two market-hours runs, zero entries, zero exits, zero orders placed.

**One thing did change in the account, and it wasn't the options desk.** Your ACGL equity position (4.069594 sh) sold at 15:05 ET for $401.10 — the mechanical RSI(2) swing exit you approved in a separate session. Result: **+$1.10, +0.27%**, a flat trade. It's recorded in the ledger with the order ID and fill. Two honest observations:

- **That was a signal exit, not a thesis exit.** RSI(2) travelled the full arc from 5.2 (oversold, the reason to buy on 08-10) to 76.2 (overbought, the reason to sell) — the mean-reversion *completed exactly as designed* while the stock itself barely budged. The setup did its job; the payoff just wasn't there. ACGL's fundamentals never broke (Q2 beat, $1.95B H1 buybacks, P/E 15), so it stays a legitimate future candidate.
- **The proceeds are not spendable yet.** $401.10 settles Monday 2026-08-17 (T+1 across a weekend). This is a cash account, so spending it before then would be a good-faith violation. Settled buying power stays $1,982.52.

---

## 3. Candidates considered and SKIPPED — the educational section

Six names got real work today. Here's what killed each, because *the pattern* matters more than the individual names.

**INTC — the closest thing to a live trade all day, and it failed on the tape.**
Momentum leader in the equity screen (rank 6 of 228, 12-1 momentum +362%). The desk wrote a trigger and INTC tested it *in real time*: it broke out to a session high of $106.87 at 10:07 ET, then gave the entire move back within eight minutes on the day's heaviest volume. A run at 14:16 ET then did something worth pointing out — it **raised** the bar rather than lowering it, rewriting the trigger from "hold above $105.45" to "a decisive close above the failure high of $106.87, held 15+ minutes." The reasoning: read literally, the old condition would have re-armed on any poke above $105.45 and fired on *exactly the false breakout the tape had already produced once*. **INTC now sits at $102.96 — below its $103.50 killing level with 28 minutes to the bell.** The name was declined eleven consecutive times today, and each decline was cheaper than the failed breakout would have been.

**AVGO — the best technical print of the week, killed by arithmetic that no thesis can fix.**
The only Connors RSI(2) oversold signal in a 230-name screen, down 5.98% to $392.84 on the AMAT revenue-miss read-through. The desk wanted this one and priced it twice. It doesn't work as a *vehicle*:
- The only earnings-clean expiry is 2026-08-21 — **7 DTE, sitting exactly on the hard floor, not comfortably above it.** Theta there is −6.8% of premium *per day*. Friday→Monday is three calendar days of carry, so **20–27% of the premium evaporates before Monday's open even if AVGO doesn't move.**
- The 14-DTE alternative (08-28) is earnings-clean but its ATM costs ≈$1,370 — **91% of the $1,500 per-trade max, on open interest of 109.** Law 1's second sentence reserves max size for A++ setups. A knife-catch whose only confirmation is "it stopped falling" is a B.

AVGO has since traded *below* its own $394.38 kill level, which converts it from a bounce candidate into a trend-continuation one. Passing looks better by the hour.

**AMD — a genuine catalyst the account structurally cannot buy.**
AMD announced a $5B AI-expansion fund this morning and is +5.32% at $508.71. This is a real catalyst, not momentum. But the breakout trigger ($530.13, the 08-04 high) never fired — it stalled at its session high for four consecutive windows instead of extending. And even if it *had* fired: a 505C is $3,308 and a 530C is $2,280. **Both are more than double the $1,500 per-trade maximum.** The instrument that would fit — a debit spread — is unavailable on this account (see §5).

**NVDA — affordable, liquid, and correctly passed on anyway.**
NVDA is the one AI-complex name where a right-delta contract fits the budget (~$225 spot). It was passed because *there was no reason to buy it today*: flat at $225.23, no catalyst, no technical trigger. "The AI complex is strong" is momentum, and this desk's mandate explicitly names momentum as a non-catalyst. Also relevant: **NVDA reports 2026-08-26**, which the 09-18 expiry straddles — any entry would carry a mandatory pre-print exit and roughly a 10-day runway, not a 35-day one.

**ROST and LIN — killed in 30 seconds each, on purpose.**
ROST had a clean RSI(2) print of 2.0. Its chain has a **12.8% bid/ask spread on zero open interest.** LIN's ran 17–48%. Both were killed on the chain check *before* anyone wrote a thesis — which is the fix adopted this week after four of five candidates last week ate full research effort and then died on liquidity anyway. At a 25% spread the underlying has to move ~5% just to break even on a round trip; widening that gate manufactures losers, it doesn't manufacture opportunities.

**And the one that didn't get taken despite being buyable.** QQQ's 09-18 board was measured: the 750C is $883.50 at a **0.79%** spread on 41,640 open interest; the 710P is $950.00 at 0.63% on 25,761. Right delta, right DTE, roughly 60% of max size, in either direction. **The desk did not trade it, because being cheap and liquid is not a thesis.** Fitting a trade to a newly-affordable contract is the same cherry-picking the playbook forbids everywhere else.

---

## 4. Sleeve state

| | |
|---|---|
| Agentic premium at risk | **$749** (the SPY hedge only) |
| Non-hedge positions open | **0 of 3** |
| New entries used today | **0 of 3** |
| Settled cash / buying power | **$1,982.52** |
| Unsettled (ACGL, frees Monday) | $401.10 |
| Account value | $3,841.96 (equity $505.34 · options $953 · cash $2,383.62) |
| Realized options P/L today | **$0.00** — daily −$200 cap untouched |
| Realized options P/L this week | **−$195** (2 round trips, broker-sourced) |

Nothing is near an exit trigger. The hedge is exempt by design and its next checkpoint is late October; ACHR is yours and gated. There is no deadline, no earnings, and no backstop level in play for either position.

**The week's honest scoreboard: zero agentic entries in five sessions, and −$195 realized from two trades that closed early in the week.** That is worth staring at rather than glossing. The read: the loss cap was never the constraint, the budget stopped being the constraint on Thursday, and what's left is a genuine pipeline problem — which §5 names.

---

## 5. The one thing I'd ask you to act on

**Apply for `option_level_3` on the agentic account** — `applink.robinhood.com/upgrade_options?account_number=718757339`.

Your individual account already has level 3; this one is stuck at level 2, which allows only single legs. That's not a preference issue, it's the binding constraint on the two best setups of the week. Measured on the AVGO 08-28 board: the single legs cost $1,285 (86% of max) at −3.67%/day theta, while the **395/415 vertical would have cost $735 at −1.02%/day**, and the 395/410 just $587 at −0.70%/day. **That's a 4–9× reduction in daily carry at roughly half the capital at risk** — on the exact variable (theta) that disqualified AVGO twice and would disqualify AMD on any breakout.

Framed honestly: your 08-14 sizing change gave the desk **more money**. It did not give it a **cheaper way to carry a position**. Level 3 would, and that's now the more binding of the two.

*(Safety note, since it matters: until `get_accounts` actually returns `option_level_3`, no run will attempt a spread. On a level-2 account the long leg fills and the short leg gets rejected — leaving an unintended full-premium naked single leg. The desk treats spreads as unavailable, not as a preference to override.)*

---

## 6. Monday's watchpoints

- **$401.10 settles Monday**, taking settled buying power to ~$2,383.62.
- **AVGO** — if it closes today below $394.38 the bounce read is dead and it becomes a continuation-short candidate. If it holds above $395 with RSI(2) still under 10, the setup is intact with two days less theta and the 08-28 board at 11 DTE. Re-price both boards; don't inherit today's numbers.
- **INTC** — if today's close is below $103.50 the name is struck outright. If it closes back above, it returns as a C with the $106.87 trigger intact and unmet.
- **AMD** — $530.13 is a real breakout trigger now, but check the chain before acting: it's likely still unbuyable at level 2. Structural kill at a close below $463.21.
- **RDDT** joins the S&P 500 on **2026-08-18** (Monday) — mechanical index-fund buying.
- **NVDA earnings 2026-08-26.** Any NVDA entry from here needs a pre-print exit plan or it's an earnings gamble, which is barred unless earnings *is* the thesis.

---

*Positions and P&L reconciled live against the broker at 19:32 UTC. Realized P&L sourced from the broker, not the journal. Zero drift between `holdings.json` and the account.*
