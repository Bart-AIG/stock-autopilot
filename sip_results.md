# Stocks-in-play day-trading test — run 2026-09-30 18:58Z

159 names with 5-minute data, 496 sessions (2024-09-30 → 2026-09-29). Returns are for the day-trading sleeve itself (1x, cash, flat every night).

QQQ buy & hold over the same sessions: 22.8%/yr, max DD -23%.

| Version | CAGR | Max DD | Sharpe | 1st year | 2nd year | Trades/day | Win % | Avg R | Avg trade | Exit mix |
|---|---|---|---|---|---|---|---|---|---|---|
| Published (top 20, long/short, 0.1 ATR stop active at once, exit at close, ideal fills) | -2.7% | -7% | -0.70 | -4.3% | -1.4% | 15.9 | 18% | +0.10 | -1.4 bp | stop 81%, time 19% |
| Published rules, long-only, ideal fills | 0.7% | -4% | 0.27 | -2.1% | 3.8% | 7.9 | 19% | +0.15 | +0.8 bp | stop 80%, time 20% |
| Realistic plain: top 10, long-only, 0.1 ATR stop from next fire, exit 15:50 | -1.7% | -11% | -0.39 | -7.6% | 4.6% | 4.0 | 20% | +0.03 | -1.6 bp | stop 53%, stop (before protected) 27%, time 20% |
| DYNAMIC: top 10, long-only, plan set at entry + 15-min monitoring | -1.9% | -6% | -0.64 | -1.9% | -1.8% | 4.0 | 37% | +0.04 | -1.9 bp | market turned 34%, stop 32%, stop (before protected) 18%, target 11%, lost VWAP 4%, time 1% |
| DYNAMIC, long/short (reference - cannot short) | -4.4% | -11% | -1.03 | -4.5% | -4.5% | 8.1 | 38% | +0.05 | -2.3 bp | market turned 37%, stop 30%, stop (before protected) 18%, target 11%, lost VWAP 3%, time 1% |
| DYNAMIC, top 5 | -5.6% | -13% | -1.51 | -5.3% | -5.8% | 2.0 | 35% | -0.01 | -5.9 bp | market turned 35%, stop 33%, stop (before protected) 17%, target 10%, lost VWAP 4%, time 1% |
| DYNAMIC, RVOL >= 2 | -3.0% | -8% | -1.14 | -3.9% | -2.2% | 3.4 | 35% | +0.00 | -3.6 bp | market turned 34%, stop 32%, stop (before protected) 18%, target 11%, lost VWAP 4%, time 1% |
| DYNAMIC, RVOL >= 3 | -1.8% | -7% | -0.77 | -1.8% | -1.8% | 2.4 | 36% | +0.02 | -3.1 bp | market turned 36%, stop 32%, stop (before protected) 17%, target 10%, lost VWAP 4%, time 1% |
| DYNAMIC without the VWAP exit | -1.6% | -6% | -0.54 | -1.8% | -1.4% | 4.0 | 37% | +0.04 | -1.6 bp | market turned 36%, stop 34%, stop (before protected) 18%, target 11%, time 1% |
| DYNAMIC without the market (QQQ) exit | -2.2% | -7% | -0.68 | -4.7% | 0.3% | 4.0 | 29% | +0.03 | -2.2 bp | stop 55%, stop (before protected) 18%, target 15%, lost VWAP 10%, time 3% |
| DYNAMIC, routine every 30 min | -2.2% | -7% | -0.59 | -5.2% | 1.0% | 4.0 | 38% | +0.04 | -2.2 bp | stop 28%, market turned 26%, stop (before protected) 24%, target 14%, lost VWAP 5%, time 2% |

## Data log

- (clean)
