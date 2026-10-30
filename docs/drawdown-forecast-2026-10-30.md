# QQQ drawdown forecast, written 2026-10-30 (experiment)

Written mid-session on Fri 2026-10-30 at ~12:20 CT, QQQ $689.07. Purpose: a dated, scoreable prediction built from the research in that session. **Advisory only. No trade is placed from this file.**

## Starting state

| Input | Value |
|---|---|
| QQQ | $689.07 (−3.7% today, −1.4% yesterday) |
| Peak | $759.66 close, 2026-10-06 (17 trading days ago) |
| Drawdown | −9.3% |
| vs 200-day SMA | +1.5% (200-day ~$679); 50-day ~$725 |
| VIX | 21.07 = 1.23x its 1-yr median (17.2) |
| 10-yr yield | ~4.91%, 7-week low, down from ~5.26% on Oct 5 |
| IEF | +2.5% in 20 days; QQQ/IEF 20-day correlation −0.64 (bonds hedging again) |
| Cause | AI-capex fear: Alphabet (Thu), Amazon + Intel earnings (Fri). Structural type, not a shock |
| Pace | Structural (shocks reach −10% in a median 13 days; this has not in 17) |

## Evidence used

1. **All 29 past episodes where QQQ first closed 9% below its 252-day high (2003-2026, no survivorship):** further drop median −4.2%; under 3% more in 14, 3-10% more in 10, over 10% more in 5. Higher 3 months later in 24/29 (median +7.3%).
   - Slow pace + above 200-day: 8 episodes, further drop median −2.0%, 6/8 higher in 3 months.
   - Yields falling (IEF 20d >= +1%): 14 episodes, further drop median −5.7%, 13/14 higher in 3 months.
2. **Drawdown type:** shocks (n=9) bottom fast (median 20 days); structural (n=15) grind (median 42-47 days), and every −35%+ bear was structural with something breaking (earnings 2000, credit 2008, rising rates 2022).
3. **This bull's prior structural corrections:** 2023 −10.9%, Oct 2025-Mar 2026 −12.2%, Jun-Jul 2026 −11.3%.
4. **Yields falling into the selloff:** better 3-month outcomes than rising-yield selloffs (17/21 vs 6/13 higher), but since 2022 the falling-yield ones fell a further 6-15% first.
5. **VIX:** buying at ~2x the 1-yr median (~34-35) was the strongest signal; 1.75x (~30) works only when yields are not rising; 25-28 is the worst zone.
6. **Calendar:** Nov 3 midterms (low before the election in 7 of 8 cycles), Nov 6 jobs, Nov 10 CPI, Nvidia earnings mid/late Nov (date unverified).

## Forecast

"Low" = lowest QQQ close before QQQ closes back above $759.66.

| Scenario | Probability | Low | Total drawdown | When the low lands | Back to $759.66 |
|---|---|---|---|---|---|
| **A. Near the low already** | **45%** | $668-689 | −9% to −12% | by ~Nov 6 | late Dec 2026 to Jan 2027 |
| **B. Typical correction** | **38%** | $620-668 | −12% to −18% | ~Nov 10-25 | Feb-Mar 2027 |
| **C. Structural break** | **17%** | below $620 | worse than −18% | Dec 2026 or later | not before mid-2027 |

**Point forecasts**
- Lowest close: **~$665** (about −3.5% from here, −12.5% from peak), around **Nov 10-13**.
- VIX peak this episode: **25-32**. Chance VIX closes >= 30: **40%**. Chance it closes >= 35: **15%**.
- QQQ on **2026-11-20** (3 weeks): above $689 with **60%** probability.
- QQQ on **2027-01-29** (3 months): above $689 with **80%** probability; median **~$740**.
- QQQ closes below the 200-day at least once before the low: **65%**.

**What moves the odds**
- Toward C: a hyperscaler cuts its capex plan; NVDA/semis earnings estimates turn down; the 10-yr goes back above ~5.1% or IEF closes below $88.95; HYG breaks down.
- Toward A: QQQ reclaims the 200-day within 1-2 sessions of any undercut; yields keep easing; VIX never gets above ~25.

## Scoring checkpoints

| Date | Check |
|---|---|
| 2026-11-06 | Has the low printed (scenario A)? |
| 2026-11-13 | Low vs the ~$665 point forecast |
| 2026-11-20 | 3-week call (above $689?) |
| 2026-12-31 | Scenario A/B/C so far; VIX peak vs 25-32 |
| 2027-01-29 | 3-month call (above $689? vs ~$740 median) |

Score: which scenario happened; Brier score on the 60% (3-week), 80% (3-month), 40% (VIX >= 30) and 65% (200-day undercut) calls; absolute error on the low price and date.

## Honest limits

- Samples are small (29 episodes; 5-14 in the conditioned groups). The probabilities are judgment built on those base rates, not a fitted model.
- The yields-falling evidence pulls in two directions: better 3-month outcomes, but deeper first legs since 2022. Scenario B's 38% carries that.
- Data: Robinhood daily bars (QQQ 1999+, VIX 2002+, IEF 2002+). IEF price is a stand-in for the 10-yr yield. Two bad VIX prints (2023-01-09, 2023-11-02) were removed.

---

## Revision 1, same day (~12:45 CT): after checking Q3 earnings

The original forecast above stays as written so both versions can be scored.

### What the quarter showed

| Company | EPS vs est | What mattered | Stock |
|---|---|---|---|
| META (10/21) | 7.40 vs 5.74, beat | Raised 2026 capex floor to $135-145B | +3% |
| MSFT (10/28) | 4.89 vs 4.72, beat | Azure +48%, but **cut 2026 capex to $170B from $175B** | flat to −2% |
| GOOGL (10/28) | 2.12 vs 2.99, miss (an $8.7B equity loss) | Cloud +103%; capex held at $195-205B, not raised; negative free cash flow | −12% |
| AMZN (10/29) | 1.89 vs 1.97, miss | AWS +39% (fastest in ~5 yrs), $578B backlog; capex $77B vs $59B est; trailing FCF −$42B; weak Q4 guide | ~−7% |
| INTC (10/29) | 0.52 vs 0.37, beat | Q4 guide $15-16B vs $17.1B est; PC slump through 1H27; memory shortage → PC market −12% | −21% to −28%; AMD −10%, NVDA −3% |
| Others | ISRG, NFLX, TXN, TSLA, LRCX, CDNS, TMUS, KLAC all beat | | |

Sources: CNBC 2026-10-29 (Google and Microsoft put off raising capex), CNBC/Investing.com (Intel), Yahoo, earnings briefs; EPS from Robinhood's earnings calendar.

### Read

1. **Current earnings are fine** (11 of 13 large QQQ names beat) and cloud demand is accelerating. This is not a 2000-style revenue collapse.
2. **But the market now punishes the AI trade from both ends.** It sells the spenders for burning cash (AMZN, GOOGL) and sells the suppliers on any hint spending is levelling off (Microsoft's trim; Alphabet not raising). QQQ owns both sides. That squeeze is a real structural warning and the closest thing yet to the scenario C trigger.
3. **Memory costs are squeezing hardware** (Intel's PC outlook; Apple warned on memory costs).
4. **The decision point is now Nvidia on Nov 17 (after the close).** Structural corrections rarely bottom ahead of a known make-or-break event.

Upcoming: AAPL + PLTR Nov 2, AMD Nov 3 (election day), QCOM + ARM Nov 4, jobs Nov 6, CPI Nov 10, AMAT + CSCO Nov 12, **NVDA Nov 17**, INTU Nov 19.

### Revised forecast

| Call | Original | Revised |
|---|---|---|
| A. Near the low already | 45% | **35%** |
| B. Typical correction ($620-668) | 38% | **43%** |
| C. Structural break (below $620) | 17% | **22%** |
| Lowest close | ~$665, Nov 10-13 | **~$660, Nov 13-18** (around Nvidia) |
| VIX closes >= 30 | 40% | **45%** |
| Close below the 200-day before the low | 65% | **70%** |
| Above $689 on 2026-11-20 | 60% | **55%** |
| Above $689 on 2027-01-29 | 80% (median ~$740) | **75%** (median ~$730) |

Toward C: Nvidia guides data-center growth down or flat; another hyperscaler trims capex; AMD/AMAT echo Intel's weak outlook; yields turn back up.
Toward A: Apple and AMD reassure next week, Nvidia beats and raises, and yields keep falling.
