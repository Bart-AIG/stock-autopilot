# Intraday strategy backtest — run 2026-10-01 15:43Z

Runs on GitHub Actions (FMP key). 5-minute bars (1-minute is paywalled on this tier)
for QQQ and SPY, as far back as FMP serves them. Every strategy is flat at the close,
so it only uses capital intraday; the hurdle it must clear is what that capital would
earn in the core (QQQ ~16-23%/yr in the tests, QLD+200d ~20-34%).

## QQQ — 1950 full sessions, 2018-01-02 → 2026-09-30

| Strategy | CAGR 1x | Max DD 1x | Sharpe 1x | CAGR 3x | Max DD 3x | Days traded | Trades | Win % | Avg trade (bp, gross) |
|---|---|---|---|---|---|---|---|---|---|
| ORB-5 | -1.4% | -29.9% | -0.12 | -6.6% | -70.5% | 100% | 1943 | 24% | +1.6 |
| ORB-15 | -0.0% | -31.6% | 0.06 | -3.5% | -72.0% | 100% | 1945 | 31% | +2.3 |
| ORB-30 | 1.6% | -24.2% | 0.21 | 1.1% | -61.8% | 100% | 1945 | 37% | +3.0 |
| ORB-5 long-only | -0.6% | -15.7% | -0.06 | -3.0% | -41.8% | 51% | 997 | 24% | +1.7 |
| ORB-5 with 200d trend | -1.3% | -26.4% | -0.19 | -5.1% | -62.4% | 55% | 1069 | 25% | +1.1 |
| ORB-5 risk-sized, cap 1x (cash) | -1.7% | -29.9% | -0.15 | (sized) | | 100% | 1943 | 24% | +1.6 |
| ORB-5 risk-sized, cap 3x (via 3x ETF) | -5.5% | -62.1% | -0.14 | (sized) | | 100% | 1943 | 24% | +1.6 |
| ORB-5 risk-sized, cap 4x (paper) | -7.3% | -68.9% | -0.16 | (sized) | | 100% | 1943 | 24% | +1.6 |
| IMOM (15:30→close) | -5.9% | -48.0% | -1.32 | -17.3% | -86.7% | 100% | 1947 | 50% | -0.7 |
| NOISE-area breakout | 8.2% | -10.8% | 1.06 | 24.3% | -29.6% | 58% | 1832 | 46% | +9.6 |
| GAP_FADE >0.3% | -5.8% | -45.4% | -0.51 | -19.4% | -88.1% | 63% | 1226 | 59% | -1.8 |
| GAP_GO >0.3% | -0.6% | -31.1% | 0.03 | -7.0% | -75.5% | 63% | 1226 | 51% | +2.2 |
| OVERNIGHT (close→open) | 6.9% | -32.3% | 0.63 | 16.5% | -71.9% | 100% | 1949 | 57% | +5.3 |
| INTRADAY (open→close) | 0.2% | -31.2% | 0.10 | -7.9% | -77.4% | 100% | 1949 | 54% | +2.8 |
| **QQQ buy & hold** | 17.1% | -41.9% | 0.91 | | | 100% | | | |

**Calendar-year returns (1x, net of costs):**

| Strategy | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|
| ORB-5 | 8.3% | 1.6% | -2.1% | -4.3% | 3.4% | -8.3% | 0.8% | -4.2% | -6.5% |
| ORB-15 | 9.9% | 3.6% | -11.4% | -5.6% | -5.8% | 1.9% | 3.4% | 11.9% | -5.4% |
| ORB-30 | 9.1% | 2.9% | 3.9% | -5.1% | -4.4% | 1.4% | 6.3% | 10.6% | -8.6% |
| ORB-5 long-only | -4.4% | 6.6% | -5.7% | 0.3% | 11.2% | -4.2% | -3.6% | -1.4% | -2.7% |
| ORB-5 with 200d trend | 5.8% | 2.6% | -0.6% | 0.3% | -7.1% | -5.2% | -3.6% | -3.8% | 0.5% |
| ORB-5 risk-sized, cap 1x (cash) | 7.2% | 1.6% | -3.0% | -4.3% | 3.3% | -8.3% | 0.8% | -4.2% | -6.5% |
| ORB-5 risk-sized, cap 3x (via 3x ETF) | 11.1% | 3.0% | -3.4% | -10.5% | -0.2% | -20.9% | 1.9% | -8.0% | -16.8% |
| ORB-5 risk-sized, cap 4x (paper) | 10.2% | 6.5% | -8.3% | -12.6% | -1.7% | -24.5% | -1.2% | -7.1% | -19.3% |
| IMOM (15:30→close) | 1.1% | -5.2% | -5.5% | -11.2% | -12.4% | -8.3% | -3.3% | -7.6% | 1.6% |
| NOISE-area breakout | 21.9% | -2.0% | 7.6% | 3.4% | 12.0% | 13.1% | 8.6% | 6.4% | 2.5% |
| GAP_FADE >0.3% | -9.0% | -4.5% | -12.3% | 2.0% | -9.2% | -5.9% | -9.8% | 8.2% | -8.3% |
| GAP_GO >0.3% | 7.9% | -0.5% | 4.9% | -5.6% | 9.8% | -9.1% | 8.3% | -20.1% | 3.6% |
| OVERNIGHT (close→open) | 4.3% | 9.1% | 30.4% | 9.5% | -26.5% | 2.9% | 23.3% | 7.1% | 10.3% |
| INTRADAY (open→close) | -11.4% | 13.4% | 11.9% | 3.3% | -20.0% | 30.7% | -16.0% | 0.1% | -0.4% |
| QQQ buy & hold | 0.4% | 35.2% | 58.8% | 23.6% | -36.0% | 47.9% | 13.7% | 17.3% | 18.0% |

## SPY: no 5-minute data

**Reading it:** a day strategy only uses capital during the session, so compare its CAGR to what the same capital earns in the core (the buy & hold row, or QLD+200d at ~20-34%/yr in backtest_results.md). The 3x column is the same trades through a 3x ETF (TQQQ/SQQQ, UPRO/SPXU), intraday only.

## Data log

- QQQ 5min 2018-04-23..2018-04-29: None
- QQQ 5min 2018-04-30..2018-05-06: None
- QQQ 5min 2018-07-23..2018-07-29: None
- QQQ 5min 2018-07-30..2018-08-05: None
- QQQ 5min 2018-08-06..2018-08-12: None
- QQQ 5min 2018-12-10..2018-12-16: None
- QQQ 5min 2018-12-17..2018-12-23: None
- QQQ 5min 2018-12-24..2018-12-30: None
- QQQ 5min 2019-05-20..2019-05-26: None
- QQQ 5min 2019-05-27..2019-06-02: None
- QQQ 5min 2019-06-03..2019-06-09: None
- QQQ 5min 2019-11-11..2019-11-17: None
- QQQ 5min 2019-11-18..2019-11-24: None
- QQQ 5min 2019-11-25..2019-12-01: None
- QQQ 5min 2020-03-09..2020-03-15: None
- QQQ 5min 2020-03-16..2020-03-22: None
- QQQ 5min 2020-03-23..2020-03-29: None
- QQQ 5min 2020-06-08..2020-06-14: None
- QQQ 5min 2020-06-15..2020-06-21: None
- QQQ 5min 2020-06-22..2020-06-28: None
- QQQ 5min 2020-11-16..2020-11-22: None
- QQQ 5min 2020-11-23..2020-11-29: None
- QQQ 5min 2021-04-12..2021-04-18: None
- QQQ 5min 2021-04-19..2021-04-25: None
- QQQ 5min 2021-04-26..2021-05-02: None
- QQQ 5min 2021-10-04..2021-10-10: None
- QQQ 5min 2021-10-11..2021-10-17: None
- QQQ 5min 2021-10-18..2021-10-24: None
- QQQ 5min 2022-02-28..2022-03-06: None
- QQQ 5min 2022-03-07..2022-03-13: None
- QQQ 5min 2022-03-14..2022-03-20: None
- QQQ 5min 2022-07-18..2022-07-24: None
- QQQ 5min 2022-07-25..2022-07-31: None
- QQQ 5min 2022-08-01..2022-08-07: None
- QQQ 5min 2022-12-12..2022-12-18: None
- QQQ 5min 2022-12-19..2022-12-25: None
- QQQ 5min 2023-10-23..2023-10-29: None
- QQQ 5min 2023-10-30..2023-11-05: None
- QQQ 5min 2024-08-05..2024-08-11: None
- QQQ 5min 2024-08-12..2024-08-18: None
