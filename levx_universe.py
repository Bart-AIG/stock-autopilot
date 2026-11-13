"""
Fund universe for the leveraged-ETF sleeve research: every US-listed leveraged LONG equity
fund FMP lists, mapped to its underlying and checked against prices.

  python levx_universe.py        -> data/levx_cache/universe.json  (+ prints a summary)

A fund is kept only if its own daily returns confirm the mapping: beta to the underlying
within 20% of the stated leverage and correlation >= 0.90 over the overlap. That removes
wrong tickers, monthly-reset funds and option-overlay funds without hand curation.
"""

from __future__ import annotations

import json
import re

import numpy as np
import pandas as pd

import levx_data as D

# Index / sector funds: the ETF used as the signal underlying.
INDEX_MAP = {
    "SOXL": "SOXX", "USD": "SOXX", "TQQQ": "QQQ", "QLD": "QQQ", "SPXL": "SPY", "UPRO": "SPY",
    "SSO": "SPY", "SPUU": "SPY", "TNA": "IWM", "URTY": "IWM", "UWM": "IWM", "UDOW": "DIA",
    "DDM": "DIA", "TECL": "XLK", "ROM": "XLK", "FAS": "XLF", "LABU": "XBI", "NAIL": "ITB",
    "DPST": "KRE", "ERX": "XLE", "DIG": "XLE", "YINN": "FXI", "KORU": "EWY", "DFEN": "ITA",
    "DRN": "IYR", "UTSL": "XLU", "CWEB": "KWEB", "EDC": "EEM", "RETL": "XRT", "WEBL": "FDN",
    "HIBL": "SPHB", "BRZU": "EWZ", "CURE": "XLV", "DUSL": "XLI", "WANT": "XLY", "MIDU": "MDY",
    "UMDD": "MDY", "MVV": "MDY", "TPOR": "IYT", "INDL": "INDA", "MEXX": "EWW", "EURL": "VGK",
    "UYG": "XLF", "UXI": "XLI", "UGE": "XLP", "UCC": "XLY", "RXL": "XLV", "UPW": "XLU",
    "URE": "IYR", "UYM": "XLB", "BIB": "IBB", "FNGU": "FNGS", "FNGA": "FNGS", "FNGB": "FNGS",
    "FNGO": "FNGS", "BULZ": "FNGS", "QQQU": "MAGS", "MAGX": "MAGS", "GUSH": "XOP", "NUGT": "GDX",
    "JNUG": "GDXJ", "PILL": "XPH", "OOTO": "PEJ", "CHAU": "ASHR", "XPP": "FXI", "EET": "EEM",
    "EFO": "EFA", "UBR": "EWZ", "EZJ": "EWJ", "UPV": "VGK", "LTL": "XLC", "SAA": "IJR",
    "TSXU": "SOXX", "AIBU": "AIQ", "UBOT": "BOTZ", "FNTC": "FINX", "EVAV": "DRIV", "CLDL": "SKYY",
    "EVEN": "RSP", "URSP": "RSP", "SPYU": "SPY", "XXXX": "SPY", "MQQQ": "QQQ",
}
# Single-stock funds whose names spell the company out instead of the ticker.
NAME_MAP = [
    (r"SpaceX|SPCX", "SPCX"), (r"NVIDIA", "NVDA"), (r"Tesla|\bTsla\b", "TSLA"), (r"Alphabet", "GOOGL"),
    (r"Microsoft", "MSFT"), (r"Apple", "AAPL"), (r"Amazon", "AMZN"), (r"\bMeta\b", "META"),
    (r"SK ?[Hh]ynix|\bSk Hynix", "SKHY"), (r"MicroStrategy|Strategy\b.*MSTR", "MSTR"),
    (r"Coinbase", "COIN"), (r"Palantir", "PLTR"), (r"Netflix", "NFLX"), (r"Broadcom", "AVGO"),
    (r"Robinhood", "HOOD"), (r"Berkshire", "BRK-B"), (r"Samsung", "SMSN"),
]
FIX = {"SK": "SKHY", "BRKB": "BRK-B", "BRK.B": "BRK-B", "B": "B", "GOOG": "GOOGL"}
PAT = [r"2[Xx] Long ([A-Z]{1,5})\b", r"Long ([A-Z]{1,5}) Daily", r"Daily ([A-Z]{1,5}) Bull",
       r"Target 2X Long ([A-Z]{1,5})", r"Corgi ([A-Z]{1,5}) 2x", r"Ultra ([A-Z]{2,5})$",
       r"2x ([A-Z]{2,5}) ", r"Leveraged ([A-Z]{2,5}) "]
NOT_TICKER = {"ETF", "ETN", "ETNS", "DAILY", "LONG", "BULL", "INDEX", "TARGET", "SHARES", "FANG", "MSCI", "FTSE", "CSI", "QQQ"}


def lev_of(name: str):
    m = re.search(r"(\d(?:\.\d+)?)\s?[xX]\b", name)
    if m:
        return float(m.group(1))
    if re.search(r"ultrapro", name, re.I):
        return 3.0
    if re.search(r"ultra", name, re.I):
        return 2.0
    return None


def und_of(sym: str, name: str, desc: str):
    if sym in INDEX_MAP:
        return INDEX_MAP[sym], "index"
    m = re.search(r"\((?:NASDAQ|NYSE|NYSE Arca|NYSE American|AMEX|CBOE|Nasdaq|NasdaqGS|NasdaqGM)\s*:\s*([A-Z][A-Z.\-]*)\)", desc or "")
    if m and m.group(1) not in NOT_TICKER:
        return FIX.get(m.group(1), m.group(1)), "stock"
    for pat, t in NAME_MAP:
        if re.search(pat, name):
            return t, "stock"
    for pat in PAT:
        m = re.search(pat, name)
        if m and m.group(1) not in NOT_TICKER:
            return FIX.get(m.group(1), m.group(1)), "stock"
    return None, None


def build():
    raw = json.loads((D.CACHE / "funds_raw.json").read_text())["prof"]
    rows = []
    for s, v in raw.items():
        if not v or v.get("currency") != "USD":
            continue
        name = v.get("companyName") or ""
        lev = lev_of(name)
        und, kind = und_of(s, name, v.get("description") or "")
        if lev is None or und is None or lev < 1.5 or und == s:
            continue
        rows.append({"fund": s, "name": name, "lev": lev, "und": und, "kind": kind,
                     "active": bool(v.get("isActivelyTrading")), "ipo": v.get("ipoDate")})
    syms = [r["fund"] for r in rows] + [r["und"] for r in rows]
    D.fetch_many(syms)
    out = []
    for r in rows:
        f, u = D.daily(r["fund"]), D.daily(r["und"])
        if f is None or u is None:
            r["ok"], r["why"] = False, "no data"
            out.append(r)
            continue
        j = pd.concat([f["c"].rename("f"), u["c"].rename("u")], axis=1, sort=True).dropna()
        x = j.pct_change().dropna()
        if len(x) < 15:
            r["ok"], r["why"] = False, "overlap < 15 days"
            out.append(r)
            continue
        beta = float(np.cov(x.f, x.u)[0, 1] / np.var(x.u, ddof=1))
        corr = float(x.f.corr(x.u))
        drag = float(-(x.f - r["lev"] * x.u).mean() * 252)
        r.update(first=str(j.index[0].date()), last=str(j.index[-1].date()), n=len(x), beta=round(beta, 3),
                 corr=round(corr, 4), drag=round(drag, 4),
                 dv60=float(f["dv"].iloc[-60:].median()), px=float(f["raw"].iloc[-1]))
        r["ok"] = bool(abs(beta / r["lev"] - 1) <= 0.20 and corr >= 0.90)
        r["why"] = "" if r["ok"] else f"beta {beta:.2f} vs {r['lev']}, corr {corr:.3f}"
        out.append(r)
    (D.CACHE / "universe.json").write_text(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    u = build()
    ok = [r for r in u if r["ok"]]
    print(f"{len(u)} mapped, {len(ok)} confirmed by price; {len({r['und'] for r in ok})} underlyings")
    bad = [r for r in u if not r["ok"]]
    for r in sorted(bad, key=lambda r: r["why"])[:60]:
        print("  dropped", r["fund"], r["und"], r["lev"], "|", r["why"], "|", r["name"][:50])
