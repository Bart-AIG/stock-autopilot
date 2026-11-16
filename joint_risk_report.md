RISK RED (9) - QQQ broke 666 (665.97 at 15:00Z, now 664.66); score 6 -> 9, tranche-1 level reached intraday

**15:41Z, Mon Nov 16.** Your QQQ < 666 alert fired at **15:00Z (665.97)**. QQQ is now **664.66 (-2.2% today)**, 0.2% under it. That adds 3 points, so the score goes from **6 to 9 and the tier goes from ORANGE to RED**. Nothing else fired. SPY is 744.45 (-1.3%). VIX is 21.53 (21.09 at 14:42Z), still under 22.

**What 666 means in the plan:** it's the **tranche-1 reinvest level** (QQQI first). Tranche buys are sized at 1/3 of the **cash raised**. No cash has been raised: cash is **-$77,937** against **$145.5k of stock**. The account is worth **$67,542**, so that's about **$2.15 of stock for each $1 of your own money**. Tranche 1 buys **$0** until the de-risk is done. The plan's levels count on a **close**, or a break that holds into the last hour. A 666 print today is a reason to finish the stage-4 sells, not to buy.

**Benchmarks (15:41Z):**
| Alert | Level | Price | Distance |
|---|---|---|---|
| **QQQ < 666** | 666.00 | 664.66 | **-0.2% (on, new)** |
| SPY < 50-day | 764.43 | 744.45 | -2.6% (on) |
| QQQ < 20-day | 695.45 | 664.66 | -4.4% (on) |
| QQQ < 704.88 | 704.88 | 664.66 | -5.7% (on) |
| QQQ < 50-day | 717.87 | 664.66 | -7.4% (on) |
| QQQ < 733 | 733.00 | 664.66 | -9.3% (on) |
| HYG < 76.35 | 76.35 | 76.89 | +0.7% |
| IEF > 91.10 | 91.10 | 90.27 | -0.9% |
| IEF < 88.95 | 88.95 | 90.27 | +1.5% |
| TIP < 102.85 | 102.85 | 104.72 | +1.8% |
| SPY < 729 | 729.00 | 744.45 | +2.1% |
| VIX (real) | 22 | 21.53 | -2.1% |
| SPY < 690 | 690.00 | 744.45 | +7.9% |

**Ladder:** stage 4 is reached and still owed: margin to zero, then the semis/high-beta trims, then the core trims. Use the share counts in joint_derisk_plan.json and skip what you've already sold. Tranche 1 is reached intraday, but it has no cash to deploy (see above).

**Today's damage (from Friday's close):** SOXL -16%, COHX -16%, AAOX -19%, CBRS -8%, BE -8%, MU -7% (723.22), MPWR -7%, LASR -7%, NVDL -5%, STRL -5%, CDNS -4%, META -2.5%, AMZN -2.2%, QQQI -2.0%.

**HOLDINGS HEALTH** (carried from 14:42Z; prices have only fallen since):
- WEAK: CDNS, COHX, MU, NVDL, SOXL, AAOX, STRL, BE, MOD, SPCX, NOW, BBAI, RUN, TLRY, CGC, LASR.
- WATCH: META, MPWR, QQQI, CBRS.
- OK: AMZN.

**SELL LIST (RED: 12% single-name cap, 15% cash target), for you to place in-app. Margin first ($77.9k), then:**
- **META**, trim ~$13.8k (44%). 22% of the book, +1%. Core: trim only, never sell out.
- **QQQI**, trim ~$7.4k (30%). 17% of the book, -2%. **Wash sale:** 395 shares were bought Nov 13. A loss sale before Dec 14 is disallowed on the shares that match. Core: trim only.
- **AMZN**, trim ~$5.2k (23%). 16% of the book, +12%. Core: trim only.
- **SPCX**, ~$15.7k (all). WEAK, -4% (loss harvest).
- **Semis and leveraged ETFs:** MU ~$5.1k (+5%), NVDL ~$5.3k (-35%, loss), SOXL ~$5.1k (-9%, loss), COHX ~$4.5k (+21%), AAOX ~$3.2k (-22%, loss).
- **CDNS** ~$6.2k (all, -2%).
- **Other WEAK names:** BE ~$3.5k (+4%), NOW ~$2.3k (half, -4%), STRL ~$1.4k (-10%), MOD ~$1.3k (+22%), LASR ~$0.8k (+10%), BBAI, RUN, TLRY, CGC (under $500 each, all losses).
- **CBRS** ~$1.0k (-9%). Bought Nov 13: a loss sale before Dec 14 is disallowed.
- **STRL** was bought Nov 12. A loss sale stays clean only if you don't rebuy it before Dec 13.
- **Thesis checks:** I found no headline dated today for the chip drop, and no company-specific break in any name. The move is sector-wide. The verdicts are carried from Friday: **intact**, with the semis and leveraged ETFs **weakened** on price.
- **Earnings:** no holding reports within 14 days (MU Dec 16 pm, not verified).

**Crack watch:** GREEN, 0 REDs (from 14:42Z). Credit is firm today: LQD +0.2%, IEF +0.3%, HYG -0.1%. This is a stock selloff, not funding stress.

**Rally check:** OK, no fragile rally.

**What brings the tier down:** a QQQ close back above 666 (score back to 6, ORANGE), then QQQ above 695.45 and 704.88, and SPY above 764.43.
