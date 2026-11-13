"""
Data layer for the leveraged-ETF sleeve research (levx_*.py). Research tooling only: the
live routine never imports this.

Sources
  Yahoo Finance chart API   daily OHLCV, split + dividend adjusted (adjclose), 2010 -> today
  FMP stable API            ETF list + profiles (fund universe), 5-minute bars 2018 -> today,
                            daily bars for funds Yahoo no longer serves
Everything is cached under data/levx_cache/ (gitignored). Delete a file to refresh it.
"""

from __future__ import annotations

import concurrent.futures as cf
import json
import os
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
CACHE = HERE / "data" / "levx_cache"
FMP = "https://financialmodelingprep.com/stable"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def _get(url: str, headers: dict | None = None, tries: int = 4):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers=headers or {})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503):
                time.sleep(1.5 + 2 * a)
                continue
            return {"_http_error": e.code}
        except Exception as e:  # noqa: BLE001
            if a == tries - 1:
                return {"_error": str(e)}
            time.sleep(1 + a)
    return {"_error": "retries exhausted"}


# ----------------------------------------------------------------------------- daily

def yahoo_raw(sym: str, refresh: bool = False):
    p = CACHE / "daily" / f"{sym}.json"
    if p.exists() and not refresh:
        return json.loads(p.read_text())
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           f"?period1=1104537600&period2={int(time.time())}&interval=1d&events=split,div")
    js = _get(url, {"User-Agent": UA})
    res = (js.get("chart") or {}).get("result") if isinstance(js, dict) else None
    if not res or not res[0].get("timestamp"):
        out = {"_missing": True, "why": str(js)[:200]}
    else:
        out = res[0]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out))
    return out


def fmp_daily_raw(sym: str, refresh: bool = False):
    p = CACHE / "daily_fmp" / f"{sym}.json"
    if p.exists() and not refresh:
        return json.loads(p.read_text())
    key = os.environ.get("FMP_API_KEY", "")
    a = _get(f"{FMP}/historical-price-eod/full?symbol={sym}&from=2005-01-01&to={date.today()}&apikey={key}")
    b = _get(f"{FMP}/historical-price-eod/dividend-adjusted?symbol={sym}&from=2005-01-01&to={date.today()}&apikey={key}")
    out = {"full": a if isinstance(a, list) else [], "adj": b if isinstance(b, list) else []}
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out))
    return out


def daily(sym: str, refresh: bool = False, drop_today_if_open: bool = True) -> pd.DataFrame | None:
    """Adjusted daily OHLCV. Columns: o h l c (all scaled by adjclose/close, so returns
    include splits and dividends and IBS is unchanged), v (shares), raw (unadjusted close),
    dv (dollar volume)."""
    r = yahoo_raw(sym, refresh)
    df = None
    if not r.get("_missing"):
        off = r["meta"].get("gmtoffset", 0)
        q = r["indicators"]["quote"][0]
        adj = r["indicators"]["adjclose"][0]["adjclose"]
        idx = pd.to_datetime([datetime.fromtimestamp(t + off, timezone.utc).date() for t in r["timestamp"]])
        df = pd.DataFrame({"o": q["open"], "h": q["high"], "l": q["low"], "raw": q["close"],
                           "adj": adj, "v": q["volume"]}, index=idx).dropna(subset=["raw", "adj"])
        df = df[~df.index.duplicated(keep="last")]
        # the price actually traded on the day: undo every later split
        fac = pd.Series(1.0, index=df.index)
        for sp in (r.get("events") or {}).get("splits", {}).values():
            d = pd.Timestamp(datetime.fromtimestamp(sp["date"] + off, timezone.utc).date())
            if sp.get("denominator"):
                fac[fac.index < d] *= sp["numerator"] / sp["denominator"]
        df["px"] = df["raw"] * fac
    else:
        f = fmp_daily_raw(sym, refresh)
        if f["full"]:
            a = pd.DataFrame(f["full"]).set_index("date").sort_index()
            a.index = pd.to_datetime(a.index)
            df = pd.DataFrame({"o": a["open"], "h": a["high"], "l": a["low"], "raw": a["close"],
                               "adj": a["close"], "v": a["volume"]})
            if f["adj"]:
                b = pd.DataFrame(f["adj"]).set_index("date").sort_index()
                b.index = pd.to_datetime(b.index)
                df["adj"] = b["adjClose"].reindex(df.index).fillna(df["raw"])
    if df is None or len(df) < 5:
        return None
    df = df[(df["raw"] > 0) & (df["adj"] > 0)]
    f = df["adj"] / df["raw"]
    out = pd.DataFrame({"o": df["o"] * f, "h": df["h"] * f, "l": df["l"] * f, "c": df["adj"],
                        "v": df["v"].fillna(0), "raw": df["raw"],
                        "px": df["px"] if "px" in df else df["raw"]}, index=df.index)
    out["dv"] = out["raw"] * out["v"]
    # repair bars where o/h/l are missing or inconsistent
    for k in ("o", "h", "l"):
        out[k] = out[k].fillna(out["c"])
    out["h"] = out[["h", "c", "o"]].max(axis=1)
    out["l"] = out[["l", "c", "o"]].min(axis=1)
    if drop_today_if_open and len(out):
        now_et = datetime.now(ZoneInfo("America/New_York"))
        if out.index[-1].date() == now_et.date() and (now_et.hour, now_et.minute) < (16, 10):
            out = out.iloc[:-1]
    return out


def fetch_many(syms, fn=yahoo_raw, workers: int = 4):
    syms = [s for s in dict.fromkeys(syms) if s]
    with cf.ThreadPoolExecutor(workers) as ex:
        list(ex.map(fn, syms))


# ----------------------------------------------------------------------------- 5-minute

def fmp_5min(sym: str, start: str = "2018-01-01", refresh: bool = False, workers: int = 4) -> pd.DataFrame | None:
    """Unadjusted 5-minute bars, regular session, as a DataFrame indexed by timestamp (ET,
    naive) with o h l c v. Cached as a pickle; an existing cache is extended to today."""
    p = CACHE / "m5" / f"{sym}.pkl"
    key = os.environ.get("FMP_API_KEY", "")
    old = None
    if p.exists() and not refresh:
        old = pd.read_pickle(p)
        if len(old) and old.index[-1].date() >= date.today() - timedelta(days=1):
            return old
        start = (old.index[-1].date() - timedelta(days=1)).isoformat() if len(old) else start
    d0, end = date.fromisoformat(start), date.today()
    spans = []
    while d0 <= end:
        e = min(d0 + timedelta(days=6), end)
        spans.append((d0, e))
        d0 = e + timedelta(days=1)

    def one(span):
        a, b = span
        r = _get(f"{FMP}/historical-chart/5min?symbol={sym}&from={a}&to={b}&apikey={key}")
        return r if isinstance(r, list) else []

    rows = []
    with cf.ThreadPoolExecutor(workers) as ex:
        for r in ex.map(one, spans):
            rows.extend(r)
    if not rows and old is None:
        return None
    if rows:
        df = pd.DataFrame(rows)
        df["date"] = pd.to_datetime(df["date"])
        df = df.drop_duplicates("date").set_index("date").sort_index()
        df = df.rename(columns={"open": "o", "high": "h", "low": "l", "close": "c", "volume": "v"})[["o", "h", "l", "c", "v"]]
        t = df.index.time
        df = df[(t >= datetime.strptime("09:30", "%H:%M").time()) & (t <= datetime.strptime("15:55", "%H:%M").time())]
        if old is not None and len(old):
            df = pd.concat([old[old.index < df.index[0]], df])
    else:
        df = old
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_pickle(p)
    return df


def split_factor(sym: str) -> pd.Series:
    """Cumulative split factor by date for un-adjusting / adjusting intraday bars:
    adjusted_price = raw_price * factor(date). From Yahoo split events."""
    r = yahoo_raw(sym)
    if r.get("_missing"):
        return pd.Series(dtype=float)
    off = r["meta"].get("gmtoffset", 0)
    ev = sorted(((datetime.fromtimestamp(s["date"] + off, timezone.utc).date(), s["numerator"] / s["denominator"])
                 for s in (r.get("events") or {}).get("splits", {}).values()))
    idx = pd.to_datetime([datetime.fromtimestamp(t + off, timezone.utc).date() for t in r["timestamp"]])
    f = pd.Series(1.0, index=idx)
    for d, ratio in ev:
        f[f.index < pd.Timestamp(d)] /= ratio
    return f


if __name__ == "__main__":
    import sys
    for s in sys.argv[1:]:
        d = daily(s)
        print(s, None if d is None else (len(d), d.index[0].date(), d.index[-1].date(), round(float(d.c.iloc[-1]), 2)))


def fmp_5min_repair(sym: str, workers: int = 3, max_rounds: int = 3) -> tuple[int, int]:
    """Re-fetch sessions that are missing from the 5-minute cache (a throttled request returns
    nothing and leaves a silent hole). Returns (missing before, missing after)."""
    p = CACHE / "m5" / f"{sym}.pkl"
    if not p.exists():
        return (-1, -1)
    key = os.environ.get("FMP_API_KEY", "")
    df = pd.read_pickle(p)
    dly = daily(sym, drop_today_if_open=True)
    if dly is None:
        return (-1, -1)
    want = dly.index[(dly.index >= max(df.index[0].normalize(), pd.Timestamp("2018-01-01")))]

    def missing(d):
        have = set(d.index.normalize().unique())
        cnt = d.groupby(d.index.normalize()).size()
        thin = set(cnt[cnt < 20].index)
        return [x for x in want if x not in have or x in thin]

    m0 = missing(df)
    before = len(m0)
    for _ in range(max_rounds):
        miss = missing(df)
        if not miss:
            break
        spans, cur = [], [miss[0], miss[0]]
        for d in miss[1:]:
            if (d - cur[0]).days <= 6:
                cur[1] = d
            else:
                spans.append(tuple(cur))
                cur = [d, d]
        spans.append(tuple(cur))

        def one(span):
            a, b = span
            r = _get(f"{FMP}/historical-chart/5min?symbol={sym}&from={a.date()}&to={b.date()}&apikey={key}")
            return r if isinstance(r, list) else []

        rows = []
        with cf.ThreadPoolExecutor(workers) as ex:
            for r in ex.map(one, spans):
                rows.extend(r)
        if not rows:
            break
        new = pd.DataFrame(rows)
        new["date"] = pd.to_datetime(new["date"])
        new = new.drop_duplicates("date").set_index("date").sort_index()
        new = new.rename(columns={"open": "o", "high": "h", "low": "l", "close": "c", "volume": "v"})[["o", "h", "l", "c", "v"]]
        t = new.index.time
        new = new[(t >= datetime.strptime("09:30", "%H:%M").time()) & (t <= datetime.strptime("15:55", "%H:%M").time())]
        df = pd.concat([df, new])
        df = df[~df.index.duplicated(keep="last")].sort_index()
    df.to_pickle(p)
    return before, len(missing(df))
