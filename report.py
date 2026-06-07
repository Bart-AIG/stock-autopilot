"""
Twice-daily combined strategy report (read-only, NO trading).

Runs TWO strategies off ONE history pull per name:
  1. 12-1 cross-sectional momentum (multi-week / monthly trend)  -> ranking
  2. Connors-style RSI(2) mean-reversion swing (days to ~2 weeks) -> entry setups

Writes a readable markdown report + json to logs/, headed ACTION or NO ACTION.

Modes:
  morning  : full scan. Fetch daily history (1 call/name), cache it, write report.
  intraday : reuse the morning cache, refresh LIVE prices (FMP quote) for a
             shortlist, recompute the swing trigger on the live price, write report.

IMPORTANT caveats (read these):
  - FMP free 'light' data is daily CLOSE only (no high/low), possibly unadjusted.
    "ATR" is approximated by close-to-close volatility (sigma). Stops/targets are
    estimates, not broker orders.
  - Daily indicators only change after the close. That's why the intraday run
    overlays a LIVE price as a provisional bar - so it can catch dips that develop
    during the day. Names FMP can't quote on the free tier keep their morning value.
  - This job CANNOT see your Robinhood positions and CANNOT trade. It flags MARKET
    setups only. Position-level exits and ALL execution happen in-session, with your
    per-order approval.
"""

from __future__ import annotations

import argparse
import json
import statistics
from collections import Counter
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Reuse the universe + helpers from the momentum tool (single source of truth).
from analyze import (
    AI_COMPLEX, BASE, LOGS, MIN_PRICE, SPECULATIVE, UNIVERSE,
    analyze as momentum_analyze,
    compute_rsi, fmp_history, load_api_key, theme_of,
)

CACHE = LOGS / "history_cache.json"

# Connors swing thresholds.
RSI2_OVERSOLD = 10.0     # buy trigger
STOP_SIGMA_MULT = 2.5    # stop distance = 2.5 * daily sigma (ATR proxy)


def fmp_quote_price(sym: str, key: str) -> float | None:
    """Live last price for the intraday overlay. None on paywall/empty."""
    url = f"{BASE}/quote?symbol={sym}&apikey={key}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        if isinstance(d, list) and d and d[0].get("price"):
            return float(d[0]["price"])
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError):
        return None
    return None


def connors_swing(sym: str, closes_desc: list[float], live_price: float | None = None) -> dict | None:
    """Connors RSI(2) mean-reversion setup. closes_desc is newest-first daily closes."""
    closes = ([live_price] + closes_desc) if live_price else list(closes_desc)
    if len(closes) < 201:
        return None
    price = closes[0]
    if price < MIN_PRICE:
        return None

    ma5 = sum(closes[:5]) / 5
    ma20 = sum(closes[:20]) / 20
    ma50 = sum(closes[:50]) / 50
    ma200 = sum(closes[:200]) / 200
    ma200_prev = sum(closes[20:220]) / 200 if len(closes) >= 220 else ma200
    rsi2 = compute_rsi(list(reversed(closes[:25])), period=2)

    rets = [closes[i] / closes[i + 1] - 1 for i in range(20) if closes[i + 1]]
    sigma = statistics.pstdev(rets) if len(rets) > 1 else 0.0

    uptrend = price > ma200 and ma200 >= ma200_prev   # only mean-revert uptrends
    oversold = rsi2 is not None and rsi2 < RSI2_OVERSOLD
    pullback = price < ma20                            # buying a dip, not a breakout
    is_setup = bool(uptrend and oversold and pullback)

    stop_dist = STOP_SIGMA_MULT * sigma
    stop = round(price * (1 - stop_dist), 2)
    target = round(max(ma20, price * (1 + 1.5 * stop_dist)), 2)  # revert toward the mean

    return {
        "symbol": sym,
        "price": round(price, 2),
        "rsi2": rsi2,
        "ma20": round(ma20, 2),
        "ma50": round(ma50, 2),
        "ma200": round(ma200, 2),
        "uptrend": uptrend,
        "is_setup": is_setup,
        "entry": round(price, 2),
        "stop": stop,
        "target": target,
        "stop_pct": -round(stop_dist * 100, 1),
        "sigma_pct": round(sigma * 100, 1),
    }


def _load_fresh_cache(key: str) -> dict:
    """Return today's cached histories, rebuilding via a full scan if missing/stale."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if CACHE.exists():
        try:
            blob = json.loads(CACHE.read_text(encoding="utf-8"))
            if blob.get("date") == today and blob.get("histories"):
                return blob["histories"]
        except (ValueError, AttributeError):
            pass
    print("  no fresh morning cache - rebuilding with a full scan...")
    _, _, cache = _scan_full_list(key, UNIVERSE)
    CACHE.write_text(json.dumps({"date": today, "histories": cache}), encoding="utf-8")
    return cache


def scan_intraday(key: str, _unused: list[str]) -> tuple[list[dict], list[dict]]:
    """Afternoon: reuse cached history (or rebuild). Refresh LIVE prices only for the
    ~20 names nearest a swing trigger (uptrend + RSI2<25), to stay under the API cap."""
    cache = _load_fresh_cache(key)
    momentum, base = [], {}
    for sym in UNIVERSE:
        rows = cache.get(sym)
        if not rows:
            continue
        m = momentum_analyze(sym, rows)
        if m:
            momentum.append(m)
        closes_desc = [r["price"] for r in rows if "price" in r]
        s = connors_swing(sym, closes_desc)
        if s:
            base[sym] = (closes_desc, s)

    # Only names already in an uptrend and near oversold can flip to a trigger intraday.
    near = [sym for sym, (_, s) in base.items()
            if s["uptrend"] and s["rsi2"] is not None and s["rsi2"] < 25][:20]

    swings = []
    for sym, (closes_desc, s) in base.items():
        if sym in near:
            live = fmp_quote_price(sym, key)
            time.sleep(0.2)
            if live:
                s2 = connors_swing(sym, closes_desc, live_price=live)
                if s2:
                    s2["live_overlay"] = True
                    swings.append(s2)
                    continue
        swings.append(s)
    return momentum, swings


def write_report(momentum: list[dict], swings: list[dict], mode: str) -> Path:
    momentum.sort(key=lambda r: r["mom_12_1_pct"], reverse=True)
    n_decile = max(1, int(len(momentum) * 0.10))
    setups = [s for s in swings if s["is_setup"]]
    setups.sort(key=lambda s: (s["rsi2"] if s["rsi2"] is not None else 99))
    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y-%m-%d_%H%M")

    # DATA-INTEGRITY GUARD: a real day ALWAYS ranks the universe (~200 names). Zero
    # resolved names means the data fetch FAILED (blocked host / network allowlist /
    # bad-or-missing FMP_API_KEY / outage) - NOT a quiet no-trade day. Scream, don't whisper.
    if len(momentum) == 0:
        msg = (f"# Strategy report - {mode.upper()}  ({now.strftime('%Y-%m-%d %H:%M UTC')})\n\n"
               "## >>> DATA ERROR <<<\n\n"
               "Zero names resolved - the data fetch FAILED. Likely causes: the host "
               "financialmodelingprep.com is not in this environment's network allowlist, "
               "a missing/invalid FMP_API_KEY, or an FMP outage.\n\n"
               "**This is NOT a no-trade day. The report is INVALID. Do NOT propose or place "
               "any trades off it.**\n")
        md_path = LOGS / f"report_{stamp}_{mode}.md"
        md_path.write_text(msg, encoding="utf-8")
        (LOGS / f"report_{stamp}_{mode}.json").write_text(json.dumps(
            {"mode": mode, "generated_utc": now.isoformat(), "action": "DATA ERROR",
             "error": "zero names resolved - data fetch failed"}, indent=2), encoding="utf-8")
        print("!!! DATA ERROR: 0 names resolved - data fetch failed. Report INVALID.")
        return md_path

    action = "ACTION" if setups else "NO ACTION (swing); momentum is informational"

    lines = []
    lines.append(f"# Strategy report - {mode.upper()}  ({now.strftime('%Y-%m-%d %H:%M UTC')})")
    lines.append(f"\n## >>> {action} <<<\n")

    lines.append("## Connors RSI(2) swing setups (1-3 week holds)")
    if setups:
        for s in setups:
            s["theme"] = theme_of(s["symbol"])
            s["speculative"] = s["symbol"] in SPECULATIVE
        lines.append("Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.\n")
        lines.append("| Ticker | Theme | Spec | Price | RSI2 | Entry | Stop | Target | Stop% |")
        lines.append("|---|---|---|---|---|---|---|---|---|")
        for s in setups:
            spec = "SPEC" if s["speculative"] else ""
            wide = " ⚠" if abs(s["stop_pct"]) > 15 else ""
            lines.append(f"| {s['symbol']} | {s['theme']} | {spec} | {s['price']} | {s['rsi2']} | "
                         f"{s['entry']} | {s['stop']} | {s['target']} | {s['stop_pct']}%{wide} |")

        # --- Concentration / correlation / sizing analysis ---
        themes = Counter(s["theme"] for s in setups)
        total = len(setups)
        ai_n = sum(n for th, n in themes.items() if th in AI_COMPLEX)
        spec_n = sum(1 for s in setups if s["speculative"])
        wide_n = sum(1 for s in setups if abs(s["stop_pct"]) > 15)
        top_theme, top_cnt = themes.most_common(1)[0]
        lines.append("\n### How to read this (concentration & sizing)")
        if ai_n >= max(3, total * 0.5):
            lines.append(f"- 🔴 **Correlated cluster:** {ai_n}/{total} setups are in the AI/tech complex "
                         "(semis, AI-infra, quantum, photonics). They move together — buying several is "
                         "**ONE leveraged AI bet, not diversification.** Pick 1-2, not the cluster.")
        elif top_cnt >= 3:
            lines.append(f"- 🟡 **Cluster:** {top_cnt}/{total} setups are '{top_theme}' — correlated, don't buy them all.")
        if spec_n:
            lines.append(f"- ⚠️ **{spec_n}/{total} are speculative** (high-vol). Size tiny; keep TOTAL speculative "
                         "exposure ≤ ~20-25% of the account.")
        if wide_n:
            lines.append(f"- ⚠️ **{wide_n} have stops wider than 15%** (marked ⚠) — extreme volatility. Size so the "
                         "dollar-risk-to-stop is small, not the dollar position.")
        lines.append("- ✅ **Discipline:** take the 1-2 highest-conviction, least-correlated names. Per-name cap "
                     "~15-20%, and set the stop on every entry.")
    else:
        lines.append("No swing setups today (nothing oversold inside an uptrend). Hold / wait — a 'no-trade' day is normal and correct.")

    lines.append(f"\n## 12-1 momentum ranking (top decile = {n_decile} of {len(momentum)})")
    lines.append("Multi-week / monthly trend holds. Rebalance on a monthly cadence, not daily.\n")
    lines.append("| # | Ticker | mom12-1% | RSI14 | >200MA |")
    lines.append("|---|---|---|---|---|")
    for rank, r in enumerate(momentum[:n_decile + 5], 1):
        flag = "**TOP**" if rank <= n_decile else ""
        lines.append(f"| {rank} {flag} | {r['symbol']} | {r['mom_12_1_pct']} | {r['rsi14']} | "
                     f"{str(r.get('above_ma200'))[0]} |")

    lines.append("\n---")
    lines.append("_Read-only. No positions checked, no trades placed. Bring this into a session "
                 "to act with live quotes and per-order approval._")

    md_path = LOGS / f"report_{stamp}_{mode}.md"
    md_path.write_text("\n".join(lines), encoding="utf-8")
    (LOGS / f"report_{stamp}_{mode}.json").write_text(
        json.dumps({"mode": mode, "generated_utc": now.isoformat(),
                    "action": action, "swing_setups": setups,
                    "momentum_top": momentum[:n_decile]}, indent=2), encoding="utf-8")
    return md_path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["morning", "intraday"], default="morning")
    ap.add_argument("--limit", type=int, default=0, help="test: only scan first N names")
    args = ap.parse_args()

    key = load_api_key()
    LOGS.mkdir(exist_ok=True)

    universe = UNIVERSE[: args.limit] if args.limit else UNIVERSE

    print(f"Combined report - mode={args.mode}, {len(universe)} names")
    if args.mode == "morning":
        # temporarily scan the (possibly limited) universe
        momentum, swings, cache = _scan_full_list(key, universe)
        if not args.limit:
            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            CACHE.write_text(json.dumps({"date": today, "histories": cache}), encoding="utf-8")
            print(f"  cached {len(cache)} histories")
        else:
            print("  (limited test, no cache)")
    else:
        shortlist = universe  # refresh live for all (intraday quote calls)
        momentum, swings = scan_intraday(key, shortlist)

    setups = [s for s in swings if s["is_setup"]]
    path = write_report(momentum, swings, args.mode)
    print(f"\nRanked {len(momentum)} momentum, found {len(setups)} swing setup(s).")
    print(f"Wrote {path}")
    print("NOTE: read-only. No trades placed. No Robinhood access.")


def _scan_full_list(key: str, names: list[str]):
    momentum, swings, cache = [], [], {}
    for i, sym in enumerate(names, 1):
        rows = fmp_history(sym, key)
        if rows is None:
            continue
        cache[sym] = rows
        m = momentum_analyze(sym, rows)
        if m:
            momentum.append(m)
        closes_desc = [r["price"] for r in rows if "price" in r]
        s = connors_swing(sym, closes_desc)
        if s:
            swings.append(s)
        if i % 25 == 0:
            print(f"  {i}/{len(names)} scanned...")
        time.sleep(0.2)
    return momentum, swings, cache


if __name__ == "__main__":
    main()
