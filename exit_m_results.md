# Exit backtest part 2 — SWING_M profit exit on real intraday prices — run 2026-10-05 19:07Z

Period 2019-01-02 → 2026-10-05. Cells are CAGR / max drawdown. Formula and K values unchanged from part 1 (exit_results.md). 'True intraday' = checks at 09:35 … 15:00 on 5-minute bars and the close decision at 15:50 for every variant; 'daily proxy' = part 1's method.

**QQQ:** full 23.4% / -35.1% · 2019–22 15.3% / -35.1% · 2023–26 33.0% / -22.8%

## SWING_M alone

| Variant | Full (true intraday) | 2019–22 | 2023–26 | Full (daily proxy) | Trades (true intraday, 1x) |
|---|---|---|---|---|---|
| BASE (current rules) | 25.2% / -25.4% | 22.3% / -25.4% | 29.1% / -22.4% | 29.5% / -21.1% | 2258 trades, win 63%, avg +1.66%, avg win +5.02% / loss -4.05%, hold 4.7d, exits rule/profit/loss 2258/0/0 |
| profit K=2 | 23.7% / -21.5% | 20.3% / -21.5% | 28.0% / -15.5% | 26.5% / -15.7% | 2750 trades, win 73%, avg +1.36%, avg win +3.23% / loss -3.66%, hold 3.2d, exits rule/profit/loss 1288/1462/0 |
| profit K=3 | 24.3% / -22.5% | 21.5% / -22.5% | 28.0% / -16.6% | 27.4% / -18.3% | 2513 trades, win 69%, avg +1.48%, avg win +3.92% / loss -3.91%, hold 3.8d, exits rule/profit/loss 1668/845/0 |
| profit K=4 | 25.7% / -22.5% | 21.6% / -22.5% | 31.0% / -19.0% | 26.3% / -18.3% | 2410 trades, win 66%, avg +1.58%, avg win +4.37% / loss -3.90%, hold 4.2d, exits rule/profit/loss 1908/502/0 |
| profit K=5 | 25.2% / -22.5% | 21.9% / -22.5% | 29.4% / -21.3% | 28.3% / -18.2% | 2342 trades, win 65%, avg +1.61%, avg win +4.58% / loss -3.94%, hold 4.4d, exits rule/profit/loss 2036/306/0 |

## Portfolio: 70% SWING_Q (current rules) + 30% SWING_M (variant), true intraday

| SWING_M variant | Full | 2019–22 | 2023–26 |
|---|---|---|---|
| BASE (current rules) | 28.8% / -24.0% | 24.3% / -24.0% | 34.4% / -18.2% |
| profit K=2 | 28.3% / -23.7% | 23.7% / -23.7% | 33.9% / -16.2% |
| profit K=3 | 28.5% / -24.5% | 24.0% / -24.5% | 33.9% / -17.2% |
| profit K=4 | 28.9% / -24.4% | 24.0% / -24.4% | 34.8% / -17.5% |
| profit K=5 | 28.8% / -24.4% | 24.1% / -24.4% | 34.4% / -17.8% |

## Walk-forward — chosen on 2019–22, scored on 2023–26 (SWING_M, true intraday)

| Choice rule | Variant | 2019–22 | 2023–26 (unseen) | BASE 2023–26 |
|---|---|---|---|---|
| Best return / drawdown (MAR) | profit K=5 | 21.9% / -22.5% | 29.4% / -21.3% | 29.1% / -22.4% |
| Best CAGR | BASE (current rules) | 22.3% / -25.4% | 29.1% / -22.4% | 29.1% / -22.4% |

## Yearly, SWING_M (true intraday)

| Variant | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| BASE (current rules) | +4.6% | +58.6% | +15.9% | +15.4% | +16.6% | +17.5% | +11.7% | +67.4% |
| profit K=2 | +8.7% | +49.5% | +14.3% | +12.3% | +15.5% | +20.7% | +19.8% | +48.7% |
| profit K=3 | +14.5% | +53.9% | +12.1% | +9.8% | +17.7% | +17.4% | +19.8% | +49.9% |
| profit K=4 | +12.3% | +51.8% | +12.5% | +13.2% | +20.2% | +19.2% | +19.4% | +58.1% |
| profit K=5 | +13.9% | +53.9% | +11.6% | +12.0% | +19.7% | +18.6% | +14.9% | +58.6% |

## Data log

- pick-days with 5-minute bars: 19303/19500 (99%); the rest use the daily-bar proxy
- QQQ 5min 2021-02-08..2021-02-14: None
- QQQ 5min 2024-08-12..2024-08-18: None
