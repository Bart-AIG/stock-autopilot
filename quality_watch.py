"""Quality-at-the-200-day watch (set 2026-09-30, Ryan's live turn).

Finds FUNDAMENTALLY high-quality companies whose stock has pulled back to, or just
under, its 200-day moving average, and keeps a Robinhood price alert on each so Ryan
is pinged the moment price touches the line. Advisory, for the JOINT (long-term)
account. It never places an order.

Why fundamentals and not grade.py: grade.py's A/A+ needs the top 10% of the universe
and two of its 12 traits require price ABOVE the 200-day, so "A-grade and below the
200-day" is empty by construction (all 22 A/A+ names on 2026-09-30 carried 200 UP).
The quality here comes from the business (Robinhood get_financials), the timing from
the chart.

Pure functions, no network. The routine (docs/quality-watch-prompt.md) fetches the
data with the Robinhood connector and calls these.
"""
from __future__ import annotations

import disruption
import valuation

# Price band around the 200-day SMA, as price / sma200 - 1.
BAND_ABOVE = 0.05    # up to 5% above: "approaching" -> alert when it touches
BAND_BELOW = -0.08   # down to 8% below: "at/under" -> alert when it reclaims
MIN_QUALITY = 7      # of 8 (quality_score below). 5 let 48 of 74 through on 2026-09-30
MAX_ALERTS = 15      # managed alerts at once, best quality first, then closest to the line
MAX_PER_GROUP = 3    # per Morningstar industry group: 8 of 24 finalists were gold miners on 2026-09-30
MIN_PRICE = 5.0

# Alert conditions the routine owns. It only ever creates/deletes alerts whose
# alert_id is recorded in quality_watch_state.json, never Ryan's own alerts.
TOUCH = "price_below_sma"    # price above the line now -> ping when it drops through
RECLAIM = "price_above_sma"  # price under the line now -> ping when it gets back over
SMA200 = {"kind": "sma", "period": 200, "interval_secs": 86400}


def _f(x) -> float | None:
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


# Scanner result columns -> the fundamental.* keys quality_score reads. The scanner
# renames expressions that match a standard column (fundamental.netProfitMargin comes
# back as "Net profit margin"), so both spellings are accepted.
SCAN_COLUMNS = {
    "fundamental.quarterlyRevenueGrowth": ("Q rev growth", "Quarterly revenue growth"),
    "fundamental.netProfitMargin": ("Net profit margin", "Net margin"),
    "fundamental.operatingMargin": ("Operating margin", "Op margin"),
    "fundamental.grossMargin": ("Gross margin",),
    "fundamental.returnOnEquity": ("Return on equity", "ROE"),
    "fundamental.cashFlowFreePerShare": ("FCF/share", "Free cash flow per share"),
}


def from_scan(result: dict) -> dict:
    """One run_scan result ({"ticker", "columns": {...}}) -> a flat row with
    symbol, name, price, sma200, dist and the fundamental.* keys."""
    c = result.get("columns") or {}
    price, sma = _f(c.get("Last")), _f(c.get("200d SMA"))
    row = {"symbol": result.get("ticker") or c.get("Symbol"), "name": c.get("Name"),
           "price": price, "sma200": sma,
           "dist": price / sma - 1 if price and sma else None, "sma200_rising": None,
           "group": c.get("Industry group") or None, "sector": c.get("Sector") or None}
    for key, names in SCAN_COLUMNS.items():
        row[key] = next((c[n] for n in names if c.get(n) not in (None, "")), None)
    return row


def sma200_rising(sma_series: list[float]) -> bool | None:
    """sma_series = the 200-day SMA's daily values OLDEST first, e.g. the 'value's from
    get_equity_technical_indicators(type=sma, period=200, interval=day, output=last:22).
    True if the latest value is at or above the one 20 sessions earlier."""
    v = [x for x in sma_series if x is not None]
    if len(v) < 21:
        return None
    return v[-1] >= v[-21]


def in_band(row: dict | None) -> bool:
    return (bool(row) and row.get("dist") is not None and (row.get("price") or 0) >= MIN_PRICE
            and BAND_BELOW <= row["dist"] <= BAND_ABOVE)


def quality_score(row: dict | None, fin: list[dict] | None = None) -> dict:
    """Business quality 0-8 from the scanner row's fundamentals (ratios, not %):

      fundamental.quarterlyRevenueGrowth  >= 0.10 (1), >= 0.20 (+1)
      fundamental.netProfitMargin         >= 0.15 (1), >= 0.25 (+1)
      fundamental.operatingMargin         >= 0.20 (1)
      fundamental.grossMargin             >= 0.45 (1)
      fundamental.returnOnEquity          >= 0.20 (1)
      fundamental.cashFlowFreePerShare    >  0    (1)

    Why the scanner and not get_financials: measured 2026-09-30, get_financials
    returned NO data for 12 of 20 large caps (BLK, CDNS, ICE, ECL, TEL, WPM ...) and
    null gross profit on several more. A gate built on it silently drops good
    companies. So get_financials (quarterly rows, newest first) is only a
    CONSISTENCY check when it has data: -1 if revenue fell year-over-year in any of
    the last 4 quarters, -1 if any of the last 4 quarters lost money. With no rows
    the name keeps its score and is flagged "consistency unverified".
    A missing scanner field scores 0 for that trait (never guessed)."""
    r = row or {}
    pts, flags = 0, []

    def tier(key, label, *cuts):
        nonlocal pts
        v = _f(r.get(key))
        if v is None:
            return
        pts += sum(1 for c in cuts if v >= c)
        flags.append(f"{label} {v:.0%}")
    tier("fundamental.quarterlyRevenueGrowth", "rev growth", 0.10, 0.20)
    tier("fundamental.netProfitMargin", "net margin", 0.15, 0.25)
    tier("fundamental.operatingMargin", "op margin", 0.20)
    tier("fundamental.grossMargin", "gross margin", 0.45)
    tier("fundamental.returnOnEquity", "ROE", 0.20)
    fcf = _f(r.get("fundamental.cashFlowFreePerShare"))
    if fcf is not None and fcf > 0:
        pts += 1
        flags.append("FCF positive")

    rows = [x for x in (fin or []) if x and x.get("fiscal_quarter") is not None]
    if len(rows) >= 8:
        def yoy(q):
            p = next((x for x in rows if x.get("fiscal_quarter") == q.get("fiscal_quarter")
                      and x.get("fiscal_year") == (q.get("fiscal_year") or 0) - 1), None)
            a, b = _f(q.get("revenue")), _f(p.get("revenue")) if p else None
            return a / b - 1 if a is not None and b else None
        ys = [yoy(q) for q in rows[:4]]
        if any(y is not None and y < 0 for y in ys):
            pts -= 1
            flags.append("revenue fell YoY in a recent quarter")
        if any((_f(q.get("net_income")) or 0) < 0 for q in rows[:4]):
            pts -= 1
            flags.append("a loss quarter in the last 4")
    else:
        flags.append("consistency unverified")
    return {"score": max(pts, 0), "flags": flags}


# Composite tie-breaker (0-100): each trait scaled to its cap, then averaged. Caps
# stop one outlier from dominating: RGLD's 115% revenue growth (a gold-price windfall)
# and MA's 241% ROE (buybacks shrinking equity) would otherwise swamp everything else.
COMPOSITE_CAPS = {
    "fundamental.quarterlyRevenueGrowth": 0.40,
    "fundamental.netProfitMargin": 0.40,
    "fundamental.operatingMargin": 0.50,
    "fundamental.grossMargin": 0.80,
    "fundamental.returnOnEquity": 0.50,
}


def composite(row: dict | None) -> float:
    """Continuous quality 0-100 used to rank names that share an integer score.
    A missing field counts 0 (never guessed); negative FCF costs 10 points."""
    r = row or {}
    parts = [max(0.0, min((_f(r.get(k)) or 0.0) / cap, 1.0)) for k, cap in COMPOSITE_CAPS.items()]
    score = 100 * sum(parts) / len(parts)
    fcf = _f(r.get("fundamental.cashFlowFreePerShare"))
    if fcf is not None and fcf <= 0:
        score -= 10
    return round(max(score, 0.0), 1)


def letter(score: int) -> str:
    """A+ = 8/8, A = 7/8 (the only two grades that qualify at MIN_QUALITY 7)."""
    return "A+" if score >= 8 else ("A" if score >= 7 else "B" if score >= 5 else "C")


def candidates(rows: list[dict], fins: dict[str, list] | None = None,
               vals: dict[str, dict] | None = None, notes: dict[str, dict] | None = None) -> list[dict]:
    """rows = [from_scan(r) ...]. Keeps names in the 200-day band scoring
    >= MIN_QUALITY and drops a second share class of the same company (GOOG/GOOGL,
    HEI/HEI.A: same name, keep the one nearer the line). Ranked by integer score,
    then the VALUATION tier (cheaper vs its own history first; added 2026-10-02, Ryan's
    live turn), then the composite, then closeness to the line; each gets rank, grade,
    composite and value.
    vals = {sym: valuation.value() dict}; None reads valuation.json (built each morning
    by report.py). A name not valued yet ranks as N/A: never promoted, never dropped.
    Each name also carries its disruption grade (disruption.py, quant from valuation.json
    plus any fresh research note from disruption_notes.json; notes=None reads that file).
    Within a quality grade, names AT RISK / BEING DISRUPTED rank after the rest, ahead of
    the valuation tier: a cheap stock whose business is under threat is a value trap."""
    if vals is None:
        vals = valuation.load_cache()
    if notes is None:
        notes = disruption.load_notes()
    out, seen = [], set()
    for r in sorted(rows, key=lambda x: abs(x["dist"]) if x.get("dist") is not None else 9):
        if not in_band(r):
            continue
        key = (r.get("name") or r["symbol"]).split(" Class ")[0].strip().lower()
        if key in seen:
            continue
        q = quality_score(r, (fins or {}).get(r["symbol"]))
        if q["score"] < MIN_QUALITY:
            continue
        seen.add(key)
        d = r["dist"]
        zone = "approaching" if d > 0.01 else ("at the line" if d >= -0.03 else "below")
        out.append({"symbol": r["symbol"], "name": r.get("name"), "price": r["price"],
                    "sma200": round(r["sma200"], 2), "dist": d, "dist_pct": round(d * 100, 1),
                    "sma200_rising": r.get("sma200_rising"), "zone": zone,
                    "group": r.get("group"), "sector": r.get("sector"),
                    "quality": q["score"], "grade": letter(q["score"]),
                    "composite": composite(r), "quality_flags": q["flags"],
                    "value": vals.get(r["symbol"]),
                    "disruption": disruption.for_row(vals.get(r["symbol"]), notes),
                    "alert": TOUCH if d > 0 else RECLAIM})
    out.sort(key=lambda c: (-c["quality"], 1 if disruption.threatened(c["disruption"]) else 0,
                            valuation.rank_tier(c["value"]), -c["composite"], abs(c["dist"])))
    for i, c in enumerate(out, 1):
        c["rank"] = i
    return out


def alert_set(cands: list[dict]) -> list[dict]:
    """The names that get a Robinhood alert: first MAX_ALERTS in candidate order,
    at most MAX_PER_GROUP per industry group (unknown group = no cap)."""
    picked, per = [], {}
    for c in cands:
        g = c.get("group")
        if g and per.get(g, 0) >= MAX_PER_GROUP:
            continue
        picked.append(c)
        if g:
            per[g] = per.get(g, 0) + 1
        if len(picked) >= MAX_ALERTS:
            break
    return picked


def plan_alerts(cands: list[dict], managed: dict[str, dict]) -> dict:
    """Diff the wanted alerts against the ones this routine already owns.
    managed: {sym: {"alert_id", "condition_type"}} from quality_watch_state.json.
    Returns {"create": [...], "delete": [...], "keep": [...]}. A name whose side of
    the line flipped gets its old alert deleted and the opposite one created."""
    want = {c["symbol"]: c["alert"] for c in alert_set(cands)}
    create, delete, keep = [], [], []
    for sym, m in managed.items():
        if want.get(sym) == m.get("condition_type"):
            keep.append(sym)
        else:
            delete.append({"symbol": sym, "alert_id": m.get("alert_id")})
    for sym, cond in want.items():
        if sym not in keep:
            create.append({"symbol": sym, "condition_type": cond, "indicator": SMA200})
    return {"create": create, "delete": delete, "keep": sorted(keep)}


def report(cands: list[dict], plan: dict, asof: str, new_syms: set[str]) -> str:
    """Markdown for quality_watch_report.md (the commit triggers the ntfy push)."""
    head = f"# QUALITY @ 200-DAY: {len(cands)} name(s) ({len(new_syms)} new)"
    lines = [head, "", f"As of {asof}. Joint account, advisory only. Quality = business "
             f"score >= {MIN_QUALITY}/8 (growth, margins, ROE, free cash flow); band = {BAND_BELOW:.0%} to "
             f"+{BAND_ABOVE:.0%} vs the 200-day SMA. Rank = grade, then Comp (0-100 blend of growth, margins and "
             "ROE, capped so one outlier can't dominate), then distance to the line. "
             "Value = valuation grade vs the stock's own 10-year multiples (positive = undervalued "
             "by that much). Disruption = is the business being disrupted or doing the disrupting. "
             "Within a grade, names not under threat rank first, then cheaper names.", ""]
    if not cands:
        lines.append("No high-quality names are near their 200-day right now.")
    else:
        alerted = {c["symbol"] for c in alert_set(cands)}
        lines += ["| # | Ticker | Grade | Q | Value | Fair | Analysts | Disruption | Comp | Sector | Zone | Price | 200-day | Dist | 200d slope | Alert | Why |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for c in cands:
            tag = " (new)" if c["symbol"] in new_syms else ""
            alert = ("touch" if c["alert"] == TOUCH else "reclaim") if c["symbol"] in alerted else "-"
            v = c.get("value") or {}
            dz = c.get("disruption")
            why = c["quality_flags"] + [f"value: {f}" for f in v.get("flags", [])]
            if disruption.why(dz):
                why.append("disruption: " + disruption.why(dz))
            if disruption.value_trap(v, dz):
                why.insert(0, "**VALUE TRAP?**")
            lines.append(f"| {c['rank']} | {c['symbol']}{tag} | {c['grade']} | {c['quality']}/8 | "
                         f"{valuation.short(v)} | {v.get('fair') or '—'} | {valuation.analyst_cell(v)} | "
                         f"{disruption.cell(dz)} | "
                         f"{c['composite']:.0f} | "
                         f"{c.get('sector') or ''} | {c['zone']} | {c['price']} | {c['sma200']} | "
                         f"{c['dist_pct']:+.1f}% | { {True: 'rising', False: 'FALLING'}.get(c['sma200_rising'], '?') } | "
                         f"{alert} | {', '.join(why)} |")
    lines += ["", f"Robinhood alerts: {len(plan['create'])} created, {len(plan['delete'])} removed, "
              f"{len(plan['keep'])} kept (touch = price drops through the 200-day; reclaim = "
              "price gets back above it). Max {MAX_ALERTS}, at most {MAX_PER_GROUP} per industry "
              "group; '-' = qualifies but no slot.",
              "", "A FALLING 200-day means the long-term trend itself is rolling over: a touch "
              "there is weaker evidence than a touch of a rising line. Every name still needs "
              "the news/thesis check before a buy; '—' in Value = not valued yet (next morning's "
              "report run values it).", "", valuation.LEGEND, "", disruption.LEGEND]
    return "\n".join(lines) + "\n"
