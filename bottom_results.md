# Bottom watch: which variables say the low is in

Data through 2026-11-19. Re-run with `python3 bottom_backtest.py`.

- **Sample:** 5,058 days inside 49 finished QQQ and SPY selloffs, 1999-09 to 2026, on closing prices. A selloff starts when the close is 10% (QQQ) or 8% (SPY) under its 1-year closing high and ends when the close is back within 3% of it. VIX history starts 2002-05, so models that use it are fitted on 4,249 days.
- **Question on each day:** has the lowest close of this selloff already printed?
- **Score:** 0.50 means the variable is useless and 1.00 means it separates the two perfectly (area under the ROC curve). "On the low day" is the same score using only days that made a new closing low, which is the hardest moment to call.

## Each variable on its own

| Variable | Score | Low more likely in when it is | On the low day | Days |
|---|---|---|---|---|
| VIX below its peak of the selloff | 0.83 | lower | 0.57 | 4,249 |
| Close vs the 200-day average | 0.81 | higher | 0.68 | 5,058 |
| Share of the drop retraced | 0.79 | higher | 0.50 | 5,058 |
| Close vs the 50-day average | 0.78 | higher | 0.65 | 5,058 |
| RSI(14) | 0.77 | higher | 0.50 | 5,058 |
| Rebound off the low, in daily ranges | 0.77 | higher | 0.50 | 5,058 |
| Bollinger: position inside the bands | 0.73 | higher | 0.54 | 5,058 |
| Close vs the 20-day average | 0.73 | higher | 0.59 | 5,058 |
| Above the 200-day | 0.72 | higher | 0.60 | 5,058 |
| Above the 50-day | 0.71 | higher | 0.50 | 5,058 |
| Sessions since the VIX peak | 0.70 | higher | 0.51 | 4,249 |
| Rebound off the low, % | 0.70 | higher | 0.50 | 5,058 |
| Bollinger: sessions since a close under the lower band | 0.70 | higher | 0.54 | 5,017 |
| Junk bonds vs Treasuries, 20 days | 0.68 | higher | 0.55 | 3,285 |
| Above the 20-day | 0.68 | higher | 0.50 | 5,058 |
| VIX vs its 20-day average | 0.68 | lower | 0.50 | 4,249 |
| Margin debt / S&P 500 vs its 5-year average | 0.68 | lower | 0.56 | 3,650 |
| Shiller P/E at the high | 0.67 | lower | 0.62 | 5,058 |
| Up-day vs down-day volume, 10 days | 0.67 | higher | 0.57 | 5,058 |
| Drawdown from the high | 0.67 | higher | 0.68 | 5,058 |
| Bollinger: band width | 0.66 | lower | 0.60 | 5,058 |
| Sessions since the low | 0.66 | higher | 0.50 | 5,058 |
| Direction of the 200-day | 0.66 | higher | 0.68 | 5,058 |
| RSI(2) | 0.65 | higher | 0.52 | 5,058 |
| Above the 10-day | 0.65 | higher | 0.50 | 5,058 |
| Bollinger: highest position since the low | 0.64 | higher | 0.54 | 5,058 |
| VIX level | 0.64 | lower | 0.56 | 4,249 |
| Junk bonds vs Treasuries, 5 days | 0.63 | higher | 0.51 | 3,285 |
| VIX peak of the selloff | 0.62 | higher | 0.52 | 4,249 |
| Shiller P/E | 0.62 | lower | 0.50 | 5,058 |
| Best rebound so far | 0.62 | higher | 0.50 | 5,058 |
| Bollinger: bands narrower than their widest | 0.61 | lower | 0.64 | 5,058 |
| Above the 5-day | 0.61 | higher | 0.50 | 5,058 |
| Bollinger: position on the low day | 0.61 | higher | 0.54 | 5,058 |
| M2 growth, 12 months | 0.60 | lower | 0.63 | 5,058 |
| Low-day volume vs peak volume | 0.60 | lower | 0.51 | 5,058 |
| Margin debt, 3-month change | 0.60 | higher | 0.68 | 5,058 |
| Close position on the low day | 0.58 | lower | 0.54 | 5,058 |
| RSI on the low day | 0.58 | higher | 0.50 | 5,058 |
| Follow-through day | 0.57 | higher | 0.50 | 5,058 |
| Volume on the low day | 0.57 | lower | 0.56 | 5,058 |
| Bollinger: new low that held inside the band (W bottom) | 0.57 | higher | 0.52 | 5,058 |
| Failed rebounds so far | 0.57 | lower | 0.69 | 5,058 |
| RSI divergence at the low | 0.56 | higher | 0.52 | 5,058 |
| Rebound given back | 0.56 | higher | 0.50 | 5,058 |
| VIX on the low day | 0.56 | higher | 0.56 | 4,193 |
| Sessions from the high to the low | 0.56 | lower | 0.69 | 5,058 |
| Peak volume into the low | 0.56 | lower | 0.51 | 5,058 |
| Depth of the low | 0.56 | higher | 0.68 | 5,058 |
| VIX vs the previous leg's low | 0.55 | lower | 0.53 | 4,249 |
| Bollinger: back inside after a close under the lower band | 0.54 | higher | 0.52 | 5,058 |
| Shiller P/E vs its 10-year average | 0.54 | lower | 0.54 | 5,058 |
| VIX divergence at the low | 0.53 | lower | 0.57 | 4,193 |
| Peak volume of the selloff | 0.53 | higher | 0.53 | 5,058 |
| M2 growth, 6 months annualized | 0.53 | lower | 0.59 | 5,058 |
| Speed of the decline | 0.53 | higher | 0.63 | 5,058 |
| Sessions since the high | 0.53 | lower | 0.69 | 5,058 |
| Sessions since peak volume | 0.52 | higher | 0.63 | 5,058 |
| Margin debt below its 3-year high | 0.52 | higher | 0.66 | 5,058 |
| S&P 500 / M2 vs its 5-year average | 0.52 | higher | 0.58 | 3,650 |
| Margin debt, 12-month change | 0.52 | higher | 0.60 | 5,058 |
| Average stock vs the index, 20 days | 0.51 | higher | 0.51 | 3,285 |

A day that makes a new closing low was the final low on 13% of such days, or 25% when every selloff counts equally (long bear markets have many new-low days). Volume on the low day, a close off the low, follow-through days and the equal-weight index all score near 0.50: they did not separate final lows from the rest.

## Combining them (tested on selloffs the model had not seen)

| Model | Score | Better than always quoting the average |
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

Adding a fourth variable did not improve the out-of-sample result, so the model stops at three.

## The model

Chance the low is in = a logistic blend of three readings, then adjusted so that the stated chance matches how often it was right out of sample.

| Reading | Average in past selloffs | Weight (per standard deviation) |
|---|---|---|
| VIX below its peak of the selloff | -0.353 | -0.83 |
| Close vs the 200-day average | -0.038 | +0.92 |
| RSI(14) | 49.859 | +0.52 |

Out of sample: score 0.835; 30.5% better than always quoting the average.

| Stated chance | Days | Low really was in (each selloff counted equally) | Low really was in (each day counted equally) |
|---|---|---|---|
| 0% to 25% | 482 | 18% | 14% |
| 25% to 50% | 766 | 39% | 30% |
| 50% to 70% | 458 | 58% | 50% |
| 70% to 85% | 884 | 78% | 68% |
| 85% to 100% | 1,659 | 92% | 89% |

Counting each day equally gives the long bear markets (2000-02, 2008, 2022) more weight, and there the readings ran too high: that column is the one to trust if this selloff turns into one. The adjustment was fitted on these same out-of-sample predictions, so both columns are slightly flattering.

## Rebound checkpoints

How often the low was already in on days when each checkpoint was met, and when it was not (every selloff counted equally). These are shown in the report; the chance above is the estimate.

| Checkpoint | Low in when met | Low in when not met | Share of days met |
|---|---|---|---|
| VIX 20% under its peak close | 78% | 42% | 79% |
| VIX 40% under its peak close | 92% | 57% | 41% |
| Close above the 20-day average | 82% | 47% | 50% |
| Close above the 50-day average | 86% | 50% | 43% |
| RSI(14) at 50 or more | 85% | 47% | 48% |
| Half of the drop retraced | 96% | 54% | 18% |
| Close above the 200-day average | 89% | 47% | 32% |
| 10 sessions without a new closing low | 74% | 49% | 71% |

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

## Bollinger bands, Shiller P/E, M2 and margin debt

Ryan asked on 2026-11-20 whether these had been tested. They had not; this section is the test. "Added to the model" is the out-of-sample result with the variable as a fourth input (the three-variable model scores 30.5%). The last column asks a different question of the slow series: does the reading at the high say how deep the selloff goes (rank correlation with depth, QQQ / SPY; +1 would mean a higher reading always came with a deeper selloff, and anything inside about 0.4 either way is indistinguishable from none on this sample).

| Group | Variable | Score alone | Added to the model | Reading at the high vs depth |
|---|---|---|---|---|
| Bollinger bands | Bollinger: position inside the bands | 0.73 | +0.1 points | n/a |
| Bollinger bands | Bollinger: band width | 0.66 | -0.7 points | n/a |
| Bollinger bands | Bollinger: bands narrower than their widest | 0.61 | -1.2 points | n/a |
| Bollinger bands | Bollinger: sessions since a close under the lower band | 0.70 | -3.6 points | n/a |
| Bollinger bands | Bollinger: back inside after a close under the lower band | 0.54 | +0.0 points | n/a |
| Bollinger bands | Bollinger: new low that held inside the band (W bottom) | 0.57 | -2.8 points | n/a |
| Bollinger bands | Bollinger: position on the low day | 0.61 | -3.5 points | n/a |
| Bollinger bands | Bollinger: highest position since the low | 0.64 | -0.5 points | n/a |
| Shiller P/E | Shiller P/E | 0.62 | -1.8 points | -0.07 (n=28) / +0.16 (n=21) |
| Shiller P/E | Shiller P/E at the high | 0.67 | -2.4 points | n/a |
| Shiller P/E | Shiller P/E vs its 10-year average | 0.54 | -3.1 points | n/a |
| M2 money supply | M2 growth, 12 months | 0.60 | -0.8 points | +0.11 (n=28) / +0.05 (n=21) |
| M2 money supply | M2 growth, 6 months annualized | 0.53 | -0.3 points | n/a |
| M2 money supply | S&P 500 / M2 vs its 5-year average | 0.52 | -1.6 points | +0.01 (n=27) / +0.04 (n=20) |
| Margin debt | Margin debt, 12-month change | 0.52 | -0.8 points | +0.29 (n=28) / +0.08 (n=21) |
| Margin debt | Margin debt, 3-month change | 0.60 | -1.4 points | n/a |
| Margin debt | Margin debt below its 3-year high | 0.52 | -2.1 points | -0.03 (n=28) / -0.05 (n=21) |
| Margin debt | Margin debt / S&P 500 vs its 5-year average | 0.68 | -5.8 points | +0.22 (n=27) / -0.07 (n=20) |

- **Bollinger bands:** the best version added 0.1 points out of sample, inside the noise. Not added to the model.
- **Shiller P/E:** every version left the out-of-sample result the same or worse. Not added to the model.
- **M2 money supply:** every version left the out-of-sample result the same or worse. Not added to the model.
- **Margin debt:** every version left the out-of-sample result the same or worse. Not added to the model.

Shiller P/E, M2 and margin debt are monthly and published weeks late, so within one selloff they barely move: they can describe the backdrop but cannot mark a day. Bollinger position is the 20-day average and RSI restated.

**The backdrop at this selloff's high (2026-10-06)** against the highs of the 28 finished QQQ selloffs. A high rank says the backdrop was stretched; the correlations above say that has not reliably meant a deeper selloff.

| Reading | At this high | Rank among past highs | Median of past highs |
|---|---|---|---|
| Shiller P/E | 41.4 | 27 of 28 (1 = lowest) | 31.3 |
| M2 growth, 12 months | +5.6% | 16 of 28 (1 = lowest) | +5.5% |
| S&P 500 / M2 vs its 5-year average | +39.5% | 25 of 27 (1 = lowest) | +13.3% |
| Margin debt, 12-month change | +37.2% | 24 of 28 (1 = lowest) | +25.7% |
| Margin debt below its 3-year high | -3.2% | 15 of 28 (1 = lowest) | -3.3% |
| Margin debt / S&P 500 vs its 5-year average | +10.8% | 25 of 27 (1 = lowest) | -9.3% |

## The selloff open now, day by day

What the model would have said at each close (not yet scored: the selloff is still open).

**QQQ**, high close $759.66 on 2026-10-06:

| Date | Close | From the high | VIX vs its peak | Chance the low is in |
|---|---|---|---|---|
| 2026-11-02 | $681.09 | -10.3% | 0% | 32% |
| 2026-11-03 | $685.28 | -9.8% | -2% | 36% |
| 2026-11-04 | $691.95 | -8.9% | -21% | 64% |
| 2026-11-05 | $647.05 | -14.8% | 0% | 19% |
| 2026-11-06 | $656.10 | -13.6% | -9% | 32% |
| 2026-11-09 | $679.35 | -10.6% | -29% | 72% |
| 2026-11-10 | $674.76 | -11.2% | -31% | 71% |
| 2026-11-11 | $690.38 | -9.1% | -38% | 83% |
| 2026-11-12 | $688.17 | -9.4% | -34% | 80% |
| 2026-11-13 | $679.89 | -10.5% | -32% | 75% |
| 2026-11-16 | $661.75 | -12.9% | -19% | 44% |
| 2026-11-17 | $656.95 | -13.5% | -10% | 36% |
| 2026-11-18 | $659.51 | -13.2% | -13% | 38% |
| 2026-11-19 | $645.04 | -15.1% | 0% | 22% |

**SPY**, high close $779.09 on 2026-10-06:

| Date | Close | From the high | VIX vs its peak | Chance the low is in |
|---|---|---|---|---|
| 2026-11-19 | $715.87 | -8.1% | 0% | 26% |

## Limits

- 49 selloffs, and QQQ and SPY mostly fall together, so the independent sample is nearer 25.
- Only three of them were long bear markets. The model cannot tell a bear-market rally from a final low early on.
- Everything is on closing prices. An intraday reading uses the live price as if it were the close.
- VIX readings before 2002-05 were not available, so the 2000-01 part of the dot-com bust is not in the VIX model.
