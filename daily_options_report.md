# Daily Options Report — Tuesday 2026-08-11

*Written 14:35 CT by the options automation (EOD run). Overwritten daily — this file always holds the latest trading day.*

**The day in one paragraph:** A quiet, disciplined day. The sleeve took one loss — the CVS Sept 100C was closed at the confirmed −50% backstop for −$108.04 — and made zero new entries across 14 runs, because nothing on the watchlist actually triggered. That's the system working, not the system idling: AMD spent the whole day close to a dip-buy signal but never confirmed it, and buying before confirmation is exactly the kind of forced trade the rules exist to prevent. Tomorrow morning's CPI print is the event that will likely decide the next move.

---

## 1. Open positions

**SPY 2026-11-20 $700 PUT** — the defensive hedge (agentic-placed 2026-08-06)
- Entry $7.49 → mark $7.20 = **−$29 (−3.9%)**. 101 days to expiry. Delta −0.15, IV 21%.
- *Why we own it:* This is the insurance Ryan authorized under the Aug–Oct drawdown watch — it pays off if SPY breaks its trend (the strike sits just below the July-low shelf at 716.6 and the rising 200-day MA at ~702), and it's expected to slowly lose money if the market stays calm. That slow bleed is the cost of insurance, so it is exempt from the mechanical loss-cut rules; the decision point is the ~21-days-to-expiry review (~Oct 30) with Ryan.
- *Today:* SPY closed the session area around $770.7 (−0.3%) — comfortably above the 746–748 early-warning level, so nothing to do.

**ACHR 2028-01-21 $5 CALL** — Ryan's LEAP (user-placed 2026-07-20)
- Entry $2.47 → mark $3.70 = **+$123 (+49.8%)**. ~17 months to expiry. Delta 0.82.
- *Why we own it:* Ryan's personal long-term eVTOL bet, deep in the money and behaving mostly like stock now. Under his standing "leave it be" instruction the automation tracks it but never touches it — it also doesn't count against the automation's $1,500 budget.

## 2. Actions taken today

**SOLD to close: CVS 2026-09-18 $100 CALL at $0.92 (17:03 UTC) — realized −$108.04 (−54%)**
- *The rule that fired:* For contracts 21–45 days from expiry, a −50% premium drawdown isn't an automatic sale — it triggers a re-check: the loss must hold ≤−50% for two consecutive runs AND the thesis re-check must fail. Both conditions met today: the mark had sat below −50% since yesterday, and the thesis re-check went against the position (the 2027 Caremark-membership/340B warning that had already downgraded CVS from "buy more" to "weakened" — the bounce the call needed no longer had a fundamental driver behind it).
- *Why not wait for a bounce?* That's what the two-run confirmation is for — one bad print is noise, a held −54% with a weakened thesis and 38 days left is a position spending theta on hope. The backstop exists so a true loser can't ride toward zero.
- *Execution detail (the exit-pricing rule in practice):* the sell was priced near the midpoint first ($0.94), not slammed at the bid; after ~50 seconds unfilled it stepped to $0.90 because a confirmed backstop exit is time-sensitive — and filled at $0.92 with price improvement. Lesson: patience at the midpoint costs nothing and often claws back a few dollars of the spread.
- One process action worth noting: this was the first day under the v3 routine prompt, so the automation bootstrapped its new self-tracking files (daily market brief, IV history, trade journal) this morning.

## 3. Considered and SKIPPED (the education section)

**AMD long call — skipped all 14 runs.** The setup we wanted: AMD is in a deep uptrend (+46% above its 200-day MA) and pulling back — a classic dip-buy candidate. The rule requires the RSI(2) to actually print below 10 (genuinely oversold) with price holding the 20-day MA. It came into the day at RSI(2) ≈ 17.6 — close, but not there — and then rallied +1.1% today, and an oversold confirm mathematically cannot print on an up day. *Why so strict?* Buying "almost oversold" is buying an ordinary red candle in a name that could keep pulling back for a week; the RSI(2)<10 gate is what separates a stretched rubber band from a mild dip. IV context said single-leg calls are the right structure if it ever triggers (options pricing cheap vs realized vol, ratio 0.68) — so the trade is pre-planned, just not triggered. It stays on the watchlist.

**NVDA long call — skipped all day.** Flat tape (+0.1%), RSI(2) neutral, no catalyst. "It's NVDA and it usually goes up" is not a thesis — no signal, no trade.

**Nothing else made the funnel.** No new catalyst hit intraday (no VIX spike, no brief-level break), so the brief's watchlist was the whole candidate pool. Conviction gate reminder: anything scoring below 7/10 is a skip, and flat is a position.

## 4. Sleeve state

- **Premium at risk: $749 of the $1,500 budget** (SPY hedge only — the CVS close freed $200). $751 available for new entries.
- **Realized P&L today: −$108.04** vs the −$400 daily loss cap → $291.96 of headroom; the cap never gated anything today.
- **Entry throttle:** 0 of 3 daily entries used. **Open agentic positions:** 1 of 3 (the hedge doesn't count toward the 3).
- **Approaching triggers:** none imminent. The hedge's 21-DTE review is ~Oct 30. No open position has earnings inside its window.
- Broker positions reconcile exactly against `holdings.json`; no flags outstanding.

## 5. Tomorrow's watchpoints (Wed 2026-08-12)

1. **CPI, 7:30 AM CT — the main event.** Consensus: headline +0.1% m/m / 3.4% y/y, core +0.1% / 2.5%. The Fed is publicly split (Iran-oil inflation risk vs Friday's weak jobs report), so a surprise in either direction moves rates expectations and the whole tape. A hot print pressures SPY toward the 746–748 tripwire (where the hedge starts earning its keep); a cool print likely extends the risk-on tape and keeps the hedge bleeding slowly — both are fine, that's what insurance is for.
2. **AMD dip-buy watch:** a red day that prints RSI(2) < 10 with the 20-day MA holding = the pre-planned long-call entry (single-leg favored, cheap IV). No confirm, no trade.
3. **Earnings:** NBIS before the open, CSCO after the close (AI-infra/networking read-throughs; nothing held reports). AMAT Thursday PM.
4. **Standing level:** a *closing* SPY break of 746–748 flips the playbook firmly defensive per the Aug–Oct posture.
