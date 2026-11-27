"""Joint leveraged-ETF signal job: the Friday update and the daily heads-up (set 2026-11-27).

Runs on a GitHub runner (.github/workflows/letf-signal.yml explains the triggers). Reads SPY, QQQ
and SOXX daily bars and live quotes from FMP, applies the rule in letf_signal.py, writes
letf_signal_report.md and letf_signal.json, and tells the workflow whether to push. No broker
connection, no trading: Ryan places every joint trade himself.

  python3 letf_signal_run.py            normal run (needs FMP_API_KEY)
  python3 letf_signal_run.py --dry      print the report and the push, write nothing
  python3 letf_signal_run.py --force    write even if this session's final reading is recorded
  python3 letf_signal_run.py --offline [--price SPY=720 ...] [--friday]
                                        use data/letf/*.csv instead of FMP (for checks)
"""
from __future__ import annotations

import argparse
import copy
import csv
import json
import os
import sys
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import letf_signal as ls
from bottom_watch_run import fmp, merge_live, quote

HERE = Path(__file__).parent
ET, CT = ZoneInfo("America/New_York"), ZoneInfo("America/Chicago")
SYMS = ("SPY", "QQQ", "SOXX")
HISTORY_DAYS = 1900          # about 5 years: the band state settles after the first close past a line
STATE, REPORT, PUSH = HERE / "letf_signal.json", HERE / "letf_signal_report.md", HERE / "letf_signal_push.txt"
REPORT_URL = "https://github.com/Bart-AIG/stock-autopilot/blob/master/letf_signal_report.md"


def daily(sym, key, today):
    rows = fmp(f"historical-price-eod/full?symbol={urllib.parse.quote(sym)}&from={today - timedelta(days=HISTORY_DAYS)}&to={today}", key)
    rows = sorted((r for r in rows if isinstance(r, dict) and r.get("close")), key=lambda r: r["date"]) if isinstance(rows, list) else []
    if len(rows) < 600:
        raise RuntimeError(f"FMP returned {len(rows)} daily bars for {sym}; need 600")
    f = lambda r, k: float(r[k]) if r.get(k) is not None else float(r["close"])
    return {"d": [r["date"][:10] for r in rows], "o": [f(r, "open") for r in rows], "h": [f(r, "high") for r in rows],
            "l": [f(r, "low") for r in rows], "c": [float(r["close"]) for r in rows], "v": [float(r.get("volume") or 0) for r in rows]}


def offline_bars():
    out = {}
    for s in SYMS:
        R = list(csv.DictReader(open(HERE / "data" / "letf" / f"{s}.csv")))
        out[s] = {"d": [r["date"] for r in R], "c": [float(r["close"]) for r in R]}
    return out


def act(r, confirmed, live):
    return ls.action_live(r, confirmed[r["sym"]]["state"]) if live else ls.action(r)


def report_md(confirmed, live, why, when, final, session):
    head = "after the close" if final else "during the session (live prices stand in for today's close)"
    L = [f"# Joint leveraged-ETF signal: {when}", "",
         f"Reading {head}. Session {session}. Rule and evidence: `docs/joint-letf-process.md`, `letf_joint_results.md`.",
         "Advisory only. Ryan places every joint trade himself.", ""]
    if why:
        L += ["**This run:** " + " | ".join(why), ""]
    for label, R in (("Live, if it closed now", live), ("On the last completed close", confirmed)):
        if not R:
            continue
        L += [f"## {label}", "", "| Index (fund) | Close | 200-day | vs 200-day | State | Turns ON above | Turns OFF below | 20-day vol | Size if ON |",
              "|---|---|---|---|---|---|---|---|---|"]
        for r in R.values():
            L.append(f"| {r['sym']} ({r['fund']}) | {r['close']:.2f} | {r['sma200']:.2f} | {r['vs_sma_pct']:+.1f}% | {r['state']}"
                     f"{' since ' + r['since'] if r['since'] else ''} | {r['on_line']:.2f} | {r['off_line']:.2f} | {r['vol20_pct']:.0f}% | {r['size_pct']:.0f}% |")
        L.append("")
    L += ["## What the rule says", ""] + [f"- **{r['fund']}** ({r['role']}): {act(r, confirmed, live)}" for r in (live or confirmed).values()]
    L += ["", "The signal is the close: a live price past a line is a heads-up, decided at about 2:45 pm CT or on the close. "
          "Size = share of that fund's part of the sleeve held in the 3x fund, the rest in cash. Never fund it with margin.", ""]
    return "\n".join(L)


def push_text(confirmed, live, why):
    base = live or confirmed
    out = [w for w in why] + [""] + [ls.line(r) for r in base.values()] + [""]
    out += [f"{r['fund']}: {act(r, confirmed, live)}" for r in base.values()]
    return "\n".join(out).strip() + "\n"


def title_for(why, kind, base):
    states = ", ".join(f"{r['sym']} {r['state']}" for r in base.values())
    flips = [w for w in why if " turned " in w]
    heads = [w for w in why if "If it closes there" in w]
    if flips:
        return "LETF signal: " + "; ".join(w.split(":")[0] for w in flips)
    if heads:
        return "LETF heads-up: " + ", ".join(w.split(" is ")[0] for w in heads) + " past a line"
    if kind.startswith("friday"):
        return f"LETF Friday update: {states}"
    return f"LETF signal: {states}"


def push_priority(important, now_et):
    night = now_et.hour >= 21 or now_et.hour < 7
    if important:
        return "default" if night else "high"
    return "low" if night else "default"


def load_state():
    try:
        st = json.loads(STATE.read_text())
        return st if isinstance(st, dict) else {}
    except FileNotFoundError:
        return {}
    except (ValueError, OSError) as e:
        print(f"::warning::letf_signal.json could not be read ({type(e).__name__}); starting from an empty state")
        return {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--price", action="append", default=[])
    ap.add_argument("--friday", action="store_true")
    a = ap.parse_args()
    state = load_state()
    now = datetime.now(ET)

    if a.offline:
        base = offline_bars()
        prices = {p.split("=")[0]: float(p.split("=")[1]) for p in a.price}
        session = max(base[s]["d"][-1] for s in SYMS)
        final = not prices
        live_bars = None
        if prices:
            session = (datetime.fromisoformat(session) + timedelta(days=1)).date().isoformat()
            live_bars = {s: {"d": base[s]["d"] + [session], "c": base[s]["c"] + [prices.get(s, base[s]["c"][-1])]} for s in SYMS}
        conf_bars = base
        friday_window = a.friday and not final
    else:
        key = os.environ.get("FMP_API_KEY", "").strip()
        if not key:
            sys.exit("ERROR: FMP_API_KEY is not set")
        today = datetime.now(timezone.utc).date()
        raw, live_bars, stamps = {}, {}, []
        for s in SYMS:
            raw[s] = daily(s, key, today)
            live_bars[s] = copy.deepcopy(raw[s])
            stamps.append(merge_live(live_bars[s], quote(s, key)))
        session = max(live_bars[s]["d"][-1] for s in SYMS)
        traded_today = session == now.date().isoformat()
        age_min = (now - max(stamps)).total_seconds() / 60
        final = (not traded_today) or (now.hour, now.minute) >= (16, 5) or (now.hour >= 13 and age_min > 45)
        friday_window = traded_today and not final and now.weekday() == 4 and now.hour >= 14
        if final:
            conf_bars, live_bars = live_bars, None
        else:     # completed closes only: drop FMP's running bar for today
            conf_bars = {s: {k: (v[:-1] if raw[s]["d"][-1] == session else v) for k, v in raw[s].items()} for s in SYMS}
        print(f"session {session} traded_today={traded_today} final={final} friday_window={friday_window} quote_age_min={age_min:.0f}")

    if final and state.get("final_session") == session and not (a.force or a.dry):
        print(f"The final reading for {session} is already recorded. Nothing to do.")
        _output(False, "default", "")
        return 0

    confirmed = {s: ls.reading(s, conf_bars[s]["d"], conf_bars[s]["c"]) for s in SYMS}
    live = {s: ls.reading(s, live_bars[s]["d"], live_bars[s]["c"]) for s in SYMS} if live_bars else None
    new, why, important, kind = ls.decide(confirmed, live, state, session, final, friday_window)
    when = datetime.now(CT).strftime("%-I:%M %p CT %a %b %-d").replace("AM", "am").replace("PM", "pm")
    report = report_md(confirmed, live, why, when, final, session)
    push = push_text(confirmed, live, why)
    title = title_for(why, kind, live or confirmed)
    print(report)
    print("-" * 60, "\nPUSH:", "yes" if why else "no", "|", title)
    if a.dry:
        print("-" * 60, "\n" + push)
        return 0
    new["updated_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    STATE.write_text(json.dumps(new, indent=1) + "\n")
    REPORT.write_text(report)
    PUSH.write_text(push)
    _output(bool(why), push_priority(important, now), title)
    return 0


def _output(notify, priority, title):
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a") as fh:
            fh.write(f"notify={'true' if notify else 'false'}\npriority={priority}\ntitle={title}\n")


if __name__ == "__main__":
    sys.exit(main())
