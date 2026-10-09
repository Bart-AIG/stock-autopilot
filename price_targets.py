"""Joint price targets: three independent methods, compared, one final target per holding,
one Robinhood alert per holding at that target (set 2026-10-09).

Ryan, live turn 2026-10-09: "I want to start placing price target alerts in the joint account
using the 200-day watch routine ... in three different ways that basically they will compare
against each other and then determine what that final price target is going to be. The first
way ... look at financials and basically do exactly what a financial analyst would do ...
Two ... Robinhood's price target tool. Three, look up respected analysts around the industry
and what their price targets are. And this is all for stocks currently owned in the joint
account."

THE THREE METHODS
1. FUNDAMENTAL: valuation.forward_target(), next fiscal year's consensus EPS / EBITDA /
   revenue x the stock's 5-year median multiples, picked by industry (valuation.FWD_LEGS).
   Built each morning by report.py into valuation.json (row["fwd"]). A LOW-confidence result
   is dropped, never averaged in. Until a holding's fwd row exists, the history fair value
   (row["fair"]) stands in only at MED/HIGH confidence.
2. ROBINHOOD: get_equity_analyst_ratings mean_price_target (what the app's analyst-ratings
   panel shows), read live by the routine. Needs >= 3 ratings.
3. RESPECTED ANALYSTS: dated targets from named major-firm / top-ranked analysts, researched
   by web search and stored in price_target_research.json (one note per symbol, refreshed
   when older than RESEARCH_TTL_DAYS). Median of targets set within TARGET_MAX_AGE_DAYS,
   needs >= MIN_ANALYSTS.

COMBINING: three values -> the MEDIAN (one outlier method can't drag it; Robinhood's mean is
pulled by extreme highs like MU's $3,000). Two -> the average. One -> that value, LOW.
Agreement = (max - min) / final: <= 15% HIGH, <= 35% MED, else LOW. Methods 2 and 3 share a
source (sell-side analysts), so without method 1 agreement tops out at MED.

ALERTS: one `price_above` alert per holding at the final target, only while the price is
below it. Re-set when the target moves more than REALERT_PCT. Once one fires (target
reached), it is not re-armed until the target rises past the old level by REALERT_PCT, so a
stock sitting at its target doesn't page Ryan every day. Ids live in
joint_price_targets.json; risk_watch.grade() skips them (they are not market-risk signals).

Advisory only: the agent never trades the joint account.
"""
from __future__ import annotations

import math
import statistics
from datetime import date

RESEARCH_TTL_DAYS = 30      # re-research a holding's analyst targets after this many days
TARGET_MAX_AGE_DAYS = 120   # an individual analyst target older than this is ignored
MIN_ANALYSTS = 2            # method 3 needs at least this many fresh targets
MIN_RH_RATINGS = 3          # method 2 needs at least this many ratings
REALERT_PCT = 0.03          # move an alert only when the target changes by more than 3%
AGREE_HIGH, AGREE_MED = 0.15, 0.35


def _f(x) -> float | None:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) and v > 0 else None


def _days(d: str | None, today: date) -> int | None:
    try:
        return (today - date.fromisoformat(str(d)[:10])).days
    except (TypeError, ValueError):
        return None


def fundamental(vrow: dict | None) -> dict | None:
    """Method 1 from a valuation.json row. Prefers the forward target; falls back to the
    history fair value only at MED/HIGH confidence. None when unusable."""
    if not vrow:
        return None
    fwd = vrow.get("fwd") or {}
    if _f(fwd.get("target")) and fwd.get("confidence") != "LOW":
        return {"value": round(_f(fwd["target"]), 2), "confidence": fwd.get("confidence"),
                "basis": fwd.get("basis") or "forward estimates x 5-yr multiples"}
    if _f(vrow.get("fair")) and vrow.get("confidence") in ("HIGH", "MED"):
        return {"value": round(_f(vrow["fair"]), 2), "confidence": vrow.get("confidence"),
                "basis": "fair value at its own 10-yr multiples (forward model not built yet)"}
    return None


def robinhood(ratings: dict | None) -> dict | None:
    """Method 2 from one get_equity_analyst_ratings result's `ratings` dict."""
    r = ratings or {}
    n = sum(int(r.get(k) or 0) for k in ("num_buy_ratings", "num_hold_ratings", "num_sell_ratings"))
    mean = _f(r.get("mean_price_target"))
    if not mean or n < MIN_RH_RATINGS:
        return None
    return {"value": round(mean, 2), "n": n, "low": _f(r.get("low_price_target")),
            "high": _f(r.get("high_price_target")),
            "buy_hold_sell": [int(r.get(k) or 0) for k in
                              ("num_buy_ratings", "num_hold_ratings", "num_sell_ratings")]}


def analysts(note: dict | None, today: date | None = None) -> dict | None:
    """Method 3 from a price_target_research.json note: median of fresh targets."""
    today = today or date.today()
    if not note:
        return None
    fresh = [t for t in note.get("targets") or []
             if _f(t.get("target")) and (_days(t.get("date"), today) or 10**6) <= TARGET_MAX_AGE_DAYS]
    if len(fresh) < MIN_ANALYSTS:
        return None
    return {"value": round(statistics.median(_f(t["target"]) for t in fresh), 2), "n": len(fresh),
            "firms": [t.get("firm") for t in fresh], "researched": note.get("date")}


def research_due(notes: dict, symbols: list[str], today: date | None = None, limit: int = 6) -> list[str]:
    """Symbols whose analyst research is missing or older than RESEARCH_TTL_DAYS, oldest
    first, at most `limit` per run (bounds the routine's web searches)."""
    today = today or date.today()

    def age(s):
        a = _days((notes.get(s) or {}).get("date"), today)
        return 10**6 if a is None else a
    return [s for s in sorted(symbols, key=age, reverse=True) if age(s) > RESEARCH_TTL_DAYS][:limit]


def combine(price: float | None, f: dict | None, r: dict | None, a: dict | None) -> dict:
    """Final target from whichever methods are available (see module docstring)."""
    vals = {k: m["value"] for k, m in (("fundamental", f), ("robinhood", r), ("analysts", a)) if m}
    out = {"methods": vals, "final": None, "agreement": None, "upside_pct": None, "status": "NO TARGET"}
    if not vals:
        return out
    xs = list(vals.values())
    final = statistics.median(xs) if len(xs) == 3 else sum(xs) / len(xs)
    spread = (max(xs) - min(xs)) / final if len(xs) > 1 else None
    agreement = "LOW" if spread is None or spread > AGREE_MED else ("HIGH" if spread <= AGREE_HIGH else "MED")
    # Methods 2 and 3 both come from sell-side analysts, so their agreement is not
    # independent: without the fundamental leg, agreement tops out at MED.
    if agreement == "HIGH" and "fundamental" not in vals:
        agreement = "MED"
    out.update(final=round(final, 2), agreement=agreement,
               spread_pct=round(spread * 100, 1) if spread is not None else None)
    p = _f(price)
    if p:
        out["upside_pct"] = round((final / p - 1) * 100, 1)
        out["status"] = "BELOW TARGET" if p < final else "AT/ABOVE TARGET"
    return out


def plan_alerts(rows: dict, managed: dict, live_ids: set[str], reached: dict | None = None) -> dict:
    """rows = {sym: {price, final, ...}}; managed = {sym: {alert_id, level}} from state;
    live_ids = alert ids get_alerts returns now; reached = {sym: {level, date}}.
    Returns {create: [{symbol, level}], update: [{symbol, alert_id, level}],
    delete: [{symbol, alert_id}], fired: [{symbol, level}]}."""
    reached = reached or {}
    plan = {"create": [], "update": [], "delete": [], "fired": []}
    for sym in sorted(set(rows) | set(managed)):
        row, m = rows.get(sym) or {}, managed.get(sym)
        final, price = _f(row.get("final")), _f(row.get("price"))
        live = bool(m and m.get("alert_id") in live_ids)
        if m and not live and sym in rows:
            plan["fired"].append({"symbol": sym, "level": m.get("level")})
        want = final is not None and price is not None and price < final and sym in rows
        if want and not live:
            # A managed alert that is no longer live fired (target reached); so did any
            # level recorded in `reached`. Re-arm only once the target is raised past it.
            prev = (m or {}).get("level") or (reached.get(sym) or {}).get("level")
            if prev and final <= prev * (1 + REALERT_PCT):
                continue        # target already reached; re-arm only when it is raised
            plan["create"].append({"symbol": sym, "level": round(final, 2)})
        elif want and live:
            if abs(final / m["level"] - 1) > REALERT_PCT:
                plan["update"].append({"symbol": sym, "alert_id": m["alert_id"], "level": round(final, 2)})
        elif live:
            plan["delete"].append({"symbol": sym, "alert_id": m["alert_id"]})
    return plan


def _money(x) -> str:
    return f"${x:,.2f}" if x is not None else "—"


def report(rows: dict, asof: str) -> str:
    """Markdown section for quality_watch_report.md."""
    lines = [f"## Joint price targets ({asof})", "",
             "| Symbol | Price | 1. Fundamental | 2. Robinhood | 3. Analysts | **Final** | Upside | Agreement | Alert |",
             "|---|---|---|---|---|---|---|---|---|"]
    order = sorted(rows.items(), key=lambda kv: -(kv[1].get("upside_pct") or -1e9))
    for sym, r in order:
        m, up = r.get("methods") or {}, r.get("upside_pct")
        up_cell = "—" if up is None else f"{up:+.1f}%"
        lines.append(f"| {sym} | {_money(r.get('price'))} | {_money(m.get('fundamental'))} | "
                     f"{_money(m.get('robinhood'))} | {_money(m.get('analysts'))} | **{_money(r.get('final'))}** | "
                     f"{up_cell} | {r.get('agreement') or '—'} | {r.get('alert') or '—'} |")
    lines += ["", "_Final = median of the three methods (average of two; one alone is LOW). "
              "Fundamental = next fiscal year's consensus estimates x the stock's 5-year median "
              "multiples, by industry. Robinhood = mean analyst target in the app. Analysts = median "
              "of dated targets from named major-firm analysts in the last 120 days. Agreement = "
              "spread between methods (HIGH <= 15%, MED <= 35%). A target is an estimate, not a "
              "sell signal: AT/ABOVE TARGET means re-check the thesis, not sell._"]
    return "\n".join(lines) + "\n"
