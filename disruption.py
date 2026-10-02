"""Disruption grade: is the business being disrupted, or is it the disruptor? (set 2026-10-02)

Ryan, live turn 2026-10-02: "add one more grade function related to the business and if
it is or seems it will get disrupted by competitors or emerging tech, as well as if the
business is doing the disruption being innovative."

TWO LAYERS, because numbers see disruption late:
1. QUANT (this module, automatic, every name valuation.py values). Ten years of annual
   revenue, gross margin and R&D plus analysts' forward revenue estimates, read through
   the same industry profile as valuation.py:
     THREAT points    revenue shrinking (3-yr CAGR < 0: +2, < 3%: +1) | analysts expect
                      revenue to fall next year (+1) | growth fading (next-year estimate
                      >= 10 pts below the 3-yr CAGR and under 5%: +1) | gross margin
                      eroding vs its 5-yr median (>= 5 pts: +2, >= 2 pts: +1; pricing power
                      is the first thing a disruptor takes) | MARKET FEAR: the stock trades
                      >= 40% below its own historical multiples while its margins are
                      normal (+2). That last one is how a threat shows up before the
                      income statement does (ADBE on 2026-10-02: revenue +10%/yr, gross
                      margin 89%, priced at half its 10-yr multiples on AI fear).
     INNOVATOR points 3-yr revenue CAGR >= 20% (+2) or >= 10% (+1) | growth accelerating
                      (next-year estimate >= 5 pts above the 3-yr CAGR and >= 10%) or
                      next-year estimate >= 20% (+1) | gross margin expanding >= 3 pts (+1)
                      | R&D >= 15% of revenue (+1, non-financial, non-REIT only).
   Industry awareness: a COMMODITY producer (Energy, Basic Materials) has revenue and
   margins set by the commodity price, so only R&D, market fear and the research note
   count, at LOW confidence. Other CYCLICALS (semis, autos, homebuilders ...) are judged
   on 5-yr trends, and margin erosion only counts when the 5-yr revenue trend is also
   negative. Banks, insurers and REITs have no gross margin or R&D line and analysts
   estimate a different revenue line for them, so only shrinking revenue counts as a
   threat and revenue growth earns no innovator points (it is mostly interest rates).
2. RESEARCH NOTE (disruption_notes.json, written by a routine or a live session after a
   news/competitor check, with sources). Who or what threatens it, what it is doing that
   is new. A note younger than NOTE_TTL_DAYS is shown next to the quant label and can
   move the final label one step (a note naming a real threat turns STABLE into AT RISK;
   a note naming real innovation turns INNOVATING into DISRUPTOR). It never moves it more.

LABELS (final):  DISRUPTOR | INNOVATING | STABLE | AT RISK | BEING DISRUPTED | N/A
VALUE TRAP flag: valuation says UNDERVALUED/DEEP VALUE while this says AT RISK or BEING
DISRUPTED. Cheap because the future is worse is not cheap.

HONEST LIMITS: no backtest; the thresholds are judgment, written down so they are the
same every run. Analyst estimates lean optimistic. Revenue can fall for reasons other
than disruption (a divestiture, a spin-off). This is context for the joint account and the
Quality @ 200-day watch. It never gates the mechanical sleeves.
"""
from __future__ import annotations

import json
import statistics
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES_FILE = HERE / "disruption_notes.json"
NOTE_TTL_DAYS = 90
MARKET_FEAR_GAP = 40.0        # valuation gap % that reads as "the market sees a threat"
# Research-note verdicts, in Ryan's terms (live turn 2026-10-02: "trends that change and if
# new innovation or tech seem to be making a particular business obsolete or if the
# innovation is creating a new market that is untapped"):
#   disruptor   its innovation is CREATING a new, largely untapped market
#   innovating  riding / adapting to a new trend well; it gains from the shift
#   neutral     no trend or technology materially changes its business
#   threatened  a trend or new tech COULD make its core business obsolete; not yet visible
#   disrupted   that obsolescence is already happening (share, pricing or demand lost)
NOTE_VERDICTS = ("disruptor", "innovating", "neutral", "threatened", "disrupted")

LABELS = ("DISRUPTOR", "INNOVATING", "STABLE", "AT RISK", "BEING DISRUPTED")
# Rank order for sorting: healthy first, N/A neutral, threatened last.
TIER = {"DISRUPTOR": 0, "INNOVATING": 1, "STABLE": 2, "N/A": 2, "AT RISK": 3, "BEING DISRUPTED": 4}
NO_MARGIN_PROFILES = ("bank", "insurer", "reit")


def _f(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if v == v else None


def _cagr(a, b, years):
    if a is None or b is None or b <= 0 or a <= 0 or years <= 0:
        return None
    return (a / b) ** (1 / years) - 1


def _label(threat: int, innov: int) -> str:
    if threat >= 4:
        return "BEING DISRUPTED"
    if threat >= 2:
        return "AT RISK"
    if innov >= 4:
        return "DISRUPTOR"
    if innov >= 2:
        return "INNOVATING"
    return "STABLE"


COMMODITY_SECTORS = ("Energy", "Basic Materials")


def score(income: list[dict], estimates: list[dict], profile: str = "steady",
          valuation: dict | None = None) -> dict:
    """income = FMP annual income statements (any order); estimates = FMP annual analyst
    estimates; profile = valuation.classify() key; valuation = valuation.value() dict.
    Returns {label, threat, innovator, confidence, evidence[], metrics{}}."""
    rows = sorted((r for r in income or [] if _f(r.get("revenue"))),
                  key=lambda r: str(r.get("fiscalYear") or r.get("date")))
    out = {"label": "N/A", "threat": 0, "innovator": 0, "confidence": "LOW",
           "evidence": [], "metrics": {}}
    if len(rows) < 4:
        out["evidence"].append("fewer than 4 years of revenue history")
        return out
    rev = [_f(r["revenue"]) for r in rows]
    gm = [(_f(r.get("grossProfit")) or 0) / rv if rv else None for r, rv in zip(rows, rev)]
    rd = (_f(rows[-1].get("researchAndDevelopmentExpenses")) or 0) / rev[-1]
    cyclical = profile == "cyclical"
    # Commodity producers (oil, steel, miners, chemicals): revenue and margin follow the
    # commodity price, so neither growth nor shrinkage says anything about competitors
    # (NUE read INNOVATING off a steel upswing on 2026-10-02). Only R&D and research count.
    commodity = cyclical and (valuation or {}).get("sector") in COMMODITY_SECTORS
    financial = profile in NO_MARGIN_PROFILES
    span = 5 if cyclical and len(rev) >= 6 else 3
    cagr = _cagr(rev[-1], rev[-1 - span], span)
    cagr5 = _cagr(rev[-1], rev[-6], 5) if len(rev) >= 6 else cagr

    # Next fiscal year's consensus revenue vs the latest actual year.
    last_end = str(rows[-1].get("date") or "")[:10]
    fut = sorted((e for e in estimates or [] if str(e.get("date"))[:10] > last_end
                  and _f(e.get("revenueAvg"))), key=lambda e: str(e.get("date")))
    fwd = _f(fut[0]["revenueAvg"]) / rev[-1] - 1 if fut else None
    if financial:
        # Analysts estimate NET revenue for lenders while the income statement reports
        # gross (JPM: -26% "expected" on 2026-10-02 was a definition mismatch).
        fwd = None

    margins_apply = profile not in NO_MARGIN_PROFILES and gm[-1] is not None and gm[-1] > 0
    gm_med = statistics.median([g for g in gm[-6:-1] if g]) if margins_apply and len(gm) >= 6 else None
    gm_delta = (gm[-1] - gm_med) * 100 if gm_med else None

    threat, innov, ev = 0, 0, []
    if commodity:
        cagr_used = None
    else:
        cagr_used = cagr
    # A one-time boom unwinding (MRNA: COVID vaccines, revenue ~$0.06B -> $18.5B -> ~$2B)
    # is a spike fading, not a technology replacing the business: shrinkage counts once.
    pk = rev.index(max(rev))
    boom = (0 < pk < len(rev) - 1 and max(rev) >= 3 * min(rev[:pk])
            and rev[-1] <= 0.5 * max(rev))
    if cagr_used is not None:
        if cagr < 0 and boom:
            threat += 1; ev.append(f"revenue {cagr:+.0%}/yr, unwinding a one-time boom "
                                   f"(peak {max(rev) / rev[-1]:.0f}x today's)")
        elif cagr < 0:
            threat += 2; ev.append(f"revenue shrinking {cagr:+.0%}/yr over {span} yrs")
        elif cagr < 0.03:
            threat += 1; ev.append(f"revenue flat ({cagr:+.0%}/yr over {span} yrs)")
        elif cagr >= 0.20 and not financial:
            innov += 2; ev.append(f"revenue {cagr:+.0%}/yr over {span} yrs")
        elif cagr >= 0.10 and not financial:
            innov += 1; ev.append(f"revenue {cagr:+.0%}/yr over {span} yrs")
    if fwd is not None and not commodity:
        if fwd < 0:
            threat += 1; ev.append(f"analysts expect revenue {fwd:+.0%} next year")
        elif cagr is not None and fwd <= cagr - 0.10 and fwd < 0.05:
            threat += 1; ev.append(f"growth fading: next year {fwd:+.0%} vs {cagr:+.0%}/yr trend")
        if fwd >= 0.20 or (cagr is not None and fwd >= cagr + 0.05 and fwd >= 0.10):
            innov += 1; ev.append(f"analysts see revenue {fwd:+.0%} next year")
    if gm_delta is not None and not commodity:
        erosion_counts = not cyclical or (cagr5 is not None and cagr5 < 0)
        if gm_delta <= -5 and erosion_counts:
            threat += 2; ev.append(f"gross margin down {-gm_delta:.0f} pts vs 5-yr median ({gm[-1]:.0%})")
        elif gm_delta <= -2 and erosion_counts:
            threat += 1; ev.append(f"gross margin slipping {-gm_delta:.0f} pts ({gm[-1]:.0%})")
        elif gm_delta >= 3:
            innov += 1; ev.append(f"gross margin up {gm_delta:.0f} pts ({gm[-1]:.0%})")
    if profile not in NO_MARGIN_PROFILES and rd >= 0.15:
        innov += 1; ev.append(f"R&D {rd:.0%} of revenue")

    # Market fear: priced far below its own history while the business looks normal.
    v = valuation or {}
    changed = any("business changed" in f for f in v.get("flags", []))
    # Not for fast growers: a 25%/yr grower's early multiples were priced for hypergrowth,
    # so compression is maturing, not fear (ZS read "market fear" on 2026-10-02).
    mature = cagr is not None and cagr < 0.20
    if (v.get("gap_pct") or 0) >= MARKET_FEAR_GAP and not changed and not cyclical and mature:
        threat += 2
        disc = 1 - 1 / (1 + v["gap_pct"] / 100)
        ev.append(f"market fear: price {disc:.0%} below what its own 10-yr multiples imply, "
                  "with normal margins")

    conf = "HIGH" if len(rev) >= 8 and fwd is not None else "MED"
    if boom and cagr is not None and cagr < 0:
        conf = "LOW"
    if commodity:
        conf = "LOW"
        ev.append("commodity producer: revenue and margins follow the commodity price, not competitors")
    elif cyclical:
        conf = "MED" if conf == "HIGH" else conf
        ev.append(f"cyclical: judged on {span}-yr trends")
    out.update(label=_label(threat, innov), threat=threat, innovator=innov, confidence=conf,
               evidence=ev, metrics={"rev_cagr_pct": round(cagr * 100, 1) if cagr is not None else None,
                                     "fwd_growth_pct": round(fwd * 100, 1) if fwd is not None else None,
                                     "gross_margin_pct": round(gm[-1] * 100, 1) if gm[-1] else None,
                                     "gm_vs_5y_pts": round(gm_delta, 1) if gm_delta is not None else None,
                                     "rd_pct": round(rd * 100, 1)})
    return out


def load_notes(path: Path = NOTES_FILE) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("notes", {})
    except (OSError, ValueError, AttributeError):
        return {}


def save_note(symbol: str, verdict: str, summary: str, threats: list[str] | None = None,
              innovation: list[str] | None = None, sources: list[str] | None = None,
              by: str = "", on: str | None = None, path: Path = NOTES_FILE) -> dict:
    """Write one research note (overwrites that symbol's previous note). verdict is one of
    NOTE_VERDICTS; summary is one line; sources are URLs. Returns the note."""
    if verdict not in NOTE_VERDICTS:
        raise ValueError(f"verdict must be one of {NOTE_VERDICTS}")
    try:
        blob = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        blob = {}
    blob.setdefault("_schema", NOTES_SCHEMA)
    note = {"date": on or date.today().isoformat(), "verdict": verdict, "summary": summary,
            "threats": threats or [], "innovation": innovation or [], "sources": sources or [],
            "by": by}
    blob.setdefault("notes", {})[symbol] = note
    blob["notes"] = dict(sorted(blob["notes"].items()))
    path.write_text(json.dumps(blob, indent=1) + "\n", encoding="utf-8")
    return note


NOTES_SCHEMA = ("{symbol: {date YYYY-MM-DD, verdict: disruptor (its innovation is creating a new, "
                "largely untapped market) | innovating (gains from a changing trend) | neutral | "
                "threatened (a trend or new tech could make its core business obsolete) | disrupted "
                "(that is already happening), summary: one line, threats: [the trend / technology / "
                "competitor that could make it obsolete], innovation: [the new or untapped market it "
                "is creating, with a size or adoption fact if known], sources: [urls], by: routine or "
                "session}}. Written via disruption.save_note(). Ignored after 90 days. Moves the quant "
                "label at most one step.")


def fresh_note(note: dict | None, today: date | None = None) -> dict | None:
    """A note counts only if its verdict is known and it is younger than NOTE_TTL_DAYS."""
    if not note or note.get("verdict") not in NOTE_VERDICTS:
        return None
    try:
        age = ((today or date.today()) - date.fromisoformat(str(note.get("date"))[:10])).days
    except ValueError:
        return None
    return note if 0 <= age <= NOTE_TTL_DAYS else None


def combine(quant: dict | None, note: dict | None, today: date | None = None) -> dict:
    """Final label: the quant label, moved at most ONE step by a fresh research note."""
    q = dict(quant or {"label": "N/A", "evidence": [], "confidence": "LOW"})
    n = fresh_note(note, today)
    final = q.get("label", "N/A")
    if n:
        verdict = n["verdict"]
        if verdict in ("threatened", "disrupted") and final in ("STABLE", "N/A", "INNOVATING", "DISRUPTOR"):
            final = {"DISRUPTOR": "INNOVATING", "INNOVATING": "STABLE"}.get(final, "AT RISK")
        elif verdict == "disrupted" and final == "AT RISK":
            final = "BEING DISRUPTED"
        elif verdict in ("disruptor", "innovating") and final in ("STABLE", "N/A", "INNOVATING"):
            final = {"INNOVATING": "DISRUPTOR"}.get(final, "INNOVATING")
    q.update(final=final, note=n)
    return q


def for_row(val_row: dict | None, notes: dict | None = None, today: date | None = None) -> dict | None:
    """Final disruption dict for one valuation.json row ({..., "disruption": quant}),
    with that symbol's research note applied. None when the row has no quant grade."""
    if not val_row or "disruption" not in val_row:
        return None
    return combine(val_row["disruption"], (notes or {}).get(val_row.get("symbol")), today)


def threatened(dis: dict | None) -> bool:
    return (dis or {}).get("final", (dis or {}).get("label")) in ("AT RISK", "BEING DISRUPTED")


def value_trap(val: dict | None, dis: dict | None) -> bool:
    """Cheap vs history AND threatened: the classic value trap."""
    return bool(val and dis and val.get("grade") in ("UNDERVALUED", "DEEP VALUE")
                and dis.get("final", dis.get("label")) in ("AT RISK", "BEING DISRUPTED"))


def rank_tier(dis: dict | None) -> int:
    return TIER.get((dis or {}).get("final", (dis or {}).get("label", "N/A")), TIER["N/A"])


def cell(dis: dict | None) -> str:
    """Compact table cell: 'AT RISK (market fear) [note: threatened]'."""
    if not dis:
        return "—"
    s = dis.get("final", dis.get("label", "N/A"))
    if dis.get("label") != s:
        s += f" (quant {dis.get('label')})"
    n = dis.get("note")
    if n:
        s += f" [research: {n['verdict']}]"
    return s


def why(dis: dict | None, limit: int = 2) -> str:
    if not dis:
        return ""
    parts = list(dis.get("evidence", [])[:limit])
    n = dis.get("note")
    if n and n.get("summary"):
        parts.append(f"research {n['date']}: {n['summary']}")
    return "; ".join(parts)


LEGEND = ("_Disruption grade: is a changing trend or new technology making this business obsolete "
          "(AT RISK / BEING DISRUPTED), or is its innovation creating a new, untapped market "
          "(DISRUPTOR / INNOVATING)? The research note (dated, sourced) is the main judgment; the quant "
          "layer is an early warning. Quant layer: "
          "10 years of revenue, gross margin and R&D plus analysts' next-year revenue (shrinking or "
          "fading revenue and eroding gross margin = threat; fast or accelerating growth, expanding "
          "margin and heavy R&D = innovator), plus MARKET FEAR when a stock with normal margins trades "
          ">= 40% below its own historical multiples. Cyclicals use 5-yr trends at LOW confidence; "
          "banks, insurers and REITs are judged on revenue only. A dated research note (competitors, "
          "emerging tech, new markets, with sources) moves the label one step. VALUE TRAP = cheap vs history "
          "but AT RISK or BEING DISRUPTED._")
