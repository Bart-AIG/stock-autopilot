# Daily Options Report — Monday, 2026-08-24

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written at 14:25 CT / 19:25 UTC by the first run at or past the 14:15 CT window, from live quotes timestamped 19:19:40Z. Broker-reconciled; not deferred to a tidier slot.*

**One-line summary: you banked +$286 this morning and the desk placed nothing — but today was not another quiet flat day. The desk got a real A-minus setup, its trigger fired, it sent the order, and Robinhood refused it: agentic accounts cannot place multi-leg options orders at all. Three days of "prefer debit spreads" doctrine turned out to rest on a capability nobody had tested. That is the finding of the day and it changes what the CORE track can do.**

---

## 1. What we own

| Contract | Placed by | Basis | Mark 19:19Z | P/L at mark | Exit nets (at bid) | DTE | Status |
|---|---|---|---|---|---|---|---|
| SPY 2026-11-20 700P ×1 | agentic (hedge) | 7.49 | 6.555 | −$93.50 / −12.48% | −$95.00 (bid 6.54, 0.46% spread) | 88 | Working as designed |

**Book: basis $749 → mark value $655.50. Unrealized −$93.50. Day: +$2.50** (Friday's official close 6.53 → 6.555) — the hedge gained while SPY fell, which is exactly its job.

**Why we own it:** this is the insurance leg of your Aug–Oct defensive posture, bought 2026-08-06 with SPY at 771.73. The 700 strike sits just below both the July-low shelf (716.6) and the rising 200-day (702.0), so it pays on a genuine trend break rather than a garden-variety dip. It is EXEMPT from every mechanical premium backstop — it is supposed to bleed in a melt-up. Next decision point is the ~21-DTE roll-or-close review with you around 2026-10-30. Delta −0.156, theta −$9.17/day, IV 20.50%, OI 25,846.

**After your two closes this is the only option position on the book.** The sleeve carries zero directional risk beyond the hedge. Equity side unchanged and untouched: PNC 1.825758 sh (~$445) — the desk never trades equities autonomously.

---

## 2. What happened today

### You closed both mixed-ownership positions at 14:32–14:33Z, for +$286

| | Contract | Qty | Fill | Proceeds | Basis | Realized |
|---|---|---|---|---|---|---|
| 14:32:58Z | RBRK 2026-09-18 90P | 2 | $4.40 | $880 | 4.10 blended | **+$60.00** |
| 14:33:25Z | QQQ 2026-09-11 680P | 3 | $4.44 | $1,332 | 3.686667 blended | **+$226.00** |

Both `placed_agent: "user"` — your trades, correctly so under the ownership gate. Broker-sourced: `get_realized_pnl` returns **+$286.00 on 2 closing trades, +14.85%**, reconciling to the cent against the order records. Nothing here consumes the −$400 daily loss cap; it is a credit.

Worth saying plainly, because it is the process point: the 14:20Z run paged you with a CLOSE recommendation on RBRK carrying the full number set, and you acted twelve minutes later. The monitoring mandate you set on 2026-08-18 ran its complete arc — monitor, stay silent through the routine drift, bring one page with the numbers attached, you make the call. That mandate is now dormant; the posture survives for any future position you choose in a live session.

### The desk placed zero trades — but it did send one order, and it was rejected

At 16:03Z the MSFT 2026-09-18 **490/510 call vertical** cleared everything. All three written trigger conditions fired (MSFT ≥ 489.00 at 489.81; two consecutive 5-minute closes ≥ 489.30 at 489.42 and 489.39; QQQ ≥ 703.00). News/thesis intact (Azure +43%, 52 buy / 0 sell, $569 average target vs $490 spot). IV fair on the ex-gap pair (0.525 raw / 1.006 ex-gap — the documented MSFT earnings-gap artifact). Trend maturity passed. Net debit $795 against a written $800 ceiling. Graded A-minus, armed since 15:05Z, and taken the moment it triggered.

`place_option_order` returned **HTTP 400: "Multi-leg options orders aren't supported in Robinhood agentic accounts yet."**

Three things about this matter more than the missed trade:

1. **It is an agentic-API limit, not an account limit.** `get_accounts` confirms 718757339 at `option_level_3` in the same run. Level 3 is real. The order endpoint simply will not take a multi-leg order at any level.
2. **`review_option_order` is a false green.** It accepted the identical payload and returned a complete, healthy preview — both legs, live quotes, greeks, an itemised fee block, a collateral block, and only a routine wide-spread note. Nothing hinted the order was unplaceable. A clean multi-leg review proves nothing; only a filled multi-leg order does.
3. **Legging around it is arithmetically impossible here, and the desk measured that rather than assuming it.** At 16:35Z it reviewed a standalone sell-to-open of a QQQ 675P — the natural short leg of a vertical — and got `OPTION_NOT_ENOUGH_BP_FOR_COLLATERAL` demanding **$67,500 cash** (the full strike value) against an account holding $3,023.56. A spread's risk offset exists only *inside* a multi-leg order; sent alone, leg two is margined as a cash-secured put. So legging would reliably fill leg one, get leg two rejected, and leave the sleeve holding a full-premium orphan single leg it never decided to own — at 4–9× the vertical's theta.

**The honest cost:** the "prefer debit spreads" doctrine was adopted 2026-08-21 from the `option_level_3` flag plus a theta measurement, and the executability underneath it was never tested. Every order on this account since 2026-08-19 has been single-leg. **A capability inferred from a permission flag is a hypothesis; the only proof a venue accepts an order type is a filled order of that type.** Three trading days of arming setups the desk could not place.

**What it means going forward:** CORE is single-leg-only, so CORE candidates must clear a *higher* bar than the spread doctrine assumed — every one now carries 4–9× the theta at roughly double the capital. A thesis that grades A-minus as a vertical is not automatically A-minus as a single leg. The MSFT case demonstrates it exactly: the 500C was cheap, liquid and affordable ($935, 0.41 delta, 3.21% of mid) and was still declined — not on cost, but on **breakeven 509.35, essentially at the vertical's 510 short strike**, so the single leg pays ~zero at precisely the price where the graded thesis said to bank $1,205. Substituting the only executable vehicle is fitting the trade to the platform.

**The spec is preserved verbatim** in `holdings.json._BLOCKED_SETUP`. If you want that trade, it is placeable by you in the app, where multi-leg works normally. The permanent fix is agentic multi-leg support.

---

## 3. What was considered and skipped — 28 market-hours runs, 25 consecutive declines

The most educational section. Grouped by what actually did the killing.

**Killed by the trigger never firing (the dominant reason, and the right one).** The tactical track requires an intraday level *actually breaking now*. Today produced four full reversals of read in two hours and never gave one:
- **SPY 2026-09-04 768C (upside)** — graded **B+** at 18:36Z and everything cleared but the trigger: liquidity 0.57% of mid, delta 0.445, $526 in-band, IV ~12% against a logged `iv_rv_ratio` of 1.038 (fair), exit plan writable in full. SPY's high was **765.11 against the 765.22 required** and QQQ's 709.53 against 709.79 — both missed in the *same minute*, by 0.11 and 0.26. The level was then rejected a third time and the whole advance retraced. A level that rejects a tape three times on its heaviest bars is resistance, not a breakout waiting to happen.
- **SPY 2026-09-04 762P (downside)** — graded **B**, the closest the desk came to a trade. At 19:03Z two of three legs had fired (SPY by a single cent) but QQQ was 0.90 above its 706.74 level, and the trigger's *volume* condition failed outright: the decline ran ~18.5k/min against the ~24.5k/min of the advance it was retracing. As of this writing it has gone backwards — SPY has reclaimed 764.00 (last closes 764.07, 764.22), so the trigger is now **1 of 3**, not 2.
- **QQQ continuation shorts, five separate attempts** (17:00Z, 17:16Z, 17:22Z, 17:47Z, 18:03Z) — each failed the same measured test: QQQ sat 4–5 points *above* the 702.70 session low, mid-range, with the leader (NVDA) reclaiming. Selling mid-range into a decelerating move is not a level break.

**Killed by the $300–600 tactical size band.** This is the constraint worth flagging to you, because today it bound on a day the trigger *did* fire. Priced at ~0.43–0.49 delta on the 2026-09-04 board: **SPY 762P $535.50 — the only one that fits**; QQQ 705P $788.00 (+31% over), QQQ 708P $911.50 (+52%), NVDA 210P $740.00 (+23%). Every chain was superb (0.56–1.35% of mid), capital was ample, all five slots free. **The tactical track is effectively a SPY-only track at this account size**, even though v4 names QQQ as a primary hunting ground. Rerouting to CORE fails on its own terms (CORE needs 21–45 DTE; the only qualifying board prices ~$1,605 — A++ money for an A-minus setup), and re-labelling to dodge a ceiling is a governance failure even when the numbers work. **Recommendation for you: widen the tactical band to roughly $300–950**, keeping every other tactical gate intact and leaving the ceiling well below the $1,500 per-position max. The alternatives are worse — accept SPY-only tactical, or buy a lower-delta QQQ strike, which discards the delta rationale the track exists for.

There is a trap inside this that is worth naming: on a Nasdaq-specific de-rating (QQQ −0.98% vs SPY −0.32% at the open), SPY is affordable *because* it is the leg that is holding. Low IV and low realized move are the same fact. Buying it because it fits the band is fitting the trade to the constraint.

**Killed by NVDA's Wednesday 2026-08-26 print.** The DTE-7 floor puts the earliest permissible expiry at ~2026-09-04, so **every** semi candidate spans the largest scheduled variance event on the board. That covered NVDA (215P/215C at 1.8% of mid on OI 33,845 — an excellent chain and still a no), AMD, TSM, AVGO, and 8 of the 19 setups on the committed equity report. IV independently killed NVDA anyway: 0.4093 with raw ratio 1.087 *and* ex-gap 1.219 — rich on both readings, which is the rare unambiguous case.

**Killed by coherence.** At 13:43Z the desk considered fresh QQQ puts and refused: it cannot in the same run tell you "sell your QQQ puts, theta is eating them" and simultaneously open new ones. That is a contradiction, not a judgement call.

**Killed by trend maturity — the ZTS failure mode, twice.** At 13:42Z, buying continuation puts eight minutes after a 1% gap down is buying the top of the intraday fear. At 16:33Z, the QQQ 2026-09-18 695P/700P bearish core idea had a genuinely superb case — 50-day lost decisively, narrow-down breadth, chains at 0.80% of mid, affordable — and was declined because **today's tape diverged**: QQQ had printed higher closes for an hour on expanding volume and was at its recovery high. Initiating a short into a mending tape with a catalyst three hours old and half-retraced is the exact error CLAUDE.md documents by name.

**Killed on the chain.** TSM and MSFT died on liquidity at the ATM strike in ~30 seconds each — before any thesis work — under the sourcing rule that screens liquidity first. Worth noting: the MSFT reading was later found to be a *measurement* artifact. The 13:39Z IV sweep recorded MSFT at 12.0% of mid on the **2026-09-25** board; the **2026-09-18 monthly** the same morning quoted 2.45% of mid on OI 7,013 — roughly 5× tighter, and the difference between "untradeable" and the best-structured candidate on the desk. Mega-cap monthlies carry the open interest; adjacent weeklies do not. An IV sweep measures IV, not liquidity — never let a spread observed during one disqualify a name.

---

## 4. Sleeve state

| | |
|---|---|
| Premium at risk | **$749** — the exempt hedge only. Zero agentic directional exposure. |
| Open positions | 1 (hedge, excluded from slot count). **0 of 2 TACTICAL, 0 of 3 CORE — all five slots free.** |
| Realized P/L today | **+$286.00** vs the −$400 cap → full **$400 headroom**, untouched |
| Entries used | **0 of 8** |
| Unleveraged buying power | **$3,023.56** (= `buying_power`, so **no margin extended**) |
| Deployable after the $250 reserve | **$2,773.56** |
| Account value | $4,123.69 (equity $445.13 / options $655 / cash $3,023.56) |

`unsettled_funds` shows $2,211.73 — the T+1 proceeds of your two sells — but the account is `limited_margin`, so settlement does not gate deployment and the broker's buying power already reflects it.

**Capital and slots were not the constraint today, and the desk says so plainly rather than hiding behind them.** Everything was available. What was missing was a setup that cleared its own written bar, and inventing one at 3pm on a tape that reversed four times is how the desk would have given back your +$286.

---

## 5. Tomorrow's watchpoints

1. **NVDA reports Wednesday 2026-08-26 after the close.** It gates every semi-adjacent candidate through Thursday, because the DTE-7 floor forces any permissible expiry to span it. Expect the desk to keep declining semis; that is the rule working, not a stall.
2. **QQQ 50-day MA — 713.44 as of Friday's bar, rising ~0.4/day (~713.8 Tuesday).** QQQ closed Friday exactly on it and opened below it today. A session close back above voids the bearish index premise entirely. Below it, the premise holds.
3. **The levels that actually matter for a downside entry:** QQQ session low **702.70**, SPY **762.08**. Today's trigger levels were intraday structure and expire with the session — they must not be inherited into Tuesday.
4. **The hedge needs nothing.** 88 DTE, exempt, next decision ~2026-10-30 at 21 DTE, and that one is yours.
5. **Two things for you, neither urgent:** the tactical size band recommendation in Section 3, and — if you want the MSFT 490/510 vertical — it is fully specced and placeable by you in the app. The desk cannot place it at any options level.

---

*Reconciliation 19:18–19:20Z: `get_option_positions(nonzero)` returns exactly one contract, matching `holdings.json` one-for-one, every `pending_*` field 0.0000 — no assignment, exercise, expiration or unauthorized fill. No HARD RULE 9 flags open. No Ryan approval is claimed or implied anywhere in this report; the two closes above are broker order records with `placed_agent: "user"`.*
