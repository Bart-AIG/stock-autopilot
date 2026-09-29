# Process backtest — run 2026-09-29 19:43Z

Data sources (daily): {'historical-price-eod/dividend-adjusted': 238}. Names with history: 238.

## Part A — equity process, 2019-01-02 → 2026-09-29

Universe: 236 names + SPY/QQQ (today's scan list — survivorship-biased, so compare strategies to EACH OTHER first, to the benchmark second). Fills at the signal close ±5 bp; `_lag1` fills at the next close.

| Strategy | CAGR | vs SPY | vs QQQ | Max DD | Sharpe | Avg invested | Trades | Win % | Payoff | Avg hold (d) |
|---|---|---|---|---|---|---|---|---|---|---|
| **SPY buy & hold** | 17.2% | | | -33.7% | 0.93 | 100% | | | | |
| **QQQ buy & hold** | 23.1% | | | -35.1% | 0.99 | 100% | | | | |
| GRADE_HOLD_any | 81.9% | +64.6% | +58.7% | -47.0% | 1.45 | 93% | 210 | 47% | 3.84 | 33 |
| ROTATE_MONTHLY_QQQcore_lag1 | 54.8% | +37.6% | +31.7% | -51.1% | 1.08 | 99% | 105 | 58% | 2.90 | 62 |
| ROTATE_MONTHLY_lag1 | 53.9% | +36.7% | +30.8% | -50.9% | 1.07 | 90% | 105 | 58% | 2.90 | 62 |
| ROTATE_MONTHLY_QQQcore | 52.5% | +35.3% | +29.4% | -52.8% | 1.05 | 99% | 107 | 59% | 2.40 | 61 |
| ROTATE_MONTHLY | 50.2% | +32.9% | +27.0% | -52.8% | 1.03 | 91% | 107 | 59% | 2.40 | 61 |
| ROTATE_MONTHLY_8 | 49.1% | +31.9% | +26.0% | -44.8% | 1.16 | 85% | 198 | 56% | 3.11 | 62 |
| LEADER_lag1 | 32.4% | +15.2% | +9.3% | -36.4% | 1.13 | 91% | 386 | 42% | 2.84 | 18 |
| GRADE_HOLD_lag1 | 30.1% | +12.8% | +6.9% | -34.1% | 1.00 | 92% | 319 | 45% | 2.58 | 22 |
| OLD_CONNORS | 27.7% | +10.5% | +4.6% | -39.6% | 0.99 | 88% | 1110 | 79% | 0.39 | 6 |
| CURRENT_QQQcore | 26.8% | +9.5% | +3.6% | -34.9% | 1.03 | 99% | 1303 | 70% | 0.60 | 4 |
| LEADER_QQQcore | 26.3% | +9.1% | +3.2% | -44.1% | 0.93 | 100% | 387 | 34% | 3.39 | 18 |
| LEADER_nocut | 25.9% | +8.6% | +2.7% | -34.3% | 0.92 | 91% | 338 | 38% | 2.99 | 20 |
| CURRENT_2pct | 24.8% | +7.5% | +1.6% | -28.6% | 1.06 | 65% | 1303 | 70% | 0.60 | 4 |
| GRADE_HOLD | 24.7% | +7.5% | +1.6% | -30.4% | 0.90 | 91% | 313 | 40% | 2.86 | 22 |
| LEADER | 24.3% | +7.1% | +1.2% | -38.6% | 0.91 | 90% | 383 | 34% | 3.34 | 18 |
| CURRENT_lag1 | 20.5% | +3.2% | -2.7% | -21.8% | 1.13 | 51% | 1254 | 63% | 0.85 | 4 |
| CURRENT | 18.8% | +1.6% | -4.3% | -22.5% | 1.06 | 50% | 1303 | 70% | 0.60 | 4 |

### Calendar-year returns

| Strategy | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 31.1% | 18.3% | 28.7% | -18.2% | 26.2% | 24.9% | 17.7% | 13.0% |
| **QQQ** | 38.4% | 48.6% | 27.4% | -32.6% | 54.9% | 25.6% | 20.8% | 20.6% |
| CURRENT | 16.4% | 39.3% | 25.2% | -12.3% | 35.9% | 24.9% | 12.6% | 11.8% |
| CURRENT_lag1 | 24.6% | 31.2% | 47.1% | -9.8% | 28.6% | 28.8% | 16.8% | 0.6% |
| CURRENT_2pct | 21.6% | 53.5% | 33.5% | -16.1% | 48.7% | 33.0% | 16.2% | 15.3% |
| CURRENT_QQQcore | 29.1% | 82.2% | 37.0% | -26.7% | 52.9% | 24.8% | 24.5% | 11.6% |
| LEADER | 32.6% | 45.7% | 66.3% | -27.3% | 4.9% | 34.1% | 40.6% | 16.6% |
| LEADER_lag1 | 38.8% | 68.0% | 76.5% | -27.6% | 11.7% | 36.5% | 57.3% | 23.1% |
| LEADER_QQQcore | 37.2% | 49.0% | 77.0% | -28.6% | 7.7% | 28.2% | 42.3% | 20.5% |
| LEADER_nocut | 36.7% | 55.5% | 61.5% | -12.5% | 18.3% | 34.4% | 22.5% | 1.4% |
| GRADE_HOLD | 36.7% | 53.8% | 54.3% | -0.1% | -9.6% | 31.6% | 34.4% | 6.8% |
| GRADE_HOLD_lag1 | 32.9% | 63.1% | 68.0% | -3.4% | -12.3% | 42.6% | 43.4% | 21.2% |
| GRADE_HOLD_any | 45.9% | 362.5% | 39.0% | -8.3% | 41.8% | 200.1% | 23.3% | 127.1% |
| ROTATE_MONTHLY | 23.3% | 163.6% | -3.1% | 2.7% | 12.0% | 373.6% | -0.3% | 35.9% |
| ROTATE_MONTHLY_lag1 | 41.7% | 147.9% | -17.8% | 5.5% | 15.5% | 397.6% | -5.4% | 69.7% |
| ROTATE_MONTHLY_QQQcore | 26.5% | 168.1% | 1.2% | -0.5% | 18.6% | 380.8% | -0.5% | 35.5% |
| ROTATE_MONTHLY_QQQcore_lag1 | 45.0% | 151.5% | -15.2% | 0.3% | 19.0% | 408.0% | -6.2% | 67.6% |
| ROTATE_MONTHLY_8 | 18.6% | 188.8% | 14.0% | 1.7% | 16.1% | 160.7% | 21.7% | 50.7% |
| OLD_CONNORS | 33.6% | 65.6% | -4.5% | 8.4% | 5.8% | 13.2% | 68.0% | 44.0% |

### Exit mix and definitions

- **CURRENT** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 901, 'grade_exit': 402}
- **CURRENT_lag1** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 851, 'grade_exit': 403}
- **CURRENT_2pct** — Same exits, only a 2% cash reserve (options bucket returned to stocks). Exits: {'rsi2_tp': 901, 'grade_exit': 402}
- **CURRENT_QQQcore** — Same exits, idle cash parked in QQQ. Exits: {'rsi2_tp': 901, 'grade_exit': 402}
- **LEADER** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 115, 'grade_exit': 246, 'trail': 22}
- **LEADER_lag1** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 120, 'grade_exit': 243, 'trail': 23}
- **LEADER_QQQcore** — LEADER with idle cash in QQQ. Exits: {'loss_cut': 113, 'grade_exit': 251, 'trail': 23}
- **LEADER_nocut** — Grade exit + 15% trail, no loss cut. Exits: {'grade_exit': 303, 'trail': 35}
- **GRADE_HOLD** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 313}
- **GRADE_HOLD_lag1** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 319}
- **GRADE_HOLD_any** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 210}
- **ROTATE_MONTHLY** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 107}
- **ROTATE_MONTHLY_lag1** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 105}
- **ROTATE_MONTHLY_QQQcore** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 107}
- **ROTATE_MONTHLY_QQQcore_lag1** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 105}
- **ROTATE_MONTHLY_8** — ROTATE_MONTHLY with 8 slots. Exits: {'grade_exit': 198}
- **OLD_CONNORS** — Pre-2026-09-25 screen for reference: RSI2<10 above a rising 200SMA; RSI2>=70 TP; 14-day time stop. Exits: {'rsi2_tp': 881, 'time_stop': 229}

_Part A compute: 162s._

## Part B — day track (QQQ 5-min opening-range breakout)

_1-minute QQQ history is not available on this FMP tier — Part B could not run. See the fetch log below._

## Data log

- 1-min fetch 2024-09-29..2024-10-03 failed: {'_http_error': 402}
