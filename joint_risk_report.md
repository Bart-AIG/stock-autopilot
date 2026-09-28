# Joint risk watch

RISK GREEN (0) - No benchmark alert near triggering, but the new per-holding health check (first run under v2) flags 13 of 35 joint positions WEAK on price trend + fundamentals -- review list only, no sale recommended at GREEN.

_Run 2026-09-28T15:46Z (hourly :40 slot, ~15:41Z quotes). Joint account 116713985343._

## What changed this run
- Alert log since the 14:41Z run: **nothing fired.**
- Tier: **GREEN, unchanged** (score 0, same as the 13:42Z and 14:41Z runs today).
- **New this run:** `risk_watch.py` v2 (merged just before this run, commit `dec2637`) added the per-holding health check. This is the **first run** that has ever computed it -- `joint_risk_state.json.holding_health` was empty going in. All 13 WEAK / 6 WATCH flags below are new information, not a change in the market -- that is why this run notifies even though the benchmark tier itself didn't move.

## Benchmark table (nearest-to-triggering first)
| Symbol | Condition | Level | Price (~15:41Z) | Distance to trigger |
|---|---|---|---|---|
| IEF | below | 88.95 | 89.32 | +0.41% |
| SPY | below 50-day SMA (761.57) | 761.57 | 765.10 | +0.46% |
| TIP | below | 102.85 | 103.99 | +1.11% |
| HYG | below | 76.35 | 77.46 | +1.45% |
| IEF | above | 91.10 | 89.32 | -1.96% |
| IEF | below | 87.35 | 89.32 | +2.25% |
| SPY | below | 729.00 | 765.10 | +4.95% |
| USO | above | 163.80 | 153.81 | -6.10% |
| QQQ | below | 689.00 | 734.66 | +6.63% |
| KRE | below | 65.25 | 70.74 | +8.41% |
| SPY | below | 690.00 | 765.10 | +10.88% |
| VIXY | above | 21.15 | 16.88 | -20.19% |

Closest to firing: **IEF < 88.95** (+0.41%) and **SPY under its 50-day** (+0.46%). Both would only push the tier from GREEN to YELLOW (1 point each) -- no single benchmark trigger gets this book to ORANGE on its own; that needs two-plus firing together or a deep-level breach (SPY <700, QQQ <670, IEF <88).

## Margin
**$18,082 of margin in use** (cash -$18,082.36 on `get_portfolio`), byte-for-byte unchanged from the 13:42Z and 14:41Z runs today -- no new margin activity. This is against the 2026-08-05 decision to keep this account unlevered, and it predates this run; not a new finding, carried forward for visibility. `sell_plan()` does not raise cash for it at GREEN (raise_usd $0) -- it only enters the plan once the tier is YELLOW+.

## HOLDINGS HEALTH (new this run -- price trend vs 50d/200d SMA and 1-yr high, plus quarterly revenue/margin trend; 13-month daily history, financials cached for today)

**WEAK (13, sorted by severity):**
- **VST** pts 7 -- under 50-day, under 200-day, -35% off 1-yr high, revenue -5% YoY. $1,640 position (12 sh, cost $145.76 vs $136.66).
- **CEG** pts 6 -- under 50-day, under 200-day, -36% off 1-yr high, net margin 14%→7%. $258 (1 sh, cost $255.27).
- **FIG** pts 6 -- under 50-day, under 200-day, -71% off 1-yr high, net margin 11%→-30%. $2,581 (127 sh, cost $20.42) -- post-IPO round trip, well-known; near breakeven on cost.
- **UBER** pts 6 -- under 50-day, under 200-day, -32% off 1-yr high, revenue growth slowing +20%→+14%→+12%. $690 (10.08 sh, cost $73.41).
- **ADBE** pts 5 -- under 50-day, under 200-day, -36% off 1-yr high. $2,309 (10.01 sh, cost $233.23) -- fundamentals (revenue/margin) still clean; this is a pure price-trend flag.
- **LDOS** pts 5 -- under 50-day, under 200-day, -39% off 1-yr high. $758 (6.22 sh, cost $114.78).
- **BMEA** pts 5 -- under 50-day, under 200-day, -51% off 1-yr high. $650 (500 sh, cost $1.76) -- micro-cap biotech, no financials data.
- **NOC** pts 5 -- under 50-day, under 200-day, -33% off 1-yr high. $515 (1.01 sh, cost $526.22).
- **APP** pts 5 -- under 50-day, under 200-day, -58% off 1-yr high. $2,478 (8 sh, cost $326.62) -- fundamentals (65% net margin, still growing) still strong; pure price-trend flag off an extreme high.
- **CRCL** pts 4 -- under 200-day, -43% off 1-yr high. $3,427 (40 sh, cost $91.11) -- post-IPO round trip.
- **CRDO** pts 4 -- under 50-day, -37% off 1-yr high, revenue growth decelerating +201%→+157%→+115% YoY. $3,987 (20.82 sh, cost $161.49) -- still triple-digit growth; flagged for deceleration off an extreme base, not a business problem.
- **PGR** pts 4 -- under 50-day, under 200-day, revenue growth slowing +12%→+9%→+7% YoY. $880 (4.24 sh, cost $218.73).
- **LMT** pts 4 -- under 50-day, under 200-day, -23% off 1-yr high. $234 (0.45 sh, cost $564.31).

**WATCH (6):** EME (under 50/200-day), ACGL (under 50/200-day), CI (under 50/200-day), NOW (-31% off 1-yr high), REGN (under 50-day, net margin 38%→30%).

**OK (16):** TEM, QQQ, AMD, NVDA, QQQI, MU, XOM, APH, HOOD, META, GOOGL, AMZN, RBRK, MRVL, V, JPM, GILD -- no material flags.

**Not priced:** EPIX^ (25 sh, $0 cost basis) is an inactive instrument on the equity-quotes feed -- likely a spin-off/rights remnant. No live price, so no health read; worth a manual look in-app since it carries zero value on this ledger and may just be dust.

## SELL LIST
**None.** Tier is GREEN -- `sell_plan()` returns no sale recommendation. The 13 WEAK names above are a **review list only**: nothing to act on today. If the tier moves to YELLOW or worse, these are the names that go first (WEAK sold before concentration trims), non-core names first, core names (MSFT/GOOGL/AMZN/META/NOW/ADBE/ZTS/ISRG/RBRK/V/JPM/QQQI) trimmed at most 50% rather than exited.

Two of the WEAK flags (ADBE, APP) are pure price-trend -- their fundamentals still read clean this quarter -- worth keeping in mind if this list is ever acted on: a price-only flag is a different animal from one with a fundamental flag attached (VST, CEG, FIG, UBER, PGR, CRDO all carry at least one).

## What would move the tier up from GREEN
Nearest live triggers (see benchmark table): **IEF below 88.95** (+0.41% away) and **SPY closing under its 50-day SMA 761.57** (+0.46% away) would each add 1 point (YELLOW starts at 2, so either alone keeps it GREEN/borderline -- both together would cross into YELLOW). A deep-level breach (SPY <700, QQQ <670, IEF <88) adds a bonus point on top of its base weight.
