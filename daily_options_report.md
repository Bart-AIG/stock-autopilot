# Daily Options Report — Wednesday, 2026-08-12

*Agentic account (cash, ••••7339). Written on the last run of the trading day (19:32 UTC / 14:32 CT). Plain-language by design — the point is that you can see how each decision was made, not just what it was.*

**One-line summary: no trades today. Both positions held on their own rules, and the one setup we armed never printed its trigger. The sleeve ends the day exactly where it started.**

---

## 1. Positions we own

| Contract | Placed by | Entry | Mark now | P/L | DTE | Status |
|---|---|---|---|---|---|---|
| SPY 2026-11-20 700 PUT ×1 | agentic | $7.49 ($749) | $6.585 | **−$90.50 (−12.1%)** | 100 | HOLD — insurance, exempt from stops |
| ACHR 2028-01-21 5 CALL ×1 | **you** | $2.47 ($247) | $3.075 | **+$60.50 (+24.5%)** | 527 | NO ACTION — your trade, hands off |

**Why we own the SPY put.** This is the defensive hedge you authorized on Aug 5 for the Aug–Oct drawdown watch. It pays off if the market genuinely breaks trend — the 700 strike sits just under the July-low shelf (716.6) and the rising 200-day MA (702), so it's insurance against a real break, not a normal dip. Today SPY printed near all-time highs (772.91, +0.31%), which is exactly the tape where a hedge bleeds. **That bleed is the cost of the insurance, not a broken trade** — which is why the rules explicitly exempt this position from the −50%/−70% premium backstops that would force a sale on any other losing option. Its next real decision point is a roll-or-close conversation with you around **Oct 30** (~21 DTE). Nothing about today changes that.

**Why we own the ACHR call.** You bought this Jan-2028 LEAP yourself on Jul 20 and told me on Jul 22 to leave it alone. So the automation only ever *watches* it. It's up +24.5% and healthy. It does not count against the sleeve's $1,500 budget, because that budget only governs trades the automation places itself.

---

## 2. Actions taken today

**None. No entries, no exits, no rolls.** Twenty-eight scheduled runs, all no-action — and that was the right outcome each time, for the reasons in the next section.

---

## 3. What we looked at and skipped — and exactly why

This is the section worth reading, because it's where the day's actual work went.

### INTC — the one setup we armed, and why we still didn't buy it

INTC was the best candidate found all day, and I want to be clear about why it *still* didn't become a trade.

**The bull case was real.** Intel's $20B equity offering (210M shares at $95, upsized from $15B) priced on Aug 10 and closed today. That dilution fear is what took the stock from $140.94 in June down to $81.88 in late July — a −42% drop. With the shares actually placed and ~$19.7B raised for AI/foundry capex, a *hanging risk* became a *finished event*. The stock had reclaimed the $95 deal price and was still 27% below its June high, so the recovery had room. It's in the momentum top decile, above its 200-day MA. Premium was cheap: implied vol 68% against realized vol 84% (ratio 0.81) — the options were charging *less* than the stock's actual daily movement, which favors buying a plain call. And it was affordable: a properly-sized 0.42-delta Sep-18 110 call cost ~$595 with 44,946 open interest and a 3.4%-wide spread. Everything that usually blocks us — money, liquidity, IV — passed.

**So what stopped it? Entry timing.** When I armed this setup at 18:05 UTC I wrote down, in advance, the only two prices that would make it a buy: **either** a pullback into $97–100 that *holds* above the $95 offering price, **or** a decisive close above the $105.45 July-21 swing high. INTC spent the entire afternoon in the dead zone between them — $102.26, $102.72, $102.54, $102.51, and $101.61 at the final check, up about +4% on the day.

Buying at $101.61 would have meant buying a mid-day rip in a name whose confirmation signal is *specifically a pullback that holds*. That is chasing. It's also the exact mistake that cost us on ZTS on Aug 10 — following a move that had already happened instead of one that was starting.

**The discipline that matters: I didn't loosen the trigger to make the trade fit.** With five runs left in the day it would have been easy to add a third, vaguer condition and call it confirmed. The setup stays armed with the structure already priced, so a future run can act the moment a real level prints — without improvising.

### AMD and TSM — good setups, wrong size for our wallet

Both confirmed technically today. AMD held its gap (482.85, above the 474.32 confirm level); TSM held above its 50-day MA (430.08 vs 426). Cheap IV on both (ratios 0.68 and 0.77), tight spreads, real open interest.

**They failed on budget, and it's worth understanding why that's a hard no rather than a "buy something smaller."** The hedge uses $749 of the $1,500 sleeve budget, leaving $751. A properly-sized ~0.35-delta call costs roughly **$1,900 on AMD** and **$1,100 on TSM** — measured from live broker prices, not estimated. What $751 *would* buy is AMD at 0.15–0.18 delta: a far-out-of-the-money lottery ticket that needs a huge move just to break even.

Buying the weak version of a setup because it's the version that fits the leftover cash is backwards. Flat was the correct position.

**One durable fix came out of this.** Thirteen consecutive runs today re-derived that same affordability wall from scratch. So the live prices are now written into `market_brief.json` as a measured "affordability frontier," along with a rule of thumb: at 30–45 DTE a 0.35-delta call costs roughly 4.5–6.5% of the share price. With $751 free, that means hunting names priced **$60–150**, not $400+ mega-caps. That's how INTC got found in the first place — and it corrected an earlier, too-pessimistic note claiming the sleeve was structurally locked into being hedge-only. It isn't.

### Also screened and dropped

- **AEHR ($133.35)** — in the affordable band, but +13.8% on the day. Chasing a 14% spike is the definition of a late-stage entry.
- **CRWV / NBIS / SMCI** — reported earnings and gapped +9% to +18%. The move already happened; reaction plays fail the trend-maturity gate.
- **NVDA ($222.70)** — in a healthy uptrend above all its moving averages, but no oversold dip and no fresh catalyst. Earnings approach in late August. Watch only.
- **CSCO** — reports tonight. We don't buy into earnings unless earnings *is* the thesis.
- **LITE, MU, LIN, TSEM, BE** — all priced out of the budget band.

---

## 4. Sleeve state

| Metric | Value | Limit | Headroom |
|---|---|---|---|
| Agentic premium at risk | **$749** (SPY hedge) | $1,500 | $751 free |
| Realized options P/L today | **$0** | −$400 daily cap | untouched |
| Open agentic positions | **1** (hedge) | 3 (hedge excluded) | full room |
| Settled cash / buying power | **$1,447.47** | — | budget cap binds first, not cash |
| Account total value | **$3,830.53** | — | equity $1,415 / options $968 / cash $1,447 |

Yesterday's realized loss (CVS, −$108.04) is closed and does not carry into today's cap.

**Nothing is near an exit trigger.** The hedge is exempt by design; ACHR is yours and untouchable. No DTE deadlines, no earnings conflicts, no backstop levels in play.

---

## 5. Tomorrow's watchpoints

1. **INTC — the armed trigger stands.** Buy only on a pullback into **$97–100 that holds above $95**, or a decisive close above **$105.45**. Structure is pre-priced: Sep-18 110C ~$595 (0.42 delta) or 115C ~$457 (0.34 delta). Kill level: a close below **$95** means the offering price failed as support and the trade is off entirely.
2. **AMAT reports tomorrow after the close** — a semicap read-through for the whole AI-semiconductor complex. It could move AMD/TSM/NVDA. No pre-earnings position.
3. **CSCO earnings tonight** — networking/AI-capex read-through, same rule.
4. **Levels:** SPY closing below **746–748** is the early-warning tripwire for your defensive posture (we're far above it at 772.91). QQQ's 20-day sits at 700.7.
5. **PPI and retail sales later this week** — the next macro inputs after today's in-line CPI.

---

## Sources & method

Positions, quotes, greeks, IV and option chains: Robinhood connector, live at 19:30–19:32 UTC. Macro/CPI and news: web search plus FMP. IV context computed from `iv_history.json` (day 2 of tracking — fewer than 20 readings, so IV-vs-realized ratios are used rather than percentiles). Equity setups cross-checked against the committed `latest_intraday.md` (19:02 UTC). Full run-by-run reasoning is in `trade_journal.json`.
