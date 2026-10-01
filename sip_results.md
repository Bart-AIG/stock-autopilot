# Stocks-in-play day-trading test — run 2026-10-01 20:28Z

159 names with 5-minute data, 496 sessions (2024-10-01 → 2026-10-01). Returns are for the day-trading sleeve itself (1x, cash, flat every night).

QQQ buy & hold over the same sessions: 23.0%/yr, max DD -23%.

| Version | CAGR | Max DD | Sharpe | 1st year | 2nd year | Trades/day | Win % | Avg R | Avg trade | Exit mix |
|---|---|---|---|---|---|---|---|---|---|---|
| Published (top 20, long/short, 0.1 ATR stop active at once, exit at close, ideal fills) | -2.8% | -8% | -0.73 | -5.0% | -0.5% | 15.9 | 18% | +0.10 | -1.4 bp | stop 81%, time 19% |
| Published rules, long-only, ideal fills | 0.7% | -4% | 0.27 | -2.4% | 4.1% | 7.9 | 19% | +0.16 | +0.9 bp | stop 80%, time 20% |
| Realistic plain: top 10, long-only, 0.1 ATR stop from next fire, exit 15:50 | -2.0% | -10% | -0.47 | -8.4% | 4.8% | 4.0 | 20% | +0.04 | -1.5 bp | stop 53%, stop (before protected) 27%, time 20% |
| DYNAMIC: top 10, long-only, plan set at entry + 15-min monitoring | -1.5% | -6% | -0.52 | -2.2% | -0.7% | 4.0 | 37% | +0.05 | -1.2 bp | market turned 35%, stop 32%, stop (before protected) 18%, target 11%, lost VWAP 4%, time 1% |
| DYNAMIC, long/short (reference - cannot short) | -4.4% | -11% | -1.04 | -5.6% | -3.1% | 8.1 | 38% | +0.05 | -2.1 bp | market turned 37%, stop 30%, stop (before protected) 18%, target 11%, lost VWAP 3%, time 1% |
| DYNAMIC, top 5 | -5.6% | -14% | -1.54 | -6.3% | -4.8% | 2.0 | 35% | -0.00 | -5.6 bp | market turned 36%, stop 33%, stop (before protected) 17%, target 10%, lost VWAP 4%, time 1% |
| DYNAMIC, RVOL >= 2 | -2.9% | -8% | -1.12 | -4.3% | -1.4% | 3.4 | 36% | +0.01 | -3.2 bp | market turned 34%, stop 32%, stop (before protected) 18%, target 11%, lost VWAP 4%, time 1% |
| DYNAMIC, RVOL >= 3 | -1.8% | -7% | -0.79 | -2.2% | -1.3% | 2.4 | 36% | +0.02 | -2.7 bp | market turned 36%, stop 32%, stop (before protected) 17%, target 10%, lost VWAP 4%, time 1% |
| DYNAMIC without the VWAP exit | -1.2% | -6% | -0.42 | -2.2% | -0.2% | 4.0 | 37% | +0.06 | -1.0 bp | market turned 36%, stop 34%, stop (before protected) 18%, target 11%, time 1% |
| DYNAMIC without the market (QQQ) exit | -1.9% | -7% | -0.57 | -4.9% | 1.4% | 4.0 | 29% | +0.04 | -1.6 bp | stop 55%, stop (before protected) 18%, target 15%, lost VWAP 10%, time 3% |
| DYNAMIC, routine every 30 min | -1.9% | -7% | -0.52 | -5.6% | 1.9% | 4.0 | 38% | +0.05 | -1.6 bp | stop 29%, market turned 26%, stop (before protected) 24%, target 15%, lost VWAP 5%, time 2% |

## Data log

- (clean)
