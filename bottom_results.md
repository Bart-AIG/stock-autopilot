# Bottom watch: which variables say the low is in

Data through 2026-11-19. Re-run with `python3 bottom_backtest.py`.

- **Sample:** 5,296 days inside 54 finished QQQ and SPY selloffs, 1999 to 2026, on closing prices. A selloff starts when the close is 10% (QQQ) or 8% (SPY) under its 1-year closing high and ends when the close is back within 3% of it.
- **Question on each day:** has the lowest close of this selloff already printed?
- **Score:** 0.50 means the variable is useless and 1.00 means it separates the two perfectly (area under the ROC curve). "On the low day" is the same score using only days that made a new closing low, which is the hardest moment to call.

## Each variable on its own

The two middle columns split the selloffs by when they peaked. 1999-2009 holds the two long bear markets; a variable that only works after 2010 is a fair-weather one.

| Variable | Score | Low more likely in when it is | 1999-2009 | 2010-2026 | On the low day | Days |
|---|---|---|---|---|---|---|
| Close vs the 200-day average | 0.78 | higher | 0.75 | 0.79 | 0.68 | 5,296 |
| Share of the drop retraced | 0.78 | higher | 0.67 | 0.86 | 0.50 | 5,296 |
| Close vs the 50-day average | 0.77 | higher | 0.78 | 0.80 | 0.67 | 5,296 |
| RSI(14) | 0.77 | higher | 0.76 | 0.79 | 0.50 | 5,296 |
| Rebound off the low, in daily ranges | 0.76 | higher | 0.76 | 0.84 | 0.50 | 5,296 |
| VIX below its peak of the selloff | 0.75 | lower | 0.69 | 0.83 | 0.51 | 5,296 |
| Bollinger: position inside the bands | 0.73 | higher | 0.72 | 0.75 | 0.52 | 5,296 |
| Close vs the 20-day average | 0.72 | higher | 0.71 | 0.75 | 0.61 | 5,296 |
| Above the 200-day | 0.71 | higher | 0.69 | 0.71 | 0.60 | 5,296 |
| Above the 50-day | 0.71 | higher | 0.71 | 0.72 | 0.51 | 5,296 |
| Bollinger: sessions since a close under the lower band | 0.69 | higher | 0.75 | 0.69 | 0.53 | 5,248 |
| Junk bonds vs Treasuries, 20 days | 0.68 | higher | 0.71 | 0.67 | 0.54 | 3,309 |
| Drawdown from the high | 0.68 | higher | 0.51 | 0.73 | 0.69 | 5,296 |
| Above the 20-day | 0.68 | higher | 0.66 | 0.70 | 0.50 | 5,296 |
| Rebound off the low, % | 0.68 | higher | 0.69 | 0.81 | 0.50 | 5,296 |
| Shiller P/E at the high | 0.67 | lower | 0.61 | 0.67 | 0.60 | 5,296 |
| Bollinger: band width | 0.67 | lower | 0.65 | 0.70 | 0.61 | 5,296 |
| Up-day vs down-day volume, 10 days | 0.66 | higher | 0.66 | 0.71 | 0.58 | 5,296 |
| VIX vs its 20-day average | 0.66 | lower | 0.63 | 0.69 | 0.50 | 5,296 |
| VIX vs the previous leg's low | 0.66 | lower | 0.72 | 0.60 | 0.50 | 5,296 |
| Margin debt / S&P 500 vs its 5-year average | 0.65 | lower | 0.75 | 0.57 | 0.56 | 4,341 |
| Sessions since the low | 0.65 | higher | 0.66 | 0.77 | 0.50 | 5,296 |
| RSI(2) | 0.64 | higher | 0.62 | 0.67 | 0.52 | 5,296 |
| Above the 10-day | 0.64 | higher | 0.62 | 0.67 | 0.50 | 5,296 |
| Bollinger: highest position since the low | 0.64 | higher | 0.68 | 0.72 | 0.52 | 5,296 |
| Direction of the 200-day | 0.63 | higher | 0.56 | 0.56 | 0.68 | 5,296 |
| Junk bonds vs Treasuries, 5 days | 0.63 | higher | 0.64 | 0.63 | 0.52 | 3,309 |
| VIX level | 0.62 | lower | 0.51 | 0.72 | 0.55 | 5,296 |
| Shiller P/E | 0.61 | lower | 0.68 | 0.55 | 0.53 | 5,296 |
| Bollinger: position on the low day | 0.61 | higher | 0.71 | 0.46 | 0.52 | 5,296 |
| VIX peak of the selloff | 0.61 | higher | 0.64 | 0.59 | 0.54 | 5,296 |
| Above the 5-day | 0.60 | higher | 0.59 | 0.62 | 0.50 | 5,296 |
| Margin debt, 3-month change | 0.60 | higher | 0.65 | 0.56 | 0.68 | 5,296 |
| Best rebound so far | 0.60 | higher | 0.61 | 0.75 | 0.50 | 5,296 |
| Bollinger: bands narrower than their widest | 0.60 | lower | 0.62 | 0.73 | 0.63 | 5,296 |
| M2 growth, 12 months | 0.60 | lower | 0.53 | 0.59 | 0.62 | 5,296 |
| Low-day volume vs peak volume | 0.59 | lower | 0.60 | 0.57 | 0.52 | 5,296 |
| RSI on the low day | 0.58 | higher | 0.68 | 0.44 | 0.50 | 5,296 |
| VIX divergence at the low | 0.58 | lower | 0.56 | 0.55 | 0.51 | 5,296 |
| Bollinger: new low that held inside the band (W bottom) | 0.57 | higher | 0.69 | 0.41 | 0.52 | 5,296 |
| Depth of the low | 0.57 | higher | 0.45 | 0.47 | 0.69 | 5,296 |
| Sessions since the VIX peak | 0.57 | higher | 0.63 | 0.61 | 0.60 | 5,296 |
| Rebound given back | 0.57 | higher | 0.57 | 0.49 | 0.50 | 5,296 |
| RSI divergence at the low | 0.56 | higher | 0.62 | 0.48 | 0.51 | 5,296 |
| Follow-through day | 0.56 | higher | 0.55 | 0.63 | 0.50 | 5,296 |
| Close position on the low day | 0.56 | lower | 0.52 | 0.58 | 0.54 | 5,296 |
| Failed rebounds so far | 0.56 | lower | 0.46 | 0.50 | 0.69 | 5,296 |
| Sessions from the high to the low | 0.56 | lower | 0.39 | 0.53 | 0.68 | 5,296 |
| Volume on the low day | 0.55 | lower | 0.54 | 0.57 | 0.53 | 5,296 |
| Peak volume into the low | 0.55 | lower | 0.62 | 0.50 | 0.52 | 5,296 |
| Peak volume of the selloff | 0.54 | higher | 0.52 | 0.54 | 0.54 | 5,296 |
| Shiller P/E vs its 10-year average | 0.54 | lower | 0.67 | 0.46 | 0.56 | 5,296 |
| Bollinger: back inside after a close under the lower band | 0.54 | higher | 0.54 | 0.55 | 0.52 | 5,296 |
| M2 growth, 6 months annualized | 0.53 | lower | 0.47 | 0.48 | 0.58 | 5,296 |
| VIX on the low day | 0.53 | higher | 0.57 | 0.53 | 0.55 | 5,296 |
| Sessions since the high | 0.53 | lower | 0.37 | 0.43 | 0.68 | 5,296 |
| Average stock vs the index, 20 days | 0.52 | higher | 0.66 | 0.43 | 0.50 | 3,713 |
| Speed of the decline | 0.52 | higher | 0.40 | 0.54 | 0.62 | 5,296 |
| Sessions since peak volume | 0.52 | higher | 0.61 | 0.59 | 0.64 | 5,296 |
| Margin debt below its 3-year high | 0.52 | higher | 0.38 | 0.46 | 0.67 | 5,296 |
| Margin debt, 12-month change | 0.51 | higher | 0.48 | 0.46 | 0.61 | 5,296 |
| S&P 500 / M2 vs its 5-year average | 0.51 | higher | 0.30 | 0.57 | 0.59 | 4,341 |

A day that makes a new closing low was the final low on 13% of such days, or 27% when every selloff counts equally (long bear markets have many new-low days). Volume on the low day, a close off the low, follow-through days and the equal-weight index all score near 0.50: they did not separate final lows from the rest.

## Combining them (tested on selloffs the model had not seen)

"Skill" is how much better the forecast is than always quoting the average (0% = no better). "Against the chosen model" compares on the same days, which matters where a variable has a shorter history.

| Model | Days | Score | Skill | Against the chosen model | Skill 1999-2009 | Skill 2010-2026 |
|---|---|---|---|---|---|---|
| Close vs the 200-day only | 5,296 | 0.770 | 20.4% | -10.0 points | 17.4% | 15.3% |
| + share of the drop retraced  [chosen] | 5,296 | 0.786 | 30.4% | +0.0 points | 19.2% | 33.5% |
| + RSI(14) | 5,296 | 0.788 | 30.1% | -0.3 points | 19.8% | 32.4% |
| + VIX below its peak | 5,296 | 0.792 | 29.8% | -0.6 points | 17.3% | 34.0% |
| + rebound in daily ranges | 5,296 | 0.795 | 30.6% | +0.2 points | 19.8% | 33.3% |
| + close vs the 50-day | 5,296 | 0.786 | 29.8% | -0.6 points | 19.4% | 32.1% |
| + failed rebounds so far | 5,296 | 0.801 | 29.3% | -1.1 points | 17.0% | 33.2% |
| + direction of the 200-day | 5,296 | 0.795 | 30.3% | -0.1 points | 20.0% | 32.6% |
| + junk bonds vs Treasuries (2007 on) | 3,309 | 0.798 | 28.9% | -1.0 points | -0.9% | 31.9% |
| 11 variables | 5,296 | 0.739 | 20.8% | -9.6 points | -0.8% | 32.1% |
| VIX below its peak, 200-day, RSI(14) (the first fit) | 5,296 | 0.786 | 26.1% | -4.3 points | 16.5% | 27.3% |
| VIX below its peak only | 5,296 | 0.690 | 6.5% | -23.9 points | -13.0% | 14.6% |

No third variable added more than one point, so the model stops at two: the simplest version within a point of the best.
It is weaker in bear markets: skill 19% on the 1999-2009 selloffs against 33% since 2010.
The first fit (2026-11-20, before the data was corrected) put the VIX first. On complete and correct VIX history the VIX alone has skill 7% and was worse than the average in 1999-2009 (-13%): in a long bear market the VIX sits far under its peak while prices keep falling.

## The model

Chance the low is in = a logistic blend of two readings, then adjusted so that the stated chance matches how often it was right out of sample.

| Reading | Average in past selloffs | Weight (per standard deviation) |
|---|---|---|
| Close vs the 200-day average | -0.049 | +0.67 |
| Share of the drop retraced | 0.284 | +1.19 |

Out of sample: score 0.786; 30.4% better than always quoting the average.

| Stated chance | Days | Low really was in (each selloff counted equally) | Low really was in (each day counted equally) |
|---|---|---|---|
| 0% to 25% | 862 | 20% | 17% |
| 25% to 50% | 1,431 | 39% | 34% |
| 50% to 70% | 693 | 55% | 44% |
| 70% to 85% | 903 | 79% | 65% |
| 85% to 100% | 1,407 | 92% | 84% |

Counting each day equally gives the long bear markets (2000-02, 2008, 2022) more weight, and there the readings ran too high: that column is the one to trust if this selloff turns into one. The adjustment was fitted on these same out-of-sample predictions, so both columns are slightly flattering.

## Rebound checkpoints

How often the low was already in on days when each checkpoint was met, and when it was not (every selloff counted equally). These are shown in the report; the chance above is the estimate.

| Checkpoint | Low in when met | Low in when not met | Share of days met |
|---|---|---|---|
| VIX 20% under its peak close | 72% | 46% | 80% |
| VIX 40% under its peak close | 84% | 55% | 41% |
| Close above the 20-day average | 82% | 48% | 50% |
| Close above the 50-day average | 86% | 51% | 43% |
| RSI(14) at 50 or more | 85% | 48% | 48% |
| Half of the drop retraced | 96% | 54% | 18% |
| Close above the 200-day average | 87% | 48% | 34% |
| 10 sessions without a new closing low | 74% | 51% | 70% |

## How fast it calls a low, and how often it is fooled

- **Speed:** across 54 selloffs the reading reached 50% a median of 3 sessions after the final low (price 3.5% off the low by then) and 70% after 4 sessions (4.7% off the low).
- **False alarms:** before the final low the reading crossed 50% 123 times and 70% 81 times. 78 and 54 of those were inside the selloffs that fell more than 25% (2000-02, 2008, 2020, 2022): bear-market rallies look like bottoms to this model.

| Index | High | Final low | Depth | Sessions to 50% | Off the low then | False 50% crossings | Sessions to 70% | Off the low then | False 70% crossings |
|---|---|---|---|---|---|---|---|---|---|
| SPY | 1999-07-16 | 1999-08-10 | -9.3% | 3 | 3.5% | 0 | 3 | 3.5% | 0 |
| SPY | 1999-07-16 | 1999-10-15 | -11.9% | 3 | 2.7% | 1 | 5 | 4.2% | 1 |
| SPY | 2000-01-19 | 2000-02-25 | -9.3% | 1 | 2.1% | 0 | 2 | 3.1% | 0 |
| QQQ | 2000-03-09 | 2000-03-15 | -10.5% | 1 | 5.4% | 0 | 1 | 5.4% | 0 |
| QQQ | 2000-03-24 | 2002-10-09 | -83.0% | 141 | 41.0% | 10 | n/a | n/a | 8 |
| SPY | 2000-03-24 | 2000-04-14 | -11.4% | 1 | 3.5% | 0 | 1 | 3.5% | 0 |
| SPY | 2000-03-24 | 2002-10-09 | -49.1% | 31 | 20.5% | 26 | 150 | 21.8% | 23 |
| QQQ | 2004-01-26 | 2004-03-23 | -11.8% | 2 | 3.8% | 0 | 2 | 3.8% | 0 |
| QQQ | 2004-01-26 | 2004-05-10 | -11.8% | 34 | 3.4% | 0 | 44 | 5.7% | 0 |
| QQQ | 2004-01-26 | 2004-08-12 | -15.9% | 6 | 4.7% | 2 | 11 | 6.4% | 0 |
| SPY | 2004-03-05 | 2004-08-06 | -8.2% | 7 | 1.9% | 0 | 8 | 3.0% | 0 |
| QQQ | 2004-12-14 | 2005-04-20 | -14.3% | 12 | 3.3% | 1 | 18 | 5.1% | 0 |
| QQQ | 2006-01-11 | 2006-07-21 | -17.4% | 17 | 5.6% | 5 | 18 | 8.1% | 0 |
| SPY | 2007-07-19 | 2007-08-15 | -9.0% | 2 | 2.6% | 0 | 4 | 2.8% | 0 |
| SPY | 2007-10-09 | 2007-11-26 | -9.9% | 2 | 4.4% | 1 | 2 | 4.4% | 1 |
| SPY | 2007-10-09 | 2009-03-09 | -56.5% | 39 | 33.4% | 9 | 57 | 35.9% | 1 |
| QQQ | 2007-10-31 | 2008-11-20 | -53.6% | 95 | 28.9% | 8 | 108 | 32.8% | 7 |
| QQQ | 2010-04-23 | 2010-07-02 | -15.9% | 2 | 3.5% | 3 | 6 | 6.7% | 4 |
| SPY | 2010-04-23 | 2010-07-02 | -16.1% | 3 | 4.9% | 4 | 6 | 7.3% | 2 |
| SPY | 2011-04-29 | 2011-10-03 | -19.4% | 5 | 8.8% | 4 | 5 | 8.8% | 2 |
| QQQ | 2011-07-26 | 2011-08-19 | -16.1% | 3 | 5.3% | 2 | 6 | 9.2% | 1 |
| QQQ | 2011-07-26 | 2011-11-23 | -16.1% | 67 | 6.5% | 0 | 69 | 9.4% | 0 |
| QQQ | 2012-04-02 | 2012-06-01 | -11.5% | 3 | 3.5% | 1 | 3 | 3.5% | 3 |
| SPY | 2012-04-02 | 2012-06-04 | -9.7% | 2 | 3.0% | 1 | 2 | 3.0% | 1 |
| QQQ | 2012-09-19 | 2012-11-15 | -11.9% | 2 | 2.8% | 0 | 5 | 4.6% | 0 |
| SPY | 2015-05-21 | 2015-08-25 | -12.3% | 1 | 3.8% | 0 | 2 | 6.4% | 0 |
| SPY | 2015-05-21 | 2016-02-11 | -14.4% | 3 | 5.5% | 3 | 6 | 6.5% | 0 |
| QQQ | 2015-07-20 | 2015-08-25 | -13.9% | 1 | 5.0% | 0 | 2 | 7.7% | 0 |
| QQQ | 2015-12-01 | 2016-02-09 | -16.4% | 5 | 6.4% | 1 | 8 | 7.2% | 0 |
| QQQ | 2018-01-26 | 2018-02-08 | -10.2% | 1 | 1.7% | 0 | 2 | 3.5% | 0 |
| SPY | 2018-01-26 | 2018-02-08 | -10.1% | 1 | 1.5% | 0 | 2 | 3.0% | 0 |
| SPY | 2018-01-26 | 2018-04-02 | -10.2% | 2 | 2.4% | 2 | 3 | 3.2% | 0 |
| QQQ | 2018-03-12 | 2018-04-02 | -10.7% | 2 | 2.7% | 0 | 3 | 3.3% | 0 |
| QQQ | 2018-08-29 | 2018-12-24 | -23.2% | 7 | 8.9% | 5 | 9 | 11.2% | 3 |
| SPY | 2018-09-20 | 2018-12-24 | -20.2% | 4 | 6.6% | 2 | 9 | 9.6% | 4 |
| QQQ | 2019-05-03 | 2019-06-03 | -11.0% | 1 | 2.8% | 0 | 2 | 3.6% | 0 |
| QQQ | 2020-02-19 | 2020-03-16 | -28.6% | 8 | 13.3% | 3 | 15 | 16.1% | 2 |
| SPY | 2020-02-19 | 2020-03-23 | -34.1% | 10 | 18.8% | 2 | 12 | 22.9% | 2 |
| QQQ | 2020-09-02 | 2020-09-23 | -12.7% | 0 | 0.0% | 1 | 2 | 2.8% | 3 |
| QQQ | 2020-09-02 | 2020-10-28 | -12.7% | 25 | 2.8% | 0 | 25 | 2.8% | 0 |
| SPY | 2020-09-02 | 2020-09-23 | -9.8% | 2 | 1.9% | 1 | 3 | 3.6% | 0 |
| SPY | 2020-09-02 | 2020-10-28 | -9.8% | 25 | 1.2% | 0 | 26 | 2.3% | 0 |
| QQQ | 2021-02-12 | 2021-03-08 | -10.9% | 1 | 3.9% | 0 | 1 | 3.9% | 0 |
| QQQ | 2021-11-19 | 2022-12-28 | -35.6% | 16 | 11.1% | 9 | 23 | 15.7% | 6 |
| SPY | 2022-01-03 | 2022-10-12 | -25.4% | 9 | 8.0% | 11 | 21 | 10.7% | 5 |
| QQQ | 2023-07-18 | 2023-10-26 | -10.9% | 2 | 1.6% | 0 | 4 | 3.9% | 0 |
| SPY | 2023-07-31 | 2023-10-27 | -10.3% | 3 | 2.9% | 0 | 4 | 4.9% | 0 |
| QQQ | 2024-07-10 | 2024-08-07 | -13.6% | 1 | 3.1% | 0 | 3 | 3.8% | 0 |
| SPY | 2024-07-16 | 2024-08-05 | -8.4% | 3 | 2.6% | 0 | 3 | 2.6% | 0 |
| QQQ | 2025-02-19 | 2025-04-08 | -22.9% | 1 | 12.0% | 2 | 1 | 12.0% | 1 |
| SPY | 2025-02-19 | 2025-04-08 | -19.0% | 1 | 10.5% | 3 | 1 | 10.5% | 1 |
| QQQ | 2025-10-29 | 2026-03-30 | -12.2% | 1 | 3.4% | 0 | 2 | 4.7% | 0 |
| SPY | 2026-01-27 | 2026-03-30 | -9.1% | 1 | 2.9% | 0 | 2 | 3.7% | 0 |
| QQQ | 2026-06-02 | 2026-07-29 | -11.3% | 1 | 3.3% | 0 | 1 | 3.3% | 0 |

## Bollinger bands, Shiller P/E, M2 and margin debt

Ryan asked on 2026-11-20 whether these had been tested. They had not; this section is the test. "Added to the model" is the out-of-sample result with the variable as a fourth input (the chosen model scores 30.4%; each comparison is on the same days). The last column asks a different question of the slow series: does the reading at the high say how deep the selloff goes (rank correlation with depth, QQQ / SPY; +1 would mean a higher reading always came with a deeper selloff, and anything inside about 0.4 either way is indistinguishable from none on this sample).

| Group | Variable | Score alone | Added to the model | Reading at the high vs depth |
|---|---|---|---|---|
| Bollinger bands | Bollinger: position inside the bands | 0.73 | -0.4 points | n/a |
| Bollinger bands | Bollinger: band width | 0.67 | -0.7 points | n/a |
| Bollinger bands | Bollinger: bands narrower than their widest | 0.60 | -0.4 points | n/a |
| Bollinger bands | Bollinger: sessions since a close under the lower band | 0.69 | -1.1 points | n/a |
| Bollinger bands | Bollinger: back inside after a close under the lower band | 0.54 | -0.2 points | n/a |
| Bollinger bands | Bollinger: new low that held inside the band (W bottom) | 0.57 | -1.8 points | n/a |
| Bollinger bands | Bollinger: position on the low day | 0.61 | -1.5 points | n/a |
| Bollinger bands | Bollinger: highest position since the low | 0.64 | -0.3 points | n/a |
| Shiller P/E | Shiller P/E | 0.61 | -0.4 points | -0.14 (n=29) / -0.00 (n=25) |
| Shiller P/E | Shiller P/E at the high | 0.67 | +0.3 points | n/a |
| Shiller P/E | Shiller P/E vs its 10-year average | 0.54 | -1.8 points | n/a |
| M2 money supply | M2 growth, 12 months | 0.60 | -0.9 points | +0.07 (n=29) / +0.01 (n=25) |
| M2 money supply | M2 growth, 6 months annualized | 0.53 | -1.0 points | n/a |
| M2 money supply | S&P 500 / M2 vs its 5-year average | 0.51 | +1.8 points | +0.01 (n=27) / +0.06 (n=20) |
| Margin debt | Margin debt, 12-month change | 0.51 | -1.2 points | +0.17 (n=29) / +0.02 (n=25) |
| Margin debt | Margin debt, 3-month change | 0.60 | -0.1 points | n/a |
| Margin debt | Margin debt below its 3-year high | 0.52 | -1.2 points | -0.10 (n=29) / -0.11 (n=25) |
| Margin debt | Margin debt / S&P 500 vs its 5-year average | 0.65 | -5.4 points | +0.21 (n=27) / -0.07 (n=20) |

- **Bollinger bands:** every version left the out-of-sample result the same or worse. Not added to the model.
- **Shiller P/E:** the best version (Shiller P/E at the high) added 0.3 points out of sample, inside the noise. Not added to the model.
- **M2 money supply:** the best version (S&P 500 / M2 vs its 5-year average) added 1.8 points out of sample, but +0.0 points with the 2007-09 bear market left out and -0.6 points on the selloffs since 2010. A gain that rests on one bear market is not evidence. Not added to the model.
- **Margin debt:** every version left the out-of-sample result the same or worse. Not added to the model.

Shiller P/E, M2 and margin debt are monthly and published weeks late, so within one selloff they barely move: they can describe the backdrop but cannot mark a day. Bollinger position is the 20-day average and RSI restated.

**The backdrop at this selloff's high (2026-10-06)** against the highs of the 29 finished QQQ selloffs. A high rank says the backdrop was stretched; the correlations above say that has not reliably meant a deeper selloff.

| Reading | At this high | Rank among past highs | Median of past highs |
|---|---|---|---|
| Shiller P/E | 41.4 | 27 of 29 (1 = lowest) | 31.3 |
| M2 growth, 12 months | +5.6% | 16 of 29 (1 = lowest) | +5.5% |
| S&P 500 / M2 vs its 5-year average | +39.5% | 25 of 27 (1 = lowest) | +13.3% |
| Margin debt, 12-month change | +37.2% | 24 of 29 (1 = lowest) | +25.7% |
| Margin debt below its 3-year high | -3.2% | 15 of 29 (1 = lowest) | -3.3% |
| Margin debt / S&P 500 vs its 5-year average | +10.8% | 25 of 27 (1 = lowest) | -9.2% |

## The selloff open now, day by day

What the model would have said at each close (not yet scored: the selloff is still open).

**QQQ**, high close $759.66 on 2026-10-06:

| Date | Close | From the high | VIX vs its peak | Chance the low is in |
|---|---|---|---|---|
| 2026-11-02 | $681.09 | -10.3% | 0% | 34% |
| 2026-11-03 | $685.28 | -9.8% | -2% | 42% |
| 2026-11-04 | $691.95 | -8.9% | -21% | 50% |
| 2026-11-05 | $647.05 | -14.8% | 0% | 27% |
| 2026-11-06 | $656.10 | -13.6% | -9% | 39% |
| 2026-11-09 | $679.35 | -10.6% | -29% | 70% |
| 2026-11-10 | $674.76 | -11.2% | -31% | 59% |
| 2026-11-11 | $690.38 | -9.1% | -38% | 81% |
| 2026-11-12 | $688.17 | -9.4% | -34% | 80% |
| 2026-11-13 | $679.89 | -10.5% | -32% | 71% |
| 2026-11-16 | $661.75 | -12.9% | -19% | 45% |
| 2026-11-17 | $656.95 | -13.5% | -10% | 40% |
| 2026-11-18 | $659.51 | -13.2% | -13% | 43% |
| 2026-11-19 | $645.04 | -15.1% | 0% | 27% |

**SPY**, high close $779.09 on 2026-10-06:

| Date | Close | From the high | VIX vs its peak | Chance the low is in |
|---|---|---|---|---|
| 2026-11-19 | $715.87 | -8.1% | 0% | 31% |

## Limits

- 54 selloffs, and QQQ and SPY mostly fall together, so the independent sample is nearer 25.
- Only three of them were long bear markets. The model cannot tell a bear-market rally from a final low early on.
- Everything is on closing prices. An intraday reading uses the live price as if it were the close.
- It is weaker in bear markets (skill 19% on 1999-2009 against 33% since 2010).
- The model was chosen among about a dozen combinations on the same out-of-sample test, so its own score is a little flattering.
