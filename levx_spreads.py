"""
Sample live bid/ask for the leveraged-fund universe (FMP quote endpoint) and append to
data/levx_cache/spreads.jsonl. Run a few times across a session; levx_backtest.py turns the
samples into its cost model.    python levx_spreads.py [N funds, default 150]
"""
from __future__ import annotations

import concurrent.futures as cf
import json
import os
import sys
import time

import levx_data as D

EXTRA = ["SOXL", "AAOX", "SPCM", "LITX", "COHX", "SPCH", "NVDL", "QLD", "TQQQ", "SOXS", "TSLL", "MUU"]


def main(n=150):
    key = os.environ["FMP_API_KEY"]
    raw = json.loads((D.CACHE / "funds_raw.json").read_text())["prof"]
    ranked = sorted((v for v in raw.values() if v and v.get("isActivelyTrading")),
                    key=lambda v: -(v.get("averageVolume") or 0) * (v.get("price") or 0))
    syms = list(dict.fromkeys(EXTRA + [v["symbol"] for v in ranked[:n]]))

    def one(s):
        r = D._get(f"{D.FMP}/aftermarket-quote?symbol={s}&apikey={key}")
        return r[0] if isinstance(r, list) and r else None

    now = time.time()
    rows = []
    with cf.ThreadPoolExecutor(4) as ex:
        for r in ex.map(one, syms):
            if r and r.get("bidPrice") and r.get("askPrice") and r["askPrice"] > r["bidPrice"] > 0:
                mid = (r["bidPrice"] + r["askPrice"]) / 2
                rows.append({"t": now, "qt": r.get("timestamp"), "sym": r["symbol"], "bid": r["bidPrice"],
                             "ask": r["askPrice"], "bs": r.get("bidSize"), "as": r.get("askSize"),
                             "spr": (r["askPrice"] - r["bidPrice"]) / mid})
    with open(D.CACHE / "spreads.jsonl", "a") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    print(f"{len(rows)} quotes sampled at {time.strftime('%H:%M:%SZ', time.gmtime(now))}")
    return rows


if __name__ == "__main__":
    rows = main(int(sys.argv[1]) if len(sys.argv) > 1 else 150)
    for r in rows[:16]:
        print(f"  {r['sym']:6s} {r['bid']:>9} x {r['ask']:<9} spread {r['spr']*1e4:7.1f} bp  size {r['bs']} x {r['as']}")
