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

# What each benchmark MEANS and how much it weighs. Keyed by (symbol, condition_type).
# Weights: 1 = early warning, 2 = real stress, 3 = regime break. Unknown alerts count 1.
SIGNALS = {
    ("SPY", "price_below_sma"): (1, "SPY closed under its 50-day: trend damage, early warning"),
    ("SPY", "price_below"):     (2, "SPY broke a price level"),     # 729 ~ -5%; 690 handled below
    ("QQQ", "price_below"):     (2, "QQQ broke its level: tech/growth de-rating (joint book is ~50% tech)"),
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


def grade(alerts: list[dict], prices: dict[str, float], smas: dict[str, float] | None = None) -> dict:
    """alerts = get_alerts()['alerts'] (enabled ones); prices = {sym: last}; smas = {sym: 50d SMA}.
    Returns score, tier, and a per-alert breakdown including distance to trigger."""
    smas = smas or {}
    rows, score = [], 0
    for a in alerts:
        if not a.get("enabled", True):
            continue
        sym, ct = a["symbol"], a["condition_type"]
        price, sma = prices.get(sym), smas.get(sym)
        weight, meaning = SIGNALS.get((sym, ct), (1, "custom alert"))
        tgt = sma if ct.endswith("_sma") else float(a["condition"].get("target_price") or 0)
        hit = _is_triggered(a, price, sma)
        pts = 0
        if hit:
            pts = weight
            bonus = DEEP_LEVEL_BONUS.get((sym, ct))
            if bonus and tgt <= bonus[0]:
                pts += bonus[1]
        score += pts
        dist = (price / tgt - 1) * 100 if (price and tgt) else None
        rows.append({"symbol": sym, "condition": ct, "level": round(tgt, 2) if tgt else None,
                     "price": price, "distance_pct": round(dist, 2) if dist is not None else None,
                     "triggered": hit, "points": pts, "meaning": meaning})
    tier = [name for floor, name in TIERS if score >= floor][-1]
    rows.sort(key=lambda r: (not r["triggered"], abs(r["distance_pct"] or 999)))
    return {"score": score, "tier": tier, "readings": rows}


def sell_plan(tier: str, positions: list[dict], cash: float, total_value: float) -> dict:
    """positions = [{symbol, qty, price, cost}] for the JOINT account.
    Returns the dollars to raise and a ranked list of sell recommendations.
    Order of preference, cheapest-to-the-thesis first:
      1. clear any MARGIN balance (Ryan de-levered this account 2026-08-05 and rejected
         re-margining; borrowed money is the first thing a drawdown punishes)
      2. tax-loss names that are not core (harvest the loss, remove weak holdings)
      3. trim concentration: single names over the tier cap, then the semis cluster
      4. RED only: high-beta non-core names to reach the cash target
    Core names are trimmed for concentration only, never sold out."""
    if tier == "GREEN":
        m = max(0.0, -cash)
        return {"raise_usd": 0.0, "margin_usd": round(m), "recs": [],
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
