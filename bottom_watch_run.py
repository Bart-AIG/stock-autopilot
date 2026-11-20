"""Bottom watch job: is the low of the QQQ / SPY selloff in, and is the rebound holding?

Runs on a GitHub runner after every Stock Report run and after the close
(.github/workflows/bottom-watch.yml explains the triggers).
It reads QQQ, SPY and the VIX from FMP, computes the reading with bottom_watch.py (the code
the backtest ran), writes bottom_watch_report.md and bottom_watch.json, and tells the
workflow whether to send a push. It never trades and has no broker connection.

  python3 bottom_watch_run.py              normal run (needs FMP_API_KEY)
  python3 bottom_watch_run.py --dry        print the report and the push decision, write nothing
  python3 bottom_watch_run.py --force      write even if this session's final reading is recorded
  python3 bottom_watch_run.py --offline [--price QQQ=615.03 --price SPY=695.46 --vix 35.4]
                                           use data/bottom/*.csv instead of FMP (for tests)
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import bottom_watch as bw

HERE = Path(__file__).parent
BASE = "https://financialmodelingprep.com/stable"
ET, CT = ZoneInfo("America/New_York"), ZoneInfo("America/Chicago")
SYMS = ("QQQ", "SPY")
HISTORY_DAYS = 3300          # about 9 years: far more than any selloff plus the 252-session lookback
STATE, REPORT, PUSH = HERE / "bottom_watch.json", HERE / "bottom_watch_report.md", HERE / "bottom_watch_push.txt"
REPORT_URL = "https://github.com/Bart-AIG/stock-autopilot/blob/master/bottom_watch_report.md"


# ------------------------------------------------------------------ data

def fmp(path, key):
    """GET one FMP endpoint. The key never appears in an error message."""
    url = f"{BASE}/{path}&apikey={key}"
    err = "no response"
    for i in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err = f"HTTP {e.code}"
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            err = type(e).__name__
        time.sleep(2 + 3 * i)
    raise RuntimeError(f"FMP request failed ({err}): {path.split('&')[0]}")


def daily(sym, key, today):
    rows = fmp(f"historical-price-eod/full?symbol={urllib.parse.quote(sym)}&from={today - timedelta(days=HISTORY_DAYS)}&to={today}", key)
    rows = sorted((r for r in rows if isinstance(r, dict) and r.get("close")), key=lambda r: r["date"]) if isinstance(rows, list) else []
    if len(rows) < 600:
        raise RuntimeError(f"FMP returned {len(rows)} daily bars for {sym}; need 600")
    f = lambda r, k: float(r[k]) if r.get(k) is not None else float(r["close"])
    return {"d": [r["date"][:10] for r in rows], "o": [f(r, "open") for r in rows], "h": [f(r, "high") for r in rows],
            "l": [f(r, "low") for r in rows], "c": [float(r["close"]) for r in rows], "v": [float(r.get("volume") or 0) for r in rows]}


def quote(sym, key):
    q = fmp(f"quote?symbol={urllib.parse.quote(sym)}", key)
    if not (isinstance(q, list) and q and q[0].get("price") and q[0].get("timestamp")):
        raise RuntimeError(f"FMP returned no quote for {sym}")
    return q[0]


def merge_live(B, q):
    """Make the live quote the last bar (replacing FMP's running bar for today, whose close lags).
    Returns the time of the quote. A quote older than the last daily bar changes nothing."""
    ts = datetime.fromtimestamp(float(q["timestamp"]), ET)
    day, px = ts.date().isoformat(), float(q["price"])
    hi = max(float(x) for x in (q.get("dayHigh"), px) if x)
    lo = min(float(x) for x in (q.get("dayLow"), px) if x)
    bar = {"d": day, "o": float(q.get("open") or px), "h": hi, "l": lo, "c": px, "v": float(q.get("volume") or 0)}
    if B["d"][-1] == day:
        for k in bar:
            B[k][-1] = bar[k]
    elif B["d"][-1] < day:
        for k in bar:
            B[k].append(bar[k])
    return ts


def offline(prices, vix_now):
    """Bars from the repo's backtest history, with optional live prices as one more bar."""
    def load(sym):
        R = list(csv.DictReader(open(HERE / "data" / "bottom" / f"{sym}.csv")))
        g = lambda r, k: float(r[k]) if r.get(k) not in (None, "") else float(r["close"])
        return {"d": [r["date"] for r in R], "o": [g(r, "open") for r in R], "h": [g(r, "high") for r in R],
                "l": [g(r, "low") for r in R], "c": [float(r["close"]) for r in R], "v": [float(r.get("volume") or 0) for r in R]}
    bars = {s: load(s) for s in SYMS}
    V = load("VIX")
    nxt = (datetime.fromisoformat(max(bars[s]["d"][-1] for s in SYMS)) + timedelta(days=1)).date().isoformat()
    for s, px in prices.items():
        for k, x in (("d", nxt), ("o", px), ("h", px), ("l", px), ("c", px), ("v", 0.0)):
            bars[s][k].append(x)
    if vix_now is not None:
        for k, x in (("d", nxt), ("o", vix_now), ("h", vix_now), ("l", vix_now), ("c", vix_now), ("v", 0.0)):
            V[k].append(x)
    return bars, V


# ------------------------------------------------------------------ one run

def compute(bars, V, state, model, plan, session, final, late_day, when):
    """Pure: bars and state in, (new state, report, push text, title, reasons, important) out."""
    vix_close = dict(zip(V["d"], V["c"])) if V else None
    readings = {s: bw.reading(s, bars[s], vix_close, model) for s in SYMS}
    live = [r for r in readings.values() if r["stage"] != "NO SELLOFF"]
    since = min((r["peak_date"] for r in live), default=plan["set"])
    items = bw.plan_status(plan, bars, V or {"d": [], "h": [], "c": []}, since, provisional=not final) if live or state.get("pushed") else []
    mid = model_id(model)
    if state.get("pushed") and state.get("model_id") != mid:
        # The model was re-fitted since the last push. Restate what was pushed in the new model's
        # terms, so a re-fit can never read as "the chance rose" or "fell".
        state = dict(state)
        state["pushed"] = {s: ({**v, "prob": round(readings[s]["prob"], 4), "band": readings[s]["band"]}
                               if readings.get(s, {}).get("prob") is not None else v) for s, v in state["pushed"].items()}
    why, note, important = bw.decide(state, readings, items, session, final, late_day)
    pushed = state.get("pushed") or {}
    report = bw.report(readings, items, why, when, final, pushed, model)
    push = bw.push_text(readings, items, why, when, final, pushed)
    new = dict(state)
    new.update({
        "updated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "session": session, "final": final, "model_id": mid,
        "readings": {s: {k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items() if k not in ("checks", "trend")}
                     for s, r in readings.items()},
        "plan": [{k: it.get(k) for k in ("key", "name", "state", "date")} for it in items],
    })
    if final:
        new["final_session"] = session
    if why:
        new["notified"] = {k: v for k, v in note.items() if k.startswith("plan:") or v >= (datetime.fromisoformat(session) - timedelta(days=200)).date().isoformat()}
        new["pushed"] = {s: ({"prob": round(r["prob"], 4), "band": r["band"], "stage": r["stage"], "episode": r["peak_date"], "session": session}
                             if r["stage"] != "NO SELLOFF" and r.get("prob") is not None else pushed.get(s))
                         for s, r in readings.items()}
        new["pushed"] = {s: v for s, v in new["pushed"].items() if v}
    return new, report, push, bw.headline(readings), why, important


def push_priority(important, now_et):
    """high for a change, default for the after-close summary. Between 9 pm and 7 am Eastern both
    drop a step: GitHub's own cron can deliver the fallback run hours late (5 to 8 hours, measured
    2026-11-20), and a reading of a 4 pm close should not buzz a phone at midnight."""
    night = now_et.hour >= 21 or now_et.hour < 7
    if important:
        return "default" if night else "high"
    return "low" if night else "default"


def load_state(path):
    """The state only stops repeat pushes, so a missing or unreadable file must not stop the job."""
    try:
        st = json.loads(Path(path).read_text())
        return st if isinstance(st, dict) else {}
    except FileNotFoundError:
        return {}
    except (ValueError, OSError) as e:
        print(f"::warning::bottom_watch.json could not be read ({type(e).__name__}); starting from an empty state")
        return {}


def model_id(model):
    return "+".join(model["features"]) + f":{model['intercept']}:" + ",".join(str(b) for b in model["beta"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--price", action="append", default=[])
    ap.add_argument("--vix", type=float)
    a = ap.parse_args()

    model = json.loads((HERE / "bottom_model.json").read_text())
    plan = json.loads((HERE / "bottom_watch_plan.json").read_text())
    state = load_state(STATE)
    now = datetime.now(ET)

    if a.offline:
        bars, V = offline({p.split("=")[0]: float(p.split("=")[1]) for p in a.price}, a.vix)
        session = max(bars[s]["d"][-1] for s in SYMS)
        final, late_day, note = not a.price, False, ""
    else:
        key = os.environ.get("FMP_API_KEY", "").strip()
        if not key:
            sys.exit("ERROR: FMP_API_KEY is not set")
        today = datetime.now(timezone.utc).date()
        bars, stamps = {}, []
        for s in SYMS:
            bars[s] = daily(s, key, today)
            stamps.append(merge_live(bars[s], quote(s, key)))
        try:
            V = daily("^VIX", key, today)
            merge_live(V, quote("^VIX", key))
            note = ""
        except RuntimeError as e:                      # the estimate does not use the VIX; the buy-back levels do
            V, note = None, f"VIX unavailable this run ({e}). The chance is unaffected; the buy-back levels that need a VIX reading were not checked."
            print("::warning::" + note)
        session = max(bars[s]["d"][-1] for s in SYMS)
        traded_today = session == now.date().isoformat()
        age_min = (now - max(stamps)).total_seconds() / 60
        final = (not traded_today) or (now.hour, now.minute) >= (16, 5) or (now.hour >= 13 and age_min > 45)
        late_day = traded_today and not final and now.hour >= 14
        print(f"session {session} traded_today={traded_today} final={final} late_day={late_day} quote_age_min={age_min:.0f}")

    if final and state.get("final_session") == session and not (a.force or a.dry):
        print(f"The final reading for {session} is already recorded. Nothing to do.")
        _output(False, "default", "")
        return 0

    when = datetime.now(CT).strftime("%-I:%M %p CT %a %b %-d").replace("AM", "am").replace("PM", "pm")
    new, report, push, title, why, important = compute(bars, V, state, model, plan, session, final, late_day, when)
    if note:
        report += "\n" + note + "\n"
        push += note + "\n"
    print(report)
    print("-" * 60, "\nPUSH:", "yes" if why else "no", "|", "; ".join(why))
    if a.dry:
        print("-" * 60, "\n" + push)
        return 0
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
