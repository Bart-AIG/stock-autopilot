"""Fetch long daily history for the joint-account leveraged-ETF research (run 2026-11-26).

Runs on the GitHub runner (the only place with FMP access). Writes data/letf/<SYM>.csv with
date, open, high, low, close, adj (dividend-adjusted close when FMP has it, else close).
Read-only research input: touches no ledger, report or account.
"""
from __future__ import annotations

import csv
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, timedelta
from pathlib import Path

FMP = "https://financialmodelingprep.com/stable"
OUT = Path("data/letf")
SYMBOLS = [
    # underlyings
    "QQQ", "SPY", "SOXX", "SMH", "XLK",
    # real leveraged funds (validation of the synthetic series)
    "TQQQ", "QLD", "UPRO", "SSO", "SPXL", "SOXL", "TECL", "USD", "ROM",
    # indexes, for history before the ETFs existed
    "^NDX", "^GSPC", "^SOX",
]


def get(url: str, tries: int = 5):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url), timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(3 * (i + 1))
                continue
            print("HTTP", e.code, url.split("apikey")[0])
            return []
        except Exception as e:  # noqa: BLE001
            if i < tries - 1:
                time.sleep(3 * (i + 1))
                continue
            print("ERR", e, url.split("apikey")[0])
            return []
    return []


def paged(endpoint: str, sym: str, key: str, start: date) -> list[dict]:
    """FMP returns at most ~5,000 rows a call, newest first: walk `to` backwards."""
    rows: dict[str, dict] = {}
    end = date.today()
    for _ in range(12):
        q = urllib.parse.quote(sym)
        js = get(f"{FMP}/{endpoint}?symbol={q}&from={start}&to={end}&apikey={key}")
        if not isinstance(js, list) or not js:
            break
        for r in js:
            rows[r["date"]] = r
        oldest = min(r["date"] for r in js)
        if len(js) < 4000 or date.fromisoformat(oldest) <= start:
            break
        end = date.fromisoformat(oldest) - timedelta(days=1)
        time.sleep(0.4)
    return [rows[d] for d in sorted(rows)]


def main() -> None:
    key = os.environ.get("FMP_API_KEY", "")
    if not key:
        raise SystemExit("FMP_API_KEY missing")
    OUT.mkdir(parents=True, exist_ok=True)
    summary = []
    for sym in SYMBOLS:
        full = paged("historical-price-eod/full", sym, key, date(1985, 1, 1))
        adj = {} if sym.startswith("^") else {
            r["date"]: r.get("adjClose") for r in paged("historical-price-eod/dividend-adjusted", sym, key, date(1985, 1, 1))}
        name = sym.replace("^", "IDX_")
        with open(OUT / f"{name}.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["date", "open", "high", "low", "close", "adj"])
            for r in full:
                a = adj.get(r["date"]) or r["close"]
                w.writerow([r["date"], r.get("open"), r.get("high"), r.get("low"), r["close"], a])
        summary.append(f"{sym}: {len(full)} rows {full[0]['date'] if full else '-'} .. {full[-1]['date'] if full else '-'}, adj {len(adj)}")
        print(summary[-1], flush=True)
        time.sleep(0.5)
    (OUT / "_fetch_log.txt").write_text("\n".join(summary) + "\n")


if __name__ == "__main__":
    main()
