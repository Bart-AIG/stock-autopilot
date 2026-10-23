"""Earnings dates from Robinhood, for every routine (set 2026-10-23, Ryan's live turn:
"build all 3 please").

Why: report.py takes earnings dates from the FMP calendar, which degrades to {} on any API
failure, so an unflagged name is "unknown", not "clear". Robinhood has two cheaper and
more reliable sources:

    get_earnings_results(symbol)   per symbol: report date, am/pm, and verified=true/false
                                   (the company confirmed it). One call per symbol.
    scanner fundamental.earningsYmd   one column on a saved scan: the next date for every
                                   row at once (an estimate; no verified flag).

Pure functions, no network. The routines fetch; this module reads the results.
"""
from __future__ import annotations

from datetime import date

SOON_DAYS = 14   # "reports soon": inside two weeks, the window a buy or a trim should know about


def _d(s) -> date | None:
    try:
        return date.fromisoformat(str(s)[:10])
    except (TypeError, ValueError):
        return None


def from_ymd(v) -> str | None:
    """Scanner earningsYmd (yyyyMMdd, often sent as a float string like "2.0261028e+07")
    -> "2026-10-28". None for blank or unparseable."""
    try:
        n = int(round(float(v)))
    except (TypeError, ValueError):
        return None
    s = f"{n:08d}"
    try:
        return date(int(s[:4]), int(s[4:6]), int(s[6:])).isoformat()
    except ValueError:
        return None


def next_report(results: list[dict], today: str) -> dict | None:
    """get_earnings_results(...)["results"] -> the next unreported quarter on or after today:
    {date, timing ("am"/"pm"/None), verified (bool), days (from today)}. None when no
    upcoming date is listed."""
    t0 = _d(today)
    best = None
    for r in results or []:
        rep = r.get("report") or {}
        d = _d(rep.get("date"))
        if d is None or t0 is None or d < t0:
            continue
        if ((r.get("eps") or {}).get("actual")) not in (None, ""):
            continue
        if best is None or d < best[0]:
            best = (d, rep)
    if best is None:
        return None
    d, rep = best
    return {"date": d.isoformat(), "timing": rep.get("timing"),
            "verified": bool(rep.get("verified")), "days": (d - t0).days}


def from_scan(ymd, today: str) -> dict | None:
    """A scanner earningsYmd value as the same shape as next_report() (verified=False:
    the scanner carries no confirmation flag)."""
    iso = from_ymd(ymd)
    t0 = _d(today)
    if iso is None or t0 is None or _d(iso) < t0:
        return None
    return {"date": iso, "timing": None, "verified": False, "days": (_d(iso) - t0).days}


def soon(info: dict | None, days: int = SOON_DAYS) -> bool:
    return bool(info) and 0 <= info["days"] <= days


def cell(info: dict | None) -> str:
    """Report cell: "Oct 29 pm (6d)", with "?" when the date is not company-verified."""
    if not info:
        return "—"
    d = _d(info["date"])
    t = f" {info['timing']}" if info.get("timing") else ""
    q = "" if info.get("verified") else "?"
    bold = "**" if soon(info) else ""
    return f"{bold}{d.strftime('%b')} {d.day}{t}{q} ({info['days']}d){bold}"


LEGEND = ("_Earnings = next report date from Robinhood: bold = inside "
          f"{SOON_DAYS} days, ? = not confirmed by the company yet, am/pm = before the open or after "
          "the close. A buy or a trim that straddles a print carries the gap risk._")
