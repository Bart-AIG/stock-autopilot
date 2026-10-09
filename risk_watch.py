"""
Joint-account RISK WATCH: grade market risk from Ryan's Robinhood benchmark alerts and
turn the grade into SELL recommendations for the joint (long-term) account.

Set 2026-09-25 (Ryan, live turn: "I set up alerts in robinhood based on a few bench
marks. I want to make sure as they hit they grade current risk and i get
recommendations on sells from my joint account.").

ADVISORY ONLY. The agent cannot trade the joint account; every recommendation is placed
by Ryan in-app. Pure functions, no network: the "Joint risk watch" routine
(docs/joint-risk-watch-prompt.md) feeds it live alerts, quotes and positions.

Why grade EVERY run instead of only when an alert fires: a Robinhood alert fires ONCE,
but the condition it describes (SPY under its 50-day, credit spreads widening) persists.
Grading the live readings each run keeps the tier honest after the one-shot alert is gone.
"""

from __future__ import annotations

import json
from pathlib import Path

# What each benchmark MEANS and how much it weighs. Keyed by (symbol, condition_type).
# Weights: 1 = early warning, 2 = real stress, 3 = regime break. Unknown alerts count 1.
SIGNALS = {
    ("SPY", "price_below_sma"): (1, "SPY closed under its 50-day: trend damage, early warning"),
    ("SPY", "price_below"):     (2, "SPY broke a price level"),     # 729 ~ -5%; 690 handled below
    ("QQQ", "price_below"):     (2, "QQQ broke its level: tech/growth de-rating (joint book is ~50% tech)"),
    ("QQQ", "price_below_sma"): (1, "QQQ under a daily SMA (20 or 50): tech trend damage, early warning"),
    ("HYG", "price_below"):     (2, "High-yield credit selling off: credit stress leads equities"),
    ("KRE", "price_below"):     (2, "Regional banks breaking: funding/credit stress"),
    ("VIXY", "price_above"):    (2, "Volatility spiking: forced de-risking in the market"),
    ("USO", "price_above"):     (1, "Oil spike: inflation/geopolitical shock risk"),
    ("IEF", "price_below"):     (1, "Treasuries falling / yields rising: valuation pressure on growth"),
    ("IEF", "price_above"):     (1, "Flight to safety into Treasuries: risk-off rotation"),
    ("TIP", "price_below"):     (1, "Real yields rising: pressure on long-duration growth stocks"),
}
# Deeper levels on the same symbol add weight (a regime break, not just a warning).
DEEP_LEVEL_BONUS = {("SPY", "price_below"): (700.0, 1),   # below ~700 = -9%+: +1 more
                    ("IEF", "price_below"): (88.0, 1)}    # 87.35 alert = rates really moving

# QQQ price levels are a LADDER (set 2026-09-28 with the de-risk plan, joint_derisk_plan.json):
# a shallow level is worth less than a deep one, so a single flat weight mis-scores it.
# (level_at_or_above, points), checked top-down: 733 range-top break = 1, 700 range-floor /
# trend break = 2, 666 200-day / July-low = 3. Cumulative with the 20/50-day SMA alerts:
# <733 -> 1 GREEN, <20d -> 2 YELLOW, <50d -> 3 YELLOW, <700 -> 5 ORANGE, <666 -> 8 RED.
LEVEL_WEIGHTS = {("QQQ", "price_below"): [(720.0, 1), (690.0, 2), (0.0, 3)]}

TIERS = [(0, "GREEN"), (2, "YELLOW"), (4, "ORANGE"), (7, "RED")]

# Joint-account policy inputs (CLAUDE.md, 2026-08-05 de-risk + 2026-07-29 mandate).
CORE = {"MSFT", "GOOGL", "AMZN", "META", "NOW", "ADBE", "ZTS", "ISRG", "RBRK", "V", "JPM", "QQQI"}
HIGH_BETA = {"MU", "AMD", "MRVL", "CRDO", "NVDA", "APP", "HOOD", "CRCL", "TEM", "FIG",
             "BMEA", "VST", "CEG", "UBER"}
SEMIS = {"MU", "AMD", "NVDA", "MRVL", "CRDO", "APH"}

NAME_CAP = {"YELLOW": None, "ORANGE": 0.12, "RED": 0.10}     # max single non-core weight
CORE_CAP = {"YELLOW": None, "ORANGE": 0.15, "RED": 0.12}     # core names trimmed less
SEMIS_CAP = {"YELLOW": None, "ORANGE": 0.30, "RED": 0.22}    # semis cluster
CASH_TARGET = {"YELLOW": 0.0, "ORANGE": 0.05, "RED": 0.15}   # of net account value; margin always to 0


def _is_triggered(a: dict, price: float | None, sma: float | None) -> bool:
    ct = a["condition_type"]
    if price is None:
        return False
    if ct == "price_below_sma":
        return sma is not None and price < sma
    if ct == "price_above_sma":
        return sma is not None and price > sma
    tgt = float(a["condition"].get("target_price") or 0)
    if ct == "price_below":
        return price < tgt
    if ct == "price_above":
        return price > tgt
    return False


def sma_period(a: dict) -> int:
    """Period of an *_sma alert (Robinhood: condition.indicator.period); 50 if absent."""
    ind = (a.get("condition") or {}).get("indicator") or {}
    try:
        return int(ind.get("period") or 50)
    except (TypeError, ValueError):
        return 50


def _sma_for(smas: dict, sym: str, period: int) -> float | None:
    """smas may be keyed {(sym, period): v} (preferred) or legacy {sym: 50d value}.
    A legacy key is only trusted for the 50-day: it must never stand in for a 20-day."""
    if (sym, period) in smas:
        return smas[(sym, period)]
    if f"{sym}:{period}" in smas:
        return smas[f"{sym}:{period}"]
    return smas.get(sym) if period == 50 else None


def quality_watch_alert_ids(path: str | Path | None = None) -> set[str]:
    """alert_ids the Quality @ 200-day routine created (quality_watch_state.json).
    Those are per-stock buy-watch alerts, not market-risk benchmarks, and must never
    score risk points (set 2026-09-30: unknown alerts count 1 each, so three of them
    triggering would have pushed the tier to YELLOW on their own)."""
    p = Path(path) if path else Path(__file__).with_name("quality_watch_state.json")
    try:
        managed = json.loads(p.read_text()).get("managed_alerts") or {}
    except (OSError, ValueError):
        return set()
    return {m.get("alert_id") for m in managed.values() if m.get("alert_id")}


def rebuy_watch_alert_ids(path: str | Path | None = None) -> set[str]:
    """alert_ids of the joint re-buy watch (rebuy_watch.json, set 2026-10-08): buy-back
    signals on names Ryan sold, not market-risk benchmarks, so they never score points."""
    p = Path(path) if path else Path(__file__).with_name("rebuy_watch.json")
    try:
        names = json.loads(p.read_text()).get("names") or {}
    except (OSError, ValueError):
        return set()
    return {a.get("alert_id") for e in names.values()
            for a in (e.get("alerts") or {}).values() if a.get("alert_id")}


def holding_support_alert_ids(path: str | Path | None = None) -> set[str]:
    """alert_ids of the per-holding support alerts on the joint account
    (joint_support_alerts.json, set 2026-10-06). Like the Quality @ 200-day alerts they
    are per-stock price alerts, not market-risk benchmarks, so they never score points."""
    p = Path(path) if path else Path(__file__).with_name("joint_support_alerts.json")
    try:
        alerts = json.loads(p.read_text()).get("alerts") or {}
    except (OSError, ValueError):
        return set()
    return {a.get("alert_id") for a in alerts.values() if a.get("alert_id")}


def option_watch_alert_ids(path: str | Path | None = None) -> set[str]:
    """alert_ids on a monitored option position's underlying (holdings.json, each
    position's `_alerts`; first used 2026-10-09 for Ryan's MU 2026-11-20 1160C). They are
    per-position exit alerts, not market-risk benchmarks, so they never score points."""
    p = Path(path) if path else Path(__file__).with_name("holdings.json")
    try:
        positions = json.loads(p.read_text()).get("positions") or []
    except (OSError, ValueError):
        return set()
    return {a.get("alert_id") for pos in positions
            for a in (pos.get("_alerts") or {}).values() if a.get("alert_id")}


def grade(alerts: list[dict], prices: dict[str, float], smas: dict | None = None,
          ignore_ids: set[str] | None = None) -> dict:
    """alerts = get_alerts()['alerts'] (enabled ones); prices = {sym: last};
    smas = {(sym, period): value} for every *_sma alert (e.g. ("QQQ", 20), ("QQQ", 50)).
    ignore_ids: alert_ids to skip; defaults to the Quality @ 200-day routine's alerts, the
    joint per-holding support alerts, the joint re-buy watch alerts and the
    monitored option positions' exit alerts.
    Returns score, tier, and a per-alert breakdown including distance to trigger."""
    smas = smas or {}
    if ignore_ids is None:
        ignore = (quality_watch_alert_ids() | holding_support_alert_ids()
                  | rebuy_watch_alert_ids() | option_watch_alert_ids())
    else:
        ignore = ignore_ids
    rows, score = [], 0
    for a in alerts:
        if not a.get("enabled", True) or a.get("alert_id") in ignore:
            continue
        sym, ct = a["symbol"], a["condition_type"]
        is_sma = ct.endswith("_sma")
        period = sma_period(a) if is_sma else None
        price = prices.get(sym)
        sma = _sma_for(smas, sym, period) if is_sma else None
        weight, meaning = SIGNALS.get((sym, ct), (1, "custom alert"))
        tgt = sma if is_sma else float(a["condition"].get("target_price") or 0)
        ladder = LEVEL_WEIGHTS.get((sym, ct))
        if ladder and tgt:
            weight = next(p for floor, p in ladder if tgt >= floor)
        hit = _is_triggered(a, price, sma)
        pts = 0
        if hit:
            pts = weight
            bonus = DEEP_LEVEL_BONUS.get((sym, ct))
            if bonus and tgt <= bonus[0]:
                pts += bonus[1]
        score += pts
        dist = (price / tgt - 1) * 100 if (price and tgt) else None
        cond = f"{ct}_{period}d" if is_sma else ct
        rows.append({"symbol": sym, "condition": cond, "level": round(tgt, 2) if tgt else None,
                     "price": price, "distance_pct": round(dist, 2) if dist is not None else None,
                     "triggered": hit, "points": pts, "meaning": meaning})
    tier = [name for floor, name in TIERS if score >= floor][-1]
    rows.sort(key=lambda r: (not r["triggered"], abs(r["distance_pct"] or 999)))
    return {"score": score, "tier": tier, "readings": rows}


def derisk_stage(plan: dict, qqq_price: float, sma20: float | None, sma50: float | None) -> dict:
    """Deepest de-risk stage and reinvest tranche QQQ has reached, from joint_derisk_plan.json.
    Levels are live: 'sma20'/'sma50' resolve to today's values, numbers are fixed prices.
    Stages are cumulative: reaching stage 3 means stages 1-3 all apply."""
    def lvl(x):
        return {"sma20": sma20, "sma50": sma50}.get(x, x) if isinstance(x, str) else x
    hit = [s for s in plan["derisk_stages"] if lvl(s["qqq_below"]) and qqq_price < lvl(s["qqq_below"])]
    buy = [t for t in plan["reinvest_tranches"] if qqq_price < t["qqq_below"]]
    return {"derisk_stage": hit[-1]["stage"] if hit else 0,
            "derisk_names": [s["name"] for s in hit],
            "reinvest_tranche": buy[-1]["tranche"] if buy else 0,
            "levels": {s["stage"]: lvl(s["qqq_below"]) for s in plan["derisk_stages"]}}


def _yoy(fin: list[dict], i: int, key: str = "revenue") -> float | None:
    """Year-over-year change of fin[i][key] vs the same fiscal quarter a year earlier.
    Matched by (fiscal_year-1, fiscal_quarter), NOT by list offset: the feed skips
    quarters (CRCL had no FY25 Q4 row on 2026-09-28), so fin[i+4] can be the wrong one."""
    if i >= len(fin):
        return None
    cur = fin[i]
    prior = next((f for f in fin if f.get("fiscal_quarter") == cur.get("fiscal_quarter")
                  and f.get("fiscal_year") == (cur.get("fiscal_year") or 0) - 1), None)
    try:
        a, b = float(cur[key]), float(prior[key])
    except (TypeError, ValueError, KeyError):
        return None
    return (a / b - 1) if b > 0 else None


def holding_health(price: float, closes_desc: list[float], fin: list[dict] | None = None) -> dict:
    """Per-holding health check for the JOINT account (set 2026-09-25, Ryan: "add something
    that helps monitor the stocks in the joint risk monitor"). Two halves:
      PRICE TREND (daily closes, newest first): under the 50-day (1), under the 200-day (2),
        20%+ off the 1-year closing high (1; 30%+ = 2).
      BUSINESS TREND (get_financials quarterly rows, newest first): latest quarter's revenue
        DOWN year-over-year (2); revenue growth slowing two quarters running (1); net margin
        down 5+ points year-over-year (1).
    OK 0-1 / WATCH 2-3 / WEAK 4+. A WEAK name is the first sale when market risk rises and
    a review item even at GREEN. Missing data scores nothing - it never invents a flag."""
    flags, pts = [], 0
    c = [x for x in closes_desc if x]
    if len(c) >= 50 and price < sum(c[:50]) / 50:
        flags.append("under 50-day"); pts += 1
    if len(c) >= 200 and price < sum(c[:200]) / 200:
        flags.append("under 200-day"); pts += 2
    if c:
        dd = price / max(c[:252]) - 1
        if dd <= -0.30:
            flags.append(f"{dd:.0%} off 1-yr high"); pts += 2
        elif dd <= -0.20:
            flags.append(f"{dd:.0%} off 1-yr high"); pts += 1
    if fin:
        g0, g1, g2 = _yoy(fin, 0), _yoy(fin, 1), _yoy(fin, 2)
        if g0 is not None and g0 < 0:
            flags.append(f"revenue {g0:+.0%} YoY"); pts += 2
        elif None not in (g0, g1, g2) and g0 < g1 < g2:
            flags.append(f"revenue growth slowing {g2:+.0%} -> {g1:+.0%} -> {g0:+.0%}"); pts += 1
        try:
            m0 = float(fin[0]["net_margin"])
            prior = next(f for f in fin if f.get("fiscal_quarter") == fin[0].get("fiscal_quarter")
                         and f.get("fiscal_year") == (fin[0].get("fiscal_year") or 0) - 1)
            m1 = float(prior["net_margin"])
            if m0 - m1 <= -5:
                flags.append(f"net margin {m1:.0f}% -> {m0:.0f}%"); pts += 1
        except (StopIteration, TypeError, ValueError, KeyError, IndexError):
            pass
    status = "WEAK" if pts >= 4 else ("WATCH" if pts >= 2 else "OK")
    return {"status": status, "points": pts, "flags": flags}


def sell_plan(tier: str, positions: list[dict], cash: float, total_value: float,
              health: dict[str, dict] | None = None) -> dict:
    """positions = [{symbol, qty, price, cost}] for the JOINT account.
    Returns the dollars to raise and a ranked list of sell recommendations.
    Order of preference, cheapest-to-the-thesis first:
      1. clear any MARGIN balance (Ryan de-levered this account 2026-08-05 and rejected
         re-margining; borrowed money is the first thing a drawdown punishes)
      2. tax-loss names that are not core (harvest the loss, remove weak holdings)
      3. trim concentration: single names over the tier cap, then the semis cluster
      4. RED only: high-beta non-core names to reach the cash target
    Core names are trimmed for concentration only, never sold out."""
    health = health or {}
    weak = [s for s, h in health.items() if h.get("status") == "WEAK"]
    if tier == "GREEN":
        m = max(0.0, -cash)
        return {"raise_usd": 0.0, "margin_usd": round(m), "recs": [],
                "review": [{"symbol": s, "flags": health[s]["flags"]} for s in weak],
                "note": (f"No risk action. NOTE: ${m:,.0f} of margin is in use, against the "
                         f"2026-08-05 decision to keep this account unlevered." if m
                         else "No action. Keep watching.")}
    eq = sum(p["qty"] * p["price"] for p in positions)
    val = {p["symbol"]: p["qty"] * p["price"] for p in positions}
    margin = max(0.0, -cash)
    need = margin + CASH_TARGET[tier] * max(total_value, 0)
    recs, raised = [], 0.0
    sold = {s: 0.0 for s in val}

    def add(sym, usd, why):
        nonlocal raised
        usd = min(usd, val[sym] - sold[sym])
        if usd < 25:
            return
        sold[sym] += usd
        raised += usd
        p = next(x for x in positions if x["symbol"] == sym)
        gain = (p["price"] / p["cost"] - 1) if p.get("cost") else None
        recs.append({"symbol": sym, "sell_usd": round(usd), "pct_of_position": round(usd / val[sym] * 100),
                     "unrealized_pct": round(gain * 100, 1) if gain is not None else None,
                     "tax": ("LOSS - harvest; check 30-day wash-sale" if gain is not None and gain < 0
                             else "GAIN - check lot holding period (short vs long-term)"),
                     "why": why})

    # 3. concentration first computes the trims we'd want anyway
    if NAME_CAP[tier]:
        for s, v in sorted(val.items(), key=lambda kv: -kv[1]):
            cap = CORE_CAP[tier] if s in CORE else NAME_CAP[tier]
            if v / eq > cap:
                add(s, v - cap * eq, f"{v/eq:.0%} of the book, over the {cap:.0%} {tier} cap")
        semis_v = sum(val[s] - sold[s] for s in val if s in SEMIS)
        if semis_v / eq > SEMIS_CAP[tier]:
            excess = semis_v - SEMIS_CAP[tier] * eq
            for s in sorted((s for s in val if s in SEMIS), key=lambda s: -(val[s] - sold[s])):
                if excess <= 0:
                    break
                cut = min(excess, (val[s] - sold[s]) * 0.5)
                add(s, cut, f"semis cluster {semis_v/eq:.0%}, over the {SEMIS_CAP[tier]:.0%} cap")
                excess -= cut
    # 0. WEAK holdings go first once risk is up: the market is telling us to raise cash and
    #    these are the names whose own trend or business is already failing. Non-core = full
    #    exit; core = half, since core names are trimmed but never sold out.
    for s in sorted(weak, key=lambda s: -health[s]["points"]):
        if s in val:
            add(s, val[s] * (0.5 if s in CORE else 1.0),
                "WEAK holding: " + ", ".join(health[s]["flags"]))
    # 1+2. margin / cash target funded by loss names first, then high-beta non-core
    losers = sorted((p for p in positions if p["symbol"] not in CORE and p.get("cost")
                     and p["price"] < p["cost"]), key=lambda p: p["price"] / p["cost"])
    for p in losers:
        if raised >= need:
            break
        add(p["symbol"], val[p["symbol"]], "non-core name under water: harvest the loss, cut a weak holding")
    if raised < need:
        for s in sorted((s for s in val if s in HIGH_BETA and s not in CORE), key=lambda s: -val[s]):
            if raised >= need:
                break
            add(s, min(need - raised, (val[s] - sold[s]) * (0.5 if tier != "RED" else 1.0)),
                "high-beta non-core: first to fall in a drawdown")
    merged: dict[str, dict] = {}
    for r in recs:                      # one line per name, reasons joined
        m = merged.get(r["symbol"])
        if m:
            m["sell_usd"] += r["sell_usd"]
            m["why"] += "; " + r["why"]
        else:
            merged[r["symbol"]] = dict(r)
    for sym, m in merged.items():
        m["pct_of_position"] = round(m["sell_usd"] / val[sym] * 100)
    recs = list(merged.values())
    return {"raise_usd": round(max(need, raised)), "margin_usd": round(margin),
            "cash_target_pct": CASH_TARGET[tier] * 100, "recs": recs,
            "note": (f"Margin ${margin:,.0f} in use: clear it first." if margin else "No margin in use.")}
