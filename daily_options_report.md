# Daily options report — Tuesday, 2026-08-11

*Written by the options automation at 19:32 UTC (14:32 CT), the final run of the trading day. This file is overwritten daily; the compact version went out via ntfy.*

## 1. Open positions

**SPY 2026-11-20 $700 put — the defensive hedge (agentic-placed, 2026-08-06)**
- Entry $7.49 → mark $7.195 = **−3.9% (−$29.50)**. 101 days to expiry, delta −0.15.
- Why we own it: this is the insurance leg of your Aug–Oct drawdown-watch posture — it pays off on a genuine trend break below the July-low shelf (~716) and the rising 200-day MA (~702), not on a routine dip. It is *expected* to bleed a little in a calm, rising tape like today's; that's the cost of the coverage, which is why it's exempt from the mechanical premium backstops. It gets its roll/close decision with you at ~21 DTE (~Oct 30), or earlier if SPY breaks the 746–748 early-warning level (we'd then be glad we own it).

**ACHR 2028-01-21 $5 call — your LEAP (you placed it 2026-07-20, manual hold)**
- Entry $2.47 → mark $3.70 = **+49.8% (+$123)**. ACHR stock jumped **+12.1% today to $7.02**.
- Your standing instruction ("I'll handle the ACHR leap, just leave it be") is respected — the automation tracks it but takes no action and doesn't count it against the agentic budget. Worth knowing today's pop happened; the contract's delta is now 0.82, so it moves nearly share-for-share with the stock.

## 2. Actions taken today

**One exit: closed the CVS 2026-09-18 $100 call at 17:03Z for $0.92 — realized −$108.04 (−54%).**
How the decision was made: the position (38 DTE, in the 21–45 DTE tier) had printed ≤−50% on two consecutive runs, which under the exit engine triggers a thesis re-check rather than an automatic cut — and the re-check *failed*: CVS broke down through the setup level (it closed today −2.6% at $93.15, confirming the weakness), so both conditions of the tier rule were met and the close was mandatory. The alternative — holding for a bounce — is exactly what the hard backstop (−65%) exists to prevent once the underlying setup is gone. Order pricing followed the exit rule: started near the midpoint ($0.94), stepped toward the bid after ~50 seconds unfilled, and actually filled with price improvement at $0.92. The plan recorded at entry was followed as written.

**No new entries.** Zero of today's 14 runs produced a setup that passed the gates (see below).

## 3. Considered and SKIPPED (the education section)

- **AMD** — screened on all 14 runs. It's the top watchlist name: a deep uptrend (spot ~$475 vs 200-day MA ~$319) pulling back, RSI(2) at 17.6 through yesterday's close — *close* to the oversold dip-buy trigger, but the rule requires RSI(2) < 10, and that mathematically cannot print on a green day. AMD was green all day (+1.3% at the last check). Chasing it early would be buying before the signal exists. IV context from our own tracking: IV/RV ratio 0.68 — premium is cheap, so *if* the trigger prints, a plain long call is the favored structure. It stays watch-only into tomorrow.
- **NVDA** — screened on all 14 runs. RSI(2) neutral (~38), price flat (+0.2%). No signal of any kind; skipping costs nothing.
- **Final-run overlay:** even a marginal trigger would have been skipped on this last run — 29 minutes to the close with the July CPI print landing pre-market tomorrow is event risk, not a setup. Flat is a position.

## 4. Sleeve state

- **Premium at risk: $749 of the $1,500 budget** (the SPY hedge only — CVS freed up $200 of exposure when it closed). $751 of headroom for the next A-grade setup.
- **Realized P&L today: −$108.04** vs the −$400 daily cap — cap never threatened after the single exit.
- Account: $3,916 total, **$1,447 cash / $1,356 buying power**. CVS sale proceeds ($92) settle T+1 (tomorrow).
- Nothing is approaching an exit trigger or deadline: the hedge's 21-DTE review is ~Oct 30; the ACHR LEAP is yours and 17 months out.
- Weekly circuit breaker (−12% on the week): not close — this week's realized is the −$108 CVS exit.

## 5. Tomorrow's watchpoints

- **CPI, 8:30 AM ET — the day's main event.** Consensus: headline +0.1% m/m / 3.4% y/y, core +0.1% / 2.5%. A hot print pressures the tape (and helps the hedge); a cool print likely extends the rally and AMD's dip may resolve without ever triggering.
- **AMD**: watching for an RSI(2) < 10 print with the 20-day MA structure holding — that's the entry trigger; a close below the 200-day MA (~$319, far away) kills the thesis.
- **SPY 746–748**: the defensive-posture early-warning level. A *closing* break flips the playbook firmly defensive.
- **Earnings**: NBIS (am) and CSCO (pm) tomorrow, AMAT Thursday pm — AI-infra/semicap read-throughs for the watchlist names; none are held.
