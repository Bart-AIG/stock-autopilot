# Leveraged ETFs in the joint account: what to trade, when, and how big (run 2026-11-26)

**Request (Ryan, live turn 2026-11-26):** research strategies to day trade and swing trade daily leveraged ETFs in the joint account. Ryan places the trades himself and needs a process, "maybe we trade on daily rsi or moving averages to help pick when we buy or weekly".

**Status:** research and a proposed process (`docs/joint-letf-process.md`). Advisory only: the agent cannot trade the joint account and placed nothing. Every number below is a backtest: historical, after the stated costs, not a forecast.

## 1. Verdict

| Question | Answer | Confidence |
|---|---|---|
| Day trade leveraged ETFs by hand in the joint? | **No.** The only day rules that survived costs (LEVX, `levx_results.md`) need a check every 30 minutes or a 15:50 buy and 09:31 sell every day, on TQQQ and SOXL only. That is not hand-executable around a day job, every gain is short term, and the agentic account already runs it | High |
| RSI as the main signal? | **No.** RSI(2) dips held in a 3x fund have the best risk-adjusted numbers before tax, but trade 15-16 times a year, lose 4 to 5 points a year to short-term tax, and lose another 2 to 4 points if placed the next morning instead of at the close. Weekly RSI(14) > 50 was the worst trend rule on every index | High |
| Moving averages? | **Yes, with two additions.** A 200-day average with a 2% band (enter 2% above, exit 2% below), plus position size capped by recent volatility. It is the only rule tested that kept the 3x worst drawdown near or under 60% on all three indexes | Moderate to high |
| Daily or weekly? | **Exits daily, sizing weekly.** Weekly-only checks were as good on the S&P 500 but cost 3 to 5 points a year on Nasdaq and semis at 3x. A Robinhood alert can do the daily part | Moderate |
| Which fund? | **UPRO (3x S&P 500) as the core.** Best drawdown, works with weekly checks, survived 1987, 2000-02 and 2008, and does not collide with the agentic account's QLD / TQQQ / SOXL (wash sales). TQQQ optional at up to half the sleeve. SOXL a small satellite at most | Moderate |
| Single-stock leveraged funds (NVDL, MUU, AAOX, COHX, NEBX)? | **Out of the process.** 0.3% to 1.1% round-trip spreads (LEVX measurement, 2026-11-13), earnings gaps, no long history. They were $9.7k of the joint's $18.0k leveraged-fund loss since 2026-10-15 | High |
| What does it say today (2026-11-25 close)? | **OFF on all three. Hold no leveraged index fund.** SPY needs a close above 747.82 (+4.3%), QQQ above 697.17 (+10.0%), SOXX above 164.43 (+28.5%) | High |

## 2. What was wrong before any strategy (measured from the broker, 2026-11-26)

| Finding | Numbers | Why it matters |
|---|---|---|
| The joint account is on margin at about 2x | Net equity $49,533; positions $97,757; cash **-$48,224** | A 3x fund held on margin is leverage on leverage. Robinhood sets maintenance per position at 25% to 100% by volatility and can change it or sell without notice |
| Discretionary leveraged-fund trading is losing | 33 closes from 2026-10-15 to 11-25: **-$17,969**, 8 winners / 25 losers. SOXL -$7,754, NVDL -$4,072, AAOX -$3,339, MUU -$1,387, COHX -$1,210, TQQQ -$431 | Repeated dip buying in 3x funds in a falling market: the losing pattern in every test here |
| Losses are being washed | Six of the seven funds were bought back within 30 days after a loss sale (`wash_sale_watch.json`, after_sale: true) | Those losses move into the replacement shares' basis and only count once the shares are sold without another buy-back inside 30 days |

Realized figures are Robinhood's per-trade P/L before wash-sale adjustment.

## 3. How it was tested

- **Prices:** FMP daily bars (split and dividend adjusted): QQQ from 1999, SPY from 1993, SOXX from 2001, the S&P 500 index from 1985. Real TQQQ, QLD, UPRO, SPXL, SSO, SOXL, TECL, ROM for calibration. 3-month T-bill from FRED (DTB3). Fetched by `letf_fetch.py` on the GitHub runner into `data/letf/`.
- **Synthetic funds:** daily 2x / 3x of the underlying's total return, minus (L-1) x (T-bill + spread) and the expense ratio. The spread was calibrated on the real funds since launch:

| Real fund | Since | Real CAGR | Synthetic CAGR | Spread over T-bill |
|---|---|---|---|---|
| TQQQ | 2010-02 | 38.11% | 38.08% | 0.50% |
| QLD | 2006-06 | 23.15% | 23.19% | 0.50% |
| UPRO | 2009-06 | 30.44% | 30.21% | 0.75% |
| SOXL | 2010-03 | 26.86% | 27.15% | 0.75% |

- **Signals** are always computed on the index ETF (SPY, QQQ, SOXX), never on the leveraged fund. Cash earns the T-bill rate.
- **Execution:** at the close the signal fires, or at the next morning's open. Overnight moves are applied to the fund at 3x before a next-open trade.
- **Costs:** 5 bp per side on every trade.
- **Tax** (the joint is taxable): FIFO lots, short-term 32% / long-term 15% (Texas has no state income tax), losses deferred under the 30-day wash-sale rule on re-entry, annual netting, loss carryforward, T-bill interest taxed as ordinary income, and liquidation at the end. The rates are an assumption; the ranking of rules does not depend on them.
- **Periods:** start = 200 days after each ETF's first bar. QQQ's test starts 1999-12-22, three months before the dot-com top: the worst start date for leveraged Nasdaq, used on purpose. Halves split at 2013 (QQQ), 2010 (SPY), 2014 (SOXX).
- **Rules tested:** 13 rules x 1x / 2x / 3x x close / next open x 3 indexes. They were fixed before seeing results, not chosen after.

## 4. The rules side by side (3x, executed at the close)

Pre-tax CAGR / after-tax CAGR / worst drawdown:

| Rule | S&P 500 (1993-2026) | Nasdaq-100 (1999-2026) | Semis (2002-2026) | Trades a year |
|---|---|---|---|---|
| Hold the index, 1x (reference) | 10.6% / 10.0% / -55% | 8.2% / 7.7% / -83% | 13.8% / 13.1% / -67% | 0 |
| Hold the 3x fund | 13.0% / 12.4% / **-98%** | **-3.5%** / -3.5% / **-100%** | -0.6% / -0.6% / **-99.8%** | 0 |
| 200-day, daily, no band | 14.9% / 12.8% / -72% | 9.2% / 7.8% / -96% | 13.0% / 11.1% / -93% | 6.5-8 |
| 200-day, 2% band | 17.6% / 15.3% / -58% | 10.5% / 9.1% / -92% | 17.6% / 15.4% / -84% | 1.5-2.7 |
| 40-week average, weekly | 12.8% / 11.1% / -83% | 13.4% / 11.8% / -95% | 10.3% / 8.9% / -91% | 3.3-4.1 |
| 10-month average, monthly | 17.5% / 15.0% / -61% | 11.9% / 10.1% / -88% | 21.3% / 18.7% / -81% | 1.5-1.9 |
| 50/200 golden cross | 18.0% / 15.9% / -76% | 17.2% / 15.3% / -81% | 18.1% / 15.9% / -89% | 0.9-1.3 |
| Weekly RSI(14) > 50 | 11.9% / 9.5% / -84% | 10.8% / 8.7% / -95% | 13.5% / 10.0% / -91% | 4.6-5.4 |
| RSI(2) < 10 dip above the 200-day, out above the 5-day | 16.2% / 11.2% / -40% | 13.0% / 8.8% / -47% | 14.9% / 10.3% / -56% | 15-16 |
| 2x core + 3x on RSI(2) dips | 16.7% / 11.5% / -50% | 13.0% / 8.6% / -87% | 17.7% / 12.1% / -77% | 22-23 |
| **Recommended: 2% band, daily exit, weekly volatility size** | **17.3% / 14.5% / -48%** | **15.4% / 12.5% / -60%** | **17.8% / 14.3% / -60%** | 3-8 |

- **The 3x fund held through a bad decade goes to zero.** Nasdaq 3x from the 2000 top lost 100%; semis 3x lost 99.8% by 2002. Holding is not an option for these funds.
- **The 200-day alone is not enough at 3x for Nasdaq and semis** (-92% to -96%). Nasdaq fell 37% from its March 2000 top before it broke the 200-day, and a 3x fund falls about 80% in that move.
- **The band matters more than the average's length.** Adding a 2% band cut trades from 6.5-8 a year to 1.5-2.7 and lifted return on every index. Any band from 1% to 5% gave similar results; no band was worse on all three:

| Band (recommended rule, 3x) | 0% | 1% | 2% | 3% | 5% |
|---|---|---|---|---|---|
| S&P 500 | 15.4% / -60% | 16.8% / -50% | 17.3% / -48% | 17.1% / -50% | 18.9% / -50% |
| Nasdaq-100 | 14.8% / -70% | 16.6% / -62% | 15.4% / -60% | 15.7% / -57% | 16.4% / -51% |
| Semis | 14.5% / -76% | 18.8% / -58% | 17.8% / -60% | 16.7% / -64% | 17.4% / -67% |

- **The volatility cap is what fixes Nasdaq and semis.** Size = min(3x, 50% / the index's 20-day realized volatility). It cut the 3x Nasdaq drawdown from -92% to -60% and semis from -84% to -60%. Targets of 40%, 50% and 60% gave similar results. This is volatility management in the sense of Moreira & Muir (2017), whose results have been debated since; the evidence here is the test above, not the paper.
- **RSI(2) dips are a good rule in the wrong account.** Best risk-adjusted numbers before tax on the S&P (Sharpe 0.75), but every gain is short term, it is in the market 11% of the time, and next-morning execution cost 2.1 to 4.3 points a year. The agentic account already runs this exact rule on QLD (SWING_Q).

## 5. The recommended rule in detail

| Index / fund | Leverage | Executed | Pre-tax CAGR | After tax | Worst drawdown | Worst year | Trades a year |
|---|---|---|---|---|---|---|---|
| S&P 500 / UPRO | 3x | close | 17.3% | 14.5% | -48% | -36% (2022) | 3.0 |
| S&P 500 / UPRO | 3x | next open | 18.5% | 15.5% | -48% | -36% | 3.0 |
| S&P 500 / SSO | 2x | close | 14.0% | 12.0% | -39% | -27% | 1.7 |
| S&P 500 index from 1985 (with 1987, no dividends) | 3x | close | 13.5% | 11.6% | -52% | -40% | 2.9 |
| Nasdaq-100 / TQQQ | 3x | close | 15.4% | 12.5% | -60% | -37% | 5.0 |
| Nasdaq-100 / QLD | 2x | close | 12.9% | 11.0% | -57% | -32% | 2.8 |
| Semis / SOXL | 3x | close | 17.8% | 14.3% | -60% | -34% | 8.3 |
| Semis / USD | 2x | close | 16.5% | 13.6% | -57% | -37% | 4.2 |

- **Weekly-only checks** (exit and size decided on Fridays only): S&P 3x 17.6% / -48%, about the same. Nasdaq 3x 13.6% / -66% and semis 3x 15.2% / -66%, both worse. Exits on Nasdaq and semis need the daily alert.
- **Next-morning execution** changed CAGR by -0.6 to +1.2 points. Trade at the close or the next morning, whichever is practical.
- **How much exposure it actually runs:** on the S&P it is ON 77% of the time at an average 2.9x. On Nasdaq it is ON 73% of the time at 2.7x. On semis it is ON 69% of the time at 2.2x, because semis volatility usually keeps it below 3x.
- **1987:** the S&P closed 5.4% under its 200-day on Friday 10-16-1987, so the rule was out before Black Monday's -20.5%. That was partly luck. A crash straight out of a calm uptrend would hit a full 3x position: a -33% index day ends a 3x fund.

**Year by year, pre-tax** (rule / holding the same fund / holding the 1x index):

| Year | S&P 3x rule | UPRO-like hold | SPY | Nasdaq 3x rule | TQQQ-like hold | QQQ |
|---|---|---|---|---|---|---|
| 2000 | -18% | -46% | -10% | -33% | -92% | -36% |
| 2001 | +3% | -46% | -12% | -7% | -89% | -33% |
| 2002 | -14% | -63% | -22% | -7% | -86% | -37% |
| 2008 | +1% | -86% | -37% | -37% | -88% | -42% |
| 2015 | -18% | -6% | +1% | -1% | +17% | +9% |
| 2018 | -24% | -25% | -5% | -9% | -20% | 0% |
| 2020 | -3% | +13% | +18% | +30% | +114% | +49% |
| 2022 | -36% | -57% | -18% | -23% | -79% | -33% |
| 2023 | +30% | +69% | +26% | +108% | +200% | +55% |
| 2024 | +63% | +64% | +25% | +48% | +60% | +26% |
| 2025 | +25% | +32% | +18% | +27% | +36% | +21% |
| 2026 to 11-25 | **-23%** | +2% | +6% | -12% | -13% | +4% |

The rule pays for itself in crash years (2000-02, 2008, 2022) and loses in choppy ones (2015, 2018, 2026). **It trailed the plain 1x index in about 4 years out of 10** (S&P 12 of 33, Nasdaq 11 of 27, semis 11 of 24) and had a losing year about 1 year in 3. **2026 is one of those years**: it went out on 2026-03-27 at SPY 634.09, back in on 04-08 at 676.01, and out on 11-20 at 689.81, two sessions before a 3.9% bounce. Full table: `data/letf/_yearly.csv`.

## 6. Semis in the fall of 2026

| Since 2026-10-01 | Return |
|---|---|
| SOXX (1x) | -33.4% |
| SOXL held | **-79.2%** |
| Rule on SOXL | -25.0% (out on 2026-11-02 at SOXX 151.22) |

- The rule is late on semis. It held SOXL at 41-45% of the sleeve while SOXL fell from $163.71 (10-02) to $68.17 (11-02), because SOXX only crossed 2% under its 200-day after falling 23% from its high.
- About $3.0k of the joint's $7.75k SOXL loss was realized after 11-02, when the rule was out.

## 7. Day trading, for completeness

From the LEVX research (`levx_results.md`, 2026-11-13; real 5-minute bars 2018-26):

- Of 11 published day-trade rules, only a noise-area breakout on TQQQ (long only) was positive in both halves. It needs a decision at every :00 and :30 bar.
- Opening-range breakouts worked in 2018-22 and stopped working after.
- The edge in leveraged index funds is overnight (+15 bp a night on TQQQ, +32 bp on SOXL, above the 200-day): buy near 15:50 ET, sell after the next open, about 200 round trips a year per fund.
- In the joint that would be about 200 round trips a year per fund, all short term, a wash-sale chain on every losing night, and a duplicate of what the agentic LEVX sleeve already holds.

## 8. Limits of this evidence

- **One history per index.** US large caps had a strong 2009-2026. The rule earns a share of the index's trend, so a flat decade means a weak rule.
- **Multiple testing.** 13 rules were tried. The recommended family (200-day trend, Gayed & Bilello 2016; volatility sizing) is published, and its settings were insensitive to band width and volatility target. That lowers but does not remove the risk of luck.
- **Synthetic before 2010.** Calibrated within 0.3 to 0.9 points a year of the real funds since launch, on daily data only. An intraday crash through -33% would end a 3x fund; it has not happened to these indexes.
- **Taxes are modelled simply.** Rates are assumed; the IRS wash-sale rule treats a spouse's or your own other accounts' purchases as replacements (IRS Publication 550), and only the re-entry case is modelled.
- **Drawdowns of -48% to -60% are the base case, not a tail.** A bootstrap was not run here.

## 9. Re-running it

| Command | What it does |
|---|---|
| push `letf_fetch.py` to a `claude/*` branch | the `letf-data.yml` workflow refreshes `data/letf/` from FMP and FRED |
| `python3 letf_joint_backtest.py` | the full battery, into `data/letf/_battery.csv` (about 4 minutes) |
| `python3 letf_joint_backtest.py recommended` | the recommended rule's table, into `data/letf/_recommended.csv` |
| `python3 letf_joint_backtest.py signals` | today's state, entry and exit lines and size for SPY / QQQ / SOXX |
