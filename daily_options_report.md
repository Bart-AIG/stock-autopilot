# Daily Options Report — Monday, 2026-08-17

*Agentic account (cash, ••••7339). Written at 14:16 CT / 19:16 UTC — **nine minutes before the usual 14:25 CT slot, deliberately**. Nothing left on today's board can produce a trade (the one live trigger, MSFT, requires a daily close that isn't observable until after the placement window shuts), so waiting for a "proper" slot buys nothing and risks the report never being written if the cron stops firing. The playbook is explicit that early beats missing. Plain-language by design — the point is that you can see **how** each decision was made, not just what it was.*

**One-line summary: no options trades today — the sixth straight session flat — and today the reason is the healthiest one yet: three separate candidates were killed by rules the desk itself wrote *in advance*, and not one of them got quietly revived when price ticked back in its favor.**

---

## 1. Positions we own

| Contract | Placed by | Entry | Mark now | P/L | DTE | Status |
|---|---|---|---|---|---|---|
| SPY 2026-11-20 700P × 1 | agentic (your authorized hedge) | $7.49 | $6.595 | **−$89.50 (−11.95%)** | 95 | Working as designed |
| ACHR 2028-01-21 5C × 1 | **you**, in-app | $2.47 | $3.175 | **+$70.50 (+28.54%)** | 522 | Held — gated, untouchable by automation |

**Why we own the SPY put:** it's the insurance leg of the Aug–Oct defensive posture you adopted on 2026-08-05. It is *supposed* to lose money on green days — that's the premium you pay for the protection. Today SPY fell 0.39% and the put gained **+$38.50** on the day, which is the contract doing precisely its job. It is exempt from every premium stop-loss rule in the book; its only scheduled decision is a roll-or-close conversation **with you** around 2026-10-30.

**Why we still hold the ACHR call:** two independent gates, either one sufficient. You placed it yourself (`placed_agent: "user"`), so the automation may notice an exit trigger but may never pull it; and you set a manual hold override on 2026-07-22. As it happens nothing fired anyway — +28.5% is below the +50% level where the profit-ratchet arms, and at 522 days to expiry theta is bleeding about **21 cents a day**, which is nothing.

---

## 2. Actions taken today

**In the options sleeve: none.** Zero option orders of any state — not a fill, not a cancel, not a rejection. Verified straight from the broker at 19:18 UTC, which also serves as the check against a duplicate sibling run.

**One thing did happen in the account, and it wasn't this automation:** an interactive session bought **CL (Colgate-Palmolive), 5 shares @ $89.97 = $449.85** at 15:08 UTC on your one-tap approval. I reconciled it against the broker and the ledger already carries the full thesis, so there's no drift and no flag. Flagging it here only because it moved ~$450 from cash into equity, which changes the sleeve arithmetic below. It's now **+$0.53/share (+0.6%)** at $90.505. *This automation never trades equities — that's your rule, and it held.*

---

## 3. Candidates considered and SKIPPED — the educational part

Today's theme: **the desk got tested on whether its own kill levels are real, and passed three times.** A kill level only means something if you honor it on the day price makes you look foolish for writing it. That happened repeatedly today.

**NVDA 2026-09-18 240C — killed at 17:10 UTC, and then NVDA went green.**
The setup was a genuine vol edge (IV/RV 0.98, $560 premium, penny-wide market, 55,243 open interest) into the 8/26 earnings print. It carried a written kill level. That level fired mid-session, and the candidate was retired — **75 minutes before its own hard expiry**. NVDA then recovered to +0.17% on the day. Four subsequent runs looked at a green NVDA and did **not** re-arm the trade. That is the whole discipline: *reviving a killed candidate because price ticked back up is exactly how a kill level becomes decoration.* Any future NVDA trade has to be a brand-new setup, written from scratch and labelled as such.

**INTC — killed Friday by a rule written days earlier, and it's been above the level ever since.**
The standing plan said "a close back below $103.50 ends the coil and takes the name off the list." INTC closed Friday at $102.50. The rule executed. Today INTC traded 102.96 → 103.29 (+0.77%), back above the kill line, and **five separate runs declined to revive it.** This name was passed on eleven consecutive times without the entry trigger ever being quietly lowered to make a trade available. Worth knowing: the rule said a *close* below, it closed below, and a tick back up the next day is not a new setup.

**AVGO — the most instructive skip, because the analysis was right and the desk still can't act on it.**
The 19:01 UTC report refresh added AVGO to the oversold list (RSI2 9.0 at $393.64), and Friday's oversold read has been mean-reverting exactly as hoped. The thesis is working. Three independent blocks stop it anyway, any one sufficient:
1. **Size (a hard law, not a preference):** the 2026-09-18 400 call mids around **$21.88 = $2,188 per contract**, which blows straight through the $1,500 per-trade maximum. No thesis can outrank that.
2. **Vol:** AVGO is the only name in the core list paying *rich* relative premium (IV/RV 1.09) — we'd be buying the most expensive vol on the board.
3. **Earnings:** its print lands 2026-09-02, inside a 2026-09-18 expiry.

The vertical spread that would fix problem #1 — half the capital, a fraction of the theta — **is unavailable on this account at `option_level_2`.** This is now the second A-grade thesis this month killed by *vehicle economics* rather than by analysis, and it's the concrete case for the standing recommendation to apply for level 3 at `applink.robinhood.com/upgrade_options?account_number=718757339` (your individual account already has it, so it's per-account, not a you-problem).

**MSFT 2026-09-18 475P — the one live trigger, and it structurally cannot fire today.**
MSFT is the day's big mover, −2.83% at $481.39, cheapest relative vol on the list (IV/RV 0.52) for a sixth straight reading. The bear trigger written this morning is a **daily close below $475.00** — the post-earnings shelf. MSFT never got there; it printed 479.47 / 479.37 / 479.94 / 480.26 / 481.39 across the last hour, i.e. it stopped falling and ticked *up*. The entire −3% is one flush bar at 13:40 UTC, and real news work (done at 16:22, re-checked 16:48) found no datable catalyst behind it — the nearest thing is a six-month-old Stifel downgrade.

Here's the structural point a run flagged at 17:47 UTC and it's the sharpest thinking of the day: **a "daily close" is only observable at or after 20:00 UTC, by which time the 9:30–4:00 ET placement window is shut.** So there was never anything MSFT could do today that produced a trade. The temptation — and a bored desk one hour from the bell is exactly who feels it — is to quietly redefine "close" as a 5-minute close so the trade becomes available *now*. That did not happen, and the asymmetry was noted deliberately: NVDA's trigger was written as a 5-minute close from the outset and was legitimately read that way all day; MSFT's says daily. **They were not harmonized retroactively to manufacture a fireable setup.** Earliest MSFT can act is tomorrow.

**Also screened and passed, briefly:**
- **CL** — killed on the vehicle (Sept 90 call at 10.7% of mid on volume of *one*; the 92.5 call at 23.5%) and independently on the trigger (making a fresh low is a falling knife, not mean reversion). It's a fine *stock* signal for your equity book — which is precisely where it ended up.
- **DE** — new to the RSI2 list on the 18:01 UTC report, measured fresh and killed three ways; earnings 2026-08-20 alone ends it.
- **ROST** — earnings Thursday 8/20, plus **zero open interest** on the strikes that matter.
- **RDDT** — S&P 500 inclusion at tomorrow's open. "Sell the news" is a pattern guess, not a signal, and this desk has no edge in index-flow mechanics. Graded C.
- **Consumer group (HD / LOW / TGT / TJX / WMT)** — the week's one genuine macro thesis, off Friday's soft retail sales and UMich 51.0 vs 54.5 expected. Still not an entry, and the honest reason matters: buying a put *ahead of* HD's Tuesday print is an earnings bet, and the standing preference is to close before earnings, not open into them. The tradeable version is the **reaction**, not the anticipation.

---

## 4. Sleeve state

| | |
|---|---|
| Account value | **$3,868.74** |
| Cash / settled buying power | **$1,933.77** (unsettled: $0.00) |
| Options value | $977.00 |
| Equity value | $957.97 (AAPL 1.652252 sh + CL 5 sh) |
| Agentic premium at risk | **$749** — the SPY hedge alone |
| Non-hedge position slots used | **0 of 3** |
| New entries used today | **0 of 3** |
| Realized options P/L today | **$0.00** vs the −$200 daily cap |

Nothing is binding. There's no budget constraint, no settlement constraint, no slot constraint, no loss-cap constraint. **The sleeve is flat by choice, not by limitation** — which is the distinction worth taking away from six flat sessions. When the constraint was real (the pre-8/14 sizing rule), the correct complaint was about the rule; now that the rule is fixed, the flatness is a series of specific, written, defensible passes.

---

## 5. Tomorrow's watchpoints

- **HD reports Tuesday morning** — the single highest-information event on the board. It is the tell for whether the consumer is genuinely rolling. Watch the *reaction*, don't pre-position; LOW and TGT on Wednesday confirm or kill the read.
- **MSFT $475.00.** The trigger becomes actionable tomorrow, for the first time. It needs a **daily close** below the post-earnings shelf. If it gets there with an identifiable catalyst, that's a real setup; if it drifts there on the same no-news bleed, that's a weaker one and should be graded honestly.
- **FOMC minutes Wednesday** — anything opened Tuesday gets carried through it.
- **RDDT joins the S&P 500 at tomorrow's open.** Not a trade for us; noting it so the index-flow noise in tomorrow's tape is recognized for what it is.
- **AVGO earnings 2026-09-02** — kills any September-expiry AVGO structure regardless of how good the oversold read looks.
- **NVDA earnings 2026-08-26 pm** — on file for whoever builds the *next* NVDA setup. The old one is dead and stays dead.

---

*Positions were reconciled against the broker at 19:15–19:18 UTC: option positions, equity positions, portfolio, and today's full order history all match the ledger with zero drift. No violation flags are open.*
