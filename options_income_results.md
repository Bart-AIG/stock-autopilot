# Options-income sleeves — run 2026-10-01 15:50Z

## 1. DIY covered call ("run the QQQI strategy ourselves") — model vs the real funds

| Check | Real fund (CAGR / max DD) | Our model | QQQ same period |
|---|---|---|---|
| QYLD (real) vs model "ATM, 100% covered (QYLD-style)", 2016-07-05 → 2026-10-01 | 10.2% / -25% | 12.9% / -19% | 21.6% / -35% |
| QQQI (real) vs model "2% OTM + buy 6% OTM call (QQQI-style call spread)", 2024-01-31 → 2026-10-01 | 20.6% / -20% | 19.7% / -20% | 24.6% / -23% |

| Covered-call variant (CAGR / max DD) | 2007–2026 | 2008 crisis | 2019–2026 | 2022 | 2023–2026 |
|---|---|---|---|---|---|
| QQQ buy & hold | 21.0% / -35% | n/a | 23.1% / -35% | -33.5% / -35% | 32.3% / -23% |
| ATM, 100% covered (QYLD-style) | 12.8% / -19% | n/a | 13.8% / -19% | -15.9% / -19% | 19.3% / -15% |
| 2% OTM, 100% covered | 17.5% / -22% | n/a | 18.3% / -22% | -18.4% / -22% | 23.6% / -17% |
| 2% OTM + buy 6% OTM call (QQQI-style call spread) | 14.6% / -33% | n/a | 15.4% / -33% | -31.3% / -33% | 24.6% / -20% |
| 1% OTM + buy 5% OTM call | 13.2% / -33% | n/a | 14.3% / -33% | -31.9% / -33% | 24.1% / -19% |
| 2% OTM, 50% covered | 19.6% / -29% | n/a | 20.8% / -29% | -26.2% / -29% | 28.0% / -20% |

## 2. QuantGlide-style 0DTE credit spread — structural test on SPY (1999 sessions)

P&L in units of spread width; the credit is an assumption because no option prices are available. QuantGlide's own example: $0.45 credit on a 15-point spread = 3% of width.

| Short strike distance | Direction | Trades / yr | Win rate | Avg loss when breached (x width) | Max-loss days | Breakeven credit (% of width) |
|---|---|---|---|---|---|---|
| 1.5× expected move | with morning direction | 186 | 97.8% | 0.81 | 21 | 2.3% |
| 1.5× expected move | fade (reverse) | 186 | 98.2% | 0.79 | 19 | 2.0% |
| 2.0× expected move | with morning direction | 186 | 99.2% | 0.76 | 7 | 1.1% |
| 2.0× expected move | fade (reverse) | 186 | 99.3% | 0.84 | 8 | 1.1% |
| 2.5× expected move | with morning direction | 186 | 99.6% | 0.72 | 4 | 0.8% |
| 2.5× expected move | fade (reverse) | 186 | 99.6% | 0.63 | 3 | 0.8% |

**Sleeve returns (CAGR / max DD) at 10% and 30% of the sleeve at risk per trade:**

| Distance | Credit | 10% at risk | 30% at risk (QuantGlide sizing) |
|---|---|---|---|
| 1.5× | 2% | -5.9% / -50% | -25.5% / -95% |
| 1.5× | 3% | 12.1% / -30% | 25.8% / -73% |
| 1.5× | 5% | 60.9% / -21% | 268.8% / -56% |
| 2.0× | 2% | 16.0% / -14% | 50.2% / -42% |
| 2.0× | 3% | 38.5% / -11% | 155.1% / -34% |
| 2.0× | 5% | 99.6% / -10% | 656.8% / -30% |
| 2.5× | 2% | 23.1% / -14% | 82.9% / -42% |
| 2.5× | 3% | 47.1% / -11% | 211.1% / -34% |
| 2.5× | 5% | 112.1% / -10% | 826.1% / -30% |

## 3. Portfolios, 2019-01-02 → 2026-10-01, monthly rebalance

CORE = vol-targeted QQQ core; SWING-M = swing rules on the momentum picks (trading at the close; the earlier test lost ~25% of swing return trading at 15:50); CC = DIY QQQI (2% OTM + 6% OTM call bought); 0DTE = 2.0× distance, 3% credit, 10% at risk per trade.

| CORE / SWING-M / CC / 0DTE | CAGR | Max DD | Sharpe | Worst year | $3,340 becomes |
|---|---|---|---|---|---|
| QQQ buy & hold | 23.1% | -35.1% | 0.99 | -32.6% | $16,782 |
| 50 / 50 / 0 / 0 | 27.1% | -16.6% | 1.30 | -3.2% | $21,337 |
| 40 / 40 / 20 / 0 | 24.9% | -17.6% | 1.26 | -9.2% | $18,567 |
| 35 / 35 / 30 / 0 | 23.7% | -18.1% | 1.22 | -12.1% | $17,289 |
| 30 / 30 / 40 / 0 | 22.5% | -19.1% | 1.18 | -14.9% | $16,079 |
| 45 / 45 / 0 / 10 | 28.5% | -14.9% | 1.47 | -1.1% | $23,223 |
| 40 / 40 / 0 / 20 | 29.9% | -13.4% | 1.68 | 1.0% | $25,213 |
| 35 / 35 / 20 / 10 | 26.2% | -15.9% | 1.44 | -7.2% | $20,184 |
| 0 / 0 / 100 / 0 | 15.4% | -32.6% | 0.81 | -30.5% | $10,137 |
| 0 / 0 / 0 / 100 | 39.7% | -10.5% | 3.51 | 18.1% | $44,528 |

## Data log

- SPY 5min 2018-08-27..2018-09-02: None
- SPY 5min 2018-09-03..2018-09-09: None
- SPY 5min 2018-09-10..2018-09-16: None
- SPY 5min 2018-09-24..2018-09-30: None
- SPY 5min 2018-10-01..2018-10-07: None
- SPY 5min 2018-10-08..2018-10-14: None
- SPY 5min 2019-06-24..2019-06-30: None
- SPY 5min 2019-07-01..2019-07-07: None
- SPY 5min 2019-07-08..2019-07-14: None
- SPY 5min 2020-04-06..2020-04-12: None
- SPY 5min 2020-04-13..2020-04-19: None
- SPY 5min 2020-04-20..2020-04-26: None
- SPY 5min 2020-10-05..2020-10-11: None
- SPY 5min 2020-10-12..2020-10-18: None
- SPY 5min 2020-10-19..2020-10-25: None
- SPY 5min 2021-05-31..2021-06-06: None
- SPY 5min 2021-06-07..2021-06-13: None
- SPY 5min 2021-06-14..2021-06-20: None
- SPY 5min 2021-11-29..2021-12-05: None
- SPY 5min 2021-12-06..2021-12-12: None
