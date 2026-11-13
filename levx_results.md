# LEVX: a sleeve for leveraged funds (run 2026-11-13)

**Request (Ryan, live turn 2026-11-13):** a sleeve trade model for SOXL, AAOX, SPCM, LITX, COHX and funds like them: day trade, swing trade, or whatever tests best, sized for the agentic account ($2,492 total, $1,900 cash).

**Status:** PROPOSED. Nothing here is live. `levx.W_LEVX` is 0.0 and no routine prompt carries the duties yet. Spec: `docs/levx-sleeve.md`.

Every number is a backtest: historical, net of the stated costs, before taxes. None of it is a forecast.

## 1. Verdict

| Question | Answer | Confidence |
|---|---|---|
| Is there a day trade that works on these funds? | **Only one, and only on TQQQ.** Of 11 published day-trade rules, the noise-area breakout (long only) was the only one positive in both halves of 2018-26: 12% to 17% a year on TQQQ with a -12% to -17% drawdown. On SOXL it made nothing in 2018-22 once positions were closed at 15:50. Opening-range breakouts worked in 2018-22 and died in 2023-26 | Moderate |
| Does a swing trade work on them? | **Not better than what the account already runs.** Dip-buying (the house swing rules) is positive on average, but in 2x and 3x funds a 4-position book had -50% to -90% drawdowns and the sign flipped between periods. On SOXL the house rule made 35%/yr in 2011-22 and -1%/yr with a -74% drawdown in 2023-26 | High |
| What is the best way to trade them? | **Own the liquid ones overnight, not during the day.** Above its 200-day average, an index earns almost all of its return between the close and the next open. That held for QQQ, SPY and SOXX in every period back to 2000, and for 14 of 15 leveraged index funds tested | High |
| The model (LEVX) | **TQQQ and SOXL, bought near 15:50 and sold after the next open, only while QQQ / SOXX is above its 200-day average, sized down when nights get volatile. Plus the TQQQ day breakout on the same money.** 2018-26: **54.0%/yr, -35% worst drawdown**; at double the assumed costs 40.7%/yr | Moderate to high |
| AAOX, COHX, LITX, SPCM | **No tested rule works on them after costs.** Their bid/ask spreads were 0.3% to 1.1% per round trip today. The night edge exists in the underlying stocks, but the spread takes most of it | High |
| Effect on the account | Moving 20% of the base from SWING_Q into LEVX took the 2019-26 mix from **29.9%/yr to 34.7%/yr with about the same drawdown (-21% to -22%)**. Pessimistic: 27.7% to 30.3%. Chosen on 2019-22 data only, every best split held 30% to 40% LEVX and beat the live split on unseen 2023-26 | Moderate |

**What to plan on:** the pessimistic rows. LEVX alone is not safe: a bootstrap of its own history gives a 57% chance of a -40% drawdown over 8 years. It is a sleeve, not an account.

## 2. How it was tested

- **Prices:** Yahoo daily bars (split and dividend adjusted) back to 1997; FMP 5-minute bars 2018 to today for 28 symbols; Robinhood quotes for spreads.
- **Fund universe:** every US-listed leveraged long equity fund FMP lists (683), mapped to its underlying and kept only if its own returns confirm the mapping (beta within 20% of the stated leverage). That left **479 funds on 275 underlyings**; 378 of them launched in 2025 or 2026.
- **No-hindsight checks:** the end-2018 S&P 100 + Nasdaq-100 list (158 names, the SWING_M test pool), and the real funds from their launch dates with a $2M/day liquidity floor. A list of "stocks that got a leveraged fund" is a list of past winners, so it is never used alone.
- **Discovery / validation:** rules were studied on data through 2022. 2023 to today scored them.
- **Engine checks:** the engine reproduces `robust_backtest.swing` on QQQ exactly (5,300 days, zero differences) and SWING_M at 26.9%/yr / -21% for 2019-01 to 2026-09 (house: 30.0% / -21% on FMP data). The live rules (`levx.simulate`) match an independent vectorised version to 1e-16 on the night legs and 2e-4 a day on the DAY leg.
- **Live path:** `test_levx.py` walks the routine's clock through the last 64 sessions and checks that `levx.decide` reaches the backtest's positions. Twenty deliberate rule changes (200-day length, volatility target, band, check times, fund shares, the guards and others) each made the tests fail.
- **Costs:** per side, from quotes sampled three times on 2026-11-13 (section 3). LEVX uses 1.5 bp for TQQQ and 2 bp for SOXL, and is re-run at 2x, 3x and 4x.

## 3. Costs decide what is tradeable

Quoted bid/ask spread, 2026-11-13 (three samples, 12:00 to 13:05 ET; a volatile day, SOXL -15%):

| Fund | What it is | $ volume / day | Spread (round trip) | Usable for a daily strategy? |
|---|---|---|---|---|
| TQQQ | 3x Nasdaq-100 | $3.9B | 1.8 bp | Yes |
| QLD | 2x Nasdaq-100 | $360M | 1.3 bp | Yes |
| SOXL | 3x semiconductors | $8.7B | 3.6 to 5.4 bp | Yes |
| NVDL | 2x NVDA | $330M | 5.8 bp | Borderline |
| TSLL | 2x TSLA | $600M | 9.6 bp | Borderline |
| SPCH | 2x SpaceX (Leverage Shares) | $217M | 12.8 bp | No |
| SPCM | 2x SpaceX (Tradr) | $14M | 7 to 15 bp | No |
| LITX | 2x LITE | $81M | 31 to 51 bp | No |
| AAOX | 2x AAOI | $93M | 61 bp (one cent on a $1.63 price) | No |
| COHX | 2x COHR | $26M | 70 to 110 bp | No |

- The night edge is about 15 to 35 bp per night in a 3x index fund. A 2 to 5 bp round trip leaves most of it. A 30 to 110 bp round trip leaves nothing.
- SPCM is not the liquid SpaceX fund: SPCH trades 16 times the dollars. Robinhood also blocks fractional buys of SPCM.

## 4. What did not work

**Daily rules, 21 of them** (trend filters, the house swing union and its legs, breakouts, continuation, washout bounces, overnight, intraday), each on 5 universes. Discovery 2011-22 | validation 2023-26, return a year / worst drawdown:

| Rule | SOXL (real fund) | AAOI + COHR + LITE at 2x | 158 large caps at 2x, no hindsight |
|---|---|---|---|
| Buy and hold | 23% / -90% then 65% / -88% | -12% / -97% then 143% / -93% | 28% / -62% then 30% / -32% |
| Above the 200-day average | 18% / -74% then 45% / -80% | -12% / -94% then 84% / -83% | 15% / -28% then 13% / -17% |
| House swing union | 35% / -61% then **-1% / -74%** | -15% / -90% then 56% / -71% | 8% / -33% then 6% / -27% |
| 20-day breakout | 5% / -70% then 73% / -57% | -3% / -69% then 104% / -75% | 6% / -21% then 10% / -10% |
| Strong-close continuation | -27% then 5% | -17% then 68% | -17% then -9% |

- On the three optical stocks every rule lost money for a decade and then made a fortune in the 2023-26 run. That is the stocks, not the rules.
- In the no-hindsight pool, no timing rule beat simply holding on a risk-adjusted basis.

**Concentrated 4-position books in leveraged funds** (2007-22 | 2023-26; the SWING_Q reference is 20.4% / -50% then 28.0% / -26%):

| Book | 26 leveraged index funds | Synthetic 2x on 158 large caps | Every real leveraged fund, 2022-08 to 2024 then 2025 to now |
|---|---|---|---|
| House swing union | 10% / -73% then 16% / -54% | 39% / -69% then 35% / -50% | -10% / -48% then 22% / -76% |
| Dips, any trend | 18% / -80% then 21% / -57% | 45% / -87% then 37% / -43% | -11% / -54% then -41% / -70% |
| Top-4 momentum, above 200-day | 6% / -87% then 11% / -68% | 39% / -90% then 16% / -85% | 77% / -47% then -37% / -93% |
| 20-day breakout | -4% / -86% then 34% / -42% | -3% / -94% then -4% / -65% | 19% / -33% then -15% / -78% |

- More leverage on the same dip-buying is not more edge. QLD is the sweet spot the account already found.
- One pattern is real: a dip bought when the VIX is above 28 earned 3 to 10 times more per trade than a dip in a calm market (2011-22, 1x: +1.4% to +1.7% against +0.15% to +0.36%). It trades too rarely to be a sleeve (44 trades in four years on real funds).

**Day trades on 5-minute bars, 2 bp per side, positions held to the close** (2018-22 | 2023-26):

| Rule | SOXL | TQQQ |
|---|---|---|
| Opening-range breakout, 5 min | 27% / -39% then **-5% / -46%** | 12% / -31% then 0% / -25% |
| Gap fade | -26% then -32% | -11% then -6% |
| First-half-hour momentum | -4% then 9% | 4% then 4% |
| Last-half-hour momentum | 10% then -19% | 3% then -11% |
| VWAP trend | 21% / -58% then -1% / -73% | 17% / -38% then -5% / -57% |
| **Noise-area breakout, long** | 13% / -33% then 13% / -34% | **14% / -13% then 12% / -13%** |
| Hold the whole session every day | -32% then -31% | -11% then 3% |

- SOXL's noise-breakout profit in 2018-22 came from the last ten minutes of trend days (the last-half-hour effect, which reversed in 2023-26). Closed at 15:50 instead, it made 1% a year in 2018-22, and it lost with a 5-minute fill delay. TQQQ's did not depend on it. So the DAY leg is TQQQ only.
- On AAOI, COHR and LITE at their real costs (25 to 40 bp a side) every same-day rule lost 20% to 97% a year.
- "Hold the whole session" loses on SOXL even before costs matter: the average session returned +2 to +4 bp.

## 5. What did work: the night

Average 1x return per night and per day session, index above its 200-day average, daily data:

| Index | 2000-06 night / day | 2007-17 night / day | 2018-26 night / day |
|---|---|---|---|
| QQQ | +6.2 bp (t 2.4) / -7.6 bp | +5.0 bp (t 4.3) / +0.2 bp | +6.5 bp (t 3.6) / +0.7 bp |
| SPY | +4.0 bp (t 3.4) / -3.2 bp | +2.8 bp (t 2.8) / +1.2 bp | +5.2 bp (t 4.2) / 0.0 bp |
| SOXX | +12.9 bp (t 3.3) / -6.5 bp | +6.4 bp (t 4.1) / -1.0 bp | +12.0 bp (t 3.8) / -1.3 bp |

- The same split shows up in stocks. The monthly top-10 momentum names earned +9.7 to +11.7 bp per night and about zero per day session in 2018-22 and 2023-26.
- It is a known effect, not something this test discovered: Cliff, Cooper & Gulen (2008) for the S&P 500, and Lou, Polk & Skouras (2019, Journal of Financial Economics) for momentum, whose profits they find arrive entirely overnight.
- **The night rule on 15 leveraged index funds** (index above 200-day, close to open, net of each fund's cost): the average night was positive in 14 of 15 (t 2.1 to 4.9 for 2018-26). Net of costs it paid in the liquid ones (TQQQ, SOXL, QLD, SPXL, UPRO, SSO, TNA, USD, LABU) and failed in the thin ones (NAIL, DPST at 8 bp a side) and in China (YINN).
- **Dot-com crash, which the house had never been able to test:** a synthetic 3x QQQ night rule returned -0.4%/yr over 2000-02 with a -54% drawdown, while 3x buy and hold lost 89% a year. Over 2003-06 it made 25.9%/yr.
- Checked and dropped: running the existing swing sleeves at night only. SWING_Q nights-only made 10.9%/yr against 34.3% as run today, because QQQ dips rebound during the session as well.

## 6. The LEVX model

| Leg | Rule | Why |
|---|---|---|
| NIGHT | At about 15:50 ET buy TQQQ if QQQ is above its 200-day average and SOXL if SOXX is above its own (today's price counted in). Half the sleeve each. Sell after the next open | Section 5 |
| Sizing | Each fund's size = its half x min(1, 40% / the annualised volatility of its last 20 overnight returns) | Cuts the worst drawdown from -52% to -35% at the same return per unit of risk |
| DAY | TQQQ only, whole sleeve. At each :00 and :30 bar close from 10:00 to 15:30 ET: hold it if that close is above max(open, prior close) x (1 + its usual move for that time of day over 14 sessions), hold none if not | Section 4. Uncorrelated with the night leg (0.03) and uses money that is idle in the day |
| No stops, targets or news gates | The tested rules have none | House rule |

**Backtest, live rules replayed on real 5-minute bars** (buy at 15:50, sell at 09:35, DAY orders filled 5 minutes late; 1.5 bp a side TQQQ, 2 bp SOXL). Cells are return a year / worst drawdown / Sharpe:

| | 2018-22 | 2023-26 | 2018-26 |
|---|---|---|---|
| **LEVX** | **45.9% / -35% / 1.24** | **65.2% / -32% / 1.50** | **54.0% / -35% / 1.36** |
| Night legs only | 29.9% / -30% / 0.99 | 41.0% / -27% / 1.18 | 34.6% / -34% / 1.08 |
| DAY leg only | 12.3% / -17% / 0.84 | 17.2% / -12% / 1.02 | 14.4% / -17% / 0.92 |
| Costs x2 (plan on this) | 33.4% / -35% / 0.99 | 50.7% / -33% / 1.26 | 40.7% / -35% / 1.11 |
| Costs x3 | 22.0% / -36% / 0.74 | 37.4% / -34% / 1.02 | 28.5% / -36% / 0.87 |
| Costs x4 | 11.5% / -37% / 0.49 | 25.4% / -34% / 0.78 | 17.4% / -37% / 0.62 |
| Without each fund's 10 best nights | 39.5% | 42.8% | 40.9% / -35% / 1.14 |
| Without each fund's 25 best nights | 29.5% | 24.2% | 27.2% / -37% / 0.86 |
| Without the 10 best DAY sessions | 34.4% | 54.8% | 42.9% / -35% / 1.18 |
| DAY orders filled 10 minutes late | 47.8% / -33% / 1.29 | 69.3% / -32% / 1.54 | 56.8% / -33% / 1.40 |
| Night bought at 15:30 | 32.9% / -37% / 0.97 | 70.5% / -33% / 1.58 | 48.1% / -37% / 1.24 |
| Night bought at the close | 45.4% / -36% / 1.23 | 62.1% / -32% / 1.45 | 52.5% / -36% / 1.33 |
| Night sold at the open | 44.3% / -36% / 1.23 | 62.2% / -30% / 1.47 | 51.9% / -36% / 1.34 |
| Night sold at 09:45 | 51.0% / -36% / 1.31 | 62.0% / -31% / 1.41 | 55.7% / -36% / 1.35 |
| Night sold at 10:00 | 57.2% / -36% / 1.39 | 56.4% / -33% / 1.28 | 56.9% / -36% / 1.34 |
| QQQ buy and hold | | | 19.0% / -35% |

- **Year by year:** 2018 +34%, 2019 +75%, 2020 +77%, 2021 +65%, 2022 -5%, 2023 +81%, 2024 +64%, 2025 +79%, 2026 +27% (to 11-12). Night legs alone: +13, +72, +77, +31, -20, +24, +56, +63, +16. DAY leg alone: +19, +2, 0, +25, +18, +43, +5, +10, +10.
- **Per trade, net:** TQQQ +15 bp a night held (1,775 nights, 56% up, t 2.7); SOXL +32 bp (1,701 nights, 56% up, t 3.2); DAY +19 bp per session traded (678 sessions, 48% up, t 2.7).
- **How often:** TQQQ is held 80% of nights and SOXL 77%, at 0.95 and 0.76 of full size on average. The DAY leg trades on 31% of sessions (about 108 round trips a year). About 1,000 orders a year.
- **Before 2018** (daily data, night legs only, same sizing): 27.1%/yr, -33% drawdown over 2007-17, including 2008 (-10%).
- **Against QQQ:** beta 0.80, correlation 0.51, about 33 points a year not explained by QQQ.
- **Insensitive to timing:** see the rows above. The 200-day length (100 to 250) and the volatility target (30% to none) did not change the return per unit of risk.
- **The bad parts:** deepest drawdown -35% (2020-02-19 to 04-02); worst day -10.9%; worst single night -19.6% (SOXL) and -18.0% (TQQQ) on the position; 49 days worse than -5% in 2,210; one month in three loses; worst month -23%. **It lost 27.9% between 2026-10-01 and 11-12.** In a fast Nasdaq and semiconductor selloff it falls with the swing sleeves.
- **Tonight (2026-11-13, prices at 13:13 ET):** QQQ (676 against a 200-day average of 682) and SOXX (147 against 160) are both below, so the night leg would hold nothing.

## 7. In the account

Sleeves alone, 2019-26 (as tested, then pessimistic: SWING_Q decided at 15:50, SWING_M with a 25% haircut, LEVX at 2x costs):

| Sleeve | As tested | Pessimistic | Daily correlation with LEVX |
|---|---|---|---|
| SWING_Q | 33.5% / -28% / 1.13 | 31.9% / -30% / 1.09 | 0.42 |
| SWING_M | 22.3% / -28% / 1.06 | 17.6% / -21% / 1.10 | 0.44 |
| BBW (live rules on NVDA 2x, then real NVDL) | 25.9% / -35% / 0.93 | same | 0.06 |
| LEVX | 56.0% / -35% / 1.38 | 42.7% / -35% / 1.14 | |

Mixes, monthly rebalance. Split = SWING_Q / SWING_M / BBW / LEVX:

| Split | 2019-22 | 2023-26 | 2019-26 | Pessimistic 2019-26 | $2,372 becomes (pessimistic) |
|---|---|---|---|---|---|
| **50 / 30 / 20 / 0 (live today)** | 28.3% / -15% | 31.6% / -21% | 29.9% / -21% / 1.38 | 27.7% / -18% | $16,120 |
| 40 / 30 / 20 / 10 | 29.5% / -14% | 35.4% / -21% | 32.4% / -21% / 1.51 | 29.0% / -19% | $17,538 |
| **30 / 30 / 20 / 20** | 30.6% / -15% | 39.2% / -22% | 34.7% / -22% / 1.61 | 30.3% / -20% | $18,954 |
| 20 / 30 / 20 / 30 | 31.6% / -18% | 42.9% / -22% | 37.0% / -22% / 1.65 | 31.5% / -20% | $20,349 |
| 50 / 30 / 0 / 20 | 37.1% / -18% | 33.9% / -26% | 35.5% / -26% / 1.40 | 30.8% / -24% | $19,484 |
| 30 / 30 / 0 / 40 | 39.2% / -21% | 41.1% / -28% | 40.1% / -28% / 1.49 | 33.1% / -26% | $22,431 |
| 0 / 0 / 0 / 100 | 48.3% / -35% | 64.5% / -32% | 56.0% / -35% / 1.38 | 42.7% / -35% | $38,750 |

Which leg does the work in the account (30 / 30 / 20 / 20):

| LEVX version | As tested | Pessimistic |
|---|---|---|
| NIGHT + DAY | 34.7% / -22% / 1.61 | 30.3% / -20% / 1.52 |
| NIGHT only | 31.2% / -21% / 1.52 | 27.7% / -18% / 1.46 |
| DAY only | 26.1% / -17% / 1.51 | 23.3% / -15% / 1.48 |
| No LEVX (live split) | 29.9% / -21% / 1.38 | 27.7% / -18% / 1.36 |

- At pessimistic costs a NIGHT-only LEVX earns no more than the SWING_Q money it replaces (27.7% both ways). It only smooths the ride. The extra return comes from the same dollars working at night and again in the day.
- The last six weeks, 2026-10-01 to 11-12: live split -13.2%, 30 / 30 / 20 / 20 -15.9%, 20 / 30 / 20 / 30 -17.3%, QQQ -7.0%. LEVX would have made that stretch worse.

**Walk-forward** (split chosen on 2019-22 only, scored on 2023-26, which it never saw):

| Rule for the pick | Pick | Unseen 2023-26 |
|---|---|---|
| Best return with drawdown under 20% | 40 / 30 / 0 / 30 | 37.5% / -27% |
| Best return with drawdown under 25% | 60 / 0 / 0 / 40 | 43.0% / -27% |
| Best Sharpe | 30 / 30 / 10 / 30 | 40.2% / -25% |
| Live split, for reference | 50 / 30 / 20 / 0 | 31.6% / -21% |

**Bootstrap** (2019-26 daily returns, 20-day blocks, 2,000 resamples):

| Series | Return a year 5th / median / 95th | Worst drawdown 5th / median / 95th | Chance of a drawdown past -25% |
|---|---|---|---|
| Live split | 18% / 31% / 46% | -35% / -23% / -16% | 37% |
| 30 / 30 / 20 / 20 | 22% / 36% / 52% | -35% / -23% / -15% | 36% |
| 20 / 30 / 20 / 30 | 23% / 39% / 56% | -37% / -24% / -16% | 43% |
| 30 / 30 / 0 / 40 | 24% / 42% / 63% | -43% / -28% / -19% | 69% |
| LEVX alone | 28% / 59% / 97% | -61% / -42% / -29% | 99% |

- 20% LEVX funded from SWING_Q adds about 3 to 5 points a year at the same drawdown odds as today.
- Past 30% the account's -25% halt line gets hit more often than not.

## 8. The five funds you named, 2026

Real fund prices, each fund from its launch (SOXL and TQQQ from 2026-01-02), modelled costs:

| Fund | Buy and hold | House swing rule | Night rule | Night, before costs | Underlying vs its 200-day today |
|---|---|---|---|---|---|
| SOXL | +56% | -6% | **+52%** | +48 bp a night | -3% |
| AAOX | -94% | +12% | -26% | +74 bp | -54% |
| COHX | -55% | -34% | -53% | +68 bp | -22% |
| LITX | +9% | +174% | +107% | +112 bp | -23% |
| SPCM | -60% | 0% | not eligible | | SpaceX has no 200-day average until about March 2027 |

- The night edge in the three optical stocks was large this year, and the spread took it from AAOX and COHX.
- LITX worked under two rules and failed under none, in one year, on one stock. That is not evidence.
- A fund joins LEVX only if it passes the test in `docs/levx-sleeve.md` (spread, volume, history, and the night rule net of twice its measured cost).

## 9. Side findings worth knowing

1. **BBW on a long history.** The live BBW rules (unchanged `bbw.py`) on NVDA 2x: 2018 -47%, 2019 +10%, 2020 -23%, 2021 +92%, 2022 -21%, 2023 +4%, 2024 +46%, 2025 +82%, 2026 +78%. On real NVDL: +22%, +26%, +57%, +94% for 2023-26. Over 9 years it lost money on SOXL (-31%) and TQQQ (-41%). The edge is a 2024-26 NVDA effect. That is a point for the monthly review, not an action taken here.
2. **The swing rules' last six weeks, and why the account did not feel them.** Replayed at full size over 2026-10-01 to 11-12: SWING_Q -14.5%, SWING_M -22.7% on the backtest's own stock pool (not the live pick list), taking that backtest's drawdown to -28% against -21% when the sleeves were adopted. The ledger shows far less: SWING_Q +$38 and SWING_M -$19 realized over the same weeks. The sleeves were under-funded: after 10-05 the QLD positions were $106 to $607 against targets of about $1,200 to $2,000, because cash had gone to the MU option purchases.
3. **Why the DAY sleeve was dropped in September, and why this is not the same test.** `noise30` charged 3 bp a side before the 3x multiplier (9 bp a side on a 3x fund) and traded the short side. FMP's 30-minute bars are identical to its 5-minute bars aggregated, so bar size was not the cause. Long only, on TQQQ's own bars at 1.5 bp a side, the rule was positive in both halves and in 8 of 9 years, and made 9% to 14% a year at double cost.
4. **The published VWAP stop did nothing on TQQQ.** The rule as first coded sold below max(band, VWAP) and re-bought above the band at the same check, so the VWAP test never changed a position. Three readings, fills one bar late: band only 14.4%/yr (-17%), band and VWAP as published 13.9% (-19%), as first coded 14.2% (-18%). The live rule is the band alone, which needs no volume data. A mutation test caught this.
5. **Data hole.** A throttled FMP request returns nothing and leaves a silent gap (TQQQ was missing 100 sessions). `levx_data.fmp_5min_repair` re-fetches them. Any future 5-minute backtest should run it.

## 10. Limits of this evidence

- **Costs are the whole question.** LEVX places about 1,000 orders a year. At 4x the assumed cost it makes 17%/yr, less than QQQ. The assumption is 1.1x to 1.7x the midday quoted half-spread; real fills, and spreads in the first minutes after the open, have not been measured. The sleeve logs every fill against the quote so that they will be.
- **One history.** 2018-26 for the exact rules, 2000-17 for the night leg on daily data. Both funds rode a strong Nasdaq and semiconductor decade; the night rule earns a share of the index's return, so a weak decade means a weak sleeve.
- **Multiple testing.** About 21 daily and 11 intraday rules were tried before the night rule was chosen. The night effect is published and showed up in 3 indices and 14 of 15 funds, so the risk is lower than for the DAY leg, which rests on one fund and one published rule.
- **Gap risk has no stop.** The worst night held cost 19.6% of the SOXL position. A 3x fund is wiped out by a -33% overnight index move; that has not happened to these indices.
- **Taxes and wash sales.** Every gain is short term. Daily round trips in the same fund defer losses into the next purchase, and a loss taken on TQQQ or SOXL in any other account within 30 days of a LEVX buy is a wash sale. Not modelled.
- **Cash and account size.** See "Open items" in `docs/levx-sleeve.md`: deployable cash is below the sleeves' combined targets, and the account sits $492 above Robinhood's $2,000 margin-account minimum.
- **Not a forecast.**

## 11. Re-running it

| Script | What it does |
|---|---|
| `levx_universe.py` | fund universe from FMP, checked against prices |
| `levx_stage1.py`, `levx_stage2a.py`, `levx_stage2b.py` | daily rules, dip anatomy, slot-limited books |
| `levx_intraday.py`, `levx_bbw_long.py` | 5-minute rule battery; BBW year by year |
| `levx_night.py`, `levx_momnight.py`, `levx_sleeve.py`, `levx_robust.py` | night against day, momentum names, night rule on daily data and on 15 funds |
| `levx_final.py`, `levx_mix.py`, `levx_report.py` | the live rules replayed, account mixes, stress and bootstrap (run in that order) |
| `levx_fixture.py`, `test_levx.py` | the test fixture; the live path equals the backtest |

Caches live in `data/levx_cache/` (not committed). FMP_API_KEY is needed for the 5-minute bars.
