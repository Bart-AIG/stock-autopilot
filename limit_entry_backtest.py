"""
Limit-entry backtest — would resting a limit buy BELOW yesterday's close on sleeve candidates
beat buying at the close?  (Ryan, live turn 2026-10-01: "Can you backtest this then? ... rest
a limit order on a candidate that's already close to triggering, a few percent below
yesterday's close. If it fills, keep the position only if the close confirms the signal; if
not, sell at the close.")

Runs on GitHub Actions (FMP key). Pure standard library. Read-only research: it never touches
the ledger, the reports or any account.

The live rules (sleeves.py / robust_backtest.swing) are unchanged; this only changes the ENTRY
on days a symbol is NOT already held going into the session:
  * Before the open, rest a buy limit at a price Lim (variants below).
  * Fill if the day's low reaches Lim; fill price = min(open, Lim) (a gap-down open fills at
    the open). The "pessimistic" rows require the low to trade 0.1% THROUGH Lim, because a
    limit resting at the exact low often does not fill.
  * At the close the normal rules decide. Confirmed (the close says hold) -> keep it; the
    position simply started below the close. Not confirmed -> sell at the close (a
    same-day round trip, two extra fees).
  * Leg state is decided by closes exactly as before, so the hold/exit path after the close
    is identical to the tested strategy; only the entry day's P/L differs.
Variants:
  RSI-trigger   Lim = the price at which today's RSI(2) would cross below 10 (solved from
                the prior closes), only if that price is within 5% of yesterday's close and
                above the 200-day SMA ("already close to triggering"). Also at -1% below it.
  pct-k         Lim = yesterday's close x (1 - k), k = 1/2/3/5%, on any not-held symbol
                that closed above its 200-day SMA yesterday.
Self-check: with the limit layer off, the code must reproduce robust_backtest.swing exactly.
Limits: daily bars (no intraday path, but a buy limit needs only the low); fees 1 bp/side;
QLD's intraday move modelled as exactly 2x QQQ; SWING_M uses the same monthly top-10 and the
same equal-weight approximation as mix_optimizer.py.
"""

from __future__ import annotations

import os
import sys
import time
from datetime import datetime
from pathlib import Path

import robust_backtest as rb
from analyze import compute_rsi
from backtest import NDX100_2018, SP100_2018
from combo_backtest import curve_stats
from momentum_sleeves_backtest import adj
from robust_backtest import combine, full_ohlc

HERE = Path(__file__).resolve().parent
FEE = rb.FEE
TOM = (1, 3)


def arrays4(ohlc, a):
    ds = [d for d in sorted(ohlc) if d in a]
    f = [a[d] / ohlc[d][3] for d in ds]
    O = [ohlc[d][0] * x for d, x in zip(ds, f)]
    H = [ohlc[d][1] * x for d, x in zip(ds, f)]
    L = [ohlc[d][2] * x for d, x in zip(ds, f)]
    C = [a[d] for d in ds]
    return ds, O, C, H, L


def rsi_trigger(prior, cut=10):
    """Highest price today at which RSI(2) on prior[-59:] + [px] is < cut, or None."""
    p0 = prior[-1]
    lo, hi = p0 * 0.5, p0
    if (compute_rsi(prior[-59:] + [hi], 2) or 100) < cut:
        return hi
    if (compute_rsi(prior[-59:] + [lo], 2) or 100) >= cut:
        return None
    for _ in range(40):
        mid = (lo + hi) / 2
        if (compute_rsi(prior[-59:] + [mid], 2) or 100) < cut:
            lo = mid
        else:
            hi = mid
    return lo


def limit_price(mode, k, C, i):
    if mode == "rsi":
        p = rsi_trigger(C[i - 59:i])
        if p is None or p < C[i - 1] * 0.95:
            return None
        if p <= (sum(C[i - 199:i]) + p) / 200:           # must still be above the 200-day
            return None
        return p * (1 - k)
    if mode == "pct":
        if C[i - 1] <= sum(C[i - 200:i]) / 200:
            return None
        return C[i - 1] * (1 - k)
    return None


def swing_lim(dates, O, C, H, L, lev=1, cash=None, mode=None, k=0.0, through=0.0, log=None):
    """robust_backtest.swing (default parameters) plus the limit-entry layer. log collects
    one row per limit fill: (date, confirmed, extra return vs the baseline that day)."""
    n = len(dates)
    month_ix = {}
    for i, d in enumerate(dates):
        month_ix.setdefault(d[:7], []).append(i)
    tom_days = set()
    for ix in month_ix.values():
        tom_days |= set(ix[:TOM[1]]) | set(ix[-TOM[0]:])
    held = {"RSI2": False, "IBS": False, "TOM": False}
    age, out, pos = 0, {}, False
    for i in range(201, n):
        d = dates[i]
        r = C[i] / C[i - 1] - 1
        c0 = (cash or {}).get(d, 0.0)
        out[d] = lev * r if pos else c0
        filled, F = False, None
        if not pos and mode:
            lim = limit_price(mode, k, C, i)
            if lim is not None and L[i] <= lim * (1 - through):
                filled, F = True, min(O[i], lim)
                out[d] = lev * (C[i] / F - 1) - FEE * lev
        px = C[i]
        up = px > sum(C[i - 199:i] + [px]) / 200
        r2 = compute_rsi(C[i - 59:i] + [px], 2)
        new = dict(held)
        if held["RSI2"]:
            new["RSI2"] = not (px > sum(C[i - 4:i] + [px]) / 5)
        else:
            new["RSI2"] = r2 is not None and r2 < 10 and up
        rng = H[i] - L[i]
        ibs = (C[i] - L[i]) / rng if rng > 0 else 0.5
        if held["IBS"]:
            age += 1
            new["IBS"] = not (ibs > 0.8 or age >= 5)
        else:
            new["IBS"] = ibs < 0.2 and up
            age = 0
        new["TOM"] = (i + 1) in tom_days
        now = any(new.values())
        if filled:
            if not now:
                out[d] -= FEE * lev                       # sell at the close
            base = c0 - (FEE * lev if now else 0.0)       # what the baseline earned today
            if log is not None:
                log.append((d, now, out[d] - base))
        elif now != pos:
            out[d] -= FEE * lev
        pos = now
        held = new
    return out


VARIANTS = [
    ("Baseline (buy at the close, as tested)", None, 0.0),
    ("RSI-trigger price", "rsi", 0.0),
    ("RSI-trigger price -1%", "rsi", 0.01),
    ("pct: 1% below prior close", "pct", 0.01),
    ("pct: 2% below prior close", "pct", 0.02),
    ("pct: 3% below prior close", "pct", 0.03),
    ("pct: 5% below prior close", "pct", 0.05),
]


def main():
    key = os.environ.get("FMP_API_KEY", "").strip()
    if not key:
        sys.exit("FMP_API_KEY not set")
    pool = sorted(set(SP100_2018) | set(NDX100_2018))
    A = {}
    for n, s in enumerate(pool + ["QQQ", "BIL"]):
        a = adj(s, key)
        if a:
            A[s] = a
        if n % 40 == 0:
            print(f"daily {n}", flush=True)
        time.sleep(0.08)
    qd = sorted(d for d in A["QQQ"] if d in A["BIL"])
    br = {qd[i]: A["BIL"][qd[i]] / A["BIL"][qd[i - 1]] - 1 for i in range(1, len(qd))}
    qr = {qd[i]: A["QQQ"][qd[i]] / A["QQQ"][qd[i - 1]] - 1 for i in range(1, len(qd))}

    # month-end top-10 by 12-month return (identical to mix_optimizer.py)
    me = [qd[k] for k in range(len(qd)) if k == len(qd) - 1 or qd[k][:7] != qd[k + 1][:7]]
    me = [m for m in me if m >= "2018-12-01"]
    picks = {}
    for m in me:
        k = qd.index(m)
        sc = sorted(((A[s][m] / A[s][qd[k - 252]] - 1, s) for s in pool
                     if s in A and m in A[s] and qd[k - 252] in A[s]), reverse=True)
        picks[m] = [s for _, s in sc[:10]]
    ever = sorted({s for v in picks.values() for s in v})

    data = {}
    for s in ever + ["QQQ"]:
        o = full_ohlc(s, key, "2016-06-01")
        if o and s in A:
            ds, O, C, H, L = arrays4(o, A[s])
            if len(ds) > 260:
                data[s] = (ds, O, C, H, L)
        time.sleep(0.05)

    # self-check: limit layer off == the tested function
    rb.FEE = FEE
    for s in ["QQQ"] + ever[:15]:
        if s not in data:
            continue
        ds, O, C, H, L = data[s]
        lev = 2 if s == "QQQ" else 1
        a = rb.swing(ds, C, H, L, None, lev=lev, cash=br)
        b = swing_lim(ds, O, C, H, L, lev=lev, cash=br)
        bad = [d for d in a if abs(a[d] - b[d]) > 1e-12]
        assert not bad, f"self-check failed on {s}: {bad[:3]}"
    print("self-check ok", flush=True)

    tdates = [d for d in qd if d > me[0]]
    start = "2019-01-02"
    pd = [d for d in tdates if d >= start]
    train = [d for d in pd if d <= "2022-12-31"]
    test = [d for d in pd if d >= "2023-01-01"]

    def run(mode, k, through):
        qlog, mlog = [], []
        ds, O, C, H, L = data["QQQ"]
        sq = swing_lim(ds, O, C, H, L, lev=2, cash=br, mode=mode, k=k, through=through, log=qlog)
        sw = {}
        for s in ever:
            if s in data:
                ds, O, C, H, L = data[s]
                lg = []
                sw[s] = swing_lim(ds, O, C, H, L, lev=1, cash=br, mode=mode, k=k, through=through, log=lg)
                sw[s + "#log"] = lg
        sm = {}
        for d in tdates:
            b = picks[[m for m in me if m < d][-1]]
            rs = [sw[s].get(d, 0.0) for s in b if s in sw]
            sm[d] = sum(rs) / len(rs) if rs else 0.0
            for s in b:                                   # only fills in a month the name was a pick
                for row in sw.get(s + "#log", []):
                    if row[0] == d:
                        mlog.append(row)
        qlog = [r for r in qlog if r[0] >= start]
        mlog = [r for r in mlog if r[0] >= start]
        return sq, sm, qlog, mlog

    def cs(ser, dates):
        st, y, _ = curve_stats([ser.get(d, 0.0) for d in dates], dates)
        return st, y

    def fills(lg, years):
        if not lg:
            return "0 fills"
        conf = [x for x in lg if x[1]]
        unc = [x for x in lg if not x[1]]
        avg = lambda xs: sum(x[2] for x in xs) / len(xs) * 1e4 if xs else 0.0
        return (f"{len(lg) / years:.0f}/yr; {len(conf) / len(lg):.0%} confirmed "
                f"(+{avg(conf):.0f} bp each) / {len(unc) / len(lg):.0%} not ({avg(unc):+.0f} bp each); "
                f"net {avg(lg):+.0f} bp per fill")

    years = (datetime.fromisoformat(pd[-1]) - datetime.fromisoformat(pd[0])).days / 365.25
    out = [f"# Limit-entry backtest — run {datetime.utcnow():%Y-%m-%d %H:%MZ}\n",
           f"Period {pd[0]} → {pd[-1]} ({years:.1f} yrs). SWING_Q = QQQ signals at 2x; SWING_M = monthly "
           "top-10 at 1x; MIX = 70/30, monthly rebalance (live split). 1 bp per side. "
           "Self-check passed: with the limit off, the code reproduces the tested sleeve exactly.\n"]
    qs, _ = cs(qr, pd)
    out.append(f"**QQQ buy-and-hold:** {qs['cagr']:.1%}/yr, max DD {qs['mdd']:.1%}.\n")
    hdr = ("| Variant | MIX CAGR / max DD | MIX 2019–22 | MIX 2023–26 | SWING_Q CAGR / DD | SWING_M CAGR / DD |\n"
           "|---|---|---|---|---|---|")
    detail = []
    for title, through in (("Optimistic fills (limit fills if the low touches it)", 0.0),
                           ("Pessimistic fills (the low must trade 0.1% through the limit)", 0.001)):
        out.append(f"\n## {title}\n")
        out.append(hdr)
        for lab, mode, k in VARIANTS:
            if mode is None and through:
                continue
            sq, sm, qlog, mlog = run(mode, k, through)
            mix = dict(zip(pd, combine([0.7, 0.3], [sq, sm], pd)))
            a, _ = cs(mix, pd)
            tr, _ = cs(mix, train)
            te, _ = cs(mix, test)
            b, _ = cs(sq, pd)
            c, _ = cs(sm, pd)
            out.append(f"| {lab} | **{a['cagr']:.1%} / {a['mdd']:.1%}** | {tr['cagr']:.1%} / {tr['mdd']:.0%} | "
                       f"{te['cagr']:.1%} / {te['mdd']:.0%} | {b['cagr']:.1%} / {b['mdd']:.0%} | "
                       f"{c['cagr']:.1%} / {c['mdd']:.0%} |")
            if mode:
                detail.append(f"| {lab} | {'pess.' if through else 'opt.'} | {fills(qlog, years)} | {fills(mlog, years)} |")
            print(out[-1], flush=True)
    out.append("\n## Fill detail (per position, extra return vs buying at the close that day)\n")
    out.append("| Variant | Fills | SWING_Q (QLD, 2x) | SWING_M (per name) |\n|---|---|---|---|")
    out.extend(detail)
    out.append("\n*Confirmed* = the close kept the position (the gain is the entry below the close). "
               "*Not* = the close did not confirm, sold at the close the same day (loss incl. two fees).")
    (HERE / "limit_entry_results.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
