"""Wash-sale watch for Ryan's JOINT account (set 2026-10-23, Ryan's live turn).

Ryan asked for a reminder list of names he must not buy back yet: *"maybe we just make a
list on robinhood and the routine updates it"*, then *"yes please"*.

The rule (IRS wash sale, 30 days either side): a loss on a sale is disallowed now if the
same stock is bought within 30 days BEFORE or AFTER that sale, in ANY of the taxpayer's
accounts (a spouse's and IRAs included). A disallowed loss in a taxable account is not
gone: it moves into the new shares' cost and comes back when those shares are sold. A
buy inside an IRA disallows it for good.

What this module computes, all pure functions, no network (the Quality @ 200-day routine
fetches with the Robinhood connector, step 4e of docs/quality-watch-prompt.md):

    lockouts()       names sold at a LOSS in the joint account in the last 30 days, with
                     the total loss and the first safe buy date (last loss sale + 31 days)
    buys_in_window() buys in ANY account that fall inside a lockout's window: those
                     losses are already deferred (washed). An IRA buy is flagged as
                     permanent.
    sell_traps()     names held now that were bought in the last 30 days: selling them at
                     a loss before the date shown is washed by that recent buy
    events()         what changed since the last run (locked, cleared) for the reminder
    report()         markdown section for quality_watch_report.md

Honest limits: this is a reminder, not tax advice and not a block (Robinhood still lets a
locked name be bought). It covers stock trades only: an OPTION on a locked stock can also
trigger a wash sale and is not checked. Lot-level matching (which shares are washed and by
how much) is the broker's 1099, not this file; the dollar figures here are the realized
losses as the broker reported them on each sale.
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

STATE = Path(__file__).resolve().parent / "wash_sale_watch.json"
WINDOW_DAYS = 30            # either side of the loss sale
MIN_LOSS_USD = 1.0          # ignore rounding-size losses (e.g. -$0.16 on a fractional)
JOINT = "116713985343"
IRA_TYPES = ("ira_roth", "ira_traditional")


def _d(s: str) -> date:
    return date.fromisoformat(str(s)[:10])


def clear_date(last_loss_sale: str) -> str:
    """First date a buy no longer washes the loss (last loss sale + 31 days)."""
    return (_d(last_loss_sale) + timedelta(days=WINDOW_DAYS + 1)).isoformat()


def _stock(sym: str) -> bool:
    s = (sym or "").strip()
    return bool(s) and s.replace(".", "").isalnum() and s.upper() == s


def lockouts(trades: list[dict], today: str) -> dict[str, dict]:
    """Joint-account loss sales whose 30-day window is still open.

    trades: get_pnl_trade_history rows {timestamp, symbol, side, quantity, price,
    realized_gain}. Returns {symbol: {loss_usd, last_loss_sale, clear, sales}} for every
    symbol with a loss sale on or after today - 30 days (so clear > today)."""
    t0 = _d(today)
    out: dict[str, dict] = {}
    for t in trades:
        sym = (t.get("symbol") or "").strip().upper()
        if not _stock(sym) or (t.get("side") or "sell") != "sell":
            continue
        try:
            g = float(t.get("realized_gain"))
        except (TypeError, ValueError):
            continue
        d = _d(t.get("timestamp"))
        if g >= 0 or d < t0 - timedelta(days=WINDOW_DAYS) or d > t0:
            continue
        r = out.setdefault(sym, {"loss_usd": 0.0, "last_loss_sale": d.isoformat(), "sales": 0})
        r["loss_usd"] = round(r["loss_usd"] + g, 2)
        r["sales"] += 1
        if d.isoformat() > r["last_loss_sale"]:
            r["last_loss_sale"] = d.isoformat()
    out = {s: r for s, r in out.items() if -r["loss_usd"] >= MIN_LOSS_USD}
    for r in out.values():
        r["clear"] = clear_date(r["last_loss_sale"])
    return dict(sorted(out.items(), key=lambda kv: (kv[1]["clear"], kv[0])))


def buys_in_window(locks: dict[str, dict], orders: list[dict], trades: list[dict],
                   account_types: dict[str, str] | None = None) -> list[dict]:
    """Buys of a locked symbol within 30 days of one of its loss sales, any account.

    orders: filled get_equity_orders rows, each tagged with "account_number" by the
    caller. account_types: {account_number: brokerage_account_type} from get_accounts.
    One row per (symbol, account): latest such buy and total shares bought in the window
    (only that many shares' worth of the loss is washed). "permanent" is True for an IRA
    buy (that part of the loss can never be used). "managed" marks buys Ryan did not place
    himself (Robinhood managed portfolios = "advisory", the agentic sleeves = "agentic")."""
    types = account_types or {}
    sale_days: dict[str, list[date]] = {}
    for t in trades:
        sym = (t.get("symbol") or "").strip().upper()
        try:
            g = float(t.get("realized_gain"))
        except (TypeError, ValueError):
            continue
        if sym in locks and g < 0:
            sale_days.setdefault(sym, []).append(_d(t.get("timestamp")))
    hits: dict[tuple[str, str], dict] = {}
    for o in orders:
        sym = (o.get("symbol") or "").strip().upper()
        if sym not in locks or o.get("side") != "buy" or float(o.get("cumulative_quantity") or 0) <= 0:
            continue
        bd = _d(o.get("last_transaction_at") or o.get("created_at"))
        if not any(abs((bd - sd).days) <= WINDOW_DAYS for sd in sale_days.get(sym, [])):
            continue
        acct = str(o.get("account_number") or JOINT)
        key = (sym, acct)
        q = float(o.get("cumulative_quantity") or 0)
        h = hits.setdefault(key, {"symbol": sym, "account": acct, "buy_date": "", "shares": 0.0,
                                  "after_sale": False,
                                  "permanent": types.get(acct, "") in IRA_TYPES,
                                  "recurring": o.get("placed_agent") == "recurring",
                                  "managed": o.get("placed_agent") in ("advisory", "agentic")})
        h["shares"] = round(h["shares"] + q, 4)
        h["after_sale"] = h["after_sale"] or any(bd > sd for sd in sale_days.get(sym, []))
        if bd.isoformat() > h["buy_date"]:
            h["buy_date"] = bd.isoformat()
    return sorted(hits.values(), key=lambda h: (h["symbol"], h["account"]))


def sell_traps(positions: list[dict], orders: list[dict], today: str) -> dict[str, str]:
    """Joint names held now and bought (in any account) in the last 30 days.

    Selling one of these at a loss before the returned date is washed by that buy.
    Returns {symbol: first date a loss sale is clean (last buy + 31 days)}."""
    t0 = _d(today)
    held = {(p.get("symbol") or "").upper() for p in positions
            if float(p.get("quantity") or 0) > 0 and _stock(p.get("symbol") or "")}
    last: dict[str, date] = {}
    for o in orders:
        sym = (o.get("symbol") or "").strip().upper()
        if sym not in held or o.get("side") != "buy" or float(o.get("cumulative_quantity") or 0) <= 0:
            continue
        bd = _d(o.get("last_transaction_at") or o.get("created_at"))
        if t0 - timedelta(days=WINDOW_DAYS) <= bd <= t0 and (sym not in last or bd > last[sym]):
            last[sym] = bd
    return {s: (d + timedelta(days=WINDOW_DAYS + 1)).isoformat() for s, d in sorted(last.items())}


def events(prev: dict[str, dict], now: dict[str, dict]) -> dict[str, list[str]]:
    """Names that ENTERED the lockout, CLEARED it, or had their date pushed out by a new
    loss sale since the last run."""
    return {
        "locked": sorted(s for s in now if s not in prev),
        "cleared": sorted(s for s in prev if s not in now),
        "extended": sorted(s for s in now if s in prev and now[s]["clear"] > prev[s].get("clear", "")),
    }


def watchlist_symbols(state: dict) -> list[str]:
    """Contents of the 🤖 Wash-Sale Lockout list: locked names, soonest-clearing first."""
    locks = state.get("lockouts") or {}
    return sorted(locks, key=lambda s: (locks[s].get("clear", ""), s))


def load_state(path: Path = STATE) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def report(locks: dict[str, dict], hits: list[dict], traps: dict[str, str],
           ev: dict[str, list[str]], today: str) -> str:
    """Markdown section for quality_watch_report.md."""
    lines = ["## Wash-sale watch (joint account)", ""]
    if ev.get("cleared"):
        lines.append("**Cleared, safe to buy again:** " + ", ".join(ev["cleared"]))
    if ev.get("locked"):
        lines.append("**Newly locked:** " + ", ".join(
            f"{s} (loss ${-locks[s]['loss_usd']:,.0f}, safe after {locks[s]['clear']})" for s in ev["locked"]))
    if ev.get("extended"):
        lines.append("**Date pushed out by a new loss sale:** " + ", ".join(
            f"{s} -> {locks[s]['clear']}" for s in ev["extended"]))
    if len(lines) > 2:
        lines.append("")
    if locks:
        total = sum(-r["loss_usd"] for r in locks.values())
        lines += [f"{len(locks)} name(s) locked, ${total:,.0f} of losses. Buying one before its date "
                  "defers that loss into the new shares (an IRA buy loses it for good).", "",
                  "| Safe to buy after | Name | Loss | Sales |", "|---|---|---|---|"]
        for s, r in locks.items():
            lines.append(f"| {r['clear']} | {s} | ${-r['loss_usd']:,.0f} | {r['sales']} |")
    else:
        lines.append("No names locked.")
    bad = [h for h in hits if h["after_sale"] and not h["recurring"] and not h["managed"]]
    auto = [h for h in hits if h["managed"]]
    rec = [h for h in hits if h["recurring"]]
    if bad:
        lines += ["", "**You bought inside the window (that part of the loss is deferred):** " + ", ".join(
            f"{h['symbol']} {h['shares']:g} sh {h['buy_date']}" + (" IN AN IRA: lost for good" if h["permanent"] else "")
            + ("" if h["account"] == JOINT else f" (acct ...{h['account'][-4:]})") for h in bad)]
    if auto:
        lines += ["", "Managed portfolios / sleeves bought locked names (only these shares' worth is washed): "
                  + ", ".join(f"{h['symbol']} {h['shares']:g} sh (...{h['account'][-4:]}{', IRA' if h['permanent'] else ''})" for h in auto)]
    if rec:
        lines += ["", "Recurring buys keep washing small losses on: " + ", ".join(sorted({h['symbol'] for h in rec}))]
    if traps:
        lines += ["", "**Sell trap:** these were bought in the last 30 days, so selling them at a loss "
                  "before the date is washed: " + ", ".join(f"{s} ({d})" for s, d in traps.items())]
    lines += ["", f"_As of {today}. A reminder, not tax advice: the 1099 decides. Options on a locked "
              "stock can also trigger a wash sale and are not checked._"]
    return "\n".join(lines) + "\n"
