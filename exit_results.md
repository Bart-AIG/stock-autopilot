# Exit backtest — run 2026-10-05 17:27Z

Period 2019-01-02 → 2026-10-05. Portfolio = 70% SWING_Q (QLD, 2x, true intraday checks on 5-minute QQQ bars, close decision at 15:50) + 30% SWING_M (top-10 momentum names, daily-bar proxy for intraday checks), monthly rebalance. Cells are CAGR / max drawdown. Formulas are in the file header.

**QQQ:** full 23.4% / -35.1% · 2019–22 15.3% / -35.1% · 2023–26 33.0% / -22.8%

## Portfolio (70/30) by variant

| Variant | Full period | 2019–22 (choose) | 2023–26 (unseen) | Full, SWING_Q on daily proxy |
|---|---|---|---|---|
| BASE (current rules) | 30.1% / -22.7% | 25.5% / -22.7% | 35.6% / -17.9% | 38.0% / -22.2% |
| profit K=2 | 26.0% / -20.5% | 23.6% / -20.5% | 29.2% / -15.4% | 28.5% / -20.2% |
| profit K=3 | 26.9% / -21.8% | 21.5% / -21.8% | 33.5% / -16.9% | 33.7% / -21.1% |
| profit K=4 | 27.4% / -23.6% | 21.3% / -23.6% | 34.7% / -17.6% | 34.1% / -20.7% |
| profit K=5 | 29.5% / -23.4% | 24.6% / -23.4% | 35.3% / -17.7% | 37.0% / -22.0% |
| loss K=2 | 20.2% / -20.3% | 22.7% / -18.3% | 17.8% / -17.3% | 27.6% / -24.2% |
| loss K=3 | 19.4% / -31.4% | 16.8% / -31.4% | 22.6% / -19.1% | 29.2% / -27.7% |
| loss K=4 | 24.8% / -34.4% | 19.5% / -34.4% | 31.1% / -19.6% | 33.3% / -26.5% |
| profit K=2 + loss K=2 | 16.5% / -21.6% | 19.5% / -21.6% | 13.5% / -14.8% | 16.6% / -25.8% |
| profit K=2 + loss K=3 | 17.6% / -30.4% | 16.3% / -30.4% | 19.4% / -16.0% | 22.5% / -26.1% |
| profit K=2 + loss K=4 | 22.2% / -33.1% | 19.6% / -33.1% | 25.3% / -17.0% | 24.4% / -25.0% |
| profit K=3 + loss K=2 | 17.4% / -17.7% | 19.1% / -17.5% | 15.7% / -14.8% | 23.4% / -24.4% |
| profit K=3 + loss K=3 | 15.7% / -31.2% | 11.3% / -31.2% | 20.9% / -18.7% | 26.4% / -27.6% |
| profit K=3 + loss K=4 | 21.9% / -34.1% | 15.6% / -34.1% | 29.5% / -18.4% | 29.2% / -27.9% |
| profit K=4 + loss K=2 | 17.1% / -22.9% | 17.4% / -21.2% | 16.9% / -16.4% | 24.4% / -25.4% |
| profit K=4 + loss K=3 | 15.9% / -31.5% | 10.8% / -31.5% | 21.9% / -18.8% | 25.4% / -29.8% |
| profit K=4 + loss K=4 | 22.3% / -34.4% | 15.5% / -34.4% | 30.4% / -19.3% | 29.5% / -27.5% |
| profit K=5 + loss K=2 | 18.7% / -22.0% | 20.7% / -20.1% | 16.9% / -16.6% | 26.5% / -24.9% |
| profit K=5 + loss K=3 | 17.5% / -31.5% | 13.6% / -31.5% | 22.2% / -19.0% | 28.2% / -27.9% |
| profit K=5 + loss K=4 | 24.2% / -34.4% | 18.6% / -34.4% | 31.0% / -19.5% | 32.4% / -27.2% |

## Walk-forward — chosen on 2019–22 only, scored on 2023–26

| Choice rule (2019–22) | Variant | 2019–22 | 2023–26 (unseen) | BASE 2023–26 |
|---|---|---|---|---|
| Best return / drawdown (MAR) | loss K=2 | 22.7% / -18.3% | 17.8% / -17.3% | 35.6% / -17.9% |
| Best CAGR | BASE (current rules) | 25.5% / -22.7% | 35.6% / -17.9% | 35.6% / -17.9% |
| Best CAGR with DD no worse than BASE | BASE (current rules) | 25.5% / -22.7% | 35.6% / -17.9% | 35.6% / -17.9% |
| Best profit-only (MAR) | profit K=2 | 23.6% / -20.5% | 29.2% / -15.4% | 35.6% / -17.9% |
| Best loss-only (MAR) | loss K=2 | 22.7% / -18.3% | 17.8% / -17.3% | 35.6% / -17.9% |

## SWING_Q (QLD 2x), true intraday

| Variant | Full | 2019–22 | 2023–26 | Trades (1x, full period) |
|---|---|---|---|---|
| BASE (current rules) | 29.5% / -31.6% | 24.4% / -31.6% | 35.6% / -20.0% | 212 trades, win 68%, avg +0.52%, avg win +1.61% / loss -1.84%, hold 3.9d, exits rule/profit/loss 212/0/0 |
| profit K=2 | 25.2% / -27.8% | 22.7% / -27.8% | 28.1% / -17.9% | 230 trades, win 73%, avg +0.41%, avg win +1.20% / loss -1.68%, hold 3.0d, exits rule/profit/loss 114/116/0 |
| profit K=3 | 26.0% / -27.8% | 20.6% / -27.8% | 32.3% / -20.0% | 220 trades, win 70%, avg +0.45%, avg win +1.41% / loss -1.78%, hold 3.4d, exits rule/profit/loss 160/60/0 |
| profit K=4 | 27.1% / -31.6% | 20.3% / -31.6% | 35.1% / -20.0% | 216 trades, win 69%, avg +0.48%, avg win +1.50% / loss -1.80%, hold 3.6d, exits rule/profit/loss 184/32/0 |
| profit K=5 | 29.2% / -31.6% | 24.2% / -31.6% | 35.2% / -20.0% | 215 trades, win 69%, avg +0.51%, avg win +1.56% / loss -1.80%, hold 3.8d, exits rule/profit/loss 200/15/0 |
| loss K=2 | 19.3% / -31.0% | 24.0% / -26.2% | 14.4% / -21.9% | 235 trades, win 64%, avg +0.34%, avg win +1.64% / loss -2.02%, hold 3.0d, exits rule/profit/loss 177/0/58 |
| loss K=3 | 16.8% / -38.6% | 14.5% / -38.6% | 19.5% / -22.9% | 221 trades, win 67%, avg +0.32%, avg win +1.62% / loss -2.37%, hold 3.5d, exits rule/profit/loss 193/0/28 |
| loss K=4 | 22.8% / -43.5% | 15.7% / -43.5% | 31.2% / -22.2% | 214 trades, win 69%, avg +0.43%, avg win +1.62% / loss -2.17%, hold 3.8d, exits rule/profit/loss 206/0/8 |
| profit K=2 + loss K=2 | 15.1% / -26.8% | 20.0% / -26.8% | 10.1% / -20.0% | 248 trades, win 68%, avg +0.25%, avg win +1.24% / loss -1.87%, hold 2.4d, exits rule/profit/loss 80/116/52 |
| profit K=2 + loss K=3 | 15.0% / -38.6% | 13.9% / -38.6% | 16.4% / -20.8% | 237 trades, win 71%, avg +0.26%, avg win +1.25% / loss -2.19%, hold 2.7d, exits rule/profit/loss 96/116/25 |
| profit K=2 + loss K=4 | 20.0% / -43.5% | 16.7% / -43.5% | 24.0% / -20.8% | 232 trades, win 73%, avg +0.34%, avg win +1.23% / loss -2.04%, hold 2.9d, exits rule/profit/loss 107/117/8 |
| profit K=3 + loss K=2 | 16.3% / -24.0% | 20.4% / -19.8% | 12.0% / -17.4% | 241 trades, win 66%, avg +0.28%, avg win +1.45% / loss -1.99%, hold 2.7d, exits rule/profit/loss 129/57/55 |
| profit K=3 + loss K=3 | 12.2% / -38.6% | 8.1% / -38.6% | 17.1% / -22.9% | 228 trades, win 69%, avg +0.24%, avg win +1.42% / loss -2.37%, hold 3.1d, exits rule/profit/loss 142/58/28 |
| profit K=3 + loss K=4 | 19.5% / -43.5% | 12.2% / -43.5% | 28.0% / -22.2% | 222 trades, win 70%, avg +0.36%, avg win +1.41% / loss -2.13%, hold 3.3d, exits rule/profit/loss 154/60/8 |
| profit K=4 + loss K=2 | 16.2% / -33.1% | 18.2% / -28.2% | 14.2% / -17.4% | 237 trades, win 65%, avg +0.29%, avg win +1.53% / loss -2.01%, hold 2.9d, exits rule/profit/loss 152/28/57 |
| profit K=4 + loss K=3 | 13.1% / -38.6% | 7.8% / -38.6% | 19.2% / -23.5% | 224 trades, win 68%, avg +0.26%, avg win +1.51% / loss -2.38%, hold 3.3d, exits rule/profit/loss 166/30/28 |
| profit K=4 + loss K=4 | 20.5% / -43.5% | 11.9% / -43.5% | 30.7% / -22.2% | 218 trades, win 69%, avg +0.38%, avg win +1.50% / loss -2.14%, hold 3.5d, exits rule/profit/loss 178/32/8 |
| profit K=5 + loss K=2 | 18.0% / -32.1% | 22.4% / -27.4% | 13.6% / -21.9% | 237 trades, win 65%, avg +0.31%, avg win +1.59% / loss -2.01%, hold 2.9d, exits rule/profit/loss 165/14/58 |
| profit K=5 + loss K=3 | 14.8% / -38.6% | 11.2% / -38.6% | 19.1% / -22.9% | 223 trades, win 68%, avg +0.29%, avg win +1.56% / loss -2.38%, hold 3.4d, exits rule/profit/loss 180/15/28 |
| profit K=5 + loss K=4 | 22.5% / -43.5% | 15.5% / -43.5% | 30.8% / -22.2% | 217 trades, win 69%, avg +0.42%, avg win +1.56% / loss -2.14%, hold 3.7d, exits rule/profit/loss 194/15/8 |

## SWING_Q (QLD 2x), daily-bar proxy

| Variant | Full | 2019–22 | 2023–26 | Trades (1x, full period) |
|---|---|---|---|---|
| BASE (current rules) | 41.0% / -27.8% | 41.9% / -27.8% | 40.7% / -25.9% | 209 trades, win 70%, avg +0.69%, avg win +1.73% / loss -1.72%, hold 4.0d, exits rule/profit/loss 209/0/0 |
| profit K=2 | 28.7% / -27.4% | 26.8% / -27.4% | 31.3% / -20.9% | 230 trades, win 70%, avg +0.46%, avg win +1.23% / loss -1.34%, hold 2.9d, exits rule/profit/loss 101/129/0 |
| profit K=3 | 35.9% / -27.4% | 32.5% / -27.4% | 40.4% / -21.5% | 217 trades, win 70%, avg +0.59%, avg win +1.49% / loss -1.53%, hold 3.4d, exits rule/profit/loss 146/71/0 |
| profit K=4 | 36.9% / -27.8% | 36.0% / -27.8% | 38.5% / -21.5% | 213 trades, win 70%, avg +0.62%, avg win +1.58% / loss -1.63%, hold 3.6d, exits rule/profit/loss 174/39/0 |
| profit K=5 | 40.2% / -27.8% | 39.9% / -27.8% | 41.2% / -25.9% | 212 trades, win 70%, avg +0.67%, avg win +1.68% / loss -1.71%, hold 3.8d, exits rule/profit/loss 192/20/0 |
| loss K=2 | 29.9% / -33.3% | 38.3% / -23.9% | 21.6% / -22.4% | 230 trades, win 63%, avg +0.48%, avg win +1.77% / loss -1.67%, hold 3.1d, exits rule/profit/loss 167/0/63 |
| loss K=3 | 30.8% / -39.5% | 30.7% / -37.1% | 31.6% / -24.8% | 219 trades, win 68%, avg +0.53%, avg win +1.78% / loss -2.19%, hold 3.5d, exits rule/profit/loss 190/0/29 |
| loss K=4 | 35.0% / -36.9% | 33.1% / -35.9% | 37.7% / -26.1% | 212 trades, win 69%, avg +0.60%, avg win +1.74% / loss -1.96%, hold 3.8d, exits rule/profit/loss 203/0/9 |
| profit K=2 + loss K=2 | 15.4% / -35.8% | 20.7% / -24.0% | 10.0% / -22.7% | 247 trades, win 64%, avg +0.25%, avg win +1.25% / loss -1.56%, hold 2.2d, exits rule/profit/loss 60/129/58 |
| profit K=2 + loss K=3 | 22.0% / -38.2% | 19.6% / -34.4% | 25.2% / -19.8% | 242 trades, win 69%, avg +0.35%, avg win +1.30% / loss -1.77%, hold 2.5d, exits rule/profit/loss 82/134/26 |
| profit K=2 + loss K=4 | 23.3% / -37.8% | 20.7% / -35.0% | 26.8% / -24.9% | 232 trades, win 70%, avg +0.39%, avg win +1.25% / loss -1.62%, hold 2.8d, exits rule/profit/loss 94/130/8 |
| profit K=3 + loss K=2 | 25.0% / -32.7% | 28.5% / -22.7% | 21.5% / -21.2% | 234 trades, win 64%, avg +0.40%, avg win +1.53% / loss -1.62%, hold 2.6d, exits rule/profit/loss 106/69/59 |
| profit K=3 + loss K=3 | 27.6% / -38.5% | 25.0% / -34.9% | 31.0% / -21.6% | 228 trades, win 69%, avg +0.46%, avg win +1.56% / loss -2.00%, hold 3.0d, exits rule/profit/loss 129/72/27 |
| profit K=3 + loss K=4 | 30.0% / -38.3% | 24.3% / -35.6% | 37.0% / -22.4% | 220 trades, win 70%, avg +0.51%, avg win +1.50% / loss -1.77%, hold 3.3d, exits rule/profit/loss 140/71/9 |
| profit K=4 + loss K=2 | 26.9% / -33.7% | 32.9% / -23.9% | 20.9% / -21.2% | 232 trades, win 63%, avg +0.43%, avg win +1.62% / loss -1.61%, hold 2.8d, exits rule/profit/loss 134/38/60 |
| profit K=4 + loss K=3 | 26.8% / -41.0% | 25.2% / -37.6% | 28.9% / -21.6% | 223 trades, win 69%, avg +0.46%, avg win +1.63% / loss -2.11%, hold 3.2d, exits rule/profit/loss 155/39/29 |
| profit K=4 + loss K=4 | 30.9% / -38.5% | 27.6% / -35.9% | 35.2% / -22.4% | 216 trades, win 69%, avg +0.53%, avg win +1.59% / loss -1.88%, hold 3.5d, exits rule/profit/loss 168/39/9 |
| profit K=5 + loss K=2 | 29.3% / -33.3% | 36.3% / -23.9% | 22.2% / -21.2% | 232 trades, win 63%, avg +0.47%, avg win +1.70% / loss -1.67%, hold 2.9d, exits rule/profit/loss 151/19/62 |
| profit K=5 + loss K=3 | 30.1% / -38.9% | 28.8% / -37.1% | 32.0% / -24.8% | 222 trades, win 69%, avg +0.51%, avg win +1.72% / loss -2.18%, hold 3.4d, exits rule/profit/loss 173/20/29 |
| profit K=5 + loss K=4 | 34.3% / -36.3% | 31.2% / -35.9% | 38.2% / -26.1% | 215 trades, win 70%, avg +0.58%, avg win +1.68% / loss -1.96%, hold 3.7d, exits rule/profit/loss 186/20/9 |

## SWING_M (10 names 1x), daily-bar proxy

| Variant | Full | 2019–22 | 2023–26 | Trades (1x, full period) |
|---|---|---|---|---|
| BASE (current rules) | 29.5% / -21.1% | 26.5% / -18.5% | 33.4% / -21.1% | 2283 trades, win 64%, avg +0.81%, avg win +3.36% / loss -3.78%, hold 4.6d, exits rule/profit/loss 2283/0/0 |
| profit K=2 | 26.5% / -15.7% | 23.6% / -15.7% | 30.4% / -12.6% | 2878 trades, win 68%, avg +0.59%, avg win +2.07% / loss -2.57%, hold 2.9d, exits rule/profit/loss 1173/1705/0 |
| profit K=3 | 27.4% / -18.3% | 21.7% / -18.3% | 34.6% / -12.6% | 2589 trades, win 68%, avg +0.68%, avg win +2.57% / loss -3.40%, hold 3.6d, exits rule/profit/loss 1626/963/0 |
| profit K=4 | 26.3% / -18.3% | 21.8% / -18.3% | 31.9% / -16.2% | 2452 trades, win 67%, avg +0.68%, avg win +2.84% / loss -3.67%, hold 4.1d, exits rule/profit/loss 1925/527/0 |
| profit K=5 | 28.2% / -18.2% | 23.8% / -18.2% | 33.8% / -16.9% | 2374 trades, win 66%, avg +0.74%, avg win +3.06% / loss -3.72%, hold 4.3d, exits rule/profit/loss 2075/299/0 |
| loss K=2 | 20.9% / -20.2% | 18.2% / -14.0% | 24.3% / -20.2% | 2662 trades, win 57%, avg +0.53%, avg win +3.54% / loss -3.45%, hold 3.4d, exits rule/profit/loss 1856/0/806 |
| loss K=3 | 23.4% / -19.2% | 20.1% / -16.0% | 27.8% / -19.2% | 2469 trades, win 62%, avg +0.64%, avg win +3.49% / loss -4.04%, hold 3.9d, exits rule/profit/loss 2048/0/421 |
| loss K=4 | 27.4% / -21.1% | 26.6% / -17.8% | 29.0% / -21.1% | 2353 trades, win 64%, avg +0.75%, avg win +3.39% / loss -3.95%, hold 4.3d, exits rule/profit/loss 2181/0/172 |
| profit K=2 + loss K=2 | 18.3% / -11.5% | 16.5% / -11.5% | 20.8% / -10.7% | 3173 trades, win 63%, avg +0.39%, avg win +2.20% / loss -2.72%, hold 2.2d, exits rule/profit/loss 832/1701/640 |
| profit K=2 + loss K=3 | 22.3% / -12.9% | 20.0% / -12.9% | 25.4% / -12.2% | 3037 trades, win 67%, avg +0.49%, avg win +2.18% / loss -2.92%, hold 2.5d, exits rule/profit/loss 961/1738/338 |
| profit K=2 + loss K=4 | 25.5% / -15.3% | 24.3% / -15.3% | 27.4% / -12.7% | 2934 trades, win 68%, avg +0.56%, avg win +2.11% / loss -2.72%, hold 2.7d, exits rule/profit/loss 1079/1718/137 |
| profit K=3 + loss K=2 | 18.6% / -14.0% | 14.8% / -14.0% | 23.3% / -11.9% | 2931 trades, win 62%, avg +0.44%, avg win +2.73% / loss -3.32%, hold 2.7d, exits rule/profit/loss 1229/963/739 |
| profit K=3 + loss K=3 | 22.2% / -16.0% | 17.1% / -16.0% | 28.6% / -11.6% | 2762 trades, win 67%, avg +0.54%, avg win +2.69% / loss -3.74%, hold 3.1d, exits rule/profit/loss 1400/974/388 |
| profit K=3 + loss K=4 | 25.8% / -17.5% | 21.4% / -17.5% | 31.4% / -11.9% | 2652 trades, win 68%, avg +0.63%, avg win +2.60% / loss -3.57%, hold 3.4d, exits rule/profit/loss 1527/967/158 |
| profit K=4 + loss K=2 | 17.5% / -17.3% | 14.1% / -13.7% | 21.8% / -17.3% | 2820 trades, win 60%, avg +0.42%, avg win +3.00% / loss -3.45%, hold 3.0d, exits rule/profit/loss 1503/529/788 |
| profit K=4 + loss K=3 | 20.6% / -16.2% | 15.9% / -16.2% | 26.4% / -15.6% | 2630 trades, win 65%, avg +0.53%, avg win +2.97% / loss -3.98%, hold 3.5d, exits rule/profit/loss 1685/537/408 |
| profit K=4 + loss K=4 | 24.6% / -17.6% | 22.1% / -17.6% | 28.0% / -16.1% | 2521 trades, win 67%, avg +0.63%, avg win +2.88% / loss -3.85%, hold 3.8d, exits rule/profit/loss 1820/534/167 |
| profit K=5 + loss K=2 | 18.9% / -17.9% | 15.2% / -13.7% | 23.4% / -17.9% | 2745 trades, win 59%, avg +0.45%, avg win +3.22% / loss -3.46%, hold 3.2d, exits rule/profit/loss 1651/291/803 |
| profit K=5 + loss K=3 | 21.9% / -16.3% | 17.3% / -16.2% | 27.7% / -16.3% | 2554 trades, win 64%, avg +0.56%, avg win +3.18% / loss -4.01%, hold 3.7d, exits rule/profit/loss 1841/298/415 |
| profit K=5 + loss K=4 | 26.3% / -17.5% | 23.8% / -17.5% | 29.8% / -16.8% | 2444 trades, win 66%, avg +0.68%, avg win +3.09% / loss -3.90%, hold 4.0d, exits rule/profit/loss 1976/298/170 |

## Data log

- engine check vs robust_backtest.swing (SWING_Q, close): max daily diff 0.00e+00
