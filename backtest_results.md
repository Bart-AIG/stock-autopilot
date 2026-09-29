# Process backtest — run 2026-09-29 20:01Z

Data sources (daily): {'historical-price-eod/dividend-adjusted': 295}. Names with history: 295.

## Part A — A1 FULL scan universe (today's list: survivorship-biased): 236 names, 2019-01-02 → 2026-09-29

| Strategy | CAGR | vs SPY | vs QQQ | 2019-22 CAGR | 2023-26 CAGR | Max DD | Sharpe | Invested | Trades | Win % | Payoff | Hold (d) | Top-5 names' share of profit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY buy & hold** | 17.2% | | | 13.1% | 22.0% | -33.7% | 0.93 | 100% | | | | | |
| **QQQ buy & hold** | 23.1% | | | 15.3% | 32.4% | -35.1% | 0.99 | 100% | | | | | |
| GRADE_HOLD_any_lag1 | 97.2% | +79.9% | +74.0% | 67.6% | 135.2% | -49.1% | 1.57 | 93% | 214 | 49% | 3.92 | 33 | 82% of 121 names |
| GRADE_HOLD_any | 81.9% | +64.6% | +58.7% | 71.4% | 95.2% | -47.0% | 1.45 | 93% | 210 | 47% | 3.84 | 33 | 84% of 115 names |
| GRADE_HOLD_any_cost25bp | 77.1% | +59.9% | +54.0% | 67.0% | 90.0% | -47.5% | 1.40 | 93% | 210 | 47% | 3.64 | 33 | 85% of 115 names |
| ROTATE_MONTHLY_QQQcore_lag1 | 54.9% | +37.6% | +31.7% | 32.8% | 83.4% | -51.1% | 1.08 | 99% | 105 | 58% | 2.90 | 62 | 90% of 78 names |
| ROTATE_MONTHLY_lag1 | 53.9% | +36.7% | +30.8% | 32.2% | 82.0% | -50.9% | 1.07 | 90% | 105 | 58% | 2.90 | 62 | 90% of 78 names |
| ROTATE_MONTHLY_QQQcore | 52.6% | +35.3% | +29.4% | 36.0% | 73.0% | -52.8% | 1.05 | 99% | 107 | 59% | 2.40 | 61 | 101% of 80 names |
| ROTATE_MONTHLY | 50.2% | +33.0% | +27.1% | 34.2% | 69.8% | -52.8% | 1.03 | 91% | 107 | 59% | 2.40 | 61 | 99% of 80 names |
| ROTATE_MONTHLY_8 | 49.1% | +31.9% | +26.0% | 41.2% | 59.0% | -44.8% | 1.16 | 85% | 198 | 56% | 3.11 | 62 | 58% of 124 names |
| ROTATE_MONTHLY_cost25bp | 48.2% | +30.9% | +25.1% | 32.5% | 67.5% | -52.8% | 1.00 | 91% | 107 | 57% | 2.50 | 61 | 101% of 80 names |
| LEADER_lag1 | 32.4% | +15.2% | +9.3% | 31.5% | 34.0% | -36.4% | 1.13 | 91% | 386 | 42% | 2.84 | 18 | 72% of 168 names |
| GRADE_HOLD_lag1 | 30.1% | +12.8% | +6.9% | 37.1% | 23.2% | -34.1% | 1.00 | 92% | 319 | 45% | 2.58 | 22 | 68% of 165 names |
| OLD_CONNORS | 27.7% | +10.5% | +4.6% | 23.1% | 33.4% | -39.6% | 0.99 | 88% | 1110 | 79% | 0.39 | 6 | 36% of 222 names |
| CURRENT_QQQcore | 26.8% | +9.5% | +3.6% | 24.0% | 29.9% | -34.9% | 1.03 | 99% | 1303 | 70% | 0.60 | 4 | 42% of 202 names |
| LEADER_QQQcore | 26.3% | +9.1% | +3.2% | 26.8% | 26.4% | -44.1% | 0.92 | 100% | 387 | 34% | 3.39 | 18 | 85% of 173 names |
| LEADER_nocut | 25.9% | +8.6% | +2.7% | 31.7% | 20.4% | -34.3% | 0.92 | 91% | 338 | 38% | 3.00 | 20 | 94% of 163 names |
| CURRENT_2pct | 24.8% | +7.5% | +1.6% | 20.3% | 29.9% | -28.6% | 1.06 | 65% | 1303 | 70% | 0.60 | 4 | 43% of 202 names |
| GRADE_HOLD | 24.7% | +7.5% | +1.6% | 34.3% | 15.5% | -30.4% | 0.90 | 91% | 313 | 40% | 2.86 | 22 | 70% of 157 names |
| LEADER | 24.3% | +7.1% | +1.2% | 23.7% | 25.4% | -38.6% | 0.91 | 90% | 383 | 34% | 3.34 | 18 | 87% of 170 names |
| CURRENT_lag1 | 20.5% | +3.2% | -2.6% | 21.4% | 19.6% | -21.8% | 1.13 | 51% | 1254 | 63% | 0.85 | 4 | 42% of 201 names |
| CURRENT | 18.8% | +1.6% | -4.3% | 15.5% | 22.6% | -22.5% | 1.06 | 50% | 1303 | 70% | 0.60 | 4 | 39% of 202 names |

**Biggest contributors (realized P&L by name, per $100k start):**

- CURRENT: LASR $38,754, PLTR $23,919, KLAC $20,520, SNOW $14,396, DDOG $12,765
- CURRENT_2pct: LASR $70,164, PLTR $41,383, KLAC $34,693, SNOW $27,260, GS $21,403
- CURRENT_QQQcore: LASR $81,049, PLTR $45,384, KLAC $40,473, SNOW $30,867, DDOG $25,264
- LEADER: TSEM $83,444, MRNA $79,892, AMAT $70,909, LASR $56,702, NET $45,269
- LEADER_QQQcore: TSEM $91,706, AMAT $80,364, MRNA $77,232, LASR $60,742, NET $49,625
- LEADER_nocut: TSEM $105,967, MRNA $96,079, AMAT $78,589, LASR $74,286, PLTR $61,613
- GRADE_HOLD: LASR $67,594, NVDA $61,233, CRDO $52,163, GOOGL $49,402, PLTR $44,762
- GRADE_HOLD_any: AAOI $3,675,058, AEHR $1,544,884, LITE $1,452,812, RKLB $792,068, ONDS $662,732
- ROTATE_MONTHLY: LASR $814,371, LITE $679,649, RGTI $338,302, RKLB $233,373, IREN $214,031
- ROTATE_MONTHLY_QQQcore: LASR $907,703, LITE $770,473, RGTI $383,940, RKLB $264,936, IREN $239,378
- ROTATE_MONTHLY_8: LITE $307,787, VIAV $296,873, LASR $287,346, RGTI $153,036, APLD $137,493
- OLD_CONNORS: CRWD $52,400, LAES $46,405, HIVE $46,256, RIVN $31,769, LRCX $28,081

**Calendar-year returns:**

| Strategy | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 31.1% | 18.3% | 28.7% | -18.2% | 26.2% | 24.9% | 17.7% | 12.9% |
| **QQQ** | 38.4% | 48.6% | 27.4% | -32.6% | 54.9% | 25.6% | 20.8% | 20.5% |
| CURRENT | 16.4% | 39.3% | 25.2% | -12.3% | 35.9% | 24.9% | 12.6% | 11.9% |
| CURRENT_lag1 | 24.6% | 31.2% | 47.1% | -9.8% | 28.6% | 28.8% | 16.8% | 0.6% |
| CURRENT_2pct | 21.6% | 53.5% | 33.5% | -16.1% | 48.7% | 33.0% | 16.2% | 15.4% |
| CURRENT_QQQcore | 29.1% | 82.2% | 37.0% | -26.7% | 52.9% | 24.8% | 24.5% | 11.6% |
| LEADER | 32.6% | 45.7% | 66.3% | -27.3% | 4.9% | 34.1% | 40.6% | 16.6% |
| LEADER_lag1 | 38.8% | 68.0% | 76.5% | -27.6% | 11.7% | 36.5% | 57.3% | 23.1% |
| LEADER_QQQcore | 37.2% | 49.0% | 77.0% | -28.6% | 7.7% | 28.2% | 42.3% | 20.4% |
| LEADER_nocut | 36.7% | 55.5% | 61.5% | -12.5% | 18.3% | 34.4% | 22.5% | 1.4% |
| GRADE_HOLD | 36.7% | 53.8% | 54.3% | -0.1% | -9.6% | 31.6% | 34.4% | 6.7% |
| GRADE_HOLD_lag1 | 32.9% | 63.1% | 68.0% | -3.4% | -12.3% | 42.6% | 43.4% | 21.1% |
| GRADE_HOLD_any | 45.9% | 362.5% | 39.0% | -8.3% | 41.8% | 200.1% | 23.3% | 127.1% |
| GRADE_HOLD_any_lag1 | 45.5% | 304.4% | 34.6% | -0.8% | 45.7% | 210.0% | 143.8% | 121.4% |
| GRADE_HOLD_any_cost25bp | 43.0% | 353.1% | 32.7% | -9.9% | 39.2% | 189.0% | 20.0% | 123.0% |
| ROTATE_MONTHLY | 23.3% | 163.6% | -3.1% | 2.7% | 12.0% | 373.6% | -0.3% | 36.2% |
| ROTATE_MONTHLY_lag1 | 41.7% | 147.9% | -17.8% | 5.5% | 15.5% | 397.6% | -5.4% | 70.0% |
| ROTATE_MONTHLY_cost25bp | 21.3% | 161.7% | -5.1% | 2.0% | 10.5% | 365.1% | -1.6% | 35.1% |
| ROTATE_MONTHLY_QQQcore | 26.5% | 168.1% | 1.2% | -0.5% | 18.6% | 380.8% | -0.5% | 35.8% |
| ROTATE_MONTHLY_QQQcore_lag1 | 45.0% | 151.5% | -15.2% | 0.3% | 19.0% | 408.0% | -6.2% | 67.9% |
| ROTATE_MONTHLY_8 | 18.6% | 188.8% | 14.0% | 1.7% | 16.1% | 160.7% | 21.7% | 50.8% |
| OLD_CONNORS | 33.6% | 65.6% | -4.5% | 8.4% | 5.8% | 13.2% | 68.0% | 43.9% |

**Definitions and exit mix:**

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
- **GRADE_HOLD_any_lag1** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 214}
- **GRADE_HOLD_any_cost25bp** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 210}
- **ROTATE_MONTHLY** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 107}
- **ROTATE_MONTHLY_lag1** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 105}
- **ROTATE_MONTHLY_cost25bp** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 107}
- **ROTATE_MONTHLY_QQQcore** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 107}
- **ROTATE_MONTHLY_QQQcore_lag1** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 105}
- **ROTATE_MONTHLY_8** — ROTATE_MONTHLY with 8 slots. Exits: {'grade_exit': 198}
- **OLD_CONNORS** — Pre-2026-09-25 screen for reference: RSI2<10 above a rising 200SMA; RSI2>=70 TP; 14-day time stop. Exits: {'rsi2_tp': 881, 'time_stop': 229}

_A1 FULL scan universe (today's list: survivorship-biased) compute: 162s._

## Part A — A2 scan universe minus the 41 SPECULATIVE names: 195 names, 2019-01-02 → 2026-09-29

| Strategy | CAGR | vs SPY | vs QQQ | 2019-22 CAGR | 2023-26 CAGR | Max DD | Sharpe | Invested | Trades | Win % | Payoff | Hold (d) | Top-5 names' share of profit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY buy & hold** | 17.2% | | | 13.1% | 22.0% | -33.7% | 0.93 | 100% | | | | | |
| **QQQ buy & hold** | 23.1% | | | 15.3% | 32.4% | -35.1% | 0.99 | 100% | | | | | |
| GRADE_HOLD_any_lag1 | 64.2% | +47.0% | +41.1% | 71.0% | 57.7% | -36.7% | 1.43 | 94% | 204 | 50% | 3.57 | 35 | 69% of 106 names |
| GRADE_HOLD_any | 59.6% | +42.4% | +36.5% | 65.1% | 54.2% | -36.2% | 1.36 | 94% | 205 | 50% | 3.41 | 35 | 69% of 105 names |
| ROTATE_MONTHLY_QQQcore_lag1 | 50.2% | +32.9% | +27.0% | 42.4% | 59.7% | -39.1% | 1.18 | 99% | 100 | 61% | 3.27 | 66 | 79% of 70 names |
| ROTATE_MONTHLY_lag1 | 49.1% | +31.8% | +25.9% | 41.9% | 57.8% | -39.8% | 1.17 | 89% | 100 | 62% | 3.12 | 66 | 82% of 70 names |
| ROTATE_MONTHLY_QQQcore | 49.0% | +31.7% | +25.8% | 45.1% | 54.0% | -40.7% | 1.16 | 99% | 103 | 61% | 2.88 | 65 | 81% of 72 names |
| ROTATE_MONTHLY | 48.3% | +31.1% | +25.2% | 44.6% | 53.1% | -41.0% | 1.17 | 91% | 101 | 61% | 2.87 | 66 | 80% of 72 names |
| ROTATE_MONTHLY_8 | 45.4% | +28.2% | +22.3% | 48.7% | 42.8% | -35.1% | 1.24 | 85% | 196 | 52% | 4.15 | 62 | 72% of 107 names |
| LEADER_lag1 | 29.6% | +12.4% | +6.5% | 29.7% | 30.1% | -39.0% | 1.09 | 92% | 404 | 44% | 2.56 | 17 | 62% of 154 names |
| GRADE_HOLD_lag1 | 28.8% | +11.6% | +5.7% | 36.0% | 22.0% | -26.9% | 1.03 | 93% | 337 | 47% | 2.32 | 21 | 67% of 152 names |
| LEADER_QQQcore | 25.1% | +7.9% | +2.0% | 23.0% | 27.9% | -42.2% | 0.92 | 100% | 390 | 35% | 3.21 | 18 | 83% of 154 names |
| LEADER | 24.5% | +7.3% | +1.4% | 21.5% | 28.3% | -38.7% | 0.93 | 92% | 388 | 36% | 3.16 | 18 | 80% of 151 names |
| GRADE_HOLD | 24.4% | +7.2% | +1.3% | 31.3% | 18.0% | -33.2% | 0.89 | 93% | 328 | 41% | 2.70 | 21 | 89% of 148 names |
| CURRENT_QQQcore | 20.6% | +3.4% | -2.5% | 24.8% | 16.4% | -28.5% | 0.86 | 99% | 1285 | 69% | 0.59 | 4 | 42% of 182 names |
| CURRENT_2pct | 18.1% | +0.8% | -5.0% | 19.8% | 16.4% | -22.8% | 0.85 | 63% | 1285 | 69% | 0.59 | 4 | 43% of 182 names |
| CURRENT_lag1 | 17.0% | -0.2% | -6.1% | 16.7% | 17.5% | -21.8% | 1.00 | 50% | 1248 | 63% | 0.84 | 4 | 37% of 183 names |
| CURRENT | 13.9% | -3.3% | -9.2% | 15.2% | 12.7% | -17.6% | 0.85 | 48% | 1285 | 69% | 0.59 | 4 | 40% of 182 names |

**Biggest contributors (realized P&L by name, per $100k start):**

- CURRENT: SHOP $17,666, KLAC $16,364, PLTR $13,691, SOFI $12,022, SNOW $10,906
- CURRENT_2pct: SHOP $26,950, KLAC $25,764, PLTR $23,041, SOFI $19,183, SNOW $18,703
- CURRENT_QQQcore: KLAC $31,260, SHOP $31,179, PLTR $25,527, SOFI $22,923, SNOW $22,148
- LEADER: NOK $84,272, MRNA $77,577, PLTR $62,450, AMAT $50,390, CRWD $42,809
- LEADER_QQQcore: NOK $86,509, MRNA $83,558, PLTR $66,766, AMAT $54,130, CRWD $45,483
- GRADE_HOLD: PLTR $116,296, CRDO $56,911, SHOP $54,904, AMAT $51,826, NVDA $45,964
- GRADE_HOLD_any: AEHR $535,143, PLTR $490,682, LITE $487,120, MU $390,806, BE $331,887
- ROTATE_MONTHLY: LITE $617,630, PLTR $269,387, BE $250,183, MU $219,765, COHR $195,379
- ROTATE_MONTHLY_QQQcore: LITE $661,243, PLTR $286,383, BE $263,729, MU $235,012, COHR $208,608
- ROTATE_MONTHLY_8: LITE $677,657, BE $153,340, AMAT $144,814, COHR $113,656, PLTR $107,156

_A2 scan universe minus the 41 SPECULATIVE names compute: 149s._

## Part A — A3 S&P 100 as of end-2018 (no hindsight in the universe): 96 names, 2019-01-02 → 2026-09-29

| Strategy | CAGR | vs SPY | vs QQQ | 2019-22 CAGR | 2023-26 CAGR | Max DD | Sharpe | Invested | Trades | Win % | Payoff | Hold (d) | Top-5 names' share of profit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY buy & hold** | 17.2% | | | 13.1% | 22.0% | -33.7% | 0.93 | 100% | | | | | |
| **QQQ buy & hold** | 23.1% | | | 15.3% | 32.4% | -35.1% | 0.99 | 100% | | | | | |
| ROTATE_MONTHLY_QQQcore | 15.4% | -1.8% | -7.7% | 21.5% | 9.8% | -25.8% | 0.69 | 99% | 120 | 45% | 3.13 | 58 | 105% of 68 names |
| ROTATE_MONTHLY_QQQcore_lag1 | 14.8% | -2.5% | -8.4% | 22.4% | 7.6% | -25.8% | 0.67 | 99% | 121 | 50% | 2.59 | 58 | 101% of 68 names |
| GRADE_HOLD_lag1 | 14.7% | -2.5% | -8.4% | 18.6% | 11.0% | -26.3% | 0.74 | 88% | 293 | 41% | 2.58 | 23 | 71% of 91 names |
| ROTATE_MONTHLY | 13.8% | -3.4% | -9.3% | 20.6% | 7.6% | -26.0% | 0.64 | 94% | 123 | 45% | 3.16 | 58 | 103% of 69 names |
| GRADE_HOLD | 13.8% | -3.5% | -9.4% | 18.5% | 9.1% | -25.8% | 0.70 | 88% | 287 | 37% | 2.88 | 23 | 69% of 91 names |
| ROTATE_MONTHLY_lag1 | 13.8% | -3.5% | -9.4% | 21.4% | 6.6% | -26.0% | 0.65 | 93% | 121 | 50% | 2.59 | 58 | 99% of 68 names |
| ROTATE_MONTHLY_8 | 12.4% | -4.8% | -10.7% | 16.0% | 9.4% | -24.6% | 0.68 | 85% | 215 | 47% | 2.67 | 59 | 70% of 84 names |
| GRADE_HOLD_any_lag1 | 12.2% | -5.0% | -10.9% | 11.3% | 13.3% | -30.0% | 0.61 | 96% | 232 | 44% | 2.11 | 32 | 124% of 83 names |
| ROTATE_MONTHLY_cost25bp | 11.9% | -5.3% | -11.2% | 19.0% | 5.6% | -26.2% | 0.58 | 94% | 123 | 44% | 2.94 | 58 | 114% of 68 names |
| GRADE_HOLD_any | 11.9% | -5.4% | -11.2% | 12.9% | 10.9% | -27.0% | 0.60 | 97% | 232 | 44% | 2.11 | 32 | 126% of 83 names |
| LEADER_QQQcore | 10.0% | -7.2% | -13.1% | 15.2% | 4.9% | -33.0% | 0.56 | 99% | 371 | 30% | 3.10 | 18 | 89% of 94 names |
| CURRENT_QQQcore | 9.7% | -7.5% | -13.4% | 14.1% | 5.4% | -33.2% | 0.53 | 99% | 954 | 70% | 0.51 | 4 | 81% of 94 names |
| LEADER_lag1 | 8.9% | -8.3% | -14.2% | 12.6% | 5.3% | -34.1% | 0.56 | 86% | 363 | 37% | 2.37 | 18 | 111% of 95 names |
| GRADE_HOLD_any_cost25bp | 8.7% | -8.6% | -14.5% | 9.7% | 7.6% | -28.7% | 0.47 | 97% | 232 | 42% | 2.04 | 32 | 160% of 83 names |
| LEADER | 6.8% | -10.4% | -16.3% | 10.6% | 3.1% | -35.6% | 0.46 | 87% | 373 | 30% | 3.00 | 18 | 104% of 94 names |
| CURRENT_2pct | 6.4% | -10.9% | -16.8% | 11.6% | 1.1% | -21.7% | 0.47 | 49% | 954 | 70% | 0.51 | 4 | 81% of 94 names |
| CURRENT_lag1 | 6.0% | -11.3% | -17.1% | 6.0% | 6.0% | -17.9% | 0.53 | 38% | 941 | 61% | 0.78 | 4 | 61% of 95 names |
| CURRENT | 5.0% | -12.2% | -18.1% | 8.9% | 0.9% | -16.9% | 0.47 | 37% | 954 | 70% | 0.51 | 4 | 77% of 94 names |

**Biggest contributors (realized P&L by name, per $100k start):**

- CURRENT: MMM $7,600, PYPL $7,570, GE $7,051, NVDA $6,899, T $6,323
- CURRENT_2pct: MMM $11,059, PYPL $10,450, GE $10,129, NVDA $9,401, T $8,956
- CURRENT_QQQcore: MMM $13,204, PYPL $12,631, GE $11,831, T $10,426, NVDA $10,244
- LEADER: GOOGL $14,899, CVX $11,896, CAT $11,893, PYPL $10,687, GILD $9,960
- LEADER_QQQcore: GOOGL $19,008, CAT $15,195, CVX $14,360, GE $12,447, MMM $12,080
- GRADE_HOLD: GOOGL $29,166, NVDA $21,974, CAT $19,464, BK $18,306, MMM $17,505
- GRADE_HOLD_any: NVDA $54,816, INTC $52,087, CAT $34,353, GE $23,270, OXY $16,864
- ROTATE_MONTHLY: NVDA $86,884, CAT $45,256, META $22,630, MMM $20,209, COF $17,631
- ROTATE_MONTHLY_QQQcore: NVDA $91,690, CAT $50,824, META $24,072, MMM $21,659, COF $19,023
- ROTATE_MONTHLY_8: NVDA $45,336, CAT $19,464, META $18,319, GE $12,345, GOOGL $11,193

**Calendar-year returns:**

| Strategy | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 31.1% | 18.3% | 28.7% | -18.2% | 26.2% | 24.9% | 17.7% | 12.9% |
| **QQQ** | 38.4% | 48.6% | 27.4% | -32.6% | 54.9% | 25.6% | 20.8% | 20.5% |
| CURRENT | 7.3% | 23.4% | 8.1% | -1.6% | 0.2% | 10.7% | -5.0% | -1.6% |
| CURRENT_lag1 | 7.9% | 10.8% | 9.2% | -3.3% | 8.4% | 15.2% | 2.3% | -2.8% |
| CURRENT_2pct | 9.5% | 31.1% | 10.4% | -2.4% | 0.1% | 14.0% | -6.7% | -2.2% |
| CURRENT_QQQcore | 26.2% | 52.2% | 14.2% | -22.8% | 10.2% | 15.2% | -0.5% | -4.2% |
| LEADER | 17.6% | 18.3% | 17.3% | -8.3% | -6.4% | 10.4% | 17.1% | -8.1% |
| LEADER_lag1 | 19.7% | 22.7% | 21.2% | -9.8% | -0.0% | 12.0% | 19.5% | -10.0% |
| LEADER_QQQcore | 29.5% | 30.0% | 15.8% | -9.7% | 1.1% | 11.4% | 16.9% | -9.8% |
| GRADE_HOLD | 14.0% | 46.6% | 15.8% | 1.8% | 23.8% | 11.2% | 8.8% | -8.1% |
| GRADE_HOLD_lag1 | 14.6% | 44.0% | 17.7% | 1.6% | 23.4% | 12.1% | 13.5% | -6.6% |
| GRADE_HOLD_any | 19.2% | 26.5% | 7.2% | 0.4% | 18.9% | 9.3% | 14.0% | -1.0% |
| GRADE_HOLD_any_lag1 | 18.0% | 26.5% | 9.0% | -5.9% | 25.0% | 5.7% | 11.5% | 8.0% |
| GRADE_HOLD_any_cost25bp | 15.3% | 24.1% | 3.0% | -1.7% | 16.1% | 5.6% | 11.2% | -3.7% |
| ROTATE_MONTHLY | 23.4% | 52.1% | -3.9% | 17.3% | 8.5% | 26.3% | 6.6% | -11.8% |
| ROTATE_MONTHLY_lag1 | 26.0% | 51.6% | -3.5% | 17.4% | 10.1% | 22.4% | 1.3% | -8.3% |
| ROTATE_MONTHLY_cost25bp | 21.8% | 50.9% | -6.0% | 15.9% | 6.8% | 24.2% | 4.3% | -13.7% |
| ROTATE_MONTHLY_QQQcore | 29.4% | 56.9% | -2.2% | 9.5% | 13.2% | 31.7% | 6.7% | -12.3% |
| ROTATE_MONTHLY_QQQcore_lag1 | 28.5% | 56.1% | -2.1% | 14.2% | 10.7% | 28.0% | 0.6% | -9.2% |
| ROTATE_MONTHLY_8 | 17.0% | 39.0% | 7.9% | 3.1% | 17.4% | 11.8% | 13.5% | -8.2% |

**Definitions and exit mix:**

- **CURRENT** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 668, 'grade_exit': 286}
- **CURRENT_lag1** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 658, 'grade_exit': 283}
- **CURRENT_2pct** — Same exits, only a 2% cash reserve (options bucket returned to stocks). Exits: {'rsi2_tp': 668, 'grade_exit': 286}
- **CURRENT_QQQcore** — Same exits, idle cash parked in QQQ. Exits: {'rsi2_tp': 668, 'grade_exit': 286}
- **LEADER** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 119, 'grade_exit': 251, 'trail': 3}
- **LEADER_lag1** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 119, 'grade_exit': 241, 'trail': 3}
- **LEADER_QQQcore** — LEADER with idle cash in QQQ. Exits: {'loss_cut': 119, 'grade_exit': 249, 'trail': 3}
- **GRADE_HOLD** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 287}
- **GRADE_HOLD_lag1** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 293}
- **GRADE_HOLD_any** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 232}
- **GRADE_HOLD_any_lag1** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 232}
- **GRADE_HOLD_any_cost25bp** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 232}
- **ROTATE_MONTHLY** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 123}
- **ROTATE_MONTHLY_lag1** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 121}
- **ROTATE_MONTHLY_cost25bp** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 123}
- **ROTATE_MONTHLY_QQQcore** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 120}
- **ROTATE_MONTHLY_QQQcore_lag1** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 121}
- **ROTATE_MONTHLY_8** — ROTATE_MONTHLY with 8 slots. Exits: {'grade_exit': 215}

_A3 S&P 100 as of end-2018 (no hindsight in the universe) compute: 78s._

## Part A — A4 Nasdaq-100 as of end-2018 (QQQ's own pool, no hindsight): 88 names, 2019-01-02 → 2026-09-29

| Strategy | CAGR | vs SPY | vs QQQ | 2019-22 CAGR | 2023-26 CAGR | Max DD | Sharpe | Invested | Trades | Win % | Payoff | Hold (d) | Top-5 names' share of profit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY buy & hold** | 17.2% | | | 13.1% | 22.0% | -33.7% | 0.93 | 100% | | | | | |
| **QQQ buy & hold** | 23.1% | | | 15.3% | 32.4% | -35.1% | 0.99 | 100% | | | | | |
| ROTATE_MONTHLY_lag1 | 29.6% | +12.4% | +6.5% | 26.0% | 33.9% | -33.3% | 0.96 | 94% | 111 | 49% | 4.11 | 63 | 102% of 61 names |
| ROTATE_MONTHLY_QQQcore | 27.7% | +10.4% | +4.6% | 23.2% | 33.0% | -39.0% | 0.90 | 99% | 116 | 47% | 3.72 | 60 | 106% of 63 names |
| ROTATE_MONTHLY_QQQcore_lag1 | 27.0% | +9.8% | +3.9% | 21.2% | 33.8% | -38.0% | 0.89 | 99% | 116 | 47% | 3.72 | 60 | 106% of 63 names |
| ROTATE_MONTHLY | 26.3% | +9.1% | +3.2% | 20.9% | 32.6% | -38.8% | 0.88 | 94% | 116 | 47% | 3.72 | 60 | 106% of 63 names |
| ROTATE_MONTHLY_cost25bp | 24.5% | +7.2% | +1.4% | 19.2% | 30.7% | -38.9% | 0.84 | 94% | 116 | 46% | 3.61 | 60 | 110% of 63 names |
| GRADE_HOLD_any_lag1 | 24.5% | +7.2% | +1.3% | 7.4% | 45.5% | -40.0% | 0.87 | 94% | 211 | 41% | 3.30 | 33 | 119% of 78 names |
| GRADE_HOLD_any | 22.2% | +5.0% | -0.9% | 4.0% | 44.9% | -47.6% | 0.81 | 94% | 213 | 36% | 3.88 | 33 | 121% of 78 names |
| ROTATE_MONTHLY_8 | 21.6% | +4.4% | -1.5% | 19.7% | 24.1% | -30.6% | 0.84 | 86% | 205 | 45% | 3.46 | 61 | 92% of 77 names |
| GRADE_HOLD_any_cost25bp | 19.4% | +2.1% | -3.8% | 1.5% | 41.7% | -50.1% | 0.73 | 94% | 212 | 36% | 3.59 | 33 | 130% of 78 names |
| CURRENT_QQQcore | 16.8% | -0.4% | -6.3% | 13.5% | 20.7% | -48.5% | 0.76 | 99% | 902 | 70% | 0.51 | 4 | 142% of 88 names |
| GRADE_HOLD | 14.9% | -2.3% | -8.2% | 20.2% | 9.6% | -46.2% | 0.66 | 85% | 279 | 36% | 3.05 | 23 | 117% of 81 names |
| GRADE_HOLD_lag1 | 13.5% | -3.7% | -9.6% | 15.8% | 11.2% | -38.6% | 0.61 | 85% | 276 | 42% | 2.19 | 23 | 136% of 82 names |
| LEADER_QQQcore | 11.6% | -5.6% | -11.5% | 9.4% | 14.1% | -48.4% | 0.55 | 99% | 392 | 31% | 2.82 | 16 | 190% of 86 names |
| CURRENT_2pct | 7.4% | -9.8% | -15.7% | 8.2% | 6.8% | -41.7% | 0.47 | 47% | 902 | 70% | 0.51 | 4 | 116% of 88 names |
| LEADER | 6.4% | -10.9% | -16.8% | 5.5% | 7.4% | -46.4% | 0.38 | 85% | 393 | 31% | 2.79 | 16 | 197% of 88 names |
| CURRENT | 5.9% | -11.4% | -17.3% | 6.5% | 5.3% | -33.5% | 0.46 | 36% | 902 | 70% | 0.51 | 4 | 106% of 88 names |
| LEADER_lag1 | 4.2% | -13.0% | -18.9% | 2.3% | 6.4% | -44.8% | 0.29 | 83% | 395 | 38% | 1.86 | 16 | 309% of 88 names |
| CURRENT_lag1 | 3.2% | -14.0% | -19.9% | -0.1% | 7.1% | -32.5% | 0.29 | 37% | 875 | 60% | 0.75 | 4 | 128% of 88 names |

**Biggest contributors (realized P&L by name, per $100k start):**

- CURRENT: KLAC $19,205, AMAT $12,555, VRTX $10,345, WDC $8,716, NVDA $7,981
- CURRENT_2pct: KLAC $27,686, AMAT $18,575, VRTX $14,659, WDC $12,824, NTAP $11,855
- CURRENT_QQQcore: KLAC $40,887, AMAT $27,862, WDC $22,998, VRTX $17,893, NTAP $17,648
- LEADER: AMAT $46,056, LRCX $13,720, GOOGL $13,356, PYPL $10,718, REGN $9,549
- LEADER_QQQcore: AMAT $55,797, MU $25,612, GOOGL $15,981, LRCX $15,666, PYPL $11,521
- GRADE_HOLD: AMAT $67,094, WDC $46,336, NVDA $32,973, LRCX $21,486, VRTX $18,779
- GRADE_HOLD_any: WDC $219,482, NVDA $66,714, AMAT $42,674, MU $41,938, JD $18,565
- ROTATE_MONTHLY: WDC $301,651, NVDA $102,065, MU $33,568, TSLA $28,949, JBHT $28,554
- ROTATE_MONTHLY_QQQcore: WDC $328,264, NVDA $108,890, MU $36,533, JBHT $30,927, TSLA $30,260
- ROTATE_MONTHLY_8: WDC $156,866, NVDA $74,043, AMAT $42,150, MU $18,914, JD $18,843

**Calendar-year returns:**

| Strategy | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 31.1% | 18.3% | 28.7% | -18.2% | 26.2% | 24.9% | 17.7% | 12.9% |
| **QQQ** | 38.4% | 48.6% | 27.4% | -32.6% | 54.9% | 25.6% | 20.8% | 20.5% |
| CURRENT | 20.2% | 28.4% | 9.3% | -23.9% | 6.9% | 8.9% | 3.2% | 0.6% |
| CURRENT_lag1 | 15.6% | 19.4% | -0.4% | -27.4% | 9.3% | 16.8% | -5.2% | 6.1% |
| CURRENT_2pct | 27.0% | 38.2% | 12.1% | -30.4% | 8.9% | 11.5% | 4.0% | 0.7% |
| CURRENT_QQQcore | 49.6% | 64.0% | 16.5% | -42.0% | 32.7% | 21.1% | 11.0% | 12.7% |
| LEADER | 27.9% | 24.4% | 14.4% | -32.0% | 8.4% | 10.7% | -10.1% | 20.6% |
| LEADER_lag1 | 21.8% | 12.9% | 15.3% | -31.0% | 1.5% | 16.3% | -10.2% | 18.4% |
| LEADER_QQQcore | 34.3% | 39.8% | 22.7% | -37.9% | 12.7% | 11.3% | -4.0% | 35.8% |
| GRADE_HOLD | 31.1% | 69.0% | 15.7% | -18.8% | -2.4% | 0.5% | -11.2% | 61.5% |
| GRADE_HOLD_lag1 | 23.2% | 58.0% | 17.9% | -21.6% | 3.2% | 6.2% | -11.6% | 53.2% |
| GRADE_HOLD_any | 35.0% | 42.5% | -2.2% | -37.9% | 18.0% | 24.0% | 36.6% | 102.1% |
| GRADE_HOLD_any_lag1 | 35.7% | 37.3% | 7.7% | -33.8% | 16.3% | 25.8% | 37.8% | 103.0% |
| GRADE_HOLD_any_cost25bp | 33.8% | 38.7% | -5.6% | -39.5% | 14.7% | 20.8% | 33.5% | 100.5% |
| ROTATE_MONTHLY | 15.7% | 77.5% | 19.4% | -13.0% | -4.2% | 24.0% | 19.9% | 100.4% |
| ROTATE_MONTHLY_lag1 | 16.4% | 112.6% | 16.7% | -12.7% | 1.0% | 20.8% | 21.8% | 99.2% |
| ROTATE_MONTHLY_cost25bp | 13.5% | 75.6% | 17.7% | -14.0% | -5.9% | 21.8% | 18.2% | 99.1% |
| ROTATE_MONTHLY_QQQcore | 19.7% | 81.4% | 22.0% | -13.2% | -3.1% | 25.0% | 18.4% | 101.3% |
| ROTATE_MONTHLY_QQQcore_lag1 | 20.3% | 74.4% | 19.0% | -13.7% | 1.0% | 21.5% | 20.3% | 100.1% |
| ROTATE_MONTHLY_8 | 20.5% | 69.5% | 18.7% | -15.6% | 4.2% | 14.2% | 11.9% | 67.0% |

**Definitions and exit mix:**

- **CURRENT** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 628, 'grade_exit': 274}
- **CURRENT_lag1** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 598, 'grade_exit': 277}
- **CURRENT_2pct** — Same exits, only a 2% cash reserve (options bucket returned to stocks). Exits: {'rsi2_tp': 628, 'grade_exit': 274}
- **CURRENT_QQQcore** — Same exits, idle cash parked in QQQ. Exits: {'rsi2_tp': 628, 'grade_exit': 274}
- **LEADER** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 147, 'grade_exit': 235, 'trail': 11}
- **LEADER_lag1** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 150, 'grade_exit': 236, 'trail': 9}
- **LEADER_QQQcore** — LEADER with idle cash in QQQ. Exits: {'loss_cut': 145, 'grade_exit': 236, 'trail': 11}
- **GRADE_HOLD** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 279}
- **GRADE_HOLD_lag1** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 276}
- **GRADE_HOLD_any** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 213}
- **GRADE_HOLD_any_lag1** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 211}
- **GRADE_HOLD_any_cost25bp** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 212}
- **ROTATE_MONTHLY** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 116}
- **ROTATE_MONTHLY_lag1** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 111}
- **ROTATE_MONTHLY_cost25bp** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 116}
- **ROTATE_MONTHLY_QQQcore** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 116}
- **ROTATE_MONTHLY_QQQcore_lag1** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 116}
- **ROTATE_MONTHLY_8** — ROTATE_MONTHLY with 8 slots. Exits: {'grade_exit': 205}

_A4 Nasdaq-100 as of end-2018 (QQQ's own pool, no hindsight) compute: 72s._

## Part C — index-based alternatives, 2019-01-02 → 2026-09-29

Real ETF closes (expense ratios and daily-reset decay included). Trend filter: in the fund while QQQ > its 200-day SMA, else T-bills (BIL); switches fill at the next close.

| Strategy | CAGR | Max DD | Sharpe | Vol | Time invested | Switches |
|---|---|---|---|---|---|---|
| QQQ buy & hold | 23.1% | -35.1% | 0.99 | 24% | 100% | 0 |
| QQQ + 200d trend filter | 19.5% | -22.1% | 1.11 | 17% | 81% | 32 |
| QLD buy & hold | 37.0% | -63.7% | 0.90 | 48% | 100% | 0 |
| QLD + 200d trend filter | 33.6% | -40.2% | 1.01 | 35% | 81% | 32 |
| TQQQ buy & hold | 45.0% | -81.7% | 0.89 | 71% | 100% | 0 |
| TQQQ + 200d trend filter | 46.3% | -54.8% | 1.00 | 52% | 81% | 32 |

| Strategy | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| QQQ buy & hold | 38.4% | 48.6% | 27.4% | -32.6% | 54.9% | 25.6% | 20.8% | 20.5% |
| QQQ + 200d trend filter | 19.1% | 36.6% | 27.4% | -16.1% | 37.5% | 25.6% | 14.4% | 15.7% |
| QLD buy & hold | 80.2% | 88.8% | 54.7% | -60.5% | 117.8% | 42.8% | 30.4% | 35.4% |
| QLD + 200d trend filter | 35.1% | 72.1% | 54.7% | -30.7% | 73.1% | 42.8% | 21.7% | 25.5% |
| TQQQ buy & hold | 130.3% | 110.2% | 83.0% | -79.1% | 203.2% | 59.4% | 34.4% | 47.8% |
| TQQQ + 200d trend filter | 52.2% | 105.7% | 83.0% | -42.8% | 116.8% | 59.4% | 27.0% | 32.5% |

## Part B — day track (QQQ 5-min opening-range breakout)

Bar size: 5-minute (1-minute is paywalled on this FMP tier; the paper itself uses the first 5-minute bar). Sessions: 500 (2024-09-30 → 2026-09-28). Cost model: 1¢ per side = 0.011R per round trip at the average OR range (1.90 pts).

| Rules | Trades | Win % | Gross R/trade | Net R/trade | Total net R | Net R excl. best trade | Best trade R |
|---|---|---|---|---|---|---|---|
| paper | 499 | 28% | +0.168 | +0.158 | +78.8 | +68.8 | +10.0 |
| ours | 462 | 29% | +0.063 | +0.053 | +24.3 | +17.3 | +7.1 |

`paper` = Zarattini & Aziz: stop at the opposite OR extreme, 10R target, else exit at the close. `ours` = docs/day-track-spec.md: body filter, late-entry gate, breakeven at +1R, 1.5×ATR(5-min) trail from +2R, 12:00 chop exit, 15:30 flat.

Dollar scale at this account: a cash-bound QQQ position of ~$2,500 on a typical OR range risks about $6.41 per R.

## Data log

- 1min fetch 2024-09-29..2024-10-03 failed: {'_http_error': 402}
