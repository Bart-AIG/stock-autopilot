# Strategy shortlist (saved 2026-09-30, Ryan: "lets remember these options")

All figures are 2019–2026 backtests (`mix_results.md`). The "pessimistic" column re-runs each mix with:
- swing trades at 15:50 instead of the close;
- a 25% haircut on the momentum-swing sleeve;
- a 2% 0DTE credit instead of 3%.

QQQ buy & hold: 23.1%/yr, max drawdown −35%. Splits are CORE / SWING_M / SWING_Q / DAY / ODTE, in %.

**Sleeve definitions:**
- **CORE:** vol-targeted QQQ (25% ÷ 20-day realized vol, ≤ 2×) while QQQ is above its 200-day SMA; T-bills otherwise.
- **SWING_M:** RSI(2) + IBS + turn-of-month swing rules on the monthly top-10 12-month-momentum names (end-2018 S&P 100 + Nasdaq-100 lists), 1×.
- **SWING_Q:** the same swing rules on QQQ, 2× (QLD).
- **DAY:** noise-area breakout. **Excluded:** it failed on 30-minute bars.
- **ODTE:** SPX/XSP 0DTE credit spread, 2× the expected move, 10% of the sleeve at risk per trade. The credit is unverified; log real quotes first.

| Option | Split | As tested | Pessimistic | Needs |
|---|---|---|---|---|
| Steady | 50 / 50 / 0 / 0 / 0 | 28.2% / −17% | 24.6% / −15% | nothing new |
| Higher return (walk-forward pick) | 0 / 30 / 70 / 0 / 0 | 38.4% / −22% on unseen 2023–26 | 27.7% / −23% | nothing new |
| Lowest drawdown | 30 / 30 / 20 / 0 / 20 | 34.2% / −13.6% | 24.8% / −13% | 0DTE credit verified |
| Best overall (walk-forward pick) | 0 / 20 / 60 / 0 / 20 | 39.7% / −17% | 26.4% / −19% | 0DTE credit verified |

**Rules for using this shortlist:**
- Cap 0DTE at 20% of the account.
- Plan on the pessimistic column.

**Open work (Ryan, 2026-09-30):**
- a research-driven high-growth sleeve (10–15%): tested 2026-09-30 with stand-ins (audit §16). **Best overall + growth = CORE 0 / SWING_M 20 / SWING_Q 50 / DAY 0 / ODTE 20 / GROWTH 10**, funded from SWING_Q. Start at 10%, not 15%. Paper-track it against SWING_Q first;
- ~~a re-calibrated day-trading sleeve~~: tested 2026-09-30 (stocks-in-play, exit plan fixed at entry, 15-minute monitoring). Every version was −1.6% to −5.6%/yr against QQQ's +22.8%. DAY stays at 0% (audit §15).
