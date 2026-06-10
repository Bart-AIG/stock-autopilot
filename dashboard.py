"""Read-only dashboard generator (NO trading, NO network).

Renders DASHBOARD.md from data the pipeline already produces:
  - logs/report_*.json   -> newest run's held_snapshot (prices/indicators) + setups
  - holdings.json        -> the open-positions ledger
  - trade_log.json       -> closed trades (appended by the trading session on sells)

Run by the GitHub Actions job right after report.py; the result is committed
alongside latest_*.md so it renders in the GitHub app. It changes nothing about
the trading process — it is a rear-view mirror, not a control panel.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from analyze import LOGS, SPECULATIVE, theme_of

HERE = Path(__file__).resolve().parent
OUT = HERE / "DASHBOARD.md"
TRADE_LOG = HERE / "trade_log.json"

SPEC_CAP_PCT = 25.0


def _load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def latest_report() -> dict | None:
    files = sorted(LOGS.glob("report_*.json"))
    return _load_json(files[-1], None) if files else None


def fmt(x, pat="{:.2f}") -> str:
    return pat.format(x) if isinstance(x, (int, float)) else "—"


def build() -> str:
    report = latest_report() or {}
    snapshot = report.get("held_snapshot", [])
    trades = _load_json(TRADE_LOG, {}).get("trades", [])
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    src = (f"{report.get('mode', '?')} run {report.get('generated_utc', '')[:16]}"
           if report else "no report found")

    lines = [f"# Dashboard — read-only  (built {now}, prices from {src})",
             "",
             "_Rear-view mirror only: nothing here places, sizes, or approves trades. "
             "Broker state (live quotes, resting stops) is authoritative — this reflects "
             "the committed ledger + the latest scheduled report._",
             ""]

    # ---------- Open positions ----------
    lines.append("## Open positions")
    if snapshot:
        total_val = sum(p["price"] * p["shares"] for p in snapshot
                        if p.get("price") and p.get("shares"))
        spec_val = sum(p["price"] * p["shares"] for p in snapshot
                       if p.get("price") and p.get("shares") and p["symbol"] in SPECULATIVE)
        lines.append("| Sym | Sleeve | Theme | Shares | Entry | Now | P&L% | Stop | Cushion | Resting stop |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|")
        for p in sorted(snapshot, key=lambda x: x.get("sleeve", "")):
            sym, price, entry = p["symbol"], p.get("price"), p.get("entry_price")
            stop, shares = p.get("stop"), p.get("shares") or 0
            pnl = (price / entry - 1) * 100 if price and entry else None
            cushion = (price / stop - 1) * 100 if price and stop else None
            whole = int(shares)
            resting = (f"{whole} sh GTC" if stop and whole >= 1 else
                       "monitored" if stop else "none (legacy)")
            flag = " 🔴" if p.get("exiting") else ""
            lines.append(f"| {sym}{flag} | {p.get('sleeve')} | {theme_of(sym)} | {shares:g} | "
                         f"{fmt(entry)} | {fmt(price)} | {fmt(pnl, '{:+.1f}')} | "
                         f"{fmt(stop)} | {fmt(cushion, '{:.1f}%')} | {resting} |")
        no_px = [p["symbol"] for p in snapshot if not p.get("price")]
        if no_px:
            lines.append(f"\n_No price this run for: {', '.join(no_px)}._")
        lines.append("\n🔴 = an exit rule fired in the latest report. 'Cushion' = distance "
                     "above the ledger stop. 'monitored' = fractional, can't rest a broker stop.")

        # ---------- Risk ----------
        lines.append("\n## Risk")
        if total_val:
            spec_pct = spec_val / total_val * 100
            icon = "🔴" if spec_pct > SPEC_CAP_PCT else "🟡" if spec_pct > SPEC_CAP_PCT - 5 else "🟢"
            lines.append(f"- {icon} **Speculative sleeve:** ${spec_val:,.0f} of ${total_val:,.0f} "
                         f"tracked = **{spec_pct:.1f}%** (cap ~{SPEC_CAP_PCT:.0f}%)")
        stops = sum(1 for p in snapshot if p.get("stop") and int(p.get("shares") or 0) >= 1)
        frac = sum(1 for p in snapshot if p.get("stop") and int(p.get("shares") or 0) < 1)
        bare = sum(1 for p in snapshot if not p.get("stop"))
        lines.append(f"- **Stop coverage:** {stops} resting GTC · {frac} monitored (fractional) "
                     f"· {bare} no stop set (legacy)")
        themes = {}
        for p in snapshot:
            if p.get("price") and p.get("shares"):
                themes[theme_of(p["symbol"])] = themes.get(theme_of(p["symbol"]), 0) \
                    + p["price"] * p["shares"]
        if total_val and themes:
            top = sorted(themes.items(), key=lambda kv: -kv[1])[:4]
            lines.append("- **Largest themes:** " + " · ".join(
                f"{th} {v / total_val * 100:.0f}%" for th, v in top))
    else:
        lines.append("_No held_snapshot in the latest report JSON (pre-dashboard report, "
                     "or no holdings). Populates on the next scheduled run._")

    # ---------- Closed trades ----------
    lines.append("\n## Closed trades — strategy scorecard")
    if trades:
        pnl_total = sum(t.get("pnl") or 0 for t in trades)
        wins = [t for t in trades if (t.get("pnl") or 0) > 0]
        rs = [t["r_multiple"] for t in trades if isinstance(t.get("r_multiple"), (int, float))]
        days = [t["days_held"] for t in trades if isinstance(t.get("days_held"), (int, float))]
        lines.append(f"- **{len(trades)} trades** · realized P&L **${pnl_total:+,.2f}** · "
                     f"win rate **{len(wins) / len(trades) * 100:.0f}%**"
                     + (f" · avg R **{sum(rs) / len(rs):+.2f}**" if rs else "")
                     + (f" · avg hold **{sum(days) / len(days):.1f}d**" if days else ""))
        by_sleeve = {}
        for t in trades:
            by_sleeve.setdefault(t.get("sleeve", "?"), []).append(t.get("pnl") or 0)
        lines.append("- **By sleeve:** " + " · ".join(
            f"{sl} {len(v)}x ${sum(v):+,.0f}" for sl, v in sorted(by_sleeve.items())))
        reasons = {}
        for t in trades:
            key = (t.get("exit_reason") or "unknown").split(";")[0].strip()[:40]
            reasons[key] = reasons.get(key, 0) + 1
        lines.append("- **Exit reasons:** " + " · ".join(
            f"{r} ×{n}" for r, n in sorted(reasons.items(), key=lambda kv: -kv[1])))
        lines.append("\n| Closed | Sym | Sleeve | Entry | Exit | P&L | P&L% | R | Days | Why |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|")
        for t in sorted(trades, key=lambda x: x.get("exit_date") or "", reverse=True)[:15]:
            lines.append(f"| {t.get('exit_date', '—')} | {t.get('symbol')} | {t.get('sleeve')} | "
                         f"{fmt(t.get('entry_price'))} | {fmt(t.get('exit_price'))} | "
                         f"{fmt(t.get('pnl'), '{:+.2f}')} | {fmt(t.get('pnl_pct'), '{:+.1f}')} | "
                         f"{fmt(t.get('r_multiple'), '{:+.1f}')} | {t.get('days_held', '—')} | "
                         f"{(t.get('exit_reason') or '')[:60]} |")
    else:
        lines.append("_No closed trades yet. The trading session appends each sell to "
                     "`trade_log.json`; win rate, avg R, and the exit-reason breakdown "
                     "appear here once the first positions close._")

    # ---------- Today's signals (context) ----------
    setups = report.get("swing_setups", [])
    exits = report.get("exit_signals", [])
    lines.append("\n## Latest report signals")
    lines.append(f"- {len(exits)} exit signal(s), {len(setups)} swing setup(s) — see "
                 f"`latest_{report.get('mode', 'morning')}.md` for the full tables.")
    lines.append("\n---")
    lines.append("_Generated by `dashboard.py` in the scheduled report run. Read-only._")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUT}")
