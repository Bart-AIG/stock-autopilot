# Leveraged ETF sell targets (2026-11-12, INTRADAY prices)

Model output describes resampled history. It is not a forecast.

## Recommendation

Place the ladder below as GTC limit sells on the leveraged ETF, re-run weekly, and rotate to the underlying when a checkpoint fails. Ranked by how much the leverage is costing you:

| ETF | Vol drag + fees /yr (long-run vol) | Hurdle: underlying return/yr to beat holding it | P(ETF beats underlying over 1y), worse run | Verdict |
|---|---|---|---|---|
| AAOX | 126% | 349% | 8% | Leverage is a losing bet on the median path; trim early or rotate now |
| COHX | 42% | 131% | 31% | Leverage needs a fast move; sell into strength |
| SOXL | 49% | 56% | 52% | Ladder is reasonable |

## Action items

1. **SOXL**: place 4 GTC limit sells ($81.08, $93.44, $107.09, $121.49), first rung 26 shares. If the underlying is below $173.66 on 2027-02-11, rotate to SOXX.
2. **COHX**: place 4 GTC limit sells ($16.40, $19.92, $23.82, $28.02), first rung 125 shares. If the underlying is below $296.29 on 2027-02-11, rotate to COHR.
3. **AAOX**: place 4 GTC limit sells ($3.56, $5.08, $6.82, $8.65), first rung 575 shares. If the underlying is below $100.12 on 2027-02-11, rotate to AAOI.
4. Re-run `python main.py` each week (and after any 10%+ move); rungs and time stops move with price, vol and drag.
5. Decide on COHX and AAOX before the Feb 2027 earnings prints: a gap through earnings is the main way a 2x fund loses half its value in a day.

## Sell ladder

| ETF | Rung | Underlying level | Underlying target | Sell price | Shares | Proceeds | P(touch) 2y | Time stop |
|---|---|---|---|---|---|---|---|---|
| SOXL | 1 | 25% to ATH | $171.40 | **$81.08** | 26 | $2,108 | 91% | 2027-01-17 |
| SOXL | 2 | 50% to ATH | $187.05 | **$93.44** | 26 | $2,429 | 84% | 2027-04-17 |
| SOXL | 3 | 75% to ATH | $202.69 | **$107.09** | 26 | $2,784 | 78% | 2027-07-04 |
| SOXL | 4 | ATH | $218.34 | **$121.49** | 26 | $3,159 | 72% | 2027-09-15 |
| **SOXL total** | | | | | | **$10,481** | | |
| COHX | 1 | 25% to ATH | $284.14 | **$16.40** | 125 | $2,050 | 82% | 2027-02-06 |
| COHX | 2 | 50% to ATH | $331.73 | **$19.92** | 125 | $2,490 | 71% | 2027-05-19 |
| COHX | 3 | 75% to ATH | $379.31 | **$23.82** | 125 | $2,978 | 61% | 2027-08-05 |
| COHX | 4 | ATH | $426.89 | **$28.02** | 125 | $3,502 | 53% | 2027-10-09 |
| **COHX total** | | | | | | **$11,020** | | |
| AAOX | 1 | 25% to ATH | $96.74 | **$3.56** | 575 | $2,046 | 65% | 2027-05-04 |
| AAOX | 2 | 50% to ATH | $138.86 | **$5.08** | 575 | $2,923 | 51% | 2027-08-18 |
| AAOX | 3 | 75% to ATH | $180.98 | **$6.82** | 575 | $3,923 | 42% | 2027-10-25 |
| AAOX | 4 | ATH | $223.10 | **$8.65** | 575 | $4,977 | 35% | 2027-12-16 |
| **AAOX total** | | | | | | **$13,868** | | |
| **All three** | | | | | | **$35,369** | | |

P(touch) is the worse of the full-history and last-2-year Monte Carlo runs. Time stop is the date the stress-case price falls below the rung if the underlying has not got there yet.

## Calibration

| ETF | Beta | Corr | Drag /yr (SE) | Synthetic TE /yr | Vol 3m / 1y / since 2016 | ETF now | Underlying now | ATH |
|---|---|---|---|---|---|---|---|---|
| SOXL | 2.96 | 0.999 | 12.9% (+/-2.2%) | 7.0% | 52% / 50% / 35% | $66.52 | $155.76 | $218.34 (2026-06-22) |
| COHX | 2.01 | 0.999 | 7.3% (+/-10.5%) | 9.0% | 100% / 91% / 58% | $12.55 | $236.56 | $426.89 (2026-06-02) |
| AAOX | 1.99 | 0.999 | 29.0% (+/-10.8%) | 8.7% | 110% / 146% / 99% | $2.07 | $54.62 | $223.10 (2026-05-13) |

## Level mapping (ceiling vs history vs simulation)

### SOXL

| Level | Underlying | Ceiling | Hist median | Hist P10-P90 | MC P(hit 1y) | MC P(hit 2y) full / 2y | MC median price on hit |
|---|---|---|---|---|---|---|---|
| 10% to ATH (extra) | $162.02 | $74.86 | $75.01 | $64.26-$78.00 | 95% | 98% / 99% | $74.76 |
| 25% to ATH | $171.40 | $88.64 | $86.28 | $59.22-$90.44 | 88% | 95% / 98% | $84.97 |
| 50% to ATH | $187.05 | $115.20 | $104.83 | $68.12-$113.34 | 74% | 89% / 96% | $101.00 |
| 75% to ATH | $202.69 | $146.59 | $122.33 | $72.21-$139.59 | 59% | 82% / 94% | $118.07 |
| ATH | $218.34 | $183.22 | $137.60 | $77.70-$168.94 | 45% | 75% / 91% | $136.53 |
| ATH +10% | $240.17 | $243.86 | $166.26 | $87.65-$215.72 | 29% | 64% / 87% | $162.34 |
| ATH +25% | $272.92 | $357.85 | $205.19 | $111.07-$296.40 | 14% | 48% / 79% | $208.04 |

### COHX

| Level | Underlying | Ceiling | Hist median | Hist P10-P90 | MC P(hit 1y) | MC P(hit 2y) full / 2y | MC median price on hit |
|---|---|---|---|---|---|---|---|
| 10% to ATH (extra) | $255.59 | $14.65 | $14.64 | $9.50-$15.76 | 90% | 94% / 98% | $14.68 |
| 25% to ATH | $284.14 | $18.11 | $16.81 | $6.85-$18.56 | 77% | 87% / 95% | $17.51 |
| 50% to ATH | $331.73 | $24.68 | $18.22 | $7.94-$24.25 | 57% | 74% / 90% | $21.47 |
| 75% to ATH | $379.31 | $32.27 | $19.39 | $9.44-$30.71 | 42% | 62% / 84% | $24.89 |
| ATH | $426.89 | $40.87 | $22.34 | $10.18-$37.06 | 30% | 53% / 79% | $28.33 |
| ATH +10% | $469.58 | $49.45 | $25.60 | $9.59-$42.01 | 22% | 46% / 74% | $31.70 |
| ATH +25% | $533.61 | $63.86 | $29.85 | $8.29-$49.44 | 14% | 36% / 68% | $37.00 |

### AAOX

| Level | Underlying | Ceiling | Hist median | Hist P10-P90 | MC P(hit 1y) | MC P(hit 2y) full / 2y | MC median price on hit |
|---|---|---|---|---|---|---|---|
| 10% to ATH (extra) | $71.47 | $3.54 | $2.78 | $0.02-$3.80 | 74% | 83% / 91% | $3.14 |
| 25% to ATH | $96.74 | $6.49 | $2.10 | $0.00-$6.16 | 53% | 68% / 82% | $3.98 |
| 50% to ATH | $138.86 | $13.38 | $2.13 | $0.00-$10.09 | 32% | 51% / 70% | $5.11 |
| 75% to ATH | $180.98 | $22.73 | $2.47 | $0.00-$13.99 | 21% | 41% / 62% | $6.21 |
| ATH | $223.10 | $34.54 | $3.16 | $0.00-$18.69 | 15% | 33% / 55% | $7.27 |
| ATH +10% | $245.41 | $41.79 | $3.07 | $0.00-$20.79 | 12% | 30% / 52% | $7.83 |
| ATH +25% | $278.88 | $53.96 | $2.67 | $0.00-$19.92 | 10% | 26% / 48% | $8.68 |

## Rotation and downside

| ETF | Hurdle (underlying return/yr needed) | Underlying needed at 3m / 6m / 1y | P(ETF beats underlying, 1y) full / 2y | P(-50% before rung 1) | P(-75%) | Cost basis touch 2y |
|---|---|---|---|---|---|---|
| SOXL | 56% | $173.66 / $193.62 / $240.69 | 52% / 56% | 20% | 9% | 79% |
| COHX | 131% | $296.29 / $371.10 / $582.16 | 36% / 31% | 29% | 16% | 78% |
| AAOX | 349% | $100.12 / $183.51 / $616.58 | 14% / 8% | 56% | 45% | 98% |

Downside columns show the worse of the two runs.

## Fund and event risk

1. SOXL (Direxion): about $19B net assets (Jul 2026), 0.75% net expense ratio. No closure or reverse-split notice found. Index moved from PHLX SOX to the ICE (now NYSE) Semiconductor Index on 2021-08-25.
2. COHX (Tradr, launched 2026-02-18, 1.49% expense ratio): AUM fell from about $94M (Sep 1) to about $58M (Oct 15). No closure notice found, but Tradr has closed about 20 single-stock funds in 2026 (Jan, Mar, May, Oct). LIQUIDATION RISK: moderate and rising.
3. AAOX (Tradr, launched 2026-03-24, 1.49% expense ratio): about $200-280M AUM, larger than COHX. No closure notice found. Same issuer closure pattern applies. A liquidation pays out NAV in cash, which realizes the gain or loss on Tradr's date, not yours.
4. Earnings: COHR reported 2026-11-04 and AAOI 2026-11-05. Next dates are not announced; expect about early Feb 2027 (COHR) and late Feb 2027 (AAOI). Both fall before rung 1's time stop on COHX and AAOX.

## Flags

1. SOXL: prices are intraday (2026-11-12); re-run after the close for settled numbers.
2. COHX: prices are intraday (2026-11-12); re-run after the close for settled numbers.
3. COHX: drag 7.3% has a standard error of 10.5% (short overlap); treat it as rough.
4. AAOX: prices are intraday (2026-11-12); re-run after the close for settled numbers.

## Data log

- AAOI: 3303 bars 2013-09-26 to 2026-11-12, last $54.62 (INTRADAY)
- AAOX: 163 bars 2026-03-24 to 2026-11-12, last $2.07 (INTRADAY)
- COHR split 2:1 on 2011-06-27: adjusted return that day +1.6% (continuous)
- COHR: 4242 bars 2010-01-04 to 2026-11-12, last $236.56 (INTRADAY)
- COHX: 186 bars 2026-02-19 to 2026-11-12, last $12.55 (INTRADAY)
- SOXL split 4:1 on 2015-05-20: adjusted return that day +0.5% (continuous)
- SOXL split 15:1 on 2021-03-02: adjusted return that day -9.4% (continuous)
- SOXL: 4196 bars 2010-03-11 to 2026-11-12, last $66.52 (INTRADAY)
- SOXX split 3:1 on 2024-03-07: adjusted return that day +3.4% (continuous)
- SOXX split 3:1 on 2026-11-05: adjusted return that day -12.1% (continuous)
- SOXX: 4242 bars 2010-01-04 to 2026-11-12, last $155.76 (INTRADAY)
- Running SOXL ...
- Running COHX ...
- Running AAOX ...
