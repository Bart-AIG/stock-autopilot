#!/usr/bin/env python3
"""
capital_backfill.py: rebuild the sleeves' real-money index from the 2026-09-30 close.
One-off research tooling for docs/sleeve-money.md; no routine imports this.

It answers one question: where should capital.py's high-water mark start? Sources:
  positions   holdings.json: _closed_positions and positions, agent-placed stock rows only
  cash        trade_journal.json (and its archives): the last "cash ... $X" in each trading
              day's reconciliation lines written from 19:40Z on
  prices      Yahoo daily closes
Each day:  sleeve money = cash + the agent's positions at the close
           sleeve P/L   = realized P/L of rows closed by that day + unrealized P/L of open rows
           index       *= 1 + (change in sleeve P/L) / (sleeve money at the prior close)

  python3 capital_backfill.py [--through 2026-11-12]
"""

from __future__ import annotations

import collections
import glob
import json
import re
import sys
import time
import urllib.parse
from pathlib import Path

import pandas as pd

import levx_data as L

HERE = Path(__file__).resolve().parent
START = "2026-09-30"


def exit_date(c: dict) -> str | None:
    return c.get("exit_date") or (c.get("exit_utc") or c.get("closed_utc") or "")[:10] or None


def agent_positions(ledger: dict) -> list[dict]:
    pos = []
    for c in ledger["_closed_positions"]:
        ed = exit_date(c)
        if c.get("sleeve") == "options" or c.get("placed_agent") == "user" or not ed or ed < START:
            continue
        real = c.get("realized_pnl") if c.get("realized_pnl") is not None else c.get("realized_pnl_usd")
        pos.append({"sym": c["symbol"], "entry": c["entry_date"], "exit": ed, "ep": float(c["entry_price"]),
                    "sh": float(c.get("shares") or c.get("exit_shares") or c.get("shares_closed")), "real": float(real)})
    for p in ledger["positions"]:
        if p.get("placed_agent") == "user" or p.get("sleeve") == "options":
            continue
        pos.append({"sym": p["symbol"], "entry": p["entry_date"], "exit": None, "ep": float(p["entry_price"]),
                    "sh": float(p["shares"]), "real": 0.0})
    return pos


def closes(sym: str) -> pd.Series:
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}"
           f"?period1=1758000000&period2={int(time.time())}&interval=1d")
    for a in range(4):
        js = L._get(url, {"User-Agent": L.UA})
        if "chart" in js and js["chart"].get("result"):
            break
        time.sleep(3 + 3 * a)
    else:
        raise SystemExit(f"price download failed for {sym}: stopping (no made-up prices)")
    r = js["chart"]["result"][0]
    idx = pd.to_datetime(r["timestamp"], unit="s", utc=True).tz_convert("America/New_York").normalize().tz_localize(None)
    s = pd.Series(r["indicators"]["quote"][0]["close"], index=idx).dropna()
    return s[~s.index.duplicated(keep="last")]


def cash_by_day() -> dict[str, float]:
    entries = []
    for f in [HERE / "trade_journal.json", *sorted(glob.glob(str(HERE / "trade_journal_archive_*.json")))]:
        entries += json.loads(Path(f).read_text())["entries"]
    pat = re.compile(r"cash[^$\d]{0,16}\$\s*([\d,]+(?:\.\d+)?)", re.I)
    by_day = collections.defaultdict(list)
    for e in entries:
        ru = str(e.get("run_utc") or e.get("timestamp_utc") or "")
        r = e.get("reconciliation")
        by_day[ru[:10]].append((ru, r if isinstance(r, str) else json.dumps(r) if r else ""))
    out = {}
    for d, es in by_day.items():
        for ru, txt in sorted(x for x in es if x[0][11:16] >= "19:40"):
            m = pat.search(txt)
            if m:
                out[d] = float(m.group(1).replace(",", ""))
    return out


def main(argv: list[str]) -> int:
    through = argv[argv.index("--through") + 1] if "--through" in argv else "2026-11-12"
    pos = agent_positions(json.loads((HERE / "holdings.json").read_text()))
    px = {s: closes(s) for s in sorted({p["sym"] for p in pos} | {"QQQ"})}
    cash = cash_by_day()
    days = [d for d in px["QQQ"].index if pd.Timestamp(START) <= d <= pd.Timestamp(through)]
    rows = []
    for d in days:
        ds = str(d.date())
        held = [p for p in pos if p["entry"] <= ds and (p["exit"] is None or p["exit"] > ds)]
        val = sum(p["sh"] * float(px[p["sym"]].loc[d]) for p in held)
        unreal = sum(p["sh"] * (float(px[p["sym"]].loc[d]) - p["ep"]) for p in held)
        real = sum(p["real"] for p in pos if p["exit"] and p["exit"] <= ds)
        if ds not in cash:
            raise SystemExit(f"no cash figure in the journal for {ds}: stopping")
        rows.append({"day": ds, "positions": len(held), "sleeve_money": cash[ds] + val, "pnl": real + unreal,
                     "qqq": float(px["QQQ"].loc[d]) / float(px["QQQ"].loc[pd.Timestamp(START)]) - 1})
    df = pd.DataFrame(rows).set_index("day")
    idx = [1.0]
    for i in range(1, len(df)):
        idx.append(idx[-1] * (1 + (df.pnl.iloc[i] - df.pnl.iloc[i - 1]) / df.sleeve_money.iloc[i - 1]))
    df["index"] = idx
    df["drawdown"] = df["index"] / df["index"].cummax() - 1
    df["pnl_since_start"] = df.pnl - df.pnl.iloc[0]
    pd.set_option("display.width", 200)
    pd.set_option("display.max_rows", 200)
    print(df[["positions", "sleeve_money", "pnl_since_start", "index", "drawdown", "qqq"]].round(4).to_string())
    print(json.dumps({"high_water_index": round(float(df["index"].max()), 6), "high_water_day": df["index"].idxmax(),
                      "last_day": df.index[-1], "last_index": round(float(df["index"].iloc[-1]), 6),
                      "last_drawdown_pct": round(100 * float(df.drawdown.iloc[-1]), 2),
                      "month_start_index (last close of the prior month)":
                          round(float(df["index"][df.index < df.index[-1][:8] + "01"].iloc[-1]), 6)}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
