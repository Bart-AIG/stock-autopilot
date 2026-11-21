"""Margin ladder: when may Ryan raise the joint account's borrowing limit, and what does he buy?

Pure functions, no network. bottom_watch_run.py calls run() on every bottom-watch reading with the
same QQQ / SPY / VIX bars, writes margin_ladder.json and margin_ladder_report.md, and pushes when
something changed. The plan is margin_ladder_plan.json (Ryan's live turns 2026-11-21).

Advisory only: the agent never trades the joint account and never changes the borrowing limit.

Rules, all on closing prices:
  * A stage unlocks when its dip trigger has happened since the plan was set, or its confirmation
    trigger holds on today's close, AND the date is on or after plan["not_before"], AND no de-lever
    fired in the last plan["cooldown_sessions"] sessions. At most one stage per session, in order.
  * A de-lever rule fires on a close when the ladder is at or above its from_stage; the ladder
    drops to to_stage (the most severe rule wins) and has to earn the stages back.
  * A provisional (intraday) reading never moves the ladder. It only shows what the close would do.
"""
from __future__ import annotations

from datetime import date

SYMS = ("QQQ", "SPY")


def _sma(c, n, end=None):
    end = len(c) if end is None else end
    if end < n:
        return None
    return sum(c[end - n:end]) / n


def metrics(B, since):
    """Closing-price facts for one symbol's bars (oldest first)."""
    c = B["c"]
    hi = max(c[-252:])
    window = [i for i, d in enumerate(B["d"]) if d >= since] or [len(c) - 1]
    lo_i = min(window, key=lambda i: (c[i], -i))
    return {
        "date": B["d"][-1], "close": c[-1], "sma50": _sma(c, 50), "sma200": _sma(c, 200),
        "sma200_20ago": _sma(c, 200, len(c) - 20), "high252": hi,
        "low": c[lo_i], "low_date": B["d"][lo_i], "since_low": len(c) - 1 - lo_i,
    }


def _vix_max(V, since, upto):
    return max(((h if h is not None else c) for d, h, c in zip(V["d"], V["h"], V["c"])
                if since <= d <= upto and c is not None), default=0.0)


def dip_date(plan, stage, bars, V):
    """First session on/after the plan was set when the dip trigger was met, else None."""
    dip = stage.get("dip")
    if not dip or not V:
        return None
    best = None
    for s in SYMS:
        if s not in dip:
            continue
        B = bars[s]
        ri = next((i for i, d in enumerate(B["d"]) if d >= plan["set"] and B["l"][i] <= dip[s]), None)
        if ri is None:
            continue
        mi = next((i for i in range(ri, len(B["d"]))
                   if B["c"][i] >= (B["h"][i] + B["l"][i]) / 2
                   and _vix_max(V, plan["vix_spike_since"], B["d"][i]) >= plan["vix_spike"]), None)
        if mi is not None and (best is None or B["d"][mi] < best):
            best = B["d"][mi]
    return best


def confirm_parts(stage, m, vix):
    """[(text, ok)] for the confirmation trigger on today's close."""
    cf = stage.get("confirm") or {}
    parts = []
    ok_syms = []
    for s in SYMS:
        x = m[s]
        if "above" in cf:
            lvl = cf["above"][s]
            ok_syms.append((s, x["close"] > lvl, f"{s} ${x['close']:,.2f} vs ${lvl:,.0f}"))
        elif "above_sma" in cf:
            lvl = x["sma%d" % cf["above_sma"]]
            ok_syms.append((s, lvl is not None and x["close"] > lvl,
                            f"{s} ${x['close']:,.2f} vs its {cf['above_sma']}-day ${lvl:,.2f}" if lvl else f"{s}: not enough history"))
        elif "near_high" in cf:
            lvl = x["high252"] * (1 - cf["near_high"])
            ok_syms.append((s, x["close"] >= lvl, f"{s} ${x['close']:,.2f} vs ${lvl:,.2f} ({cf['near_high']:.0%} under its high ${x['high252']:,.2f})"))
    if ok_syms:
        if cf.get("any"):
            parts.append((" or ".join(t for _, _, t in ok_syms), any(o for _, o, _ in ok_syms)))
        else:
            parts += [(t, o) for _, o, t in ok_syms]
    if "vix_below" in cf:
        parts.append((f"VIX close {vix:.2f} under {cf['vix_below']}" if vix is not None else "VIX unavailable",
                      vix is not None and vix < cf["vix_below"]))
    if "sessions_no_new_low" in cf:
        n = m["QQQ"]["since_low"]
        parts.append((f"QQQ {n} sessions without a new closing low (needs {cf['sessions_no_new_low']})", n >= cf["sessions_no_new_low"]))
    if cf.get("sma200_rising"):
        a, b = m["QQQ"]["sma200"], m["QQQ"]["sma200_20ago"]
        parts.append((f"QQQ 200-day rising (${b:,.2f} 20 sessions ago, ${a:,.2f} now)" if a and b else "QQQ 200-day: not enough history",
                      bool(a and b and a > b)))
    return parts


def delever_fired(plan, stage_now, m, vix):
    """[(rule, to_stage)] for every de-lever rule that applies on this close."""
    q = m["QQQ"]
    tests = {
        "below_50d": q["sma50"] is not None and q["close"] < q["sma50"],
        "below_200d": q["sma200"] is not None and q["close"] < q["sma200"],
        "new_selloff": q["close"] <= 0.90 * q["high252"] or (vix is not None and vix > 30),
    }
    return [r for r in plan["delever"] if stage_now >= r["from_stage"] and tests.get(r["key"])]


def _money(x):
    return f"${x:,.0f}"


def _buys_text(stage):
    return ", ".join(f"{s} {_money(v)}" for s, v in stage["buys"].items())


def run(plan, bars, V, state, session, final):
    """Returns (new_state, status, push_lines). push_lines is [] when nothing is worth a push."""
    if state.get("set") != plan["set"]:
        state = {"set": plan["set"], "stage": 0, "history": [], "notified": {}}
    st = dict(state)
    st["notified"] = dict(state.get("notified") or {})
    st["history"] = list(state.get("history") or [])
    since = plan.get("vix_spike_since", plan["set"])
    m = {s: metrics(bars[s], since) for s in SYMS}
    vix = V["c"][-1] if V and V["c"] and V["d"][-1] == session else None
    stages = {s["n"]: s for s in plan["stages"]}
    stage_now = int(st.get("stage", 0))
    push = []
    qd = bars["QQQ"]["d"]

    def sessions_since(d):
        return sum(1 for x in qd if x > d)

    # ---- de-lever first (closing prices only)
    fired = delever_fired(plan, stage_now, m, vix)
    if final and fired:
        to = min(r["to_stage"] for r in fired)
        if to < stage_now:
            st["history"].append({"session": session, "event": "delever", "from": stage_now, "to": to, "rules": [r["key"] for r in fired]})
            st["last_delever"] = session
            push.append(f"DE-LEVER: cut margin to {_money(stages[to]['limit']) if to else '$0'} (stage {to}).")
            push += [f"  {r['text']}" for r in fired]
            stage_now = to
    # ---- one stage up per session
    cool = st.get("last_delever")
    cooling = bool(cool) and sessions_since(cool) < plan.get("cooldown_sessions", 5)
    status_stages = []
    for n in sorted(stages):
        s = stages[n]
        dd = dip_date(plan, s, bars, V)
        parts = confirm_parts(s, m, vix)
        conf_ok = bool(parts) and all(o for _, o in parts)
        status_stages.append({"n": n, "limit": s["limit"], "spend": s["spend"], "buys": s["buys"],
                              "dip_text": (s.get("dip") or {}).get("text"), "dip_date": dd,
                              "confirm_text": s["confirm"]["text"], "confirm_parts": [{"text": t, "ok": o} for t, o in parts],
                              "confirm_ok": conf_ok, "note": s.get("note")})
    nxt = stage_now + 1
    if nxt in stages:
        row = status_stages[nxt - 1]
        trig = row["dip_date"] or (session if row["confirm_ok"] else None)
        path = "dip" if row["dip_date"] else ("confirmation" if row["confirm_ok"] else None)
        waiting_date = session < plan["not_before"]
        already = (st["history"] and st["history"][-1]["session"] == session)
        if trig and final and not waiting_date and not cooling and not already:
            s = stages[nxt]
            st["history"].append({"session": session, "event": "unlock", "stage": nxt, "path": path, "trigger_date": trig})
            push.append(f"STAGE {nxt} UNLOCKED ({path} trigger, {trig}).")
            push.append(f"  1. Raise the joint borrowing limit to {_money(s['limit'])}.")
            push.append(f"  2. Buy: {_buys_text(s)} (about {_money(s['spend'])}).")
            if s.get("note"):
                push.append(f"  {s['note']}")
            stage_now = nxt
        elif trig and final and waiting_date:
            k = f"wait:{nxt}"
            if k not in st["notified"]:
                st["notified"][k] = session
                push.append(f"Stage {nxt} trigger met ({path}, {trig}), but it waits for {plan['not_before']} (wash-sale locks). No margin yet.")
    st["stage"] = stage_now
    # ---- trims coming due
    for t in plan.get("trims", []):
        k = f"trim:{t['sym']}:{t['after']}"
        if session >= t["after"] and final and k not in st["notified"]:
            st["notified"][k] = session
            push.append(f"Now allowed: {t['text']}")
    st["session"] = session
    st["final"] = final
    nx = status_stages[stage_now] if stage_now < len(status_stages) else None
    status = {
        "session": session, "final": final, "stage": stage_now,
        "limit": stages[stage_now]["limit"] if stage_now else 0,
        "max_limit": max(s["limit"] for s in plan["stages"]),
        "not_before": plan["not_before"], "cooling": cooling,
        "market": {s: {k: (round(v, 2) if isinstance(v, float) else v) for k, v in m[s].items()} for s in SYMS},
        "vix": vix, "vix_spike_high": round(_vix_max(V, since, session), 2) if V else None,
        "stages": status_stages, "next": nx["n"] if nx else None,
        "delever_watch": [{"key": r["key"], "text": r["text"], "from_stage": r["from_stage"],
                           "active": stage_now >= r["from_stage"],
                           "firing": r in delever_fired(plan, max(stage_now, r["from_stage"]), m, vix)} for r in plan["delever"]],
        "trims": [{**t, "due": session >= t["after"]} for t in plan.get("trims", [])],
        "history": st["history"],
    }
    return st, status, push


def report(plan, status, when):
    """Markdown for margin_ladder_report.md."""
    st = status
    L = [f"Margin ladder: stage {st['stage']} of 4, borrowing limit {_money(st['limit'])}", "",
         f"**{when}{'' if st['final'] else ' (provisional, the close decides)'}.** Joint account, advisory: you raise the limit and place the orders.", ""]
    q, s = st["market"]["QQQ"], st["market"]["SPY"]
    L.append(f"QQQ ${q['close']:,.2f} (50-day ${q['sma50']:,.2f}, 200-day ${q['sma200']:,.2f}, high ${q['high252']:,.2f}). "
             f"SPY ${s['close']:,.2f} (50-day ${s['sma50']:,.2f}, 200-day ${s['sma200']:,.2f}, high ${s['high252']:,.2f}). "
             + (f"VIX {st['vix']:.2f}." if st["vix"] is not None else "VIX unavailable."))
    L.append("")
    if st["session"] < st["not_before"]:
        L += [f"No margin stage can unlock before **{st['not_before']}** (wash-sale locks).", ""]
    if st["cooling"]:
        L += ["A de-lever fired in the last 5 sessions: no stage up until the cooldown ends.", ""]
    L += ["| Stage | Limit | Status | Dip trigger | Confirmation trigger | Buys |", "|---|---|---|---|---|---|"]
    for r in st["stages"]:
        if r["n"] <= st["stage"]:
            state = "DONE"
        elif r["n"] == st["stage"] + 1:
            state = "NEXT"
        else:
            state = "later"
        dip = (f"met {r['dip_date']}" if r["dip_date"] else "not met") if r["dip_text"] else "none"
        conf = "; ".join(("yes: " if p["ok"] else "no: ") + p["text"] for p in r["confirm_parts"])
        L.append(f"| {r['n']} | {_money(r['limit'])} | {state} | {dip} | {conf} | {_buys_text(r)} |")
    L += ["", "**De-lever rules** (they apply from the stage shown):", ""]
    for d in st["delever_watch"]:
        flag = "FIRING" if (d["active"] and d["firing"]) else ("armed" if d["active"] else f"from stage {d['from_stage']}")
        L.append(f"- [{flag}] {d['text']}")
    L += ["", "**Cash-only trims:**", ""]
    for t in st["trims"]:
        L.append(f"- {'Allowed now' if t['due'] else 'From ' + t['after']}: {t['text']}")
    L += ["", "**Hard rules:** " + " ".join(plan["hard_rules"]), ""]
    if st["history"]:
        L += ["**History:**", ""] + [f"- {h['session']}: {h['event']} " + (f"to stage {h.get('stage')}" if h['event'] == 'unlock' else f"{h['from']} to {h['to']} ({', '.join(h['rules'])})") for h in st["history"]] + [""]
    return "\n".join(L) + "\n"
