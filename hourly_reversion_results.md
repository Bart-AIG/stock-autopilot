# Hourly mean-reversion screen (TrendSpider META idea, tested)

Generated 2026-10-18 by `hourly_reversion_backtest.py`. 1-hour regular-session bars, 2021-01-01 to today. Long only, signal on a bar's close, fill at the next bar's open, exit at the close of the 12th bar (~2 sessions, so every trade holds overnight). One position per symbol. Costs 2 bp per side.

**Edge** = mean trade return minus the mean 12-bar return from ANY bar (the 'random entry' baseline). **Works** = t-stat > 2 over the full period AND positive edge in both 2021-23 and 2024-26.

Read with the multiple-testing caveat: ~225 tests, so ~10 can pass t > 2 by luck before the halves check.

## META detail

10148 bars. Baseline 12-bar return +0.173%.

| Entry | Trades | Avg trade | Edge vs random | Win % | Profit factor | t | Edge 21-23 | Edge 24-26 | Works |
|---|---|---|---|---|---|---|---|---|---|
| RSI2_UPTREND | 224 | +0.290% | +0.117% | 57% | 1.39 | 0.75 | +0.340% | -0.129% | no |
| BB_VOLUME | 149 | +0.222% | +0.050% | 51% | 1.23 | 0.19 | -0.018% | +0.113% | no |
| SHARP_5BAR | 44 | +0.223% | +0.051% | 57% | 1.20 | 0.11 | -0.008% | +0.126% | no |
| STRETCH_EMA20 | 185 | +0.015% | -0.158% | 51% | 1.01 | -0.73 | -0.234% | -0.084% | no |
| STOCH_HOOK | 210 | +0.232% | +0.059% | 51% | 1.21 | 0.24 | +0.110% | +0.002% | no |

## Each entry across all names

| Entry | Names where it works | Avg edge (all names) | Names with positive edge | Pooled trades |
|---|---|---|---|---|
| RSI2_UPTREND | 0/45: - | -0.134% | 9/45 | 9010 |
| BB_VOLUME | 0/45: - | -0.133% | 10/45 | 6254 |
| SHARP_5BAR | 0/45: - | -0.147% | 19/45 | 2192 |
| STRETCH_EMA20 | 0/45: - | -0.080% | 16/45 | 8441 |
| STOCH_HOOK | 0/45: - | -0.026% | 21/45 | 9400 |

## Names ranked by best robust entry

| Symbol | Entries that work | Best entry | Trades | Edge | Win % | PF | t | Edge 21-23 | Edge 24-26 |
|---|---|---|---|---|---|---|---|---|---|
| IWM | 0 | STRETCH_EMA20 | 208 | +0.230% | 57% | 1.47 | 1.76 | +0.323% | +0.127% |
| QCOM | 0 | STOCH_HOOK | 229 | +0.315% | 52% | 1.38 | 1.44 | +0.217% | +0.430% |
| AMD | 0 | STOCH_HOOK | 224 | +0.431% | 56% | 1.51 | 1.37 | +0.783% | +0.007% |
| AMZN | 0 | STOCH_HOOK | 227 | +0.244% | 55% | 1.37 | 1.28 | +0.375% | +0.089% |
| BA | 0 | RSI2_UPTREND | 187 | +0.220% | 49% | 1.28 | 1.13 | +0.331% | +0.097% |
| UBER | 0 | BB_VOLUME | 157 | +0.268% | 55% | 1.36 | 1.06 | +0.392% | +0.140% |
| TSLA | 0 | STRETCH_EMA20 | 211 | +0.324% | 54% | 1.29 | 0.96 | +0.044% | +0.598% |
| AAPL | 0 | RSI2_UPTREND | 213 | +0.152% | 54% | 1.42 | 0.94 | +0.352% | -0.081% |
| NFLX | 0 | RSI2_UPTREND | 196 | +0.190% | 56% | 1.32 | 0.91 | +0.199% | +0.179% |
| ISRG | 0 | STRETCH_EMA20 | 187 | +0.187% | 49% | 1.30 | 0.91 | +0.129% | +0.252% |
| UNH | 0 | STRETCH_EMA20 | 185 | +0.145% | 52% | 1.28 | 0.90 | +0.310% | -0.026% |
| ORCL | 0 | STOCH_HOOK | 220 | +0.199% | 51% | 1.36 | 0.88 | +0.337% | +0.053% |
| MSFT | 0 | SHARP_5BAR | 53 | +0.281% | 51% | 1.58 | 0.87 | -0.311% | +0.895% |
| HD | 0 | STRETCH_EMA20 | 210 | +0.106% | 54% | 1.23 | 0.87 | +0.112% | +0.109% |
| PEP | 0 | STOCH_HOOK | 220 | +0.090% | 51% | 1.16 | 0.85 | +0.052% | +0.134% |
| SPY | 0 | STOCH_HOOK | 186 | +0.087% | 60% | 1.37 | 0.82 | +0.213% | -0.052% |
| PG | 0 | RSI2_UPTREND | 194 | +0.076% | 53% | 1.23 | 0.79 | +0.174% | -0.026% |
| META | 0 | RSI2_UPTREND | 224 | +0.117% | 57% | 1.39 | 0.75 | +0.340% | -0.129% |
| TXN | 0 | STRETCH_EMA20 | 188 | +0.106% | 57% | 1.26 | 0.64 | +0.252% | -0.050% |
| GOOGL | 0 | STRETCH_EMA20 | 183 | +0.110% | 55% | 1.38 | 0.61 | +0.080% | +0.138% |
| WMT | 0 | SHARP_5BAR | 53 | +0.230% | 49% | 1.45 | 0.60 | -0.353% | +0.782% |
| XLF | 0 | BB_VOLUME | 138 | +0.091% | 61% | 1.32 | 0.59 | +0.150% | +0.023% |
| NVDA | 0 | STOCH_HOOK | 204 | +0.190% | 56% | 1.40 | 0.58 | +0.356% | -0.022% |
| COST | 0 | BB_VOLUME | 121 | +0.088% | 55% | 1.37 | 0.54 | +0.021% | +0.152% |
| AMAT | 0 | SHARP_5BAR | 56 | +0.301% | 57% | 1.37 | 0.51 | +0.948% | -0.309% |
| QQQ | 0 | STRETCH_EMA20 | 193 | +0.066% | 54% | 1.27 | 0.46 | +0.175% | -0.057% |
| XOM | 0 | STRETCH_EMA20 | 193 | +0.070% | 53% | 1.34 | 0.42 | +0.209% | -0.083% |
| MA | 0 | SHARP_5BAR | 56 | +0.119% | 59% | 1.29 | 0.42 | +0.033% | +0.191% |
| V | 0 | STOCH_HOOK | 195 | +0.051% | 49% | 1.23 | 0.38 | +0.037% | +0.070% |
| NOW | 0 | STOCH_HOOK | 208 | +0.090% | 53% | 1.15 | 0.38 | -0.090% | +0.277% |
| AVGO | 0 | SHARP_5BAR | 45 | +0.140% | 64% | 1.43 | 0.32 | +0.133% | +0.134% |
| SMH | 0 | SHARP_5BAR | 49 | +0.142% | 53% | 1.29 | 0.28 | -0.044% | +0.310% |
| MU | 0 | STOCH_HOOK | 208 | +0.079% | 55% | 1.30 | 0.25 | +0.593% | -0.532% |
| LLY | 0 | SHARP_5BAR | 40 | +0.078% | 55% | 1.39 | 0.18 | +0.288% | -0.102% |
| GE | 0 | STOCH_HOOK | 202 | +0.020% | 51% | 1.28 | 0.10 | +0.195% | -0.186% |
| JPM | 0 | STOCH_HOOK | 194 | +0.011% | 57% | 1.18 | 0.06 | +0.115% | -0.115% |
| KO | 0 | BB_VOLUME | 121 | +0.002% | 57% | 1.16 | 0.02 | -0.095% | +0.091% |
| CAT | 0 | SHARP_5BAR | 58 | +0.004% | 59% | 1.21 | 0.01 | +0.210% | -0.229% |
| PANW | 0 | STRETCH_EMA20 | 183 | -0.002% | 49% | 1.26 | -0.01 | +0.001% | -0.004% |
| ADBE | 0 | STRETCH_EMA20 | 209 | -0.032% | 49% | 0.95 | -0.14 | -0.235% | +0.172% |
| INTU | 0 | STOCH_HOOK | 203 | -0.091% | 54% | 0.95 | -0.39 | -0.250% | +0.076% |
| PLTR | 0 | RSI2_UPTREND | 192 | -0.156% | 53% | 1.14 | -0.45 | -0.575% | +0.021% |
| SHOP | 0 | STOCH_HOOK | 226 | -0.166% | 46% | 1.01 | -0.47 | -0.223% | -0.054% |
| MCD | 0 | STRETCH_EMA20 | 181 | -0.049% | 50% | 0.95 | -0.48 | +0.048% | -0.126% |
| CRM | 0 | BB_VOLUME | 143 | -0.170% | 45% | 0.90 | -0.62 | -0.289% | -0.061% |

