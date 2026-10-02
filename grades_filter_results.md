# Do the valuation and disruption grades improve SWING_M?

Run 2026-10-02 21:20Z. Universe: S&P 100 + Nasdaq 100 as of 2018 (159 names). Period 2019-01-02 to 2026-10-02. Grades computed point in time by the production valuation.py / disruption.py from annual statements filed by each month-end; no analyst forecasts, targets or research notes (no history exists). A filtered name is replaced by the next-ranked one, so every variant holds 10.

## SWING_M with each filter (1x, close-to-close, as in mix_optimizer.py)

| Variant | CAGR | Max DD | Sharpe | 2019-22 CAGR | 2023-26 CAGR | Months a pick changed |
|---|---|---|---|---|---|---|
| BASE | 29.8% | -21.1% | 1.34 | 27.2% | 33.4% | 0 of 95 |
| NO_DISRUPTED | 26.3% | -18.5% | 1.24 | 26.4% | 27.0% | 39 of 95 |
| NO_AT_RISK | 27.4% | -17.9% | 1.32 | 30.4% | 25.0% | 95 of 95 |
| NO_EXPENSIVE | 17.6% | -17.9% | 1.01 | 23.6% | 11.7% | 95 of 95 |
| NO_RICH | 21.6% | -17.9% | 1.09 | 23.7% | 19.4% | 95 of 95 |
| PREFER_CHEAP | 23.2% | -18.7% | 1.21 | 21.7% | 25.1% | 94 of 95 |

## Next-month buy-and-hold return of the top-20 momentum names, by grade

| Grade | n | Mean | Median | Share positive |
|---|---|---|---|---|
| all: all | 1880 | +2.05% | +1.34% | 56% |
| dis: AT RISK | 436 | +1.45% | +0.88% | 54% |
| dis: BEING DISRUPTED | 67 | +5.12% | +2.63% | 61% |
| dis: DISRUPTOR | 25 | -0.64% | +0.03% | 52% |
| dis: INNOVATING | 496 | +3.22% | +2.02% | 60% |
| dis: STABLE | 856 | +1.51% | +0.94% | 54% |
| val: DEEP VALUE | 72 | +3.25% | +3.31% | 64% |
| val: EXPENSIVE | 1001 | +2.17% | +1.35% | 55% |
| val: FAIR | 141 | +1.90% | +0.94% | 57% |
| val: N/A or LOW | 383 | +2.17% | +1.44% | 58% |
| val: RICH | 230 | +1.11% | +0.27% | 51% |
| val: UNDERVALUED | 53 | +1.71% | +1.70% | 68% |

## How often each grade appeared among BASE picks

dis AT RISK: 228, dis BEING DISRUPTED: 41, dis DISRUPTOR: 13, dis INNOVATING: 275, dis STABLE: 393, val DEEP VALUE: 54, val EXPENSIVE: 643, val FAIR: 80, val N/A: 28, val RICH: 122, val UNDERVALUED: 23
