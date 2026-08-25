# Daily Options Report — Tuesday, 2026-08-25

*Agentic account (••••7339, `limited_margin` / `option_level_3`). Written at 14:25 CT / 19:25 UTC by the first run at or past the 14:15 CT window, from live quotes timestamped 19:19Z. Not deferred to a tidier slot.*

**One-line summary: a flat day by decision, not by absence — the desk hunted both tracks across 27 runs, had its one tactical trigger actually fire at 18:45Z, and declined it; the more useful news is what the last 40 minutes did, which is that the break was not merely unheld but actively rejected, and NVDA has spent the final hour giving back its whole day into its own print tomorrow. Book is one hedge and $3,023.56 of cash. Nothing was bought, nothing was sold, $0.00 realized against a −$400 cap.**

---

## 1. What we own

| Contract | Placed by | Basis | Mark 19:19Z | P/L at mark | What an exit nets (at bid) | DTE | Status |
|---|---|---|---|---|---|---|---|
| SPY 2026-11-20 700P ×1 | agentic (hedge) | 7.49 | 6.225 | **−$126.50 / −16.89%** | −$128.00 (bid 6.21, **0.48%** spread) | 87 | Working as designed |

**Book: basis $749.00 → mark value $622.50. Unrealized −$126.50.**

**Why we own it:** the authorized defensive hedge under your Aug–Oct drawdown posture. It is insurance, not a directional bet — it is *supposed* to bleed in a tape that grinds up, and it is explicitly exempt from every premium backstop precisely so a run cannot talk itself into cutting it on a red number. Today it behaved exactly like the 0.151-delta, 87-DTE put it is: theta −$9.00/day against a +0.46% QQQ day, so it gave back roughly a day of carry and nothing more. Its only scheduled decision is the ~21-DTE roll/close conversation **with you**, around 2026-10-30. No action, and no run today re-litigated it.

Lot invariant asserted on every run: 1 × 7.49 × 100 = $749.00 = `max_loss` = broker `average_price`. Zero drift.

---

## 2. Actions taken today

**None.** No entry, no exit, no order sent. Broker-confirmed: `get_realized_pnl` returns **0 closing trades and $0.00 realized** for 2026-08-25.

That is the honest headline, and I want to separate two things that look identical from the outside: a desk that found nothing, and a desk that found something and said no. Today was the second. The tactical trigger the morning runs armed **actually fired** — and was declined on merits that were written down *before* it fired, which is the only version of this that counts.

---

## 3. What we considered and skipped — the educational section

### 3a. The tactical QQQ long — the trigger FIRED and we passed

This is the one worth reading. The desk armed a two-sided trigger on QQQ's 20-day SMA (710.3985) with a strict three-part clause: a **completed** 5-minute close beyond the level, **holding** beyond it on the following bar, on volume materially above the **trailing-30-minute** mean.

At **18:45Z it fired both entry clauses for the first time all session**:

- **Price:** completed close 710.570, clearing the level by +0.1715.
- **Volume:** 117,971 reconciled = **168.8%** of the reconciled trailing-30 baseline (69,902/bar). A clean clear on both raw and reconciled readings — for the first time today the data-quality caveat was *not* the deciding factor.
- **Hold:** **failed.** 18:50Z closed 710.340 (−0.0585 below); 18:55Z 710.260 (−0.1385 below).

Sixth failed level test of the session, first on the upside. And it would have been declined anyway: an entry with under an hour left buys a scalp whose entire life is Wednesday's pre-print drift, and whose hard time stop forces it flat *before* the only event that would move it. Paying the spread and a day of theta to be liquidated immediately ahead of the catalyst is the worst version of that trade, not a protected one. **Grade C.**

### 3b. What the last 40 minutes added — the break was REJECTED, not just unheld

This is new since the 19:00Z run, which read the tape as "chop at a moving average." It has resolved, and not upward. Measured off completed 5-minute bars:

- The five completed bars after the break ran **88,017/bar = 125.9% of the pre-break baseline** — while price fell **−0.810 points** (710.570 → 709.760). From the break high 710.670 to the 19:15Z low 709.4499 is **−1.220 points**.
- The last completed close (19:10Z, 709.760) sits **0.6385 BELOW** the level it broke 25 minutes earlier.

Sustained above-baseline volume with price going the other way is not a break fading on thin drift — that is active selling into the break. The correct read on the day's one fired trigger is now stronger than "unconfirmed": it was **faded**.

*(Caveat kept honest: the 19:15Z bar was still forming and this session documented a feed defect that truncates the newest bar, so every conclusion above is anchored on the 19:10Z completed bar. If anything the defect **understates** the rejection volume.)*

### 3c. NVDA reversed the divergence six runs had been carrying

Every run since 17:22Z logged the same standout: NVDA firming to session highs while QQQ faded. **That has now closed in the opposite direction from the one the 18:45Z run recorded.** NVDA printed its session high of **213.435** on the 19:00Z bar and has since fallen to **211.94 — −1.495 / −0.70% in twenty minutes, on 1.91× its early-afternoon volume rate** (572,385/bar vs 299,819/bar).

QQQ did not rally up to NVDA. NVDA came down to QQQ, and led it down.

Why this matters more than a price tick: the standing reason to stay flat has been "do not open into the 08-26 NVDA print." That was an inherited rule. This afternoon the **market did the same thing independently** — positioning came *off* into the print, on rising volume, in the final hour. The posture is now corroborated rather than merely asserted. It also **retires the "NVDA is firming into its print" observation** before it could be inherited into tomorrow as a bullish tell, which is exactly the kind of stale read this desk keeps having to correct.

### 3d. CORE swing — blocked on tech, hunted anyway on non-tech

- **Index and mega-cap tech: blocked, and the block is DATED, not structural.** CORE needs 21–45 DTE; the nearest qualifying board (2026-09-18, 24 DTE) spans the NVDA print. The exit engine says close *before* earnings, not open into them, and the "unless earnings IS the thesis" exception does not apply — the desk has no edge on a print the entire market is positioned for. **This expires with the print.** Runs on 08-27 must hunt CORE properly rather than quoting today's block.
- **NVDA itself — the single most tempting trade on the board — was disqualified on a measurement, not a hunch.** Reading this desk's own `iv_history.json` as a time series showed **four consecutive sessions of monotonic ATM-IV expansion into the print, on falling spot**, while every other core name's ratio stayed flat. You are being asked to pay up for the event. No.
- **The non-tech sidestep was worked nine names deep** so the block could not become an excuse to skip the hunt: TLT, GDX, GLD, EEM, XLV, XLU, IWM, SLV, XLF. Every one declined on its own gate — TLT on a stale catalyst plus an ex-gap IV ratio of 1.122 and a breakeven above its 50-day; GDX and GLD on measured trend maturity; EEM on "why NOW"; the rest on inertness. TLT is worth noting as a genuine near-miss: a CORE-eligible, tightly-quoted chain (09-18 84C at 1.68% of mid, 0.415 delta, 51,155 OI) that failed on merits rather than on tradeability.
- **Fresh RSI2 names off the 17:01Z equity report, all four dead:** CRWD (2026-08-26 print inside the hold window), TSEM and AMAT (semis — the *most* print-correlated group, not a sidestep of it; **re-screen AMAT on 08-27**), GEV (coarse 0.10/0.05 tick tier killed it free of charge, and grid-power-for-AI is not an uncorrelated name anyway).

---

## 4. Sleeve state

| | |
|---|---|
| Account value | **$4,092.03** — equity $445.47 / options $623.00 / cash $3,023.56 |
| Premium at risk — TACTICAL | **$0.00** (0 of 2 slots) |
| Premium at risk — CORE | **$0.00** (0 of 3 slots) |
| Hedge (excluded from slots) | $749.00 basis, $622.50 mark |
| `unleveraged_buying_power` | **$3,023.56** — equals `buying_power`, so **no margin is extended** |
| Deployable after the $250 reserve | **$2,773.56** |
| Realized P/L today | **$0.00** vs the −$400 cap — not binding |
| Entries used | **0 of 8** |

Nothing was scarce today. Five free slots, $2,773.56 deployable, the loss cap untouched. **The constraint was never capital — it was that nothing cleared the bar**, which is the correct reason to be flat and the one I'd rather report than a trade taken to look busy.

---

## 5. Tomorrow's watchpoints

1. **NVDA reports after the close on 2026-08-26.** That is the event the whole board is arranged around. The desk does not open into it.
2. **The 20-day SMA is RETIRED as a level — do not carry 710.3985 into tomorrow.** Its roll-off was computed for the first time today and it is climbing steeply as the late-July crash closes leave the window: with QQQ *motionless* the level goes 710.40 → **712.14 tomorrow** → 714.58 Wednesday → 717.04 by Friday. QQQ must rally ~1.74 points overnight merely to stand still against it. A run that re-derives only its *value* each morning will keep scoring a widening gap as a near-miss.
3. **Live structural references for 08-26:** the session high/low and the 50-day (713.2256 as of the 08-24 close — which needs the same roll-off treatment before anyone quotes it). Re-derive both halves of any trigger, price and volume, off the same window, on the run that tests it. Inherit nothing.
4. **The CORE block expires with the print.** 08-27 runs hunt CORE properly. Re-screen AMAT.
5. **A real calendar hole to plan around:** the 2026-09-18 board is CORE-eligible only through 08-28 (21 DTE), and the next monthly (10-16) does not enter the 21–45 window until 09-01. TLT was checked and carries 09-25/09-30 boards so it has no gap — but a monthly-only name would.
6. **Hedge:** no action until the ~21-DTE review around 2026-10-30, and that decision is yours, not the desk's.

---

*Twenty-seven scheduled runs today, zero orders. The day's one fired trigger was declined on a written pre-condition and then faded by the tape within the hour, which is the outcome that argues the gate was set in the right place.*
