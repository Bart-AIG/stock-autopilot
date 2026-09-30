# Options-income sleeves — run 2026-09-30 01:38Z

## 1. DIY covered call ("run the QQQI strategy ourselves") — model vs the real funds

| Check | Real fund (CAGR / max DD) | Our model | QQQ same period |
|---|---|---|---|
| QYLD (real) vs model "ATM, 100% covered (QYLD-style)", 2016-07-05 → 2026-09-29 | 10.2% / -25% | 12.8% / -19% | 21.6% / -35% |
| QQQI (real) vs model "2% OTM + buy 6% OTM call (QQQI-style call spread)", 2024-01-31 → 2026-09-29 | 20.7% / -20% | 19.9% / -20% | 24.6% / -23% |

| Covered-call variant (CAGR / max DD) | 2007–2026 | 2008 crisis | 2019–2026 | 2022 | 2023–2026 |
|---|---|---|---|---|---|
| QQQ buy & hold | 21.1% / -35% | n/a | 23.1% / -35% | -33.5% / -35% | 32.3% / -23% |
| ATM, 100% covered (QYLD-style) | 12.8% / -19% | n/a | 13.7% / -19% | -15.9% / -19% | 19.3% / -15% |
| 2% OTM, 100% covered | 17.5% / -22% | n/a | 18.3% / -22% | -18.4% / -22% | 23.7% / -17% |
| 2% OTM + buy 6% OTM call (QQQI-style call spread) | 14.6% / -33% | n/a | 15.4% / -33% | -31.3% / -33% | 24.7% / -20% |
| 1% OTM + buy 5% OTM call | 13.3% / -33% | n/a | 14.3% / -33% | -31.9% / -33% | 24.2% / -19% |
| 2% OTM, 50% covered | 19.6% / -29% | n/a | 20.8% / -29% | -26.2% / -29% | 28.1% / -20% |

## 2. QuantGlide-style 0DTE credit spread — structural test on SPY (2174 sessions)

P&L in units of spread width; the credit is an assumption because no option prices are available. QuantGlide's own example: $0.45 credit on a 15-point spread = 3% of width.

| Short strike distance | Direction | Trades / yr | Win rate | Avg loss when breached (x width) | Max-loss days | Breakeven credit (% of width) |
|---|---|---|---|---|---|---|
| 1.5× expected move | with morning direction | 185 | 97.7% | 0.79 | 22 | 2.3% |
| 1.5× expected move | fade (reverse) | 185 | 98.1% | 0.78 | 20 | 2.0% |
| 2.0× expected move | with morning direction | 185 | 99.2% | 0.75 | 8 | 1.1% |
| 2.0× expected move | fade (reverse) | 185 | 99.2% | 0.87 | 10 | 1.2% |
| 2.5× expected move | with morning direction | 185 | 99.6% | 0.76 | 5 | 0.8% |
| 2.5× expected move | fade (reverse) | 185 | 99.6% | 0.65 | 3 | 0.8% |

**Sleeve returns (CAGR / max DD) at 10% and 30% of the sleeve at risk per trade:**

| Distance | Credit | 10% at risk | 30% at risk (QuantGlide sizing) |
|---|---|---|---|
| 1.5× | 2% | -7.7% / -61% | -30.8% / -97% |
| 1.5× | 3% | 11.5% / -38% | 21.8% / -84% |
| 1.5× | 5% | 64.5% / -22% | 288.9% / -61% |
| 2.0× | 2% | 17.5% / -14% | 55.3% / -42% |
| 2.0× | 3% | 42.2% / -11% | 175.1% / -34% |
| 2.0× | 5% | 111.0% / -10% | 790.6% / -30% |
| 2.5× | 2% | 24.2% / -14% | 86.7% / -42% |
| 2.5× | 3% | 50.5% / -11% | 231.3% / -34% |
| 2.5× | 5% | 123.4% / -10% | 975.9% / -30% |

## 3. Portfolios, 2019-01-02 → 2026-09-29, monthly rebalance

CORE = vol-targeted QQQ core; SWING-M = swing rules on the momentum picks (trading at the close; the earlier test lost ~25% of swing return trading at 15:50); CC = DIY QQQI (2% OTM + 6% OTM call bought); 0DTE = 2.0× distance, 3% credit, 10% at risk per trade.

| CORE / SWING-M / CC / 0DTE | CAGR | Max DD | Sharpe | Worst year | $3,340 becomes |
|---|---|---|---|---|---|
| QQQ buy & hold | 23.1% | -35.1% | 0.99 | -32.6% | $16,776 |
| 50 / 50 / 0 / 0 | 28.2% | -16.8% | 1.34 | -3.3% | $22,763 |
| 40 / 40 / 20 / 0 | 25.7% | -17.8% | 1.30 | -9.3% | $19,555 |
| 35 / 35 / 30 / 0 | 24.4% | -18.3% | 1.26 | -12.1% | $18,093 |
| 30 / 30 / 40 / 0 | 23.2% | -19.5% | 1.21 | -15.0% | $16,720 |
| 45 / 45 / 0 / 10 | 29.9% | -15.1% | 1.54 | -0.3% | $25,131 |
| 40 / 40 / 0 / 20 | 31.5% | -13.4% | 1.76 | 2.8% | $27,668 |
| 35 / 35 / 20 / 10 | 27.3% | -16.1% | 1.49 | -6.4% | $21,564 |
| 0 / 0 / 100 / 0 | 15.4% | -32.6% | 0.81 | -30.5% | $10,155 |
| 0 / 0 / 0 / 100 | 43.3% | -10.5% | 3.62 | 26.6% | $54,194 |

## Data log

- (clean)
