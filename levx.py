"""
LEVX sleeve: liquid leveraged index funds, owned overnight and on intraday breakouts.

STATUS: APPROVED 2026-11-13 at 10% of the base, funded from SWING_Q (Ryan, live turn). It
trades on the first routine run whose prompt carries the LEVX duties (v19).
Evidence: levx_results.md. Spec: docs/levx-sleeve.md.

Two legs, both rules are formulas (no stops, no targets, no news gate):
  NIGHT  At about 15:50 ET buy each fund whose INDEX is above its 200-day SMA (today's live
         price counted in). Size = the fund's night share x min(1, 40% / annualised volatility
         of its last 20 overnight returns). Sell everything at the first run after the next
         open (about 09:31-09:35 ET).
  DAY    TQQQ only. At each :00 / :30 bar close from 10:00 to 15:30 ET the fund is held if
         that close is above the band and not held otherwise. Band = max(today's open,
         prior close) x (1 + its average move from the open at that time of day over the
         last 14 sessions). Flat by the NIGHT decision, which then sets the overnight size.
         (Noise-area breakout, Zarattini, Aziz & Barbon 2024, long side only. Their VWAP
         trailing stop is left out: on TQQQ it changed no result, see levx_results.md.)

Commands
  python levx.py build                      (GitHub Actions, FMP key) -> levx_inputs.json
  python levx.py decide LIVE.json --now ISO-UTC [--tv SLEEVE_MONEY]
        (--tv is sleeve money since 2026-11-13: total value minus Ryan's own positions, capital.py)
        LIVE.json = {"quotes": {"QQQ": px, "SOXX": px, "TQQQ": px, "SOXL": px},
                     "bars5": {"TQQQ": [Robinhood 5-minute bars for today]}}
        Prints the mode (paper / live / paused), the phase and each fund's target as a
        fraction of the sleeve (and dollars). A target of null means "no usable price data:
        leave the position as it is".
  python levx.py score                      scorecard and pause check from levx_state.json
The backtest (simulate) and the live decision (decide) call the same pure functions;
test_levx.py checks them against an independent implementation.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
INPUTS = HERE / "levx_inputs.json"
STATE = HERE / "levx_state.json"
ET = ZoneInfo("America/New_York")

W_LEVX = 0.10                # share of the investable base (0.0 = paper). Set 2026-11-13, from SWING_Q. Only a live Ryan turn changes it.
INVEST_FRAC = 0.95           # same 5% operational reserve as sleeves.py
FUNDS = {
    "TQQQ": {"index": "QQQ", "night_share": 0.5, "day": True},
    "SOXL": {"index": "SOXX", "night_share": 0.5, "day": False},
}
DAY_SHARE = 1.0              # the DAY leg uses the whole sleeve (the night capital is idle in the day)
SMA_N = 200
VOL_N = 20
VOL_TARGET = 0.40
SIGMA_N = 14
SIGMA_MIN = 10               # sessions needed before a band is trusted
CHECKS = [f"{h:02d}:{m:02d}" for h in range(10, 16) for m in (0, 30) if (h, m) <= (15, 30)]   # bar-CLOSE times, ET
MORNING_END = "10:00"        # before this, the only action is selling the night position
NIGHT_FROM, NIGHT_TO = "15:45", "16:00"
FRESH_MIN = 12               # a DAY entry is taken only within this many minutes of its signal bar
EARLY_CLOSE = {"2026-11-27", "2026-12-24", "2027-11-26"}   # 13:00 ET closes: morning exit only
DD_NOTIFY, DD_PAUSE = -0.30, -0.40     # sleeve drawdown from its own high: tell Ryan / stop new entries
COST_BP = {"TQQQ": 3.0, "SOXL": 4.0}   # round-trip cost the backtest charges (1.5 and 2 bp a side)
COST_MIN_TRIPS = 20                    # round trips needed before the measured cost is judged
PAPER_SLEEVE_USD = 500.0               # notional used for the paper log while W_LEVX is 0


# ----------------------------------------------------------------------------- pure rules

def night_weight(index_px: float, prior_sum: float, overnight: list[float]) -> dict:
    """NIGHT size for one fund, as a fraction of its night share.
    prior_sum = sum of the index's last SMA_N-1 completed closes; overnight = the fund's
    completed overnight returns, oldest first (the last VOL_N are used)."""
    sma = (prior_sum + index_px) / SMA_N
    gate = index_px > sma
    o = [x for x in overnight if x is not None][-VOL_N:]
    vol = None
    if len(o) >= VOL_N // 2:
        m = sum(o) / len(o)
        vol = math.sqrt(sum((x - m) ** 2 for x in o) / (len(o) - 1)) * math.sqrt(252)
    w = 0.0
    if gate and vol:
        w = min(1.0, VOL_TARGET / vol)
    return {"gate": bool(gate), "sma200": sma, "vol": vol, "weight": w}


def sigma_profile(sessions: list[dict]) -> dict[str, float]:
    """Average absolute move from the open at each check time over the given sessions.
    sessions = [{"open": px, "closes": {"10:00": px, ...}}, ...], the last SIGMA_N are used."""
    use = sessions[-SIGMA_N:]
    out = {}
    for t in CHECKS:
        v = [abs(s["closes"][t] / s["open"] - 1) for s in use if s.get("open") and t in s.get("closes", {})]
        if len(v) >= SIGMA_MIN:
            out[t] = sum(v) / len(v)
    return out


def day_replay(bars: list[tuple], prev_close: float, sigma: dict[str, float], upto: str | None = None) -> dict:
    """Replay today's DAY checks. bars = [(start "HH:MM" ET, o, h, l, c, v), ...] in time order,
    regular session. A check at T reads the bar that STARTS five minutes before T.
    Returns the state after the last check at or before `upto`."""
    if not bars:
        return {"in": False, "entered_at": None, "last_check": None, "trades": 0, "log": []}
    by = {b[0]: b for b in bars}
    op = bars[0][1]
    ref = max(op, prev_close)
    state, entered, last, n, log = False, None, None, 0, []
    for t in CHECKS:
        if upto is not None and t > upto:
            break
        hh, mm = int(t[:2]), int(t[3:])
        start = f"{(hh * 60 + mm - 5) // 60:02d}:{(hh * 60 + mm - 5) % 60:02d}"
        b = by.get(start)
        s = sigma.get(t)
        if b is None or s is None:
            continue
        last = t
        band, c = ref * (1 + s), b[4]
        if state and not c > band:
            state = False
            log.append((t, "sell", c))
        elif not state and c > band:
            state, entered, n = True, t, n + 1
            log.append((t, "buy", c))
    return {"in": state, "entered_at": entered if state else None, "last_check": last, "trades": n, "log": log,
            "ref": ref}


def phase_of(now_et: datetime) -> str:
    d, hm = now_et.date().isoformat(), now_et.strftime("%H:%M")
    if now_et.weekday() >= 5 or hm < "09:30" or hm >= "16:00":
        return "closed"
    if d in EARLY_CLOSE:
        return "morning" if hm < "13:00" else "closed"
    if hm < MORNING_END:
        return "morning"
    if NIGHT_FROM <= hm < NIGHT_TO:
        return "night"
    return "day"


def norm_bars(rh_bars: list[dict], day: date) -> list[tuple]:
    """Robinhood 5-minute bars -> [(start HH:MM ET, o, h, l, c, v)] for `day`'s regular session."""
    out = []
    for b in sorted(rh_bars, key=lambda x: x["begins_at"]):
        if b.get("interpolated"):
            continue
        t = datetime.fromisoformat(b["begins_at"].replace("Z", "+00:00")).astimezone(ET)
        hm = t.strftime("%H:%M")
        if t.date() != day or not ("09:30" <= hm <= "15:55"):
            continue
        out.append((hm, float(b["open_price"]), float(b["high_price"]), float(b["low_price"]),
                    float(b["close_price"]), float(b.get("volume") or 0)))
    return out


def decide(inputs: dict, live: dict, now_utc: datetime) -> dict:
    """One live decision. Returns each fund's target as a fraction of the sleeve.
    `buy_ok` False means: do not open or add, only reduce to the target."""
    now_et = now_utc.astimezone(ET)
    ph = phase_of(now_et)
    out = {"phase": ph, "now_et": now_et.isoformat(timespec="minutes"), "targets": {}, "detail": {}}
    session = now_et.date().isoformat()
    stale = inputs.get("for_session") != session
    out["stale_inputs"] = stale
    for f in FUNDS:
        out["targets"][f] = {"frac": 0.0, "buy_ok": False}
    if ph in ("closed", "morning"):
        return out
    if stale:
        out["note"] = f"levx_inputs.json is for {inputs.get('for_session')}, not {session}: sell-only this run"
        return out
    q = live.get("quotes") or {}
    if ph == "night":
        for f, cfg in FUNDS.items():
            fi = inputs["funds"][f]
            px = q.get(cfg["index"])
            if not px:
                out["detail"][f] = {"error": f"no live quote for {cfg['index']}"}
                continue
            nw = night_weight(float(px), fi["index_prior_sum"], fi["overnight"])
            out["targets"][f] = {"frac": round(cfg["night_share"] * nw["weight"], 4), "buy_ok": True}
            out["detail"][f] = {"index": cfg["index"], "index_px": float(px), "sma200": round(nw["sma200"], 4),
                                "above_200d": nw["gate"], "night_vol": None if nw["vol"] is None else round(nw["vol"], 4),
                                "weight": round(nw["weight"], 4)}
        return out
    # day phase
    hm = now_et.strftime("%H:%M")
    for f, cfg in FUNDS.items():
        if not cfg["day"]:
            continue
        fi = inputs["funds"][f]
        bars = norm_bars((live.get("bars5") or {}).get(f) or [], now_et.date())
        due = max((t for t in CHECKS if t <= hm), default=None)
        need = None
        if due:
            m = int(due[:2]) * 60 + int(due[3:]) - 5
            need = f"{m // 60:02d}:{m % 60:02d}"
        if not bars or bars[0][0] != "09:30" or (need and need not in {b[0] for b in bars}):
            # a hole in the feed is not a signal: leave the position alone, open nothing
            out["targets"][f] = {"frac": None, "buy_ok": False}
            out["detail"][f] = {"error": f"5-minute bars incomplete (need 09:30 and {need}, got {len(bars)} bars): "
                                         "hold what is held, no entry"}
            continue
        st = day_replay(bars, fi["prev_close"], fi.get("sigma") or {}, upto=hm)
        fresh = False
        if st["in"] and st["entered_at"] == st["last_check"]:
            t = st["entered_at"]
            sig_t = now_et.replace(hour=int(t[:2]), minute=int(t[3:]), second=0, microsecond=0)
            fresh = 0 <= (now_et - sig_t).total_seconds() <= FRESH_MIN * 60
        out["targets"][f] = {"frac": DAY_SHARE if st["in"] else 0.0, "buy_ok": bool(fresh)}
        out["detail"][f] = {"in": st["in"], "entered_at": st["entered_at"], "last_check": st["last_check"],
                            "fresh_entry": fresh, "bars": len(bars), "ref": round(st["ref"], 4), "log": st["log"][-4:]}
        if len(bars) > 1 and bars[1][0] == "09:35" and bars[0][5] < 0.2 * bars[1][5]:
            # Robinhood sometimes returns one minute in place of a 5-minute bar; then the open is off
            out["detail"][f]["warning"] = "the 09:30 bar has very little volume: today's open may be misread"
    return out


def sleeve_usd(total_value: float) -> float:
    """LEVX's dollars. Pass SLEEVE MONEY (capital.py), not total account value."""
    return INVEST_FRAC * W_LEVX * total_value


# ----------------------------------------------------------------------------- backtest

def simulate(fund: dict, index_prior_sum: list[float], index_px: list[float], day_leg: bool,
             cost: float, lag: int = 1, b_night: int = 75, b_exit: int = 0, exit_open: bool = False) -> list[dict]:
    """Day-by-day replay of the live rules on 5-minute sessions.
    fund = {"days": [...], "O","H","L","C","V": rows of 78, "pc": prior closes}. index_prior_sum[d]
    and index_px[d] are the 200-day inputs at day d's NIGHT decision. Night entries fill at bar
    b_night's close (15:50), night exits at bar b_exit's close next session (09:35), or at the
    session's first print when exit_open is set (a sell queued after the bell); DAY orders
    fill `lag` bars after the signal bar. Returns one row per day."""
    O, H, Lo, C, V, pc = (fund[k] for k in ("O", "H", "L", "C", "V", "pc"))
    days = fund["days"]
    n = len(days)
    slots = [f"{(570 + 5 * i) // 60:02d}:{(570 + 5 * i) % 60:02d}" for i in range(78)]
    bar_of = {t: i for i, t in enumerate(slots)}
    overnight: list[float] = []            # completed nights, through yesterday's open
    hist: list[dict] = []
    rows = []
    held_w = 0.0
    entry_px = None
    for d in range(n):
        row = {"day": days[d], "night_ret": 0.0, "day_ret": 0.0, "night_w": 0.0, "day_trades": 0}
        # 1. sell last night's position at the morning exit
        if held_w > 0 and entry_px:
            out_px = O[d][0] if exit_open else C[d][b_exit]
            row["night_ret"] = held_w * (out_px / entry_px - 1 - 2 * cost)
            row["night_w"] = held_w
        held_w, entry_px = 0.0, None
        # 2. DAY leg
        if day_leg:
            sig = sigma_profile(hist)
            bars = [(slots[i], O[d][i], H[d][i], Lo[d][i], C[d][i], V[d][i]) for i in range(78)]
            st = day_replay(bars, pc[d], sig)
            acc, pos_px = 1.0, None
            for t, what, _ in st["log"]:
                fill = C[d][min(bar_of[t] - 1 + lag, 77)]
                if what == "buy":
                    pos_px = fill
                else:
                    acc *= fill / pos_px * (1 - 2 * cost)
                    pos_px = None
            if pos_px is not None:                      # still long at the NIGHT decision: flatten there
                acc *= C[d][b_night] / pos_px * (1 - 2 * cost)
            row["day_ret"] = DAY_SHARE * (acc - 1)
            row["day_trades"] = st["trades"]
            row["day_held_to_night"] = pos_px is not None
        # 3. NIGHT decision
        if index_prior_sum[d] is not None and index_px[d] is not None:
            nw = night_weight(index_px[d], index_prior_sum[d], overnight)
            near = d + 1 < n and (days[d + 1] - days[d]).days <= 5
            if nw["weight"] > 0 and near:
                held_w, entry_px = nw["weight"], C[d][b_night]
        # 4. roll the histories forward (what tomorrow's build will know)
        if d > 0:
            overnight.append(O[d][0] / C[d - 1][77] - 1)
        hist.append({"open": O[d][0], "closes": {t: C[d][bar_of[t] - 1] for t in CHECKS}})
        rows.append(row)
    return rows


# ----------------------------------------------------------------------------- state and scorecard

def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"status": "active", "paper_sleeve_usd": PAPER_SLEEVE_USD, "positions": {}, "trade_log": []}


def mode_of(state: dict) -> str:
    """paper while W_LEVX is 0; paused when the pause rule or Ryan stopped entries; else live."""
    if state.get("status") == "paused":
        return "paused"
    return "live" if W_LEVX > 0 else "paper"


def scorecard(state: dict, paper: bool | None = None) -> dict:
    """Results from the trade log. Each row is one closed round trip:
    {fund, leg, out (ISO time), weight (position dollars / sleeve dollars at entry), ret
     (exit / entry - 1), slip_in_bp, slip_out_bp, late, paper}.
    slip_in_bp = (buy fill / quote mid just before the order - 1) x 1e4; slip_out_bp =
    (quote mid / sell fill - 1) x 1e4. Their sum is the measured round-trip cost, judged
    against COST_BP once a fund has COST_MIN_TRIPS of them: above 2x the backtest's cost is
    "notify" (the 2x-cost backtest is the planning case); above 4x is "propose_pause" (at 4x
    the sleeve tested below QQQ).
    A day's sleeve return is (1 + sum of night weight x ret) x (1 + sum of day weight x ret) - 1,
    the same compounding the backtest uses. `paper` filters the rows (None = all)."""
    rows = [r for r in state.get("trade_log", []) if paper is None or bool(r.get("paper")) == paper]
    by_day: dict[str, dict[str, float]] = {}
    legs: dict[str, dict] = {}
    slip: dict[str, list[float]] = {}
    for r in rows:
        d = datetime.fromisoformat(r["out"].replace("Z", "+00:00")).astimezone(ET).date().isoformat()
        contrib = float(r["weight"]) * float(r["ret"])
        by_day.setdefault(d, {"night": 0.0, "day": 0.0})[r["leg"]] += contrib
        g = legs.setdefault(r["leg"], {"trades": 0, "wins": 0, "sum_ret": 0.0, "contribution": 0.0, "late": 0})
        g["trades"] += 1
        g["wins"] += r["ret"] > 0
        g["sum_ret"] += float(r["ret"])
        g["contribution"] += contrib
        g["late"] += bool(r.get("late"))
        if r.get("slip_in_bp") is not None and r.get("slip_out_bp") is not None:
            slip.setdefault(r["fund"], []).append(float(r["slip_in_bp"]) + float(r["slip_out_bp"]))
    eq = hwm = 1.0
    worst = 0.0
    for d in sorted(by_day):
        eq *= (1 + by_day[d]["night"]) * (1 + by_day[d]["day"])
        hwm = max(hwm, eq)
        worst = min(worst, eq / hwm - 1)
    dd = eq / hwm - 1
    for g in legs.values():
        g["win_rate"] = round(g["wins"] / g["trades"], 3)
        g["avg_ret_bp"] = round(g.pop("sum_ret") / g["trades"] * 1e4, 1)
        g["contribution"] = round(g["contribution"], 5)
    costs = {}
    for f, v in slip.items():
        avg, model = sum(v) / len(v), COST_BP.get(f)
        chk = "too_few"
        if model and len(v) >= COST_MIN_TRIPS:
            chk = "propose_pause" if avg > 4 * model else "notify" if avg > 2 * model else "ok"
        costs[f] = {"n": len(v), "avg": round(avg, 1), "backtest": model, "check": chk}
    return {"days": len(by_day), "return": round(eq - 1, 5), "drawdown": round(dd, 5), "worst_drawdown": round(worst, 5),
            "legs": legs, "round_trip_cost_bp": costs,
            "check": "pause" if dd <= DD_PAUSE else "notify" if dd <= DD_NOTIFY else "ok"}


# ----------------------------------------------------------------------------- build (Actions)

def _fmp(url: str):
    import urllib.error
    import urllib.request
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(3 + 3 * attempt)
                continue
            return None
        except Exception:  # noqa: BLE001
            time.sleep(2)
    return None


def _eod(sym: str, key: str, days: int = 420) -> list[dict]:
    base = "https://financialmodelingprep.com/stable"
    frm = (date.today() - timedelta(days=days)).isoformat()
    data = _fmp(f"{base}/historical-price-eod/full?symbol={sym}&from={frm}&to={date.today()}&apikey={key}")
    if not isinstance(data, list):
        return []
    return sorted(({"date": r["date"][:10], "open": float(r["open"]), "close": float(r["close"])}
                   for r in data if r.get("close") and r.get("open")), key=lambda r: r["date"])


def _m5(sym: str, key: str, days: int = 32) -> dict[str, dict[str, tuple]]:
    base = "https://financialmodelingprep.com/stable"
    out: dict[str, dict[str, tuple]] = {}
    d, end = date.today() - timedelta(days=days), date.today()
    while d <= end:
        e = min(d + timedelta(days=6), end)
        data = _fmp(f"{base}/historical-chart/5min?symbol={sym}&from={d}&to={e}&apikey={key}")
        for r in data if isinstance(data, list) else []:
            day, hm = r["date"][:10], r["date"][11:16]
            if "09:30" <= hm <= "15:55":
                out.setdefault(day, {})[hm] = (float(r["open"]), float(r["close"]))
        d = e + timedelta(days=1)
        time.sleep(0.2)
    return out


def build(key: str) -> dict:
    from sleeves import is_session, next_session
    now = datetime.now(timezone.utc)
    et_now = now.astimezone(ET)
    today = et_now.date().isoformat()

    def done(rows):          # drop a bar for a session that has not closed yet
        if rows and rows[-1]["date"] == today and (et_now.hour, et_now.minute) < (16, 5):
            return rows[:-1]
        return rows

    funds, asof = {}, None
    for f, cfg in FUNDS.items():
        idx = done(_eod(cfg["index"], key))
        fd = done(_eod(f, key))
        if len(idx) < SMA_N or len(fd) < VOL_N + 2:
            raise SystemExit(f"{f}: not enough history")
        if idx[-1]["date"] != fd[-1]["date"]:
            raise SystemExit(f"{f}: index and fund bars end on different days")
        asof = asof or fd[-1]["date"]
        if fd[-1]["date"] != asof:
            raise SystemExit("funds end on different days")
        overnight = [fd[i]["open"] / fd[i - 1]["close"] - 1 for i in range(1, len(fd))][-VOL_N:]
        rec = {"index": cfg["index"], "night_share": cfg["night_share"],
               "index_prior_sum": round(sum(r["close"] for r in idx[-(SMA_N - 1):]), 4),
               "index_last_close": idx[-1]["close"], "prev_close": fd[-1]["close"],
               "overnight": [round(x, 6) for x in overnight]}
        if cfg["day"]:
            m5 = _m5(f, key)
            sess = []
            for day in sorted(m5):
                if day > asof or len(m5[day]) < 74 or "09:30" not in m5[day]:
                    continue
                closes = {}
                for t in CHECKS:
                    hh, mm = int(t[:2]), int(t[3:])
                    st = f"{(hh * 60 + mm - 5) // 60:02d}:{(hh * 60 + mm - 5) % 60:02d}"
                    if st in m5[day]:
                        closes[t] = m5[day][st][1]
                sess.append({"date": day, "open": m5[day]["09:30"][0], "closes": closes})
            use = sess[-SIGMA_N:]
            rec["sigma"] = {t: round(v, 6) for t, v in sigma_profile(use).items()}
            rec["sigma_sessions"] = [s["date"] for s in use]
            if len(rec["sigma"]) < len(CHECKS):
                raise SystemExit(f"{f}: sigma profile incomplete ({len(rec['sigma'])} of {len(CHECKS)} checks)")
            # a throttled 5-minute request leaves a silent hole: the profile must be the last
            # SIGMA_N full sessions of the daily calendar, or the build fails (sells only that day)
            want = [r["date"] for r in fd if r["date"] not in EARLY_CLOSE][-SIGMA_N:]
            if rec["sigma_sessions"] != want:
                missing = sorted(set(want) - set(rec["sigma_sessions"]))
                raise SystemExit(f"{f}: 5-minute history has gaps, missing sessions {missing}")
        funds[f] = rec
    nxt = next_session(date.fromisoformat(asof)).isoformat()
    return {"built_utc": now.isoformat(timespec="seconds"), "asof": asof, "for_session": nxt,
            "params": {"sma": SMA_N, "vol_n": VOL_N, "vol_target": VOL_TARGET, "sigma_n": SIGMA_N,
                       "checks": CHECKS, "day_share": DAY_SHARE, "w_levx": W_LEVX},
            "funds": funds}


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "build":
        key = os.environ.get("FMP_API_KEY", "").strip()
        if not key:
            print("FMP_API_KEY not set")
            return 1
        st = build(key)
        INPUTS.write_text(json.dumps(st, indent=1) + "\n")
        print(f"levx_inputs.json: as of {st['asof']}, for session {st['for_session']}")
        for f, r in st["funds"].items():
            nw = night_weight(r["index_last_close"], r["index_prior_sum"], r["overnight"])
            print(f"  {f}: {r['index']} last {r['index_last_close']:.2f} vs 200d {nw['sma200']:.2f} "
                  f"({'above' if nw['gate'] else 'BELOW'}), night vol {nw['vol']:.0%}, weight {nw['weight']:.2f}")
        return 0
    if len(argv) >= 3 and argv[1] == "decide":
        live = json.loads(Path(argv[2]).read_text())
        now = datetime.now(timezone.utc)
        if "--now" in argv:
            now = datetime.fromisoformat(argv[argv.index("--now") + 1].replace("Z", "+00:00"))
        inputs = json.loads(INPUTS.read_text())
        out = decide(inputs, live, now)
        state = load_state()
        out["mode"] = mode_of(state)
        if out["mode"] == "paused":                      # exits still run; nothing is opened or added
            for t in out["targets"].values():
                t["buy_ok"] = False
        if "--tv" in argv:
            tv = float(argv[argv.index("--tv") + 1])
            live_usd = sleeve_usd(tv)
            out["sleeve_usd"] = round(live_usd if W_LEVX > 0 else float(state.get("paper_sleeve_usd", PAPER_SLEEVE_USD)), 2)
            for f, t in out["targets"].items():
                t["usd"] = None if t["frac"] is None else round(t["frac"] * out["sleeve_usd"], 2)
        print(json.dumps(out, indent=1))
        return 0
    if len(argv) >= 2 and argv[1] == "score":
        state = load_state()
        print(json.dumps({"mode": mode_of(state), "all": scorecard(state), "live_only": scorecard(state, paper=False),
                          "paper_only": scorecard(state, paper=True)}, indent=1))
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
