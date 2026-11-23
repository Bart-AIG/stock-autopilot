"""Same-day option trades on QQQ / SPY: first-pass backtest (Ryan, live turn 2026-11-23).

Question: can a same-day trade in a short-dated option (bought and sold the
same session, never held overnight) make money from intraday signals?

Structure tested (fixed before any result was seen):
  * Underlyings QQQ and SPY. Option = the strike nearest the entry price,
    expiring 2 trading days after the entry day (inside the 1-3 DTE band), a
    call for a long signal and a put for a short one, 1 contract.
  * Entries 10:00-14:30 ET (9:00 AM-1:30 PM CT). Hard exit at the 15:50 ET bar
    open (2:50 PM CT). At most 2 entries per day per strategy per symbol, one
    position at a time. Signals use bars up to and including bar i; the entry
    fills at the OPEN of bar i+1 (no look-ahead).
  * Option value from Black-Scholes in trading time (each session = 1/252 of a
    year, so a 1-hour hold costs 1/6.5 of a day's time decay, which is
    conservative against an option's real intraday decay), implied volatility
    = prior-day VIX close x 1.30 for QQQ and x 1.05 for SPY, held fixed through
    the trade. Cost per round trip $0.06 (QQQ) / $0.05 (SPY) per share, from
    the spreads quoted on 2026-11-23 plus fees; also reported at 2x.

Strategies:
  A  Time-of-day noise band (the LEVX DAY leg rule, both directions). At each
     :00/:30 close, upper band = max(open, prior close) x (1 + average
     |close/open - 1| at that time over the prior 14 sessions), lower band the
     mirror. Close above the upper band = long, below the lower = short. Exit
     at the next :00/:30 close back inside the band, or 15:50.
  B  Trend pullback on 5-minute bars. Long: close > session VWAP, EMA9 > EMA21,
     RSI(14) was below 40 within the prior 3 bars and is now rising with a
     higher close. Short is the mirror (VWAP below, EMA9 < EMA21, RSI was
     above 60, now falling). Stop = the 3-bar swing low (high), target = 2x
     risk, 90-minute time stop, 15:50 hard exit.
  C  Range fade. From 11:00 ET: RSI(14) > 70 with the bar's high within 0.15%
     of the session high = short (put); RSI < 30 at the session low = long.
     Stop 0.10% beyond the session extreme, target the session midpoint
     (taken only when reward >= risk), 90-minute time stop, 15:50 hard exit.
  R  Control: random entry time and direction in the same window, held 60
     minutes, same option and costs (100 seeds, matched trade count).

Pass bar, set before the run: positive expected profit per trade at 2x costs
in BOTH halves of the sample (Feb 23-Jun 30, Jul 1-Nov 23) and on BOTH
symbols, and a win rate above the break-even rate its payoff implies. A pass
here only earns the 5-minute 2018-2026 re-test (step 2); it is not a licence
to trade.

Data: Robinhood 5-minute bars 2026-02-23..2026-11-23 (data/intraday5/), all
78 bars present on all 191 sessions; about 4% of bars carry a volume hole,
which can understate a bar's high/low. VIX daily closes from
data/bottom/VIX.csv (Cboe), 2026-11-20 added from bottom_watch_report.md.

Run: python3 sameday_options_backtest.py  (writes sameday_options_results.md)
"""
import csv
import json
import math
import random
import statistics as st
from collections import defaultdict
from datetime import datetime, date, time
from statistics import NormalDist
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
N = NormalDist()
R_RATE = 0.04
IV_MULT = {"QQQ": 1.30, "SPY": 1.05}
COST = {"QQQ": 0.06, "SPY": 0.05}          # $ per share, round trip
ENTRY_FIRST, ENTRY_LAST = time(10, 0), time(14, 30)   # signal bar CLOSE times
HARD_EXIT = time(15, 50)                   # exit at this bar's open
MAX_ENTRIES = 2
SPLIT = date(2026, 7, 1)
VIX_EXTRA = {date(2026, 11, 20): 35.90}


# ---------------------------------------------------------------- data
def load_bars(sym):
    rows = json.load(open(f"data/intraday5/{sym}.json"))
    days = defaultdict(list)
    for ts, o, h, l, c, v in rows:
        t = datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(ET)
        days[t.date()].append(dict(t=t, o=o, h=h, l=l, c=c, v=v))
    out = []
    for d in sorted(days):
        bars = sorted(days[d], key=lambda b: b["t"])
        assert len(bars) == 78, (sym, d, len(bars))
        out.append((d, bars))
    return out


def load_vix():
    vix = {}
    for r in csv.DictReader(open("data/bottom/VIX.csv")):
        vix[date.fromisoformat(r["date"])] = float(r["close"])
    vix.update(VIX_EXTRA)
    return vix


def prior_vix(vix, d):
    prev = [k for k in vix if k < d]
    return vix[max(prev)]


# ---------------------------------------------------------------- indicators
def add_indicators(days):
    """EMA9/21 and Wilder RSI14 continuous across sessions; VWAP per session."""
    k9, k21 = 2 / 10, 2 / 22
    e9 = e21 = None
    gain = loss = None
    prev_c = None
    n = 0
    for _, bars in days:
        cpv = cv = 0.0
        for b in bars:
            c = b["c"]
            e9 = c if e9 is None else c * k9 + e9 * (1 - k9)
            e21 = c if e21 is None else c * k21 + e21 * (1 - k21)
            b["ema9"], b["ema21"] = e9, e21
            if prev_c is not None:
                ch = c - prev_c
                g, lo = max(ch, 0.0), max(-ch, 0.0)
                n += 1
                if n <= 14:
                    gain = (gain or 0) + g / 14
                    loss = (loss or 0) + lo / 14
                else:
                    gain = (gain * 13 + g) / 14
                    loss = (loss * 13 + lo) / 14
            b["rsi"] = None if n < 14 else (100.0 if loss == 0 else 100 - 100 / (1 + gain / loss))
            prev_c = c
            tp = (b["h"] + b["l"] + c) / 3
            cpv += tp * b["v"]
            cv += b["v"]
            b["vwap"] = cpv / cv if cv else c


def close_time(b):
    """5-minute bar labelled by its start; its close is 5 minutes later."""
    m = b["t"].hour * 60 + b["t"].minute + 5
    return time(m // 60, m % 60)


# ---------------------------------------------------------------- option model
def bs(S, K, T, v, cp):
    if T <= 0:
        return max(S - K, 0.0) if cp == "C" else max(K - S, 0.0)
    d1 = (math.log(S / K) + (R_RATE + v * v / 2) * T) / (v * math.sqrt(T))
    d2 = d1 - v * math.sqrt(T)
    c = S * N.cdf(d1) - K * math.exp(-R_RATE * T) * N.cdf(d2)
    return c if cp == "C" else c - S + K * math.exp(-R_RATE * T)


DECAY_W = 1.0   # 1.0 = trading time (conservative); 0.27 = calendar time (6.5 of 24 hours)


def tdays_left(t):
    """Trading days from time t to the close of the option's expiry day (entry day + 2 sessions).
    DECAY_W scales how much of a full day's time decay the session itself carries."""
    mins_left_today = max(0, (16 * 60) - (t.hour * 60 + t.minute))
    return DECAY_W * mins_left_today / 390 + 2


def option_pnl(sym, direction, t_in, s_in, t_out, s_out, iv, cost_mult=1.0):
    cp = "C" if direction > 0 else "P"
    K = round(s_in)
    T_in = tdays_left(t_in) / 252
    T_out = tdays_left(t_out) / 252
    p_in = bs(s_in, K, T_in, iv, cp)
    p_out = bs(s_out, K, T_out, iv, cp)
    pnl = p_out - p_in - COST[sym] * cost_mult
    return pnl * 100, p_in * 100     # $ per contract, premium paid


# ---------------------------------------------------------------- trade engine
def manage(bars, i_in, direction, stop, target, max_bars):
    """Walk bars from the entry bar; returns (exit index, exit price, reason)."""
    entry = bars[i_in]["o"]
    for j in range(i_in, len(bars)):
        b = bars[j]
        if b["t"].time() >= HARD_EXIT:
            return j, b["o"], "hard"
        if j - i_in >= max_bars:
            return j, b["o"], "time"
        if direction > 0:
            hit_stop = stop is not None and b["l"] <= stop
            hit_tgt = target is not None and b["h"] >= target
            if hit_stop:
                return j, min(stop, b["o"]), "stop"
            if hit_tgt:
                return j, max(target, b["o"]), "target"
        else:
            hit_stop = stop is not None and b["h"] >= stop
            hit_tgt = target is not None and b["l"] <= target
            if hit_stop:
                return j, max(stop, b["o"]), "stop"
            if hit_tgt:
                return j, min(target, b["o"]), "target"
    return len(bars) - 1, bars[-1]["c"], "eod"


def strat_B(day, bars, use_ema=True):
    trades = []
    i = 3
    entries = 0
    while i < len(bars) - 1 and entries < MAX_ENTRIES:
        b = bars[i]
        ct = close_time(b)
        if not (ENTRY_FIRST <= ct <= ENTRY_LAST) or b["rsi"] is None or bars[i - 1]["rsi"] is None:
            i += 1
            continue
        prior = [bars[k]["rsi"] for k in range(i - 3, i) if bars[k]["rsi"] is not None]
        sig = 0
        up = b["ema9"] > b["ema21"] if use_ema else True
        dn = b["ema9"] < b["ema21"] if use_ema else True
        if b["c"] > b["vwap"] and up and prior and min(prior) < 40 \
                and b["rsi"] > bars[i - 1]["rsi"] and b["c"] > bars[i - 1]["c"]:
            sig = 1
        elif b["c"] < b["vwap"] and dn and prior and max(prior) > 60 \
                and b["rsi"] < bars[i - 1]["rsi"] and b["c"] < bars[i - 1]["c"]:
            sig = -1
        if sig:
            i_in = i + 1
            entry = bars[i_in]["o"]
            if sig > 0:
                stop = min(bars[k]["l"] for k in range(i - 2, i + 1))
                risk = entry - stop
            else:
                stop = max(bars[k]["h"] for k in range(i - 2, i + 1))
                risk = stop - entry
            if risk > 0:
                target = entry + 2 * risk * sig
                j, px, why = manage(bars, i_in, sig, stop, target, 18)
                trades.append((day, bars[i_in]["t"], sig, entry, bars[j]["t"], px, why))
                entries += 1
                i = j + 1
                continue
        i += 1
    return trades


def strat_C(day, bars):
    trades = []
    i = 1
    entries = 0
    while i < len(bars) - 1 and entries < MAX_ENTRIES:
        b = bars[i]
        ct = close_time(b)
        if not (time(11, 0) <= ct <= ENTRY_LAST) or b["rsi"] is None:
            i += 1
            continue
        sh = max(x["h"] for x in bars[: i + 1])
        sl = min(x["l"] for x in bars[: i + 1])
        mid = (sh + sl) / 2
        sig = 0
        if b["rsi"] > 70 and b["h"] >= sh * (1 - 0.0015):
            sig = -1
        elif b["rsi"] < 30 and b["l"] <= sl * (1 + 0.0015):
            sig = 1
        if sig:
            i_in = i + 1
            entry = bars[i_in]["o"]
            if sig < 0:
                stop, target = sh * 1.001, mid
                risk, reward = stop - entry, entry - target
            else:
                stop, target = sl * 0.999, mid
                risk, reward = entry - stop, target - entry
            if risk > 0 and reward >= risk:
                j, px, why = manage(bars, i_in, sig, stop, target, 18)
                trades.append((day, bars[i_in]["t"], sig, entry, bars[j]["t"], px, why))
                entries += 1
                i = j + 1
                continue
        i += 1
    return trades


CHECKS = [time(h, m) for h in range(10, 16) for m in (0, 30) if time(h, m) <= time(15, 30)]


def strat_A(days):
    """Needs 14 prior sessions for the time-of-day average move."""
    trades = []
    for n in range(15, len(days)):
        day, bars = days[n]
        O = bars[0]["o"]
        PC = days[n - 1][1][-1]["c"]
        idx = {close_time(b): k for k, b in enumerate(bars)}
        sigma = {}
        for t in CHECKS:
            moves = []
            for m in range(n - 14, n):
                pb = days[m][1]
                pidx = {close_time(b): k for k, b in enumerate(pb)}
                moves.append(abs(pb[pidx[t]]["c"] / pb[0]["o"] - 1))
            sigma[t] = sum(moves) / len(moves)
        pos = 0
        entries = 0
        cur = None
        for t in CHECKS:
            k = idx[t]
            c = bars[k]["c"]
            ub = max(O, PC) * (1 + sigma[t])
            lb = min(O, PC) * (1 - sigma[t])
            if pos == 0 and entries < MAX_ENTRIES and t <= ENTRY_LAST:
                sig = 1 if c > ub else (-1 if c < lb else 0)
                if sig:
                    i_in = k + 1
                    pos = sig
                    cur = (bars[i_in]["t"], bars[i_in]["o"])
                    entries += 1
            elif pos != 0:
                still = (c > ub) if pos > 0 else (c < lb)
                if not still:
                    i_out = k + 1
                    trades.append((day, cur[0], pos, cur[1], bars[i_out]["t"], bars[i_out]["o"], "band"))
                    pos = 0
        if pos != 0:
            k = idx[time(15, 50)] - 1   # the 15:45 bar closes at 15:50; exit at the 15:50 bar open
            k_exit = k + 1
            trades.append((day, cur[0], pos, cur[1], bars[k_exit]["t"], bars[k_exit]["o"], "hard"))
    return trades


def strat_R(days, n_trades, seed):
    rnd = random.Random(seed)
    trades = []
    usable = days[15:]
    for _ in range(n_trades):
        day, bars = rnd.choice(usable)
        cands = [k for k, b in enumerate(bars) if ENTRY_FIRST <= close_time(b) <= ENTRY_LAST and k + 13 < len(bars)]
        k = rnd.choice(cands)
        sig = rnd.choice((1, -1))
        i_in = k + 1
        j, px, why = manage(bars, i_in, sig, None, None, 12)
        trades.append((day, bars[i_in]["t"], sig, bars[i_in]["o"], bars[j]["t"], px, why))
    return trades


# ---------------------------------------------------------------- scoring
def score(sym, trades, vix, cost_mult=1.0):
    rows = []
    for day, t_in, sig, s_in, t_out, s_out, why in trades:
        iv = prior_vix(vix, day) / 100 * IV_MULT[sym]
        pnl, prem = option_pnl(sym, sig, t_in, s_in, t_out, s_out, iv, cost_mult)
        und_bps = sig * (s_out / s_in - 1) * 1e4
        rows.append(dict(day=day, sig=sig, pnl=pnl, prem=prem, bps=und_bps, why=why,
                         mins=(t_out - t_in).total_seconds() / 60))
    return rows


def stats(rows):
    if not rows:
        return dict(n=0)
    p = [r["pnl"] for r in rows]
    wins = [x for x in p if x > 0]
    losses = [x for x in p if x <= 0]
    aw = st.mean(wins) if wins else 0.0
    al = -st.mean(losses) if losses else 0.0
    be = al / (aw + al) if (aw + al) else float("nan")
    sd = st.pstdev(p) if len(p) > 1 else 0.0
    eq = 0.0
    peak = 0.0
    mdd = 0.0
    for x in p:
        eq += x
        peak = max(peak, eq)
        mdd = min(mdd, eq - peak)
    return dict(n=len(p), win=len(wins) / len(p), aw=aw, al=al, be=be, exp=st.mean(p),
                exp_pct=st.mean(r["pnl"] / r["prem"] for r in rows if r["prem"] > 0),
                tot=sum(p), t=(st.mean(p) / (sd / math.sqrt(len(p))) if sd else 0.0),
                mdd=mdd, bps=st.mean(r["bps"] for r in rows),
                mins=st.mean(r["mins"] for r in rows), longs=sum(r["sig"] > 0 for r in rows))


def fmt(s):
    if s["n"] == 0:
        return "| 0 | | | | | | | | |"
    return (f"| {s['n']} | {s['win']*100:.0f}% | {s['be']*100:.0f}% | ${s['aw']:.0f} / ${s['al']:.0f} | "
            f"**${s['exp']:+.1f}** ({s['exp_pct']*100:+.1f}%) | {s['t']:+.2f} | ${s['tot']:+,.0f} | ${s['mdd']:,.0f} | "
            f"{s['bps']:+.1f} | {s['mins']:.0f} |")


HDR = ("| Trades | Win rate | Break-even win rate | Avg win / avg loss | Expected P/L per trade (% of premium) "
       "| t-stat | Total | Worst drawdown | Underlying bps per trade | Avg hold (min) |\n"
       "|---|---|---|---|---|---|---|---|---|---|")


def main():
    vix = load_vix()
    out = ["# Same-day option trades on QQQ / SPY: first-pass backtest",
           "",
           "Generated by `sameday_options_backtest.py` (see its docstring for every rule, set before the run). "
           "Robinhood 5-minute bars 2026-02-23..2026-11-23, 191 sessions; option P/L modeled with Black-Scholes "
           "from prior-day VIX (QQQ x1.30, SPY x1.05), 1 contract, strike nearest the entry, expiry 2 sessions out, "
           "costs $0.06/$0.05 per share round trip (2x also shown). Per-trade P/L is in dollars per contract.",
           ""]
    verdicts = {}
    for sym in ("QQQ", "SPY"):
        days = load_bars(sym)
        add_indicators(days)
        tr = {"A": strat_A(days)}
        tr["B"] = [t for d, b in days[15:] for t in strat_B(d, b)]
        tr["C"] = [t for d, b in days[15:] for t in strat_C(d, b)]
        tr["B2"] = [t for d, b in days[15:] for t in strat_B(d, b, use_ema=False)]
        out += [f"## {sym}", ""]
        for name in ("A", "B", "B2", "C"):
            label = {"A": "A: time-of-day noise band", "B": "B: trend pullback (VWAP / EMA9>21 / RSI)",
                     "B2": "B2 (added AFTER seeing B fire 7-10 times; lower evidentiary weight): B without the EMA filter",
                     "C": "C: range fade (RSI at session extreme)"}[name]
            out += [f"### {label}", "", "| Sample | Costs " + HDR.split("\n")[0][1:], "|---|---|" + HDR.split("\n")[1][1:]]
            for cm in (1.0, 2.0):
                rows = score(sym, tr[name], vix, cm)
                h1 = [r for r in rows if r["day"] < SPLIT]
                h2 = [r for r in rows if r["day"] >= SPLIT]
                for lab, rs in (("All", rows), ("Feb-Jun", h1), ("Jul-Nov", h2)):
                    out.append(f"| {lab} | {cm:.0f}x " + fmt(stats(rs)))
                if cm == 2.0:
                    verdicts[(sym, name)] = (stats(h1), stats(h2))
            rows = score(sym, tr[name], vix, 1.0)
            reasons = defaultdict(int)
            for r in rows:
                reasons[r["why"]] += 1
            out += ["", "Exit reasons: " + ", ".join(f"{k} {v}" for k, v in sorted(reasons.items())), ""]
        # random control matched to strategy B's count
        n_ctrl = max(len(tr["B"]), 50)
        ctrl = [stats(score(sym, strat_R(days, n_ctrl, seed), vix, 1.0)) for seed in range(100)]
        out += [f"### R: random-entry control ({n_ctrl} trades x 100 seeds, 60-minute hold, 1x costs)", "",
                f"Median expected P/L per trade ${st.median(c['exp'] for c in ctrl):+.1f} "
                f"({st.median(c['exp_pct'] for c in ctrl)*100:+.1f}% of premium); "
                f"5th-95th percentile of the seed means ${sorted(c['exp'] for c in ctrl)[4]:+.1f} to "
                f"${sorted(c['exp'] for c in ctrl)[94]:+.1f}. A strategy has to beat this band to show any skill.", ""]
    global DECAY_W
    out += ["## Sensitivity: lighter intraday time decay (calendar time, 0.27 of a day per session)", "",
            "The base case charges a full trading day's decay across the session, which is conservative. "
            "This is the optimistic bound; real decay sits between the two. 1x costs, full sample.", "",
            "| Strategy | QQQ expected P/L per trade | SPY expected P/L per trade |", "|---|---|---|"]
    DECAY_W = 0.27
    light = {}
    for sym in ("QQQ", "SPY"):
        days = load_bars(sym)
        add_indicators(days)
        light[(sym, "A")] = stats(score(sym, strat_A(days), vix))
        light[(sym, "B2")] = stats(score(sym, [t for d, b in days[15:] for t in strat_B(d, b, use_ema=False)], vix))
        light[(sym, "C")] = stats(score(sym, [t for d, b in days[15:] for t in strat_C(d, b)], vix))
        light[(sym, "R")] = st.median(stats(score(sym, strat_R(days, 100, seed), vix))["exp"] for seed in range(50))
    for name in ("A", "B2", "C"):
        out.append(f"| {name} | ${light[('QQQ', name)]['exp']:+.1f} (n={light[('QQQ', name)]['n']}) | "
                   f"${light[('SPY', name)]['exp']:+.1f} (n={light[('SPY', name)]['n']}) |")
    out.append(f"| R (random control, median) | ${light[('QQQ', 'R')]:+.1f} | ${light[('SPY', 'R')]:+.1f} |")
    out.append("")
    DECAY_W = 1.0
    out += ["## Verdict against the pass bar (2x costs, both halves, both symbols)", "",
            "| Strategy | QQQ Feb-Jun | QQQ Jul-Nov | SPY Feb-Jun | SPY Jul-Nov | Pass? |", "|---|---|---|---|---|---|"]
    for name in ("A", "B", "B2", "C"):
        cells = []
        ok = True
        for sym in ("QQQ", "SPY"):
            for s in verdicts[(sym, name)]:
                good = s["n"] > 0 and s["exp"] > 0 and s["win"] > s["be"]
                ok &= good
                cells.append(f"${s['exp']:+.1f} (n={s['n']})" if s["n"] else "n=0")
        out.append(f"| {name} | " + " | ".join(cells) + f" | {'PASS' if ok else 'fail'} |")
    out += ["", "## Limits", "",
            "- Nine months, one regime (a long rally into October, then a selloff). A pass earns the 2018-2026 5-minute re-test, nothing more.",
            "- Implied volatility is a VIX multiple held fixed through each trade. Real short-dated IV moves intraday; "
            "on a selloff it rises (helps puts) and on a rally it falls (hurts calls), which this model does not capture.",
            "- About 4% of Robinhood 5-minute bars have a volume hole, which can understate a bar's high or low, so some stops and targets "
            "may be touched later than they really were.",
            "- Stops are on the underlying and checked on 5-minute bars; a real option stop fills at the option's bid, usually worse.",
            "- QQQ and SPY trades are highly correlated; the two symbols are not independent evidence."]
    open("sameday_options_results.md", "w").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
