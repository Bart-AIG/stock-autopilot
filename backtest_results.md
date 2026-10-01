# Process backtest — run 2026-10-01 16:03Z

Data sources (daily): {'historical-price-eod/dividend-adjusted': 275, 'historical-price-eod/light': 7, 'none': 13}. Names with history: 282.

## Part A — A1 FULL scan universe (today's list: survivorship-biased): 225 names, 2019-01-02 → 2026-10-01

| Strategy | CAGR | vs SPY | vs QQQ | 2019-22 CAGR | 2023-26 CAGR | Max DD | Sharpe | Invested | Trades | Win % | Payoff | Hold (d) | Top-5 names' share of profit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY buy & hold** | 15.4% | | | 11.2% | 20.3% | -34.1% | 0.84 | 100% | | | | | |
| **QQQ buy & hold** | 23.1% | | | 15.3% | 32.3% | -35.1% | 0.99 | 100% | | | | | |
| GRADE_HOLD_any | 71.7% | +56.2% | +48.6% | 53.9% | 93.5% | -46.6% | 1.37 | 94% | 216 | 49% | 3.39 | 32 | 93% of 117 names |
| GRADE_HOLD_any_cost25bp | 67.7% | +52.3% | +44.6% | 49.6% | 90.1% | -47.1% | 1.32 | 94% | 216 | 48% | 3.31 | 32 | 94% of 116 names |
| GRADE_HOLD_any_lag1 | 65.6% | +50.2% | +42.5% | 44.8% | 91.7% | -56.1% | 1.29 | 94% | 215 | 48% | 3.15 | 33 | 83% of 115 names |
| ROTATE_MONTHLY_QQQcore_lag1 | 57.2% | +41.7% | +34.1% | 39.5% | 79.3% | -51.1% | 1.11 | 99% | 109 | 60% | 2.62 | 60 | 88% of 80 names |
| ROTATE_MONTHLY_QQQcore | 56.0% | +40.6% | +32.9% | 39.1% | 76.8% | -50.8% | 1.10 | 99% | 110 | 59% | 2.49 | 59 | 107% of 82 names |
| ROTATE_MONTHLY_lag1 | 55.4% | +40.0% | +32.3% | 37.7% | 77.7% | -50.9% | 1.10 | 90% | 109 | 60% | 2.62 | 60 | 88% of 80 names |
| ROTATE_MONTHLY | 53.1% | +37.7% | +30.1% | 36.8% | 73.2% | -50.7% | 1.08 | 90% | 109 | 59% | 2.53 | 59 | 105% of 82 names |
| ROTATE_MONTHLY_cost25bp | 51.1% | +35.6% | +28.0% | 35.1% | 70.6% | -50.7% | 1.05 | 90% | 109 | 57% | 2.63 | 59 | 106% of 82 names |
| ROTATE_MONTHLY_8 | 45.5% | +30.1% | +22.4% | 33.3% | 60.5% | -44.8% | 1.11 | 85% | 203 | 55% | 2.94 | 61 | 63% of 120 names |
| LEADER_lag1 | 27.5% | +12.1% | +4.4% | 27.8% | 27.4% | -41.5% | 1.02 | 91% | 399 | 43% | 2.50 | 17 | 64% of 162 names |
| GRADE_HOLD_lag1 | 27.0% | +11.5% | +3.9% | 26.8% | 27.1% | -34.1% | 0.95 | 92% | 306 | 47% | 2.29 | 22 | 68% of 155 names |
| LEADER_QQQcore | 26.8% | +11.3% | +3.7% | 24.4% | 29.6% | -40.5% | 0.95 | 99% | 389 | 35% | 3.29 | 18 | 67% of 164 names |
| LEADER | 26.2% | +10.8% | +3.1% | 24.2% | 28.6% | -37.5% | 0.96 | 91% | 387 | 36% | 3.26 | 18 | 65% of 164 names |
| CURRENT_QQQcore | 25.7% | +10.3% | +2.7% | 25.5% | 25.9% | -30.9% | 1.00 | 99% | 1291 | 71% | 0.58 | 4 | 47% of 192 names |
| CURRENT_2pct | 24.3% | +8.9% | +1.2% | 22.4% | 26.4% | -23.0% | 1.06 | 64% | 1291 | 71% | 0.58 | 4 | 49% of 192 names |
| OLD_CONNORS | 23.9% | +8.5% | +0.9% | 19.8% | 29.2% | -40.5% | 0.89 | 88% | 1098 | 78% | 0.39 | 6 | 33% of 213 names |
| LEADER_nocut | 22.8% | +7.4% | -0.3% | 28.9% | 16.9% | -32.6% | 0.87 | 91% | 326 | 40% | 2.65 | 21 | 96% of 154 names |
| GRADE_HOLD | 21.5% | +6.1% | -1.6% | 25.5% | 17.4% | -34.4% | 0.80 | 91% | 309 | 39% | 2.70 | 22 | 84% of 155 names |
| CURRENT_lag1 | 19.2% | +3.8% | -3.9% | 21.0% | 17.3% | -21.1% | 1.07 | 50% | 1244 | 62% | 0.87 | 4 | 42% of 190 names |
| CURRENT | 18.5% | +3.1% | -4.6% | 17.0% | 20.1% | -18.0% | 1.05 | 49% | 1291 | 71% | 0.58 | 4 | 45% of 192 names |

**Biggest contributors (realized P&L by name, per $100k start):**

- CURRENT: LASR $39,827, PLTR $30,294, KLAC $20,612, CRDO $18,148, SHOP $14,375
- CURRENT_2pct: LASR $72,448, PLTR $53,205, KLAC $34,946, CRDO $33,180, DDOG $23,492
- CURRENT_QQQcore: LASR $81,291, PLTR $55,816, KLAC $40,038, CRDO $36,255, DDOG $27,298
- LEADER: AMAT $69,382, LASR $63,445, NET $52,414, PLTR $52,348, NVDA $51,736
- LEADER_QQQcore: AMAT $72,887, LASR $64,821, NVDA $55,412, NET $54,304, PLTR $53,469
- LEADER_nocut: PLTR $101,865, LASR $67,210, NET $55,444, MRNA $50,553, GOOGL $40,833
- GRADE_HOLD: SHOP $56,807, LASR $56,509, NVDA $53,547, GOOGL $40,828, CRDO $38,992
- GRADE_HOLD_any: AAOI $2,464,300, LITE $922,836, AEHR $919,605, IREN $693,222, ONDS $431,405
- ROTATE_MONTHLY: LASR $914,672, LITE $763,349, RGTI $349,253, PLTR $257,183, IREN $240,391
- ROTATE_MONTHLY_QQQcore: LASR $1,043,891, LITE $886,061, RGTI $405,466, PLTR $296,230, IREN $275,293
- ROTATE_MONTHLY_8: LITE $252,742, VIAV $243,031, LASR $229,990, APLD $141,912, RGTI $120,007
- OLD_CONNORS: LAES $37,538, CRWD $37,538, RIVN $24,421, LRCX $22,624, PLTR $21,559

**Calendar-year returns:**

| Strategy | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 28.7% | 16.2% | 27.0% | -19.5% | 24.3% | 23.3% | 16.4% | 11.5% |
| **QQQ** | 38.4% | 48.6% | 27.4% | -32.6% | 54.9% | 25.6% | 20.8% | 20.4% |
| CURRENT | 16.9% | 38.2% | 29.4% | -10.4% | 33.8% | 24.0% | 10.1% | 8.8% |
| CURRENT_lag1 | 28.2% | 39.5% | 35.5% | -11.6% | 19.4% | 27.1% | 17.2% | 2.3% |
| CURRENT_2pct | 22.3% | 52.0% | 39.3% | -13.6% | 45.8% | 31.8% | 12.9% | 11.2% |
| CURRENT_QQQcore | 32.4% | 80.0% | 40.6% | -26.0% | 47.6% | 22.5% | 23.2% | 6.8% |
| LEADER | 26.8% | 49.2% | 51.3% | -16.9% | 18.0% | 39.0% | 19.3% | 30.3% |
| LEADER_lag1 | 34.2% | 72.9% | 56.1% | -26.6% | 2.4% | 36.3% | 37.4% | 28.7% |
| LEADER_QQQcore | 31.6% | 53.3% | 56.1% | -24.0% | 20.2% | 39.6% | 19.5% | 30.9% |
| LEADER_nocut | 38.2% | 57.4% | 51.1% | -16.2% | 2.2% | 54.9% | 4.5% | 7.7% |
| GRADE_HOLD | 38.2% | 53.6% | 32.7% | -12.2% | -3.7% | 31.4% | 31.3% | 10.1% |
| GRADE_HOLD_lag1 | 34.1% | 64.3% | 31.9% | -11.3% | 7.5% | 30.8% | 62.8% | 7.7% |
| GRADE_HOLD_any | 44.0% | 218.0% | 32.0% | -7.7% | 39.6% | 145.2% | 66.5% | 106.4% |
| GRADE_HOLD_any_lag1 | 40.1% | 191.2% | 17.5% | -8.7% | 43.3% | 168.5% | 41.8% | 108.1% |
| GRADE_HOLD_any_cost25bp | 41.0% | 212.7% | 25.8% | -9.9% | 34.2% | 150.5% | 61.5% | 102.6% |
| ROTATE_MONTHLY | 20.8% | 149.4% | 13.8% | 1.8% | 12.0% | 361.3% | 6.5% | 41.3% |
| ROTATE_MONTHLY_lag1 | 39.2% | 151.0% | 0.8% | 1.9% | 15.5% | 340.3% | -5.4% | 76.2% |
| ROTATE_MONTHLY_cost25bp | 18.9% | 147.8% | 11.5% | 1.1% | 10.5% | 351.4% | 5.2% | 40.1% |
| ROTATE_MONTHLY_QQQcore | 23.9% | 157.9% | 18.6% | -1.4% | 18.6% | 372.1% | 6.4% | 40.9% |
| ROTATE_MONTHLY_QQQcore_lag1 | 42.5% | 157.6% | 4.3% | -1.3% | 19.0% | 351.8% | -6.2% | 74.0% |
| ROTATE_MONTHLY_8 | 17.4% | 137.5% | 11.8% | 1.0% | 16.6% | 154.0% | 27.2% | 53.7% |
| OLD_CONNORS | 26.1% | 54.2% | -17.1% | 27.5% | -0.1% | 17.2% | 47.5% | 48.6% |

**Definitions and exit mix:**

- **CURRENT** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 900, 'grade_exit': 391}
- **CURRENT_lag1** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 840, 'grade_exit': 404}
- **CURRENT_2pct** — Same exits, only a 2% cash reserve (options bucket returned to stocks). Exits: {'rsi2_tp': 900, 'grade_exit': 391}
- **CURRENT_QQQcore** — Same exits, idle cash parked in QQQ. Exits: {'rsi2_tp': 900, 'grade_exit': 391}
- **LEADER** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 106, 'grade_exit': 256, 'trail': 25}
- **LEADER_lag1** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 122, 'grade_exit': 255, 'trail': 22}
- **LEADER_QQQcore** — LEADER with idle cash in QQQ. Exits: {'loss_cut': 106, 'grade_exit': 258, 'trail': 25}
- **LEADER_nocut** — Grade exit + 15% trail, no loss cut. Exits: {'grade_exit': 295, 'trail': 31}
- **GRADE_HOLD** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 309}
- **GRADE_HOLD_lag1** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 306}
- **GRADE_HOLD_any** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 216}
- **GRADE_HOLD_any_lag1** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 215}
- **GRADE_HOLD_any_cost25bp** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 216}
- **ROTATE_MONTHLY** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 109}
- **ROTATE_MONTHLY_lag1** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 109}
- **ROTATE_MONTHLY_cost25bp** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 109}
- **ROTATE_MONTHLY_QQQcore** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 110}
- **ROTATE_MONTHLY_QQQcore_lag1** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 109}
- **ROTATE_MONTHLY_8** — ROTATE_MONTHLY with 8 slots. Exits: {'grade_exit': 203}
- **OLD_CONNORS** — Pre-2026-09-25 screen for reference: RSI2<10 above a rising 200SMA; RSI2>=70 TP; 14-day time stop. Exits: {'rsi2_tp': 867, 'time_stop': 231}

_A1 FULL scan universe (today's list: survivorship-biased) compute: 186s._

## Part A — A2 scan universe minus the 41 SPECULATIVE names: 185 names, 2019-01-02 → 2026-10-01

| Strategy | CAGR | vs SPY | vs QQQ | 2019-22 CAGR | 2023-26 CAGR | Max DD | Sharpe | Invested | Trades | Win % | Payoff | Hold (d) | Top-5 names' share of profit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY buy & hold** | 15.4% | | | 11.2% | 20.3% | -34.1% | 0.84 | 100% | | | | | |
| **QQQ buy & hold** | 23.1% | | | 15.3% | 32.3% | -35.1% | 0.99 | 100% | | | | | |
| ROTATE_MONTHLY_QQQcore_lag1 | 52.9% | +37.5% | +29.8% | 40.5% | 68.1% | -39.1% | 1.21 | 99% | 103 | 60% | 3.30 | 64 | 84% of 68 names |
| ROTATE_MONTHLY_lag1 | 51.4% | +35.9% | +28.3% | 39.5% | 65.9% | -39.8% | 1.20 | 90% | 101 | 59% | 3.40 | 65 | 86% of 68 names |
| GRADE_HOLD_any | 50.8% | +35.4% | +27.7% | 43.7% | 58.8% | -36.3% | 1.24 | 93% | 213 | 48% | 3.05 | 33 | 67% of 101 names |
| ROTATE_MONTHLY_QQQcore | 49.8% | +34.3% | +26.7% | 39.7% | 62.1% | -40.7% | 1.18 | 99% | 105 | 57% | 3.32 | 64 | 91% of 71 names |
| GRADE_HOLD_any_lag1 | 48.9% | +33.5% | +25.8% | 38.1% | 61.8% | -39.3% | 1.21 | 93% | 212 | 49% | 2.92 | 33 | 64% of 100 names |
| ROTATE_MONTHLY | 48.0% | +32.5% | +24.9% | 37.5% | 60.7% | -41.0% | 1.16 | 91% | 103 | 57% | 3.23 | 65 | 89% of 71 names |
| ROTATE_MONTHLY_8 | 42.3% | +26.9% | +19.2% | 35.1% | 51.3% | -33.9% | 1.19 | 85% | 198 | 53% | 3.83 | 62 | 78% of 105 names |
| GRADE_HOLD_lag1 | 31.0% | +15.6% | +7.9% | 34.0% | 27.7% | -29.0% | 1.10 | 92% | 309 | 47% | 2.52 | 22 | 47% of 140 names |
| LEADER_lag1 | 30.3% | +14.9% | +7.3% | 32.4% | 28.4% | -33.3% | 1.12 | 92% | 400 | 45% | 2.50 | 18 | 52% of 147 names |
| GRADE_HOLD | 24.9% | +9.5% | +1.9% | 27.0% | 22.5% | -29.4% | 0.92 | 91% | 318 | 42% | 2.63 | 22 | 55% of 138 names |
| LEADER_QQQcore | 23.6% | +8.2% | +0.5% | 21.3% | 26.4% | -42.2% | 0.89 | 100% | 392 | 36% | 3.09 | 18 | 64% of 146 names |
| LEADER | 23.0% | +7.6% | -0.1% | 20.5% | 25.9% | -39.8% | 0.90 | 92% | 396 | 36% | 3.08 | 18 | 66% of 147 names |
| CURRENT_QQQcore | 22.4% | +6.9% | -0.7% | 23.2% | 21.4% | -35.0% | 0.92 | 99% | 1248 | 69% | 0.61 | 4 | 42% of 172 names |
| CURRENT_2pct | 20.0% | +4.6% | -3.1% | 19.5% | 20.5% | -29.6% | 0.94 | 61% | 1248 | 69% | 0.61 | 4 | 42% of 172 names |
| CURRENT_lag1 | 18.5% | +3.0% | -4.6% | 17.0% | 20.1% | -19.9% | 1.09 | 48% | 1211 | 63% | 0.87 | 4 | 36% of 172 names |
| CURRENT | 15.3% | -0.1% | -7.8% | 14.9% | 15.7% | -23.4% | 0.93 | 47% | 1248 | 69% | 0.61 | 4 | 41% of 172 names |

**Biggest contributors (realized P&L by name, per $100k start):**

- CURRENT: PLTR $20,453, SHOP $19,768, KLAC $18,799, SOFI $11,964, DDOG $11,411
- CURRENT_2pct: PLTR $34,368, KLAC $30,544, SHOP $30,258, SOFI $19,108, DDOG $18,240
- CURRENT_QQQcore: PLTR $37,323, KLAC $36,455, SHOP $34,259, DDOG $22,247, SOFI $21,995
- LEADER: NOK $71,576, AMAT $44,571, PLTR $40,449, MRNA $36,817, CRWD $36,419
- LEADER_QQQcore: NOK $73,676, AMAT $47,906, PLTR $42,403, CRWD $38,675, GOOGL $38,409
- GRADE_HOLD: CRDO $48,567, AMAT $46,891, GOOGL $42,199, SPOT $38,613, NVDA $34,473
- GRADE_HOLD_any: MU $316,167, AEHR $294,837, LITE $289,735, PLTR $236,245, BE $189,328
- ROTATE_MONTHLY: LITE $593,102, BE $321,134, PLTR $220,448, MU $211,698, COHR $186,677
- ROTATE_MONTHLY_QQQcore: LITE $665,689, BE $363,617, PLTR $246,256, MU $238,065, COHR $208,744
- ROTATE_MONTHLY_8: LITE $495,450, VIAV $192,860, AEHR $134,367, BE $112,108, COHR $85,467

_A2 scan universe minus the 41 SPECULATIVE names compute: 157s._

## Part A — A3 S&P 100 as of end-2018 (no hindsight in the universe): 93 names, 2019-01-02 → 2026-10-01

| Strategy | CAGR | vs SPY | vs QQQ | 2019-22 CAGR | 2023-26 CAGR | Max DD | Sharpe | Invested | Trades | Win % | Payoff | Hold (d) | Top-5 names' share of profit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY buy & hold** | 15.4% | | | 11.2% | 20.3% | -34.1% | 0.84 | 100% | | | | | |
| **QQQ buy & hold** | 23.1% | | | 15.3% | 32.3% | -35.1% | 0.99 | 100% | | | | | |
| ROTATE_MONTHLY_QQQcore | 14.2% | -1.3% | -8.9% | 21.8% | 7.0% | -26.0% | 0.65 | 99% | 124 | 44% | 3.04 | 57 | 113% of 68 names |
| ROTATE_MONTHLY_QQQcore_lag1 | 13.8% | -1.6% | -9.2% | 21.9% | 6.3% | -25.8% | 0.64 | 99% | 122 | 49% | 2.47 | 57 | 100% of 67 names |
| ROTATE_MONTHLY_lag1 | 13.5% | -2.0% | -9.6% | 21.8% | 5.7% | -25.9% | 0.64 | 93% | 122 | 49% | 2.47 | 57 | 99% of 67 names |
| ROTATE_MONTHLY | 13.3% | -2.1% | -9.8% | 20.6% | 6.5% | -26.0% | 0.63 | 93% | 125 | 43% | 3.04 | 57 | 113% of 68 names |
| GRADE_HOLD_any | 12.4% | -3.0% | -10.7% | 14.9% | 9.9% | -27.9% | 0.61 | 97% | 231 | 42% | 2.30 | 32 | 126% of 78 names |
| ROTATE_MONTHLY_8 | 12.3% | -3.2% | -10.8% | 15.2% | 9.9% | -24.4% | 0.68 | 85% | 219 | 47% | 2.49 | 58 | 73% of 83 names |
| GRADE_HOLD_any_lag1 | 11.9% | -3.5% | -11.2% | 13.5% | 10.3% | -27.1% | 0.59 | 95% | 229 | 44% | 2.17 | 32 | 131% of 77 names |
| ROTATE_MONTHLY_cost25bp | 11.5% | -3.9% | -11.6% | 18.9% | 4.7% | -26.5% | 0.56 | 93% | 125 | 42% | 2.95 | 57 | 125% of 68 names |
| GRADE_HOLD | 9.4% | -6.1% | -13.7% | 14.8% | 4.1% | -23.4% | 0.54 | 88% | 298 | 36% | 2.57 | 22 | 97% of 88 names |
| GRADE_HOLD_any_cost25bp | 9.0% | -6.4% | -14.1% | 11.2% | 6.8% | -29.6% | 0.48 | 97% | 233 | 41% | 2.19 | 32 | 160% of 78 names |
| CURRENT_QQQcore | 8.8% | -6.6% | -14.3% | 12.6% | 5.1% | -33.0% | 0.49 | 99% | 961 | 70% | 0.49 | 4 | 105% of 89 names |
| GRADE_HOLD_lag1 | 8.8% | -6.6% | -14.3% | 14.0% | 3.7% | -25.6% | 0.51 | 88% | 303 | 40% | 2.18 | 22 | 109% of 88 names |
| LEADER_QQQcore | 7.3% | -8.1% | -15.8% | 12.4% | 2.3% | -29.1% | 0.44 | 99% | 392 | 30% | 2.79 | 17 | 175% of 91 names |
| LEADER_lag1 | 5.9% | -9.5% | -17.1% | 8.7% | 3.3% | -31.2% | 0.40 | 86% | 387 | 38% | 2.11 | 17 | 165% of 91 names |
| CURRENT_lag1 | 5.7% | -9.7% | -17.3% | 6.8% | 4.7% | -19.1% | 0.53 | 38% | 947 | 61% | 0.77 | 4 | 64% of 91 names |
| CURRENT_2pct | 4.8% | -10.7% | -18.3% | 9.2% | 0.3% | -23.0% | 0.38 | 49% | 961 | 70% | 0.49 | 4 | 97% of 89 names |
| CURRENT | 3.8% | -11.6% | -19.3% | 7.1% | 0.4% | -17.9% | 0.37 | 37% | 961 | 70% | 0.49 | 4 | 92% of 89 names |
| LEADER | 3.6% | -11.8% | -19.5% | 8.3% | -0.9% | -32.8% | 0.29 | 86% | 388 | 30% | 2.75 | 17 | 207% of 91 names |

**Biggest contributors (realized P&L by name, per $100k start):**

- CURRENT: PYPL $7,805, GE $7,196, T $6,283, GS $5,098, GILD $4,972
- CURRENT_2pct: PYPL $10,710, GE $10,134, T $8,704, GS $7,121, GILD $6,445
- CURRENT_QQQcore: PYPL $13,048, GE $12,303, T $10,452, GS $9,589, GM $8,178
- LEADER: GOOGL $13,281, CVX $10,860, GE $10,267, PYPL $9,938, GILD $8,939
- LEADER_QQQcore: GOOGL $16,045, CAT $11,564, GE $11,356, PYPL $11,150, META $10,457
- GRADE_HOLD: NVDA $23,913, GOOGL $22,127, CAT $14,689, CVX $14,099, META $13,942
- GRADE_HOLD_any: NVDA $63,152, INTC $55,384, GE $29,598, CAT $27,809, GOOGL $17,998
- ROTATE_MONTHLY: NVDA $82,781, CAT $44,230, META $23,567, KMI $21,522, GE $21,202
- ROTATE_MONTHLY_QQQcore: NVDA $86,188, CAT $47,305, META $24,444, KMI $22,933, GE $22,181
- ROTATE_MONTHLY_8: NVDA $42,857, CAT $20,077, META $17,805, GE $16,393, GOOG $12,747

**Calendar-year returns:**

| Strategy | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 28.7% | 16.2% | 27.0% | -19.5% | 24.3% | 23.3% | 16.4% | 11.5% |
| **QQQ** | 38.4% | 48.6% | 27.4% | -32.6% | 54.9% | 25.6% | 20.8% | 20.4% |
| CURRENT | 6.4% | 20.6% | 6.9% | -4.0% | 0.0% | 5.8% | -1.4% | -3.0% |
| CURRENT_lag1 | 9.7% | 14.2% | 7.7% | -3.7% | 7.9% | 12.3% | 2.1% | -4.1% |
| CURRENT_2pct | 8.4% | 27.2% | 8.8% | -5.5% | -0.1% | 7.4% | -1.9% | -4.0% |
| CURRENT_QQQcore | 24.9% | 47.7% | 13.3% | -23.1% | 10.6% | 10.8% | 2.3% | -4.6% |
| LEADER | 17.0% | 11.7% | 15.9% | -9.4% | -5.1% | 4.1% | 16.8% | -16.9% |
| LEADER_lag1 | 18.8% | 13.3% | 22.6% | -15.5% | 1.2% | 6.3% | 20.1% | -13.2% |
| LEADER_QQQcore | 25.8% | 22.6% | 17.1% | -11.6% | 0.4% | 3.7% | 16.0% | -10.6% |
| GRADE_HOLD | 9.9% | 29.0% | 17.6% | 4.1% | 10.1% | 2.9% | 15.7% | -12.1% |
| GRADE_HOLD_lag1 | 11.7% | 29.2% | 23.6% | -5.4% | 9.6% | 4.2% | 20.9% | -17.6% |
| GRADE_HOLD_any | 17.5% | 39.8% | 7.2% | -1.2% | 22.8% | 9.5% | 20.6% | -12.2% |
| GRADE_HOLD_any_lag1 | 19.3% | 34.1% | 8.3% | -4.2% | 25.1% | 4.3% | 16.7% | -5.5% |
| GRADE_HOLD_any_cost25bp | 13.6% | 38.8% | 3.3% | -6.1% | 20.3% | 5.6% | 17.7% | -14.6% |
| ROTATE_MONTHLY | 24.3% | 64.9% | -8.0% | 12.0% | 13.0% | 23.4% | 2.7% | -13.1% |
| ROTATE_MONTHLY_lag1 | 27.3% | 65.2% | -8.9% | 14.7% | 12.7% | 21.0% | -2.0% | -9.3% |
| ROTATE_MONTHLY_cost25bp | 22.6% | 63.7% | -10.3% | 10.7% | 11.4% | 21.2% | 1.2% | -14.6% |
| ROTATE_MONTHLY_QQQcore | 30.2% | 68.6% | -6.7% | 7.3% | 13.3% | 25.9% | 3.0% | -13.6% |
| ROTATE_MONTHLY_QQQcore_lag1 | 29.9% | 67.7% | -6.8% | 8.7% | 13.2% | 23.7% | -1.7% | -10.1% |
| ROTATE_MONTHLY_8 | 17.2% | 41.3% | 6.3% | -0.0% | 16.3% | 16.7% | 16.1% | -11.7% |

**Definitions and exit mix:**

- **CURRENT** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 668, 'grade_exit': 293}
- **CURRENT_lag1** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 657, 'grade_exit': 290}
- **CURRENT_2pct** — Same exits, only a 2% cash reserve (options bucket returned to stocks). Exits: {'rsi2_tp': 668, 'grade_exit': 293}
- **CURRENT_QQQcore** — Same exits, idle cash parked in QQQ. Exits: {'rsi2_tp': 668, 'grade_exit': 293}
- **LEADER** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 117, 'grade_exit': 267, 'trail': 4}
- **LEADER_lag1** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 123, 'grade_exit': 260, 'trail': 4}
- **LEADER_QQQcore** — LEADER with idle cash in QQQ. Exits: {'loss_cut': 118, 'grade_exit': 270, 'trail': 4}
- **GRADE_HOLD** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 298}
- **GRADE_HOLD_lag1** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 303}
- **GRADE_HOLD_any** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 231}
- **GRADE_HOLD_any_lag1** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 229}
- **GRADE_HOLD_any_cost25bp** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 233}
- **ROTATE_MONTHLY** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 125}
- **ROTATE_MONTHLY_lag1** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 122}
- **ROTATE_MONTHLY_cost25bp** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 125}
- **ROTATE_MONTHLY_QQQcore** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 124}
- **ROTATE_MONTHLY_QQQcore_lag1** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 122}
- **ROTATE_MONTHLY_8** — ROTATE_MONTHLY with 8 slots. Exits: {'grade_exit': 219}

_A3 S&P 100 as of end-2018 (no hindsight in the universe) compute: 82s._

## Part A — A4 Nasdaq-100 as of end-2018 (QQQ's own pool, no hindsight): 85 names, 2019-01-02 → 2026-10-01

| Strategy | CAGR | vs SPY | vs QQQ | 2019-22 CAGR | 2023-26 CAGR | Max DD | Sharpe | Invested | Trades | Win % | Payoff | Hold (d) | Top-5 names' share of profit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SPY buy & hold** | 15.4% | | | 11.2% | 20.3% | -34.1% | 0.84 | 100% | | | | | |
| **QQQ buy & hold** | 23.1% | | | 15.3% | 32.3% | -35.1% | 0.99 | 100% | | | | | |
| ROTATE_MONTHLY_lag1 | 30.5% | +15.0% | +7.4% | 25.8% | 36.0% | -33.3% | 0.98 | 93% | 112 | 46% | 4.71 | 61 | 104% of 62 names |
| ROTATE_MONTHLY_QQQcore | 29.4% | +14.0% | +6.3% | 22.9% | 37.2% | -39.0% | 0.94 | 99% | 117 | 46% | 3.89 | 58 | 108% of 64 names |
| ROTATE_MONTHLY | 28.1% | +12.6% | +5.0% | 20.8% | 36.6% | -38.8% | 0.92 | 92% | 116 | 47% | 3.91 | 59 | 107% of 63 names |
| ROTATE_MONTHLY_QQQcore_lag1 | 28.0% | +12.5% | +4.9% | 20.9% | 36.3% | -38.0% | 0.91 | 99% | 117 | 44% | 4.17 | 58 | 109% of 64 names |
| ROTATE_MONTHLY_cost25bp | 26.2% | +10.8% | +3.1% | 19.1% | 34.6% | -38.9% | 0.88 | 92% | 116 | 46% | 3.78 | 59 | 111% of 63 names |
| GRADE_HOLD_any | 22.9% | +7.5% | -0.2% | 6.9% | 42.4% | -44.7% | 0.81 | 95% | 223 | 36% | 4.00 | 32 | 122% of 77 names |
| ROTATE_MONTHLY_8 | 22.1% | +6.6% | -1.0% | 20.7% | 23.8% | -30.6% | 0.85 | 85% | 209 | 46% | 3.34 | 60 | 91% of 76 names |
| GRADE_HOLD_any_cost25bp | 19.8% | +4.4% | -3.3% | 4.1% | 39.1% | -47.5% | 0.73 | 94% | 222 | 36% | 3.69 | 32 | 131% of 77 names |
| GRADE_HOLD_any_lag1 | 19.6% | +4.2% | -3.5% | 5.8% | 36.2% | -47.7% | 0.73 | 94% | 226 | 40% | 3.11 | 31 | 125% of 77 names |
| CURRENT_QQQcore | 18.3% | +2.9% | -4.8% | 16.4% | 20.6% | -43.2% | 0.81 | 99% | 875 | 70% | 0.52 | 4 | 112% of 85 names |
| GRADE_HOLD_lag1 | 17.1% | +1.6% | -6.0% | 19.9% | 14.3% | -36.8% | 0.72 | 85% | 300 | 44% | 2.24 | 22 | 102% of 81 names |
| GRADE_HOLD | 15.1% | -0.3% | -8.0% | 18.3% | 12.1% | -45.6% | 0.66 | 84% | 297 | 36% | 2.99 | 21 | 111% of 82 names |
| LEADER_QQQcore | 9.2% | -6.2% | -13.8% | 8.7% | 10.0% | -48.3% | 0.47 | 99% | 403 | 30% | 2.85 | 16 | 352% of 85 names |
| CURRENT_2pct | 8.6% | -6.8% | -14.5% | 10.2% | 7.0% | -35.0% | 0.53 | 45% | 875 | 70% | 0.52 | 4 | 93% of 85 names |
| LEADER_lag1 | 8.6% | -6.9% | -14.5% | 5.2% | 12.4% | -42.1% | 0.47 | 82% | 401 | 40% | 2.04 | 15 | 154% of 85 names |
| CURRENT | 6.7% | -8.7% | -16.4% | 7.9% | 5.5% | -27.8% | 0.53 | 34% | 875 | 70% | 0.52 | 4 | 88% of 85 names |
| CURRENT_lag1 | 5.1% | -10.4% | -18.0% | 2.5% | 8.2% | -30.1% | 0.42 | 36% | 854 | 61% | 0.77 | 4 | 88% of 85 names |
| LEADER | 3.1% | -12.3% | -20.0% | 3.9% | 2.5% | -51.2% | 0.25 | 83% | 404 | 29% | 2.77 | 15 | 513% of 85 names |

**Biggest contributors (realized P&L by name, per $100k start):**

- CURRENT: KLAC $16,770, AMAT $14,430, LRCX $10,788, VRTX $8,440, MU $7,934
- CURRENT_2pct: KLAC $24,348, AMAT $21,378, LRCX $15,301, VRTX $11,783, MU $11,706
- CURRENT_QQQcore: KLAC $37,149, AMAT $33,666, LRCX $22,215, WDC $17,983, MU $17,596
- LEADER: AMAT $38,273, GOOGL $15,451, REGN $11,381, PYPL $10,593, AVGO $10,236
- LEADER_QQQcore: AMAT $51,940, MU $26,174, GOOGL $19,082, AVGO $12,477, REGN $11,867
- GRADE_HOLD: AMAT $67,531, WDC $50,665, GOOGL $23,439, JD $23,218, NVDA $20,261
- GRADE_HOLD_any: WDC $239,570, NVDA $72,062, MU $48,115, AMAT $36,279, LRCX $27,089
- ROTATE_MONTHLY: WDC $348,389, NVDA $128,695, MU $39,268, JBHT $30,511, TSLA $28,949
- ROTATE_MONTHLY_QQQcore: WDC $373,331, NVDA $136,683, MU $42,932, JBHT $33,251, TSLA $30,260
- ROTATE_MONTHLY_8: WDC $164,166, NVDA $75,386, AMAT $43,472, MU $19,442, JD $19,065

**Calendar-year returns:**

| Strategy | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| **SPY** | 28.7% | 16.2% | 27.0% | -19.5% | 24.3% | 23.3% | 16.4% | 11.5% |
| **QQQ** | 38.4% | 48.6% | 27.4% | -32.6% | 54.9% | 25.6% | 20.8% | 20.4% |
| CURRENT | 19.9% | 25.7% | 9.3% | -17.7% | 7.3% | 5.1% | 4.8% | 3.2% |
| CURRENT_lag1 | 16.4% | 26.6% | 1.5% | -26.3% | 9.0% | 11.8% | -2.5% | 12.1% |
| CURRENT_2pct | 26.5% | 34.5% | 12.0% | -22.7% | 9.4% | 6.5% | 6.1% | 4.0% |
| CURRENT_QQQcore | 47.8% | 64.3% | 19.1% | -36.6% | 34.8% | 12.4% | 12.2% | 17.9% |
| LEADER | 27.0% | 24.6% | 8.4% | -32.1% | 0.4% | 7.2% | -11.5% | 14.4% |
| LEADER_lag1 | 24.4% | 16.5% | 17.8% | -28.2% | 0.2% | 16.0% | -1.9% | 35.1% |
| LEADER_QQQcore | 32.1% | 43.5% | 19.5% | -38.3% | 9.1% | 8.5% | -6.3% | 28.1% |
| GRADE_HOLD | 26.0% | 64.9% | 9.6% | -14.2% | -12.8% | 6.9% | -7.7% | 77.4% |
| GRADE_HOLD_lag1 | 22.2% | 75.5% | 18.7% | -18.9% | -7.5% | 17.9% | -6.8% | 61.3% |
| GRADE_HOLD_any | 38.7% | 40.8% | 8.9% | -38.5% | 11.5% | 11.2% | 46.0% | 108.4% |
| GRADE_HOLD_any_lag1 | 29.3% | 35.8% | 15.6% | -38.4% | 7.7% | -2.7% | 40.8% | 116.7% |
| GRADE_HOLD_any_cost25bp | 35.3% | 37.6% | 5.1% | -40.1% | 7.9% | 7.4% | 42.6% | 109.0% |
| ROTATE_MONTHLY | 15.7% | 77.5% | 19.0% | -13.0% | 12.4% | 24.0% | 17.1% | 95.9% |
| ROTATE_MONTHLY_lag1 | 16.4% | 112.6% | 16.7% | -13.3% | 12.5% | 20.8% | 18.2% | 95.0% |
| ROTATE_MONTHLY_cost25bp | 13.5% | 75.6% | 17.3% | -14.0% | 10.5% | 21.8% | 15.4% | 94.4% |
| ROTATE_MONTHLY_QQQcore | 19.7% | 81.4% | 21.6% | -13.8% | 12.5% | 25.0% | 17.9% | 95.2% |
| ROTATE_MONTHLY_QQQcore_lag1 | 20.3% | 74.4% | 18.3% | -14.0% | 13.2% | 21.5% | 18.2% | 94.9% |
| ROTATE_MONTHLY_8 | 21.9% | 69.7% | 20.9% | -15.3% | 4.5% | 14.2% | 12.0% | 65.4% |

**Definitions and exit mix:**

- **CURRENT** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 611, 'grade_exit': 264}
- **CURRENT_lag1** — Live process: A/A+ + pullback trigger; exits RSI2>=70 (green) or grade exit; 25% of account idle (20% options bucket + 5% reserve). Exits: {'rsi2_tp': 578, 'grade_exit': 276}
- **CURRENT_2pct** — Same exits, only a 2% cash reserve (options bucket returned to stocks). Exits: {'rsi2_tp': 611, 'grade_exit': 264}
- **CURRENT_QQQcore** — Same exits, idle cash parked in QQQ. Exits: {'rsi2_tp': 611, 'grade_exit': 264}
- **LEADER** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 144, 'grade_exit': 246, 'trail': 14}
- **LEADER_lag1** — Pullback entry; exits grade exit, 15% trail from high, -8% / below-50SMA loss cut; no RSI2 take-profit. Exits: {'loss_cut': 142, 'grade_exit': 248, 'trail': 11}
- **LEADER_QQQcore** — LEADER with idle cash in QQQ. Exits: {'loss_cut': 142, 'grade_exit': 248, 'trail': 13}
- **GRADE_HOLD** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 297}
- **GRADE_HOLD_lag1** — Pullback entry; only exit = grade exit (hold while top 25%). Exits: {'grade_exit': 300}
- **GRADE_HOLD_any** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 223}
- **GRADE_HOLD_any_lag1** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 226}
- **GRADE_HOLD_any_cost25bp** — No pullback wait: buy the top-ranked A/A+ names as slots free; exit = grade exit. Exits: {'grade_exit': 222}
- **ROTATE_MONTHLY** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 116}
- **ROTATE_MONTHLY_lag1** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 112}
- **ROTATE_MONTHLY_cost25bp** — Monthly: hold top-4 A/A+ names, sell only if out of top 25% at month start. Exits: {'grade_exit': 116}
- **ROTATE_MONTHLY_QQQcore** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 117}
- **ROTATE_MONTHLY_QQQcore_lag1** — ROTATE_MONTHLY with idle cash in QQQ. Exits: {'grade_exit': 117}
- **ROTATE_MONTHLY_8** — ROTATE_MONTHLY with 8 slots. Exits: {'grade_exit': 209}

_A4 Nasdaq-100 as of end-2018 (QQQ's own pool, no hindsight) compute: 69s._

## Part C — index-based alternatives, 2019-01-02 → 2026-10-01

Real ETF closes (expense ratios and daily-reset decay included). Trend filter: in the fund while QQQ > its 200-day SMA, else T-bills (BIL); switches fill at the next close.

| Strategy | CAGR | Max DD | Sharpe | Vol | Time invested | Switches |
|---|---|---|---|---|---|---|
| QQQ buy & hold | 23.1% | -35.1% | 0.99 | 24% | 100% | 0 |
| QQQ + 200d trend filter | 19.5% | -22.1% | 1.11 | 17% | 81% | 32 |
| QLD buy & hold | 36.9% | -63.7% | 0.90 | 48% | 100% | 0 |
| QLD + 200d trend filter | 33.6% | -40.2% | 1.01 | 35% | 81% | 32 |
| TQQQ buy & hold | 45.0% | -81.7% | 0.88 | 71% | 100% | 0 |
| TQQQ + 200d trend filter | 46.3% | -54.8% | 1.00 | 52% | 81% | 32 |

| Strategy | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| QQQ buy & hold | 38.4% | 48.6% | 27.4% | -32.6% | 54.9% | 25.6% | 20.8% | 20.4% |
| QQQ + 200d trend filter | 19.1% | 36.6% | 27.4% | -16.1% | 37.5% | 25.6% | 14.4% | 15.6% |
| QLD buy & hold | 80.2% | 88.8% | 54.7% | -60.5% | 117.8% | 42.8% | 30.4% | 35.4% |
| QLD + 200d trend filter | 35.1% | 72.1% | 54.7% | -30.7% | 73.1% | 42.8% | 21.7% | 25.5% |
| TQQQ buy & hold | 130.3% | 110.2% | 83.0% | -79.1% | 203.2% | 59.4% | 34.4% | 47.7% |
| TQQQ + 200d trend filter | 52.2% | 105.7% | 83.0% | -42.8% | 116.8% | 59.4% | 27.0% | 32.4% |

## Part D — skipped (no long QQQ history: None)

## Part B — day track (QQQ 5-min opening-range breakout)

Bar size: 5-minute (1-minute is paywalled on this FMP tier; the paper itself uses the first 5-minute bar). Sessions: 467 (2024-10-01 → 2026-09-30). Cost model: 1¢ per side = 0.011R per round trip at the average OR range (1.90 pts).

| Rules | Trades | Win % | Gross R/trade | Net R/trade | Total net R | Net R excl. best trade | Best trade R |
|---|---|---|---|---|---|---|---|
| paper | 466 | 28% | +0.147 | +0.137 | +63.7 | +53.7 | +10.0 |
| ours | 431 | 29% | +0.057 | +0.046 | +20.0 | +12.9 | +7.1 |

`paper` = Zarattini & Aziz: stop at the opposite OR extreme, 10R target, else exit at the close. `ours` = docs/day-track-spec.md: body filter, late-entry gate, breakeven at +1R, 1.5×ATR(5-min) trail from +2R, 12:00 chop exit, 15:30 flat.

Dollar scale at this account: a cash-bound QQQ position of ~$2,500 on a typical OR range risks about $6.41 per R.

## Data log

- 1min fetch 2024-10-01..2024-10-05 failed: None
- 5min fetch 2024-12-30..2025-01-03 failed: None
- 5min fetch 2025-01-04..2025-01-08 failed: None
- 5min fetch 2025-05-19..2025-05-23 failed: None
- 5min fetch 2025-05-24..2025-05-28 failed: None
- 5min fetch 2025-10-31..2025-11-04 failed: None
- 5min fetch 2025-11-05..2025-11-09 failed: None
- 5min fetch 2026-02-08..2026-02-12 failed: None
- 5min fetch 2026-02-13..2026-02-17 failed: None
- 5min fetch 2026-08-12..2026-08-16 failed: None
- 5min fetch 2026-08-17..2026-08-21 failed: None
