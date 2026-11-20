# Bottom watch: which variables say the low is in

Built 2026-08-04 data. Re-run with `python3 bottom_backtest.py`.

- **Sample:** 5,058 days inside 49 QQQ and SPY selloffs, 1999-09 to 2026 (closing prices). VIX history starts 2002-05, so models that use it are fitted on 4,249 days.
- **Question on each day:** has the lowest close of this selloff already printed?
- **Score:** 0.50 means the variable is useless; 1.00 means it separates the two perfectly (AUC, direction-adjusted). "On the low day" is the same score using only days that made a new closing low.

## Each variable on its own

| Variable | Score | Low more likely in when it is | On the low day | Days |
|---|---|---|---|---|
| VIX below its peak of the selloff | 0.83 | lower | 0.57 | 4,249 |
| Close vs the 200-day average | 0.81 | higher | 0.68 | 5,058 |
| Share of the drop retraced | 0.79 | higher | 0.50 | 5,058 |
| Close vs the 50-day average | 0.78 | higher | 0.65 | 5,058 |
| RSI(14) | 0.77 | higher | 0.50 | 5,058 |
| Rebound off the low, in daily ranges | 0.77 | higher | 0.50 | 5,058 |
| Close vs the 20-day average | 0.73 | higher | 0.59 | 5,058 |
| Above the 200-day | 0.72 | higher | 0.60 | 5,058 |
| Above the 50-day | 0.71 | higher | 0.50 | 5,058 |
| Sessions since the VIX peak | 0.70 | higher | 0.51 | 4,249 |
| Rebound off the low, % | 0.70 | higher | 0.50 | 5,058 |
| Junk bonds vs Treasuries, 20 days | 0.68 | higher | 0.55 | 3,285 |
| Above the 20-day | 0.68 | higher | 0.50 | 5,058 |
| VIX vs its 20-day average | 0.68 | lower | 0.50 | 4,249 |
| Up-day vs down-day volume, 10 days | 0.67 | higher | 0.57 | 5,058 |
| Drawdown from the high | 0.67 | higher | 0.68 | 5,058 |
| Sessions since the low | 0.66 | higher | 0.50 | 5,058 |
| Direction of the 200-day | 0.66 | higher | 0.68 | 5,058 |
| RSI(2) | 0.65 | higher | 0.52 | 5,058 |
| Above the 10-day | 0.65 | higher | 0.50 | 5,058 |
| VIX level | 0.64 | lower | 0.56 | 4,249 |
| Junk bonds vs Treasuries, 5 days | 0.63 | higher | 0.51 | 3,285 |
| VIX peak of the selloff | 0.62 | higher | 0.52 | 4,249 |
| Best rebound so far | 0.62 | higher | 0.50 | 5,058 |
| Above the 5-day | 0.61 | higher | 0.50 | 5,058 |
| Low-day volume vs peak volume | 0.60 | lower | 0.51 | 5,058 |
| Close position on the low day | 0.58 | lower | 0.54 | 5,058 |
| RSI on the low day | 0.58 | higher | 0.50 | 5,058 |
| Follow-through day | 0.57 | higher | 0.50 | 5,058 |
| Volume on the low day | 0.57 | lower | 0.56 | 5,058 |
| Failed rebounds so far | 0.57 | lower | 0.69 | 5,058 |
| RSI divergence at the low | 0.56 | higher | 0.52 | 5,058 |
| Rebound given back | 0.56 | higher | 0.50 | 5,058 |
| VIX on the low day | 0.56 | higher | 0.56 | 4,193 |
| Sessions from the high to the low | 0.56 | lower | 0.69 | 5,058 |
| Peak volume into the low | 0.56 | lower | 0.51 | 5,058 |
| Depth of the low | 0.56 | higher | 0.68 | 5,058 |
| VIX vs the previous leg's low | 0.55 | lower | 0.53 | 4,249 |
| VIX divergence at the low | 0.53 | lower | 0.57 | 4,193 |
| Peak volume of the selloff | 0.53 | higher | 0.53 | 5,058 |
| Speed of the decline | 0.53 | higher | 0.63 | 5,058 |
| Sessions since the high | 0.53 | lower | 0.69 | 5,058 |
| Sessions since peak volume | 0.52 | higher | 0.63 | 5,058 |
| Average stock vs the index, 20 days | 0.51 | higher | 0.51 | 3,285 |

A day that makes a new closing low turns out to be the final low 13% of the time. Volume on the low day, a close off the low, follow-through days and the equal-weight index all score near 0.50: they did not separate final lows from the rest.

## Combining them (tested on selloffs the model had not seen)

| Model | Score | Improvement over always guessing the base rate |
|---|---|---|
| VIX off its peak only | 0.803 | 16.5% |
| + close vs the 200-day | 0.836 | 28.9% |
| + RSI(14)  [chosen] | 0.835 | 30.5% |
| + share of the drop retraced | 0.810 | 28.7% |
| + failed rebounds so far | 0.834 | 29.9% |
| + direction of the 200-day | 0.823 | 28.2% |
| + junk bonds vs Treasuries | 0.827 | 26.6% |
| 11 variables | 0.804 | 25.1% |
| No VIX: 200-day + RSI(14) | 0.807 | 27.9% |

Adding a fourth variable made the out-of-sample result worse every time, so the model stops at three.

## The model

Chance the low is in = a logistic blend of three readings, then adjusted so that the stated chance matches how often it was right out of sample.

| Reading | Average in past selloffs | Weight (per standard deviation) |
|---|---|---|
| VIX below its peak of the selloff | -0.353 | -0.83 |
| Close vs the 200-day average | -0.038 | +0.92 |
| RSI(14) | 49.859 | +0.52 |

Out of sample: score 0.835; 30.5% better than the base rate.

| Stated chance | Days | Low really was in |
|---|---|---|
| 0% to 25% | 482 | 14% |
| 25% to 50% | 766 | 30% |
| 50% to 70% | 458 | 50% |
| 70% to 85% | 884 | 68% |
| 85% to 100% | 1,659 | 89% |

## How fast it calls a low, and how often it is fooled

- **Speed:** across 49 selloffs the reading reached 50% a median of 2 sessions after the final low (price 3.1% off the low by then) and 70% after 4 sessions (4.4% off the low).
- **False alarms:** before the final low the reading crossed 50% 111 times and 70% 77 times. 61 and 47 of those were inside the selloffs that fell more than 25% (2000-02, 2008, 2020, 2022): bear-market rallies look like bottoms to this model.

| Index | High | Final low | Depth | Sessions to 50% | Off the low then | False 50% crossings | Sessions to 70% | Off the low then | False 70% crossings |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 2000-03-24 | 2002-10-09 | -49.1% | 8 | 15.5% | 3 | 17 | 15.6% | 4 |
| QQQ | 2000-03-27 | 2002-10-09 | -83.0% | 12 | 22.7% | 1 | 17 | 25.9% | 0 |
| QQQ | 2004-01-26 | 2004-03-23 | -11.8% | 2 | 3.9% | 0 | 4 | 5.2% | 0 |
| QQQ | 2004-01-26 | 2004-04-30 | -11.8% | 28 | 3.1% | 0 | 30 | 4.4% | 0 |
| QQQ | 2004-01-26 | 2004-08-12 | -15.9% | 4 | 4.3% | 4 | 9 | 6.4% | 1 |
| SPY | 2004-03-05 | 2004-08-06 | -8.2% | 7 | 1.9% | 0 | 8 | 3.0% | 0 |
| QQQ | 2004-12-14 | 2005-04-20 | -14.3% | 10 | 3.0% | 1 | 13 | 3.8% | 0 |
| QQQ | 2006-01-11 | 2006-07-21 | -17.4% | 1 | 2.0% | 5 | 5 | 3.9% | 4 |
| SPY | 2007-07-19 | 2007-08-15 | -9.0% | 3 | 2.6% | 0 | 5 | 4.0% | 0 |
| SPY | 2007-10-09 | 2007-11-26 | -9.9% | 2 | 4.4% | 4 | 2 | 4.4% | 1 |
| SPY | 2007-10-09 | 2009-03-09 | -56.5% | 7 | 17.4% | 15 | 13 | 22.0% | 9 |
| QQQ | 2007-10-31 | 2008-11-20 | -53.6% | 28 | 21.4% | 11 | 53 | 23.2% | 12 |
| QQQ | 2010-04-23 | 2010-07-02 | -15.9% | 1 | 0.3% | 2 | 2 | 3.5% | 3 |
| SPY | 2010-04-23 | 2010-07-02 | -16.1% | 1 | 0.7% | 4 | 2 | 3.8% | 4 |
| SPY | 2011-04-29 | 2011-10-03 | -19.4% | 3 | 6.0% | 4 | 5 | 8.8% | 2 |
| QQQ | 2011-07-26 | 2011-08-19 | -16.1% | 3 | 5.3% | 1 | 6 | 9.2% | 1 |
| QQQ | 2011-07-26 | 2011-11-23 | -16.1% | 69 | 9.4% | 0 | 69 | 9.4% | 0 |
| QQQ | 2012-04-02 | 2012-06-01 | -11.5% | 3 | 3.5% | 1 | 3 | 3.5% | 0 |
| SPY | 2012-04-02 | 2012-06-04 | -9.7% | 2 | 3.0% | 2 | 4 | 3.9% | 0 |
| QQQ | 2012-09-19 | 2012-11-15 | -11.9% | 2 | 2.8% | 0 | 8 | 5.6% | 0 |
| SPY | 2015-05-21 | 2015-08-25 | -12.3% | 2 | 6.4% | 0 | 2 | 6.4% | 0 |
| SPY | 2015-05-21 | 2016-02-11 | -14.4% | 1 | 2.1% | 4 | 2 | 3.8% | 3 |
| QQQ | 2015-07-20 | 2015-08-25 | -13.9% | 2 | 7.7% | 0 | 2 | 7.7% | 0 |
| QQQ | 2015-12-01 | 2016-02-09 | -16.4% | 5 | 6.4% | 1 | 8 | 7.2% | 0 |
| QQQ | 2018-01-26 | 2018-02-08 | -10.2% | 1 | 1.7% | 0 | 1 | 1.7% | 0 |
| SPY | 2018-01-26 | 2018-02-08 | -10.1% | 1 | 1.5% | 0 | 2 | 3.0% | 0 |
| SPY | 2018-01-26 | 2018-04-02 | -10.2% | 0 | 0.0% | 1 | 0 | 0.0% | 1 |
| QQQ | 2018-03-12 | 2018-04-02 | -10.7% | 1 | 1.1% | 0 | 2 | 2.7% | 0 |
| QQQ | 2018-08-29 | 2018-12-24 | -23.2% | 5 | 7.9% | 5 | 7 | 8.9% | 3 |
| SPY | 2018-09-20 | 2018-12-24 | -20.2% | 5 | 6.8% | 3 | 7 | 7.7% | 3 |
| QQQ | 2019-05-03 | 2019-06-03 | -10.9% | 1 | 2.8% | 0 | 3 | 4.3% | 0 |
| QQQ | 2020-02-19 | 2020-03-16 | -28.6% | 8 | 13.3% | 3 | 10 | 13.4% | 2 |
| SPY | 2020-02-19 | 2020-03-23 | -34.1% | 10 | 18.8% | 2 | 12 | 22.9% | 1 |
| QQQ | 2020-09-02 | 2020-09-23 | -12.7% | 0 | 0.0% | 1 | 0 | 0.0% | 1 |
| QQQ | 2020-09-02 | 2020-10-28 | -12.7% | 25 | 2.8% | 0 | 26 | 4.6% | 0 |
| SPY | 2020-09-02 | 2020-09-23 | -9.8% | 0 | 0.0% | 1 | 2 | 1.9% | 1 |
| SPY | 2020-09-02 | 2020-10-28 | -9.8% | 26 | 2.3% | 0 | 29 | 4.2% | 0 |
| QQQ | 2021-02-12 | 2021-03-08 | -10.9% | 1 | 3.9% | 0 | 1 | 3.9% | 0 |
| QQQ | 2021-11-19 | 2022-12-28 | -35.6% | 1 | 2.4% | 13 | 6 | 3.3% | 10 |
| SPY | 2022-01-03 | 2022-10-12 | -25.4% | 8 | 6.3% | 13 | 9 | 8.0% | 9 |
| QQQ | 2023-07-18 | 2023-10-26 | -10.9% | 3 | 2.1% | 0 | 4 | 3.9% | 0 |
| SPY | 2023-07-31 | 2023-10-27 | -10.3% | 3 | 2.9% | 0 | 3 | 2.9% | 0 |
| QQQ | 2024-07-10 | 2024-08-07 | -13.6% | 0 | 0.0% | 1 | 1 | 3.1% | 0 |
| SPY | 2024-07-16 | 2024-08-05 | -8.4% | 1 | 0.9% | 0 | 1 | 0.9% | 0 |
| QQQ | 2025-02-19 | 2025-04-08 | -22.9% | 1 | 12.0% | 3 | 1 | 12.0% | 1 |
| SPY | 2025-02-19 | 2025-04-08 | -19.0% | 1 | 10.5% | 2 | 1 | 10.5% | 1 |
| QQQ | 2025-10-29 | 2026-03-30 | -12.2% | 1 | 3.4% | 0 | 4 | 5.4% | 0 |
| SPY | 2026-01-27 | 2026-03-30 | -9.1% | 1 | 2.9% | 0 | 6 | 7.0% | 0 |
| QQQ | 2026-06-02 | 2026-07-29 | -11.3% | 1 | 3.3% | 0 | 1 | 3.3% | 0 |

## Limits

- About 50 selloffs, and QQQ and SPY mostly fall together, so the independent sample is nearer 25.
- Only three of them were long bear markets. The model cannot tell a bear-market rally from a final low early on.
- Everything is on closing prices. An intraday reading uses the live price as if it were the close.
- VIX readings before 2002-05 were not available, so the 2000-01 part of the dot-com bust is not in the VIX model.
