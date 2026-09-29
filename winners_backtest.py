"""
Winner persistence test — do the names in SPY / QQQ that gained the most in one calendar
year keep outperforming the next year?  (Ryan, 2026-09-29: "looking at the names in spy
and qqq that had made the most gains each year and see if there is any correlation of
picking those same names for the next year".)

Runs on GitHub Actions (FMP key). Pure standard library.

Universe, point-in-time where possible:
  1. FMP historical constituent changes for the S&P 500 and Nasdaq-100 (rolled back from
     today's list to rebuild membership at the start of each year), if this FMP tier
     serves them;
  2. otherwise the S&P 100 and Nasdaq-100 as of end-2018 (years 2019+ only; picking a
     pre-period list keeps hindsight out of the selection).
A name is ranked only if it was a member at the start of year Y and has prices for the
whole of year Y-1. Its year-Y return is measured to year end, or to its last price if it
stopped trading (a delisted name is NOT dropped; its return runs to its last print).

For each index and year:
  * Spearman rank correlation between names' year Y-1 and year Y returns.
  * Next-year return of the prior year's top 5 / top 10 / top decile / bottom decile vs
    the equal-weight universe and the ETF (SPY / QQQ).
  * Hit rate: share of the top 10 that beat the ETF the next year.
Strategies (equal weight, no costs beyond 5 bp per trade):
  TOP10_ANNUAL   each January buy last year's 10 biggest gainers, hold the year.
  TOP5_ANNUAL    same with 5.
  TOP10_12M_MONTHLY  each month hold the 10 names with the best trailing 12-month return.
  TOP10_12_1_MONTHLY same, skipping the most recent month (classic 12-1 momentum).

Limits: FMP may not carry every delisted name (those are logged and excluded, a small
survivorship bias); taxes ignored.
"""

from __future__ import annotations

import os
import statistics
import sys
import time
from datetime import date, datetime
from pathlib import Path

from backtest import BASE, NDX100_2018, SP100_2018, _get, stats

HERE = Path(__file__).resolve().parent
COST = 5e-4


def adj_closes(sym, key, start="2005-06-01"):
    data = _get(f"{BASE}/historical-price-eod/dividend-adjusted?symbol={sym}&from={start}&to={date.today()}&apikey={key}")
    if not isinstance(data, list) or not data:
        return None
    rows = sorted(((r["date"][:10], float(r.get("adjClose") or r.get("close") or 0)) for r in data), key=lambda x: x[0])
    return [(d, p) for d, p in rows if p > 0]


def membership(index, key, log):
    """Return {year: set(symbols at the start of that year)} or None."""
    cur_ep, hist_ep = {"SPX": ("sp500-constituent", "historical-sp500-constituent"),
                       "NDX": ("nasdaq-constituent", "historical-nasdaq-constituent")}[index]
    cur = _get(f"{BASE}/{cur_ep}?apikey={key}")
    hist = _get(f"{BASE}/{hist_ep}?apikey={key}")
    if not isinstance(cur, list) or not cur or not isinstance(hist, list) or not hist:
        log.append(f"{index}: constituent endpoints unavailable ({str(cur)[:60]} / {str(hist)[:60]})")
        return None
    members = {r["symbol"] for r in cur if r.get("symbol")}
    changes = []
    for r in hist:
        d = (r.get("date") or r.get("dateAdded") or "")[:10]
        if len(d) == 10:
            changes.append((d, r.get("symbol") or "", r.get("removedTicker") or ""))
    changes.sort(reverse=True)
    out, ci = {}, 0
    for y in range(date.today().year, 2004, -1):
        cutoff = f"{y}-01-01"
        while ci < len(changes) and changes[ci][0] >= cutoff:
            _, added, removed = changes[ci]
            if added:
                members.discard(added)
            if removed:
                members.add(removed)
            ci += 1
        out[y] = set(members)
    log.append(f"{index}: rebuilt membership from {len(changes)} changes; "
               f"sizes {min(out)}={len(out[min(out)])}, {max(out)}={len(out[max(out)])}")
    return out


def year_end_prices(series):
    ye = {}
    for d, p in series:
        ye[d[:4]] = (d, p)
    return ye


def spearman(xs, ys):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for k, i in enumerate(order):
            r[i] = k
        return r
    if len(xs) < 5:
        return float("nan")
    return statistics.correlation(ranks(xs), ranks(ys))


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    log = []
    universes = {}
    for idx, etf, fallback in (("SPX", "SPY", SP100_2018), ("NDX", "QQQ", NDX100_2018)):
        m = membership(idx, key, log)
        if m:
            universes[idx] = (etf, m, "point-in-time membership (FMP historical constituents)")
        else:
            universes[idx] = (etf, {y: set(fallback) for y in range(2019, date.today().year + 1)},
                              f"fallback: {'S&P 100' if idx == 'SPX' else 'Nasdaq-100'} as of end-2018, years 2019+")

    need = set()
    for etf, m, _ in universes.values():
        need.add(etf)
        for y, s in m.items():
            if y >= 2006:
                need |= s
    prices, missing = {}, []
    for n, s in enumerate(sorted(need)):
        ser = adj_closes(s.replace(".", "-"), key)
        if ser:
            prices[s] = ser
        else:
            missing.append(s)
        if n % 50 == 0:
            print(f"fetched {n}/{len(need)}", flush=True)
        time.sleep(0.12)
    log.append(f"prices for {len(prices)} of {len(need)} symbols; missing {len(missing)} "
               f"(delisted/renamed names FMP does not carry): {', '.join(missing[:40])}{' ...' if len(missing) > 40 else ''}")

    ye = {s: year_end_prices(ser) for s, ser in prices.items()}
    this_year = str(date.today().year)

    out = [f"# Winner persistence test — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           "Question: do last year's biggest gainers in SPY / QQQ keep outperforming the next year?\n"]

    for idx, (etf, mem, how) in universes.items():
        years = sorted(y for y in mem if y - 1 >= 2006 and str(y) <= this_year)
        rows, strat = [], {"TOP10_ANNUAL": [], "TOP5_ANNUAL": [], "ETF": [], "EQUAL_WEIGHT_ALL": []}
        for y in years:
            ys, yp = str(y), str(y - 1)
            ypp = str(y - 2)
            cands = []
            for s in mem[y]:
                e = ye.get(s)
                if not e or yp not in e or ypp not in e:
                    continue
                prev_ret = e[yp][1] / e[ypp][1] - 1
                # next-year return: to year end, or to the last print if it stopped trading
                last = e.get(ys) or None
                if last is None:
                    later = [v for k, v in e.items() if k > yp]
                    if later:
                        last = later[-1]
                    else:
                        continue
                nxt = last[1] / e[yp][1] - 1
                cands.append((prev_ret, nxt, s))
            if len(cands) < 20 or etf not in ye or ys not in ye[etf] or yp not in ye[etf]:
                continue
            etf_ret = ye[etf][ys][1] / ye[etf][yp][1] - 1
            cands.sort(reverse=True)
            n = len(cands)
            dec = max(1, n // 10)
            mean = lambda xs: sum(xs) / len(xs)
            top5, top10 = [c[1] for c in cands[:5]], [c[1] for c in cands[:10]]
            topd, botd = [c[1] for c in cands[:dec]], [c[1] for c in cands[-dec:]]
            allr = [c[1] for c in cands]
            rho = spearman([c[0] for c in cands], allr)
            hit = sum(1 for r in top10 if r > etf_ret) / 10
            rows.append((ys, n, rho, mean(top5), mean(top10), mean(topd), mean(botd), mean(allr), etf_ret, hit,
                         ", ".join(f"{c[2]} {c[0]:+.0%}→{c[1]:+.0%}" for c in cands[:5])))
            strat["TOP10_ANNUAL"].append(mean(top10) - 2 * COST)
            strat["TOP5_ANNUAL"].append(mean(top5) - 2 * COST)
            strat["ETF"].append(etf_ret)
            strat["EQUAL_WEIGHT_ALL"].append(mean(allr))
        if not rows:
            out.append(f"## {idx}: not enough data\n")
            continue
        out.append(f"## {idx} (benchmark {etf}) — {how}\n")
        out.append("| Year | Names | Rank corr (last yr vs this yr) | Top 5 | Top 10 | Top decile | Bottom decile | All (eq-wt) | "
                   f"{etf} | Top-10 hit rate vs {etf} |")
        out.append("|---|---|---|---|---|---|---|---|---|---|")
        for ys, n, rho, t5, t10, td, bd, al, er, hit, _ in rows:
            tag = " (YTD)" if ys == this_year else ""
            out.append(f"| {ys}{tag} | {n} | {rho:+.2f} | {t5:+.1%} | {t10:+.1%} | {td:+.1%} | {bd:+.1%} | "
                       f"{al:+.1%} | {er:+.1%} | {hit:.0%} |")
        full = [r for r in rows if r[0] != this_year]
        if full:
            avg = lambda k: sum(r[k] for r in full) / len(full)
            out.append(f"| **Average ({len(full)} full years)** | | **{avg(2):+.2f}** | **{avg(3):+.1%}** | **{avg(4):+.1%}** | "
                       f"**{avg(5):+.1%}** | **{avg(6):+.1%}** | **{avg(7):+.1%}** | **{avg(8):+.1%}** | **{avg(9):.0%}** |")
            pos = sum(1 for r in full if r[2] > 0)
            beat = sum(1 for r in full if r[4] > r[8])
            out.append(f"\nRank correlation positive in {pos} of {len(full)} years; last year's top 10 beat {etf} "
                       f"in {beat} of {len(full)} years.\n")
            # compounded annual strategies (full years only)
            out.append("| Annual strategy (full years) | CAGR | Worst year | Best year |")
            out.append("|---|---|---|---|")
            k = len(full)
            for name, rs in strat.items():
                rs = rs[:k] if rows[-1][0] == this_year else rs
                rs = rs[:len(full)]
                g = 1.0
                for r in rs:
                    g *= 1 + r
                out.append(f"| {name if name != 'ETF' else etf + ' buy & hold'} | {g ** (1 / len(rs)) - 1:.1%} | "
                           f"{min(rs):+.1%} | {max(rs):+.1%} |")
        out.append("\n**Last year's top 5 each year (prior-year gain → next-year gain):**\n")
        for ys, *_, names in rows:
            out.append(f"- {ys}: {names}")
        out.append("")

        # monthly trailing-12-month momentum inside the same point-in-time universe
        monthly = {}
        for s, ser in prices.items():
            mm = {}
            for d, p in ser:
                mm[d[:7]] = p
            monthly[s] = mm
        months = sorted(monthly.get(etf, {}))
        first_year = min(int(r[0]) for r in rows)
        months = [m for m in months if m >= f"{first_year - 2}-12"]
        for skip, label in ((0, "TOP10_12M_MONTHLY"), (1, "TOP10_12_1_MONTHLY")):
            eq, curve, dates, held = 1.0, [], [], []
            for i in range(12, len(months)):
                m, pm = months[i], months[i - 1]
                # return of holdings chosen last month
                if held:
                    rs = []
                    for s in held:
                        a, b = monthly[s].get(pm), monthly[s].get(m)
                        rs.append(b / a - 1 if a and b else 0.0)
                    eq *= 1 + sum(rs) / len(rs)
                curve.append(eq)
                dates.append(m + "-28")
                # choose for next month using data to month m
                y = int(m[:4]) + (1 if m[5:] == "12" else 0)
                mem_now = mem.get(int(m[:4]) if m[5:] != "12" else y, set())
                look_end, look_start = months[i - skip], months[i - 12]
                sc = []
                for s in mem_now:
                    a, b = monthly.get(s, {}).get(look_start), monthly.get(s, {}).get(look_end)
                    if a and b and monthly[s].get(m):
                        sc.append((b / a - 1, s))
                sc.sort(reverse=True)
                new = [s for _, s in sc[:10]]
                turnover = len(set(new) - set(held)) / 10 if held else 1.0
                eq *= 1 - 2 * COST * turnover
                held = new
            if len(curve) > 24:
                st = stats(curve, dates)
                ec = [monthly[etf][months[i]] for i in range(12, len(months))]
                se = stats(ec, dates)
                out.append(f"- **{label}** ({dates[0][:7]} → {dates[-1][:7]}): CAGR {st['cagr']:.1%}, max DD {st['mdd']:.0%} "
                           f"vs {etf} {se['cagr']:.1%} / {se['mdd']:.0%}")
        out.append("")
    out.append("## Data log\n")
    out.extend(f"- {x}" for x in log)
    (HERE / "winners_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
