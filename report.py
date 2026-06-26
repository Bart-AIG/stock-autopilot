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
  - This job CANNOT see your Robinhood positions live and CANNOT trade. It flags
    MARKET setups (entries) and reads a committed ledger (holdings.json, maintained
    by the trading session) to flag EXITS on the names you hold. ALL execution and
    the actual sell happen in-session, with your per-order approval.
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
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Reuse the universe + helpers from the momentum tool (single source of truth).
from analyze import (
    AI_COMPLEX, BASE, LOGS, MIN_PRICE, SPECULATIVE, UNIVERSE,
    analyze as momentum_analyze,
    compute_rsi, fmp_fundamentals, fmp_history, load_api_key, theme_of,
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
    # MIN_PRICE gates new ENTRIES only — a held name dropping under $5 must keep
    # producing indicators so the exit engine can still see it.
    is_setup = bool(uptrend and oversold and pullback and price >= MIN_PRICE)

    stop_dist = STOP_SIGMA_MULT * sigma
    stop = round(price * (1 - stop_dist), 2)
    # Revert toward the mean: 1.5R, but capped at the 20-day high — a mean-reversion
    # bounce rarely clears the recent range, and uncapped 1.5R targets on high-sigma
    # names (30%+ away) were never going to be hit before the RSI2/MA5 exits fire.
    hi20 = max(closes[:20])
    target = round(max(ma20, min(price * (1 + 1.5 * stop_dist), hi20)), 2)

    return {
        "symbol": sym,
        "price": round(price, 2),
        "rsi2": rsi2,
        "ma5": round(ma5, 2),
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


HOLDINGS = Path(__file__).resolve().parent / "holdings.json"
JOINT_WATCH = Path(__file__).resolve().parent / "watchlist_joint.json"

# Exit thresholds (mirror the entry rules).
RSI2_OVERBOUGHT = 70.0        # swing take-profit: bounce done (mirror of the <10 entry)
SWING_TIME_STOP_DAYS = 14     # ~10 trading days held without a target -> recycle capital
TRAIL_PCT = 0.15              # trailing-stop distance below the high; a winner is "green
                              # enough" to trail once price >= entry/(1-TRAIL_PCT) (~+17.6%),
                              # so a 15%-below-high stop clears breakeven (set 2026-06-17)


def load_holdings() -> list[dict]:
    """Read the committed positions ledger that the trading session maintains
    (a buy appends, a sell removes). Each position: symbol, sleeve
    (swing|momentum — no 'legacy'; every position is judged each run), entry_date,
    entry_price, shares, stop, target.
    Missing/empty file -> no portfolio review (report still flags entries)."""
    if not HOLDINGS.exists():
        return []
    try:
        blob = json.loads(HOLDINGS.read_text(encoding="utf-8"))
        return blob.get("positions", []) if isinstance(blob, dict) else []
    except (ValueError, AttributeError):
        return []


def load_joint_watch() -> list[str]:
    """WATCH-ONLY list of the JOINT (long-term) account's holdings — kept SEPARATE
    from holdings.json on purpose. The agent can't trade the joint account, so these
    names get COVERAGE (added to the scan) and BUY/ACCUMULATE signals only; they NEVER
    drive the Agentic exit alerts (SELL/TRAIL/THESIS-CHECK) or the ntfy ACTION trigger.
    Missing/empty file -> no joint coverage (the rest of the report is unaffected)."""
    if not JOINT_WATCH.exists():
        return []
    try:
        blob = json.loads(JOINT_WATCH.read_text(encoding="utf-8"))
        return [s for s in blob.get("symbols", []) if s] if isinstance(blob, dict) else []
    except (ValueError, AttributeError):
        return []


def scan_universe() -> list[str]:
    """UNIVERSE plus any AGENTIC-held symbols (so the exit engine always has data for
    every ledger position — a held name that isn't scanned can never fire its exit
    rules) plus the JOINT watch-list names (coverage for the long-term buy screen)."""
    held = {p.get("symbol") for p in load_holdings()}
    joint = set(load_joint_watch())
    return UNIVERSE + sorted(s for s in (held | joint) if s and s not in UNIVERSE)


def evaluate_portfolio(holdings: list[dict], swing_by_sym: dict,
                       momentum_rank: dict, n_decile: int) -> tuple[list[dict], list[str]]:
    """Evaluate EVERY held position and assign a per-name action. No position is parked
    in a 'legacy' bucket — the whole book is judged on each run (BUY/SELL/HOLD style),
    treating the account as an income / grow-the-balance portfolio. Returns (rows, no_data).

    Policy (set 2026-06-17):
      • SELL / TAKE-PROFIT: a name reached its target, or a swing bounce printed
        RSI2>=70 (mean-reversion done). Bank the gain.
      • TRAIL: a winner that has run far enough that a stop 15% below its high clears
        breakeven gets a ratchet-UP trailing stop = max(entry, 0.85*price). Up only — a
        winner can then only ever be sold for a locked-in gain. (Current price proxies the
        running high; the session ratchets the broker stop only when this would raise it.)
      • REVIEW / THESIS-CHECK: below the 200-day MA, or a momentum name out of the top
        decile — a possible thesis break. Research the news; sell only if the thesis is
        dead, otherwise hold to the monthly rebalance.
      • HOLD: in profit but still building a cushion toward a trailing stop; or underwater
        with an intact thesis — NO price stop (thesis-managed, culled at monthly rebalance)."""
    rows, no_data = [], []
    for pos in holdings:
        sym = pos.get("symbol")
        sleeve = pos.get("sleeve") or "momentum"
        s = swing_by_sym.get(sym)
        if not s:
            no_data.append(sym)
            continue
        price = s["price"]
        entry, target, stop = pos.get("entry_price"), pos.get("target"), pos.get("stop")
        native = pos.get("native_trail_pct")  # native (in-app) trailing stop, % trail
        ma200, rsi2 = s.get("ma200"), s.get("rsi2")
        rank = momentum_rank.get(sym)
        pnl = (price - entry) / entry if entry else None

        sell_reasons, review = [], []
        if target and price >= target:
            sell_reasons.append(f"hit target {target} — take profit")
        if sleeve == "swing" and rsi2 is not None and rsi2 >= RSI2_OVERBOUGHT:
            sell_reasons.append(f"RSI2 {rsi2} overbought — swing bounce done, take profit")
        if ma200 and price < ma200:
            review.append(f"below 200-day MA ({ma200}) — possible trend/thesis break")
        if sleeve == "momentum" and rank and rank > n_decile:
            review.append(f"out of top decile (rank {rank}/{n_decile}) — rotate candidate")

        # "Green enough" to trail: the name has run far enough that a TRAIL_PCT-below-high
        # stop clears breakeven (price >= entry / (1-TRAIL_PCT) ≈ +17.6% for 15%). The
        # suggested stop floors at breakeven so a winner can only ever be sold for a gain.
        green_enough = bool(entry and price >= entry / (1 - TRAIL_PCT))
        suggested = round(max(entry, price * (1 - TRAIL_PCT)), 2) if green_enough else None

        if sell_reasons:
            action, note = "SELL / TAKE-PROFIT", sell_reasons + review
        elif native:
            action = "HOLD"
            note = [f"native {native}% trailing stop set in-app — auto-locks the gain "
                    f"({pnl:+.0%})"] + review
        elif review:
            action = "REVIEW / THESIS-CHECK"
            note = review + ["sell only if the thesis is dead; else hold to monthly rebalance"]
        elif green_enough:
            action = f"TRAIL: set {TRAIL_PCT:.0%} native trailing stop in-app"
            note = [f"winner {pnl:+.0%} — GREEN ENOUGH: Ryan sets a {TRAIL_PCT:.0%} NATIVE "
                    f"trailing stop in-app (locks ≥{suggested}). The agent places no stop."] + review
        elif pnl is not None and pnl < 0:
            action = "HOLD (thesis-watch)"
            note = [f"underwater {pnl:+.0%}; no price stop — sell only if the thesis breaks, "
                    f"else cull at monthly rebalance"]
        else:
            action = "HOLD"
            note = [f"{('up '+format(pnl, '+.0%')) if pnl is not None else 'flat'}; "
                    f"building toward the +{(1 / (1 - TRAIL_PCT) - 1):.0%} trailing-stop trigger"]

        rows.append({"symbol": sym, "sleeve": sleeve, "price": price, "entry": entry,
                     "pnl": pnl, "stop": stop, "new_stop": suggested, "native": native,
                     "action": action, "note": "; ".join(note)})
    return rows, no_data



# Long-term accumulation (joint port) thresholds. "Growth on sale" = a confirmed
# long-term uptrend in a name with positive 12-1 momentum, currently pulled back to
# a relative-value entry. PRICE-BASED v1; a fundamental value lens (P/E, P/FCF,
# revenue growth) is the planned fast-follow once the data tier is confirmed.
LT_RSI_VALUE = 45.0      # RSI14 <= this = pulled back enough to be a value entry
LT_MA50_BAND = 1.01      # price at/under 50-day MA * this = "on sale" within the uptrend


def long_term_accumulation(momentum: list[dict], swing_by_sym: dict,
                           joint_held: set, agentic_held: set) -> list[dict]:
    """Buy/accumulate screen for the long-term (joint) port: GROWTH ON SALE.

    Gate (durable growth trend): price above a RISING 200-day MA AND positive 12-1
    momentum — a high-growth name whose long-term trend is intact (not a falling knife).
    Trigger (value entry): pulled back to support — price at/below the 50-day MA, OR
    RSI14 in a moderate value zone (<=45). This surfaces quality growth names currently
    discounted, which is the long-term investor's 'value in high-growth' entry.

    PRICE-BASED only (free-tier data is daily closes). It is NOT a fundamental value
    verdict — confirm each with the news/thesis and a real valuation (FCF, P/E) before buying."""
    rows = []
    for r in momentum:  # momentum rows carry mom_12_1, rsi14, ma50/ma200, above_ma200, close
        sym = r["symbol"]
        mom, rsi14 = r.get("mom_12_1_pct"), r.get("rsi14")
        ma50, price, above200 = r.get("ma50"), r.get("close"), r.get("above_ma200")
        s = swing_by_sym.get(sym)
        rising200 = s["uptrend"] if s else bool(above200)  # price>ma200 AND ma200 rising
        # Durable long-term uptrend in a growth name (positive 12-1 momentum).
        if not (above200 and rising200 and mom is not None and mom > 0):
            continue
        # On sale within the uptrend — pulled back, not extended.
        disc50 = round((price / ma50 - 1) * 100, 1) if ma50 else None
        on_sale = (ma50 and price <= ma50 * LT_MA50_BAND) or (rsi14 is not None and rsi14 <= LT_RSI_VALUE)
        if not on_sale:
            continue
        rows.append({"symbol": sym, "theme": theme_of(sym), "price": price,
                     "mom_12_1_pct": mom, "rsi14": rsi14, "disc_ma50_pct": disc50,
                     "rsi2": s.get("rsi2") if s else None,
                     "held_joint": sym in joint_held, "held_agentic": sym in agentic_held})
    # Strongest growth first; deepest discount to the 50-day breaks ties.
    rows.sort(key=lambda x: (-(x["mom_12_1_pct"] or 0), x["disc_ma50_pct"] if x["disc_ma50_pct"] is not None else 0))
    return rows


# Fundamental VALUE lens (Phase 2). Rough thresholds — a transparent flag, not a model.
# PEG is the PRIMARY read (P/E ÷ growth): ≤1.5 reasonably priced for the growth, >3 rich.
# P/FCF is a FALLBACK only when PEG isn't meaningful (missing, or ≤0 = declining earnings),
# because P/FCF is capex-distorted — e.g. a heavy-capex name (GOOGL) can show a high P/FCF
# while its PEG says it's fairly priced. ≤25 cheap / >45 rich on the fallback.
VALUE_FETCH_CAP = 40   # bound the per-run fundamentals calls (candidate list is small anyway)


def value_verdict(f: dict) -> str:
    """One-word value read from the TTM fundamentals. PEG-primary, P/FCF fallback. '' when no data."""
    if not f:
        return ""
    peg, pfcf = f.get("peg"), f.get("pfcf")
    if peg is not None and peg > 0:          # PEG is the cleaner 'value for growth' signal
        if peg <= 1.5:
            return "✅ value"
        return "⚠️ rich" if peg > 3 else "—"
    if pfcf is not None and pfcf > 0:        # fall back to P/FCF when PEG isn't meaningful
        if pfcf <= 25:
            return "✅ value"
        return "⚠️ rich" if pfcf > 45 else "—"
    return "—"


def build_value_data(momentum: list[dict], swings: list[dict], key: str) -> dict:
    """Fetch the TTM valuation snapshot (P/E, P/FCF, PEG) for the long-term (joint)
    accumulation candidates ONLY — a small set (the names that pass the price gate),
    so the extra fundamentals calls stay tiny. Degrades to {} per name if the data
    tier doesn't expose the endpoint (the screen then runs price-only)."""
    swing_by_sym = {s["symbol"]: s for s in swings}
    joint_held = set(load_joint_watch())
    agentic_held = {p.get("symbol") for p in load_holdings()}
    cands = long_term_accumulation(momentum, swing_by_sym, joint_held, agentic_held)
    out = {}
    for r in cands[:VALUE_FETCH_CAP]:
        f = fmp_fundamentals(r["symbol"], key)
        if f:
            out[r["symbol"]] = f
        time.sleep(0.2)
    return out


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
    _, _, cache = _scan_full_list(key, scan_universe())
    CACHE.write_text(json.dumps({"date": today, "histories": cache}), encoding="utf-8")
    return cache


def scan_intraday(key: str, _unused: list[str]) -> tuple[list[dict], list[dict]]:
    """Afternoon: reuse cached history (or rebuild). Refresh LIVE prices for the
    names nearest a swing trigger (uptrend + RSI2<25) AND every held position —
    exits (stop breaches especially) must be judged on live prices, not the
    morning cache. Starter plan (300 calls/min) absorbs the quote calls easily."""
    cache = _load_fresh_cache(key)
    momentum, base = [], {}
    for sym in scan_universe():
        rows = cache.get(sym)
        if not rows:
            continue
        m = momentum_analyze(sym, rows)
        if m:
            momentum.append(m)
        closes_desc = [r["price"] for r in rows if "price" in r]
        s = connors_swing(sym, closes_desc)
        if s:
            base[sym] = (rows, s)

    held_syms = {p.get("symbol") for p in load_holdings()}
    # Names already in an uptrend and near oversold can flip to an entry trigger
    # intraday; held names always get a live price so exit rules see reality.
    near = {sym for sym, (_, s) in base.items()
            if sym in held_syms
            or (s["uptrend"] and s["rsi2"] is not None and s["rsi2"] < 25)}

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    swings = []
    for sym, (rows, s) in base.items():
        if sym in near:
            live = fmp_quote_price(sym, key)
            time.sleep(0.2)
            if live:
                # Drop today's partial EOD row (if FMP already lists one) so the
                # live overlay doesn't count today twice.
                closes_hist = [r["price"] for r in rows
                               if "price" in r and r.get("date") != today_str]
                s2 = connors_swing(sym, closes_hist, live_price=live)
                if s2:
                    s2["live_overlay"] = True
                    swings.append(s2)
                    continue
        swings.append(s)
    return momentum, swings


def pick_options_candidates(momentum: list[dict], max_each: int = 5) -> dict:
    """From the momentum ranking, pick options-worthy UNDERLYINGS (not contracts).

      CALLS (bullish): strongest uptrends — above the 200-day MA and not already
            extended (RSI14 < 75), taken in momentum-rank order.
      PUTS  (bearish): clear downtrends — below the 200-day MA with weak momentum and
            RSI14 in ~25-55 (rolling over, not already washed out), weakest first.

    These are candidates for the options sleeve (single-leg long calls/puts). This is
    PURELY TECHNICAL and runs in CI with no broker access — the session still picks the
    actual contract off the live chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid) and
    gates each with the news/thesis check. See docs/options-strategy.md."""
    calls, puts = [], []
    for r in momentum:  # already sorted by momentum desc → strongest first
        rsi = r.get("rsi14")
        if r.get("above_ma200") and rsi is not None and rsi < 75 and len(calls) < max_each:
            calls.append({"symbol": r["symbol"], "mom_12_1_pct": r.get("mom_12_1_pct"),
                          "rsi14": rsi, "spec": r["symbol"] in SPECULATIVE})
    for r in sorted(momentum, key=lambda x: x.get("mom_12_1_pct") or 0):  # weakest first
        rsi = r.get("rsi14")
        if r.get("above_ma200") is False and rsi is not None and 25 <= rsi < 55 \
                and len(puts) < max_each:
            puts.append({"symbol": r["symbol"], "mom_12_1_pct": r.get("mom_12_1_pct"),
                         "rsi14": rsi, "spec": r["symbol"] in SPECULATIVE})
    return {"calls": calls, "puts": puts}


def _first_trading_day_of_month(d):
    """First weekday (Mon-Fri) of d's month. Approximates the first trading day —
    it ignores market holidays, which is fine for a reminder nudge (worst case the
    reminder lands a day early when Jan 1 / July 4 etc. fall on the first weekday)."""
    first = d.replace(day=1)
    while first.weekday() >= 5:  # Sat=5, Sun=6
        first += timedelta(days=1)
    return first


def write_report(momentum: list[dict], swings: list[dict], mode: str,
                 value_data: dict | None = None) -> Path:
    value_data = value_data or {}
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

    # --- Portfolio review: judge EVERY held position, assign a per-name action ---
    swing_by_sym = {s["symbol"]: s for s in swings}
    momentum_rank = {r["symbol"]: i for i, r in enumerate(momentum, 1)}
    holdings = load_holdings()
    port, port_no_data = evaluate_portfolio(holdings, swing_by_sym, momentum_rank, n_decile)
    sells = [r for r in port if r["action"].startswith("SELL")]
    trailing = [r for r in port if r["action"].startswith("TRAIL")]
    reviews = [r for r in port if r["action"].startswith("REVIEW")]
    held_syms = {p.get("symbol") for p in holdings}
    rotation = ([r["symbol"] for r in momentum[:n_decile] if r["symbol"] not in held_syms][:8]
                if (sells or reviews) else [])

    # Joint long-term port — buy/accumulate signals only (watch-only; never an exit
    # alert and never part of the ACTION trigger, which stays driven by the Agentic book).
    joint_held = set(load_joint_watch())
    lt_rows = long_term_accumulation(momentum, swing_by_sym, joint_held, held_syms)
    for r in lt_rows:  # attach the fundamental value snapshot (Phase 2) when available
        r["value"] = value_data.get(r["symbol"], {})

    action = ("ACTION" if (setups or sells or trailing)
              else "NO ACTION (swing); momentum is informational")

    lines = []
    lines.append(f"# Strategy report - {mode.upper()}  ({now.strftime('%Y-%m-%d %H:%M UTC')})")
    lines.append(f"\n## >>> {action} <<<\n")

    # Monthly rebalance ritual — fires on the first trading day of the month so the
    # alert itself reminds the session to run the periodic portfolio review (swing +
    # options stay daily/rule-driven; only momentum/concentration/laggard-cull are calendar-based).
    today = now.date()
    if today == _first_trading_day_of_month(today):
        lines.append("## 📅 MONTHLY REBALANCE DUE (first trading day of the month)")
        lines.append("Run the monthly portfolio review alongside today's signals:")
        lines.append("- **Momentum rotate:** re-rank the 12-1 top decile (below); exit held momentum "
                     "names that dropped out of the decile or broke the 200-day MA; weigh the better-play list.")
        lines.append("- **Concentration check:** trim any position over the per-name cap (~15-20%) or the "
                     "speculative sleeve over ~25%; confirm the cash buffer.")
        lines.append("- **Cull the laggards:** this is the moment to sell underwater names whose thesis "
                     "has weakened — they carry no price stop, so the monthly review is their exit gate.")
        if today.month in (1, 4, 7, 10):
            lines.append("- **Quarterly deep review:** re-confirm the thesis on every long-held position "
                         "and re-sleeve (swing/momentum) anything that has drifted.")
        lines.append("")

    # Portfolio review first — managing what we hold (take profit / trail / hold) takes
    # priority over new entries. EVERY position is judged each run; nothing is parked.
    lines.append("## Portfolio review — every position (take-profit / trail / hold)")
    if port:
        lines.append("Each holding is judged on every run. Confirm with a live quote and approve any "
                     "action in-session.\n")
        lines.append("| Ticker | Sleeve | Price | Entry | P/L | Action | Why |")
        lines.append("|---|---|---|---|---|---|---|")
        for r in port:
            pnl = f"{r['pnl']:+.0%}" if r["pnl"] is not None else "—"
            entry = r["entry"] if r["entry"] is not None else "—"
            lines.append(f"| {r['symbol']} | {r['sleeve']} | {r['price']} | {entry} | {pnl} | "
                         f"{r['action']} | {r['note']} |")
        if rotation:
            lines.append(f"\n- 🔄 **Better-play rotation:** top-decile momentum names you don't hold — "
                         f"{', '.join(rotation)}. Fund a new entry by exiting a weak name above.")
    else:
        lines.append("_No holdings ledger yet. The trading session writes `holdings.json` on each fill "
                     "(buy → add, sell → remove); once populated, every position is judged here._")
    if port_no_data:
        lines.append(f"\n_No price data this run for held: {', '.join(s for s in port_no_data if s)} — not evaluated._")
    lines.append("")

    lines.append("## Connors RSI(2) swing setups (1-3 week holds)")
    if setups:
        for s in setups:
            s["theme"] = theme_of(s["symbol"])
            s["speculative"] = s["symbol"] in SPECULATIVE
            s["held"] = s["symbol"] in held_syms
        lines.append("Oversold (RSI2<10) inside a rising 200-day uptrend. Entry/stop/target are ESTIMATES.\n")
        lines.append("| Ticker | Theme | Spec | Held | Price | RSI2 | Entry | Stop | Target | Stop% |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|")
        for s in setups:
            spec = "SPEC" if s["speculative"] else ""
            held = "HELD" if s["held"] else ""
            wide = " ⚠" if abs(s["stop_pct"]) > 15 else ""
            lines.append(f"| {s['symbol']} | {s['theme']} | {spec} | {held} | {s['price']} | {s['rsi2']} | "
                         f"{s['entry']} | {s['stop']} | {s['target']} | {s['stop_pct']}%{wide} |")

        # --- Concentration / correlation / sizing analysis ---
        themes = Counter(s["theme"] for s in setups)
        total = len(setups)
        ai_n = sum(n for th, n in themes.items() if th in AI_COMPLEX)
        spec_n = sum(1 for s in setups if s["speculative"])
        wide_n = sum(1 for s in setups if abs(s["stop_pct"]) > 15)
        # "Other" is the fallback for unmapped tickers, not a real theme — never
        # call it a correlated cluster.
        clusters = Counter({th: n for th, n in themes.items() if th != "Other"})
        lines.append("\n### How to read this (concentration & sizing)")
        held_overlap = [s["symbol"] for s in setups if s["held"]]
        if held_overlap:
            lines.append(f"- 📌 **Already held (marked HELD):** {', '.join(held_overlap)}. A new buy "
                         "ADDS to the existing position — skip unless you mean to add, and re-check "
                         "the per-name cap on the combined size.")
        if ai_n >= max(3, total * 0.5):
            lines.append(f"- 🔴 **Correlated cluster:** {ai_n}/{total} setups are in the AI/tech complex "
                         "(semis, AI-infra, quantum, photonics). They move together — buying several is "
                         "**ONE leveraged AI bet, not diversification.** Pick 1-2, not the cluster.")
        elif clusters and clusters.most_common(1)[0][1] >= 3:
            top_theme, top_cnt = clusters.most_common(1)[0]
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

    # --- Joint long-term port — accumulate signals (watch-only, BUY side only) ---
    lines.append("\n## Joint long-term port — accumulate signals (growth-on-sale)")
    lines.append("Watch-only — the agent can't trade the joint account, so this surfaces BUY/ADD "
                 "ideas ONLY (no exit alerts, not part of the ACTION trigger). Screen: a confirmed "
                 "long-term uptrend (price above a RISING 200-day MA + positive 12-1 momentum) that "
                 "has pulled back to a value entry (≤ 50-day MA, or RSI14 ≤ 45), then graded on a "
                 "TTM **value** lens. **Value** (PEG-primary, P/FCF fallback): ✅ = reasonably priced "
                 "for the growth (PEG ≤ ~1.5, or P/FCF ≤ ~25 when PEG isn't meaningful), ⚠️ = rich "
                 "(PEG > 3 / P/FCF > 45), — = middling, blank = fundamentals not on the data tier.\n")
    if lt_rows:
        adds = [r for r in lt_rows if r["held_joint"]]
        ideas = [r for r in lt_rows if not r["held_joint"] and not r["held_agentic"]][:10]
        hdr = "| Ticker | Theme | Price | 12-1 mom% | RSI14 | vs 50-day | P/E | P/FCF | PEG | Value |"
        sep = "|---|---|---|---|---|---|---|---|---|---|"
        def _fmt(x):
            return f"{x:.1f}" if isinstance(x, (int, float)) else "—"
        def _row(r):
            f = r.get("value") or {}
            d = f"{r['disc_ma50_pct']:+.1f}%" if r["disc_ma50_pct"] is not None else "—"
            return (f"| {r['symbol']} | {r['theme']} | {r['price']} | {r['mom_12_1_pct']} | {r['rsi14']} | {d} | "
                    f"{_fmt(f.get('pe'))} | {_fmt(f.get('pfcf'))} | {_fmt(f.get('peg'))} | {value_verdict(f)} |")
        if adds:
            lines.append("**Held in the joint port — ADD / average-in candidates (on sale within their uptrend):**")
            lines.append(hdr); lines.append(sep)
            lines.extend(_row(r) for r in adds)
        if ideas:
            lines.append("\n**New long-term ideas you don't hold (growth on sale):**")
            lines.append(hdr); lines.append(sep)
            lines.extend(_row(r) for r in ideas)
        if not adds and not ideas:
            lines.append("_Qualifying names this run are all already held in the Agentic book — nothing new for the joint port._")
        lines.append("\n_The price screen + value grade are SIGNALS, not a buy. Confirm each with the "
                     "news/thesis (HARD RULE 7) before buying — a ⚠️-rich name can still be right if the "
                     "growth justifies it, and a ✅-value name can be a value trap if the thesis is broken._")
    else:
        lines.append("_No long-term accumulation signals this run — no qualifying growth name is currently on sale. "
                     "Normal; wait for a pullback._")

    # --- Options candidates (sleeve: options) — underlyings only, acted in-session ---
    opts = pick_options_candidates(momentum)
    lines.append("\n## Options candidates (sleeve: options — single-leg LONG)")
    lines.append("Underlyings only. In-session: pick the contract off the live Robinhood "
                 "chain (~30-45 DTE, ~0.35 delta, IV-sane, liquid), gate with news/thesis, "
                 "≤$150/trade & ≤15% total. See docs/options-strategy.md.\n")
    if opts["calls"]:
        lines.append("**Calls (bullish — strong uptrend > 200MA):**")
        lines.append("| Ticker | mom12-1% | RSI14 | Spec |")
        lines.append("|---|---|---|---|")
        for c in opts["calls"]:
            lines.append(f"| {c['symbol']} | {c['mom_12_1_pct']} | {c['rsi14']} | "
                         f"{'SPEC' if c['spec'] else ''} |")
    if opts["puts"]:
        lines.append("\n**Puts (bearish — downtrend < 200MA):**")
        lines.append("| Ticker | mom12-1% | RSI14 | Spec |")
        lines.append("|---|---|---|---|")
        for p in opts["puts"]:
            lines.append(f"| {p['symbol']} | {p['mom_12_1_pct']} | {p['rsi14']} | "
                         f"{'SPEC' if p['spec'] else ''} |")
    if not opts["calls"] and not opts["puts"]:
        lines.append("_No clean options candidates this run._")

    lines.append("\n---")
    lines.append("_Read-only. No positions checked, no trades placed. Bring this into a session "
                 "to act with live quotes and per-order approval._")

    md_path = LOGS / f"report_{stamp}_{mode}.md"
    md_path.write_text("\n".join(lines), encoding="utf-8")
    (LOGS / f"report_{stamp}_{mode}.json").write_text(
        json.dumps({"mode": mode, "generated_utc": now.isoformat(),
                    "action": action, "swing_setups": setups,
                    "portfolio_review": port, "sell_signals": sells,
                    "trail_signals": trailing, "review_signals": reviews,
                    "rotation_candidates": rotation,
                    "momentum_top": momentum[:n_decile],
                    "joint_accumulation": lt_rows,
                    "options_candidates": opts}, indent=2), encoding="utf-8")
    return md_path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["morning", "intraday"], default="morning")
    ap.add_argument("--limit", type=int, default=0, help="test: only scan first N names")
    args = ap.parse_args()

    key = load_api_key()
    LOGS.mkdir(exist_ok=True)

    # Always include held symbols so the exit engine sees every ledger position.
    universe = scan_universe()[: args.limit] if args.limit else scan_universe()

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
    # Phase 2 value lens: fetch TTM fundamentals for the joint long-term candidates only.
    value_data = build_value_data(momentum, swings, key) if momentum else {}
    path = write_report(momentum, swings, args.mode, value_data)
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
