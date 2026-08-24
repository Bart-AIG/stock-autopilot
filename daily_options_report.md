# Daily Options Report — Monday, 2026-08-24

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written at 14:20 CT / 19:20 UTC by the first run at or past the 14:15 CT window, from live quotes timestamped 19:16Z. Not deferred to a tidier slot.*

**One-line summary: you took the money off the table this morning and you were right to — your two closes booked +$286 realized (+14.8%), the desk's first green day in seven sessions, and everything the tape did afterward vindicated the exit. The desk itself placed nothing, for two reasons worth your attention: one setup was refused outright by the platform (agentic accounts cannot place spreads — discovered by actually sending one), and the one live trigger that fired all afternoon was for a trade the rulebook prices out of its own size band. Book is now a single hedge and $3,023.56 of cash.**

---

## 1. What we own

| Contract | Placed by | Basis | Mark 19:16Z | P/L at mark | What an exit nets (at bid) | DTE | Status |
|---|---|---|---|---|---|---|---|
| SPY 2026-11-20 700P ×1 | agentic (hedge) | 7.49 | 6.58 | −$91.00 / −12.15% | −$92.00 (bid 6.57, **0.30%** spread) | 88 | Working as designed |

**Book: basis $749 → mark value $658. Unrealized −$91.00.**

**Why we own it:** this is the authorized defensive hedge under your Aug–Oct drawdown posture — insurance, not a directional bet. It is *expected* to bleed in a flat-to-up tape and it is explicitly exempt from every premium backstop. Its decision point is the ~21-DTE roll/close conversation with you, which is still ~67 days out. Today it did its job in miniature: a −0.84% QQQ day moved it +$5 against a −$9.18/day theta burn, which is roughly what a 0.157-delta, 88-DTE put should do. No action.

---

## 2. Actions taken today

**By the desk: none.** Zero entries, zero exits. Twenty-fifth consecutive market-hours run declining to trade.

**By you, at 14:32–14:33Z — and this is the day's real event:**

| Contract | Qty | Basis | Exit | Realized |
|---|---|---|---|---|
| RBRK 2026-09-18 90P | 2 | 4.10 blended | 4.40 | **+$60.00 / +7.3%** |
| QQQ 2026-09-11 680P | 3 | 3.6867 blended | 4.44 | **+$226.00 / +20.4%** |

**Broker-confirmed total: +$286.00 realized on 2 closing trades, +14.85% on capital deployed.** (Sourced from `get_realized_pnl`, not from the journal — the journal is the thesis record, the broker is the ledger of record.)

**The honest read on your timing, because it's the most useful thing in this report:** you sold the QQQ puts at 4.44 into the morning's semi-led break. QQQ was ~706.5 then; it is 707.46 now, six hours later, having spent the entire afternoon chopping in a 1.3-point range that went nowhere. Had you held, the position would be worth roughly what it was worth when you sold, minus a day of theta. **You did not leave money on the table — you converted a working thesis into cash at the moment it stopped paying you to wait.** That is the pop-bank discipline this playbook keeps trying to codify, executed by hand.

It also closed out an open question. Both positions were MIXED ownership (one agentic lot, one yours), and my standing recommendation since Friday had been close-or-roll on the QQQ put at its 21-DTE review. You answered it by acting. The ledger, the exit ladder, and the monitoring mandate are all reconciled to the closes.

---

## 3. Candidates considered and SKIPPED — the educational section

Five things got real work today. None were placed. Here is exactly why, because four of the five failed for *structural* reasons rather than because the setups were bad — and that distinction is the thing to take away.

### (a) MSFT 2026-09-18 490/510 call vertical — **the platform refused it**
This was the best-structured candidate the desk has produced in weeks: MSFT was the only green name on the core board all day (+1.12% into a red tape), the trigger fired, the chain was clean (490C at 2.45% of mid, OI 7,013), and the vertical priced to a $800 ceiling with $1,205 max profit.

It was armed, triggered, priced, reviewed — and **sent**. `place_option_order` returned **HTTP 400: "Multi-leg options orders aren't supported in Robinhood agentic accounts yet."**

Two things about this you should know:
- **This is an agentic-API limit, not an account limit.** The account genuinely is `option_level_3`; the order endpoint just won't take a multi-leg order at any level.
- **`review_option_order` accepted the identical payload and returned a clean, healthy preview** — both legs, live quotes, greeks, an itemized fee block, no warning of any kind. The review endpoint does not run the multi-leg check that the place endpoint runs. A clean review is not proof an order is placeable; only a fill is.

The full spec is preserved in the ledger and can be revived intact if agentic multi-leg is ever enabled.

### (b) Legging that spread manually — **tested, and it is arithmetically impossible here**
The obvious workaround is to send the two legs as separate orders. The desk tested it rather than assuming, and the result is worth recording: `review_option_order` on a standalone short leg returns **`OPTION_NOT_ENOUGH_BP_FOR_COLLATERAL` demanding $67,500 in cash** — the full strike value.

The mechanism: **a spread's risk offset exists only inside a multi-leg order.** Sent alone, the short leg isn't "the short leg of a spread" — the broker has no way to know a long leg is meant to cover it, so it's margined as a fully cash-secured position. Legging destroys the exact property that makes a vertical capital-efficient. And the failure mode isn't a clean rejection: leg one fills, leg two is refused, and the sleeve is left holding an orphaned full-premium single leg at 4–9× the vertical's theta that it never decided to own.

**Practical consequence for you:** when a thesis genuinely wants a vertical, the desk will fully spec it — both legs, net debit, max profit, breakevens, invalidation — and hand it to you to place in the app, where multi-leg works normally. That preserves the carry advantage; it just moves the button-press to you.

### (c) MSFT 500C single leg (the substitute) — **declined on breakeven, not on cost**
With the spread unavailable, the natural move is to express the same view with a single call. The 500C was affordable ($935) and perfectly liquid. It was still declined: its **breakeven is 509.35 — essentially at the vertical's 510 short strike.** The single leg pays roughly nothing at exactly the price where the graded thesis said to bank $1,205.

Substituting the only vehicle that's left is fitting the trade to the platform. A cheap, liquid contract supplies no thesis.

### (d) QQQ tactical put on the failed-bounce trigger — **priced out of its own rulebook**
At 17:03Z a live, volume-confirmed downside trigger actually fired on QQQ. Everything was in place: five free slots, $2,773 deployable, chains superb (0.56–1.35% of mid), loss cap sitting at a +$286 *credit*. Priced at ~0.43–0.49 delta on the 11-DTE board:

| Vehicle | Cost | vs. $300–600 tactical band |
|---|---|---|
| **SPY 762P** | $535.50 | ✅ the only fit |
| QQQ 705P | $788.00 | ✗ +31% over |
| QQQ 708P | $911.50 | ✗ +52% over |
| NVDA 210P | $740.00 | ✗ +23% over |

The $300–600 tactical band sits inside the Four Laws, so no run may relax it, and re-labeling the trade "core" to escape the ceiling would be a governance failure even where the numbers work (they don't — the only qualifying core board prices at ~$1,605, A++ money for an A-minus setup).

**The trap worth naming:** SPY was the only affordable vehicle *because it was the leg holding up.* On a Nasdaq-specific de-rating (QQQ −0.84% vs SPY −0.22%), SPY's low premium and low realized move are the same fact. Buying it because it fits the band is buying the wrong index. Declining was correct — but be clear that **the ruleset, not the tape, was binding here.**

→ **This is the one thing on the list that's yours to decide** — see §5.

### (e) QQQ core re-entry — **no trigger, and it would have second-guessed you**
The house view (QQQ downside, below its 50-day at 713.44) is intact. But you banked exactly this exposure four hours earlier. Re-establishing the same position the same session, on a bounce, requires a *new* trigger — the mere persistence of a thesis is not one. The trigger written for it (a failed retest of the 50-day, or a decisive loss of the session low on expanding volume) never fired.

**Late-session note:** the downside trigger got to 2-of-3 at 19:03Z and has since *weakened* to 1-of-3 — SPY reclaimed 764.00, QQQ sits 0.72 above its 706.74 level, and the volume condition failed throughout (declines ran ~18.5k/min against the advance's ~24.5k). Sellers never arrived in size. No entry into the close.

---

## 4. Sleeve state

| | |
|---|---|
| **Premium at risk — tactical** | $0 (0 of 2 slots used) |
| **Premium at risk — core** | $0 (0 of 3 slots used) |
| **Hedge (excluded from caps)** | $749 basis / $658 mark |
| **Cash / `unleveraged_buying_power`** | **$3,023.56** (equal — no margin extended) |
| **Deployable after $250 reserve** | **$2,773.56** |
| **Realized P/L today** | **+$286.00** vs the −$400 cap — a credit, cap untouched |
| **Entries used today** | 0 of 8 |
| **Account equity** | $4,126.93 — above the $2,000 margin minimum |

For the first time in weeks the sleeve is **not** capital-constrained. Every prior flat day had a real budget excuse; today did not. Both slots and all the cash were free, and the desk still didn't trade — because the two setups that cleared the bar were blocked by the platform and the rulebook respectively, not because nothing looked good.

---

## 5. Tomorrow's watchpoints

1. **A decision for you: the tactical size band.** The $300–600 band and the "hunt SPY, QQQ, NVDA" instruction cannot both be satisfied on QQQ at current prices — QQQ tactical entries price $740–911. Today that combination vetoed a live, volume-confirmed trigger on a day with five free slots and $2,773 free. My recommendation: **widen the band to roughly $300–950**, keeping every other tactical gate (delta, ≤3% chains, time stop, −30% stop) intact and the ceiling still far below the $1,500 per-position max. The alternatives are to accept a SPY-only tactical track (clean, but SPY is often the wrong index) or to buy lower-delta QQQ strikes (worst — it discards the delta rationale the track exists for). *No approval is claimed or implied here; this needs a real turn from you.*
2. **Agentic multi-leg support.** Until it exists, the desk is single-leg-only, which means every core candidate carries 4–9× the theta the "prefer spreads" doctrine assumed when it set the bar. Verticals will be specced and handed to you rather than placed.
3. **QQQ 50-day MA at 713.44.** Friday closed exactly on it; today opened and stayed below. A failed retest into 712–713.44 is the cleanest core re-entry trigger on the board.
4. **Semi complex.** AMD −3.51%, TSLA −3.66%, NVDA −2.48%, TSM −2.15%, AVGO −2.08% against MSFT +1.12%. This is a two-day rotation *out of semis*, not a broad risk-off — SPY is down only 0.22% and holding above both its 20- and 50-day. Watch whether MSFT's divergence persists; a lone green mega-cap is either the tell or the trap.
5. **Hedge:** no action until ~21 DTE (late October). It is exempt from backstops by design.

---

*Book: 1 open contract (hedge). Realized today +$286.00, broker-sourced. No agentic entries or exits. Next run: Tuesday's open.*
