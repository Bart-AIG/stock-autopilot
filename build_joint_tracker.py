"""Build joint_portfolio_tracker.xlsx: the joint account's holdings, price targets and sell targets.

Inputs (blue) come from joint_tracker_data.json (refreshed by the Quality @ 200-day
routine, step 4f) joined with joint_price_targets.json, valuation.json, setups.json,
rebuy_watch.json and wash_sale_watch.json.
Every output column is an Excel formula, so editing an input (price, target,
an assumption on the Inputs sheet) recalculates the sheet.

Refresh: update joint_tracker_data.json (or edit the cells in Excel) and run
    python3 build_joint_tracker.py
"""
import json
import re
from datetime import date

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

DATA_FILE = "joint_tracker_data.json"


def _load(path, default=None):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def _date(v):
    """'YYYY-MM-DD' -> date (Excel date cell); anything else passes through as text."""
    if isinstance(v, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
        return date.fromisoformat(v)
    return v if v not in (None, "") else "n/a"


def _val_text(v):
    if not v or not v.get("grade") or v.get("grade") == "N/A":
        return "n/a"
    gap = v.get("gap_pct")
    conf = (v.get("confidence") or "").lower()
    return f"{v['grade']} {gap:+.0f}% ({conf})" if gap is not None else f"{v['grade']} ({conf})"


def _setup_text(row):
    if not row or row.get("pre") is None:
        return None
    return f"{row['pre']} {row.get('pre_label', '')}".strip()


def holdings_rows(data, targets, vals):
    """Rows for the Holdings sheet, biggest position first. Targets come from
    joint_price_targets.json (the routine's 3-method target); a leveraged ETF with no
    target uses its 50-day SMA; a plain ETF has none."""
    mk, notes, out, skipped = data["market"], data.get("notes", {}), [], []
    for sym, h in data["holdings"].items():
        m = mk.get(sym) or {}
        if not m.get("price"):
            skipped.append(sym)
            continue
        t = (targets.get("rows") or {}).get(sym) or {}
        meth = t.get("methods") or {}
        final, agree = t.get("final"), t.get("agreement")
        typ = m.get("type") or "Stock"
        if final is None and "Lev" in typ and m.get("sma50"):
            final, agree = m["sma50"], "TECH (50-day)"
        v = (vals.get("rows") or {}).get(sym) or {}
        out.append((
            sym, m.get("name") or sym, typ, m.get("sector") or "", h["shares"], h["avg_cost"],
            m["price"], m.get("after_hours"), m.get("sma50"), m.get("sma200"), m.get("low60"),
            m.get("high60"), m.get("high52"), meth.get("fundamental"),
            meth.get("robinhood", m.get("analyst_mean")), meth.get("analysts"), final, agree or "n/a",
            _val_text(v), (v.get("disruption") or {}).get("label") or "n/a", _date(m.get("earnings")),
            notes.get(sym, "")))
    out.sort(key=lambda r: -(r[4] * r[6]))
    return out, skipped


def watch_rows(data, setups, rebuy, wash):
    """Rows for the Watchlist sheet: the quality list ordered by pre-breakout setup
    (most coiled first, then business rank), then the re-buy watch, then the
    new-industry names curated in live turns."""
    mk, notes, held = data["market"], data.get("notes", {}), set(data["holdings"])
    srows = (setups or {}).get("rows") or {}
    locks = (wash or {}).get("lockouts") or {}
    rb = (rebuy or {}).get("names") or {}
    out = []

    def row(sym, lst, grade, rank, setup, clear, note):
        m = mk.get(sym) or {}
        if not m.get("price") or not m.get("sma200"):
            return
        v = data.get("_vals", {}).get(sym) or {}
        out.append((
            sym, m.get("name") or sym, lst, "HELD" if sym in held else "", grade or "n/a", rank,
            setup or "n/a", _val_text(v), (v.get("disruption") or {}).get("label") or "n/a",
            m["price"], m.get("sma50"), m["sma200"], m.get("analyst_mean"), m.get("n_buy"),
            m.get("n_hold"), m.get("n_sell"), _date(m.get("earnings")),
            _date(clear) if clear else None, note))

    def pre(q):
        p = (srows.get(q["sym"]) or {}).get("pre")
        return (p is None, -(p or 0), q.get("rank") or 99)

    for q in sorted(data.get("quality", []), key=pre):
        sym = q["sym"]
        row(sym, "Buy Zone", q.get("grade"), q.get("rank"), _setup_text(srows.get(sym)),
            (locks.get(sym) or {}).get("clear"), notes.get(sym, ""))
    for sym, e in rb.items():
        row(sym, "Re-buy", None, None, f"{e.get('stage', '?')} (re-buy stage)",
            e.get("wash_clear") or (locks.get(sym) or {}).get("clear"), notes.get(sym, ""))
    for sym, e in data.get("new_industry", {}).items():
        row(sym, "New industry", e.get("grade"), None,
            _setup_text(srows.get(sym)) or e.get("industry"), (locks.get(sym) or {}).get("clear"),
            (e.get("industry", "") + ". " if e.get("industry") else "") + notes.get(sym, ""))
    return out


BLUE = Font(color="0000FF")
BOLD = Font(bold=True)
WHITE_BOLD = Font(bold=True, color="FFFFFF")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
HEAD_IN = PatternFill("solid", fgColor="1F4E78")
HEAD_OUT = PatternFill("solid", fgColor="375623")
TOTAL_FILL = PatternFill("solid", fgColor="D9D9D9")
RED_FILL = PatternFill("solid", fgColor="F8CBAD")
GREEN_FILL = PatternFill("solid", fgColor="C6EFCE")
AMBER_FILL = PatternFill("solid", fgColor="FFEB9C")
THIN = Side(style="thin", color="BFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def build(path="joint_portfolio_tracker.xlsx", data_path=DATA_FILE):
    data = _load(data_path)
    vals = _load("valuation.json", {})
    data["_vals"] = vals.get("rows") or {}
    SNAPSHOT, skipped = holdings_rows(data, _load("joint_price_targets.json", {}), vals)
    WATCH = watch_rows(data, _load("setups.json", {}), _load("rebuy_watch.json", {}),
                       _load("wash_sale_watch.json", {}))
    AS_OF = date.fromisoformat(data["asof"])
    wb = Workbook()

    # ---------------- Inputs (assumptions) ----------------
    inp = wb.active
    inp.title = "Inputs"
    inp["A1"] = "Joint Portfolio Tracker - Assumptions"
    inp["A1"].font = Font(bold=True, size=14)
    inp["A2"] = "Blue on yellow = input. Change any of these and the Holdings sheet recalculates."
    rows = [
        ("As-of date (prices)", AS_OF, "Date of the prices in the Price column (see the Holdings header).", "0"),
        ("Price to use", "Price", "Price or After-hours. After-hours falls back to Price when blank.", None),
        ("Trim 1 trigger (% of final target)", 1.00, "Sell target 1 = final target x this. 100% = sell at the target.", "0%"),
        ("Trim 2 stretch above target", 0.15, "Sell target 2 = final target x (1 + this).", "0%"),
        ("Shares sold at each trim", 1 / 3, "Fraction of the position sold at T1 and again at T2. Last third rides the trail.", "0%"),
        ("Support buffer below 60-day low", 0.01, "Review level sits this far under the 60-day low.", "0.0%"),
        ("Max loss from cost - stocks", 0.25, "Review level never sits lower than cost x (1 - this).", "0%"),
        ("Max loss from cost - leveraged ETFs", 0.30, "Same, for 2x/3x ETFs.", "0%"),
        ("Trailing stop %", 0.15, "Trail = 60-day high x (1 - this), floored at cost, once price >= cost / (1 - this).", "0%"),
        ("Position cap - stocks (% of portfolio)", 0.15, "Flags OVERWEIGHT above this.", "0%"),
        ("Position cap - leveraged ETFs", 0.05, "Leveraged ETFs lose value in choppy markets; keep them small.", "0%"),
        ("Earnings warning window (days)", 7, "Flags a holding reporting within this many days.", "0"),
        ("Watchlist: buy zone low vs 200-day", -0.08, "Bottom of the buy zone. Below it the 200-day has failed: wait for a reclaim.", "0%"),
        ("Watchlist: buy zone high vs 200-day", 0.05, "Top of the buy zone. Above it the name is extended: wait.", "0%"),
        ("Watchlist: entry vs 200-day", 0.0, "Buy target = 200-day SMA x (1 + this). 0% = buy at the line.", "0%"),
    ]
    inp["A4"], inp["B4"], inp["C4"] = "Assumption", "Value", "What it does"
    for c in ("A4", "B4", "C4"):
        inp[c].font = WHITE_BOLD
        inp[c].fill = HEAD_IN
    names = ["AsOf", "PriceMode", "Trim1", "Stretch", "TrimSize", "Buffer", "MaxLoss", "MaxLossLev",
             "Trail", "Cap", "CapLev", "ErnDays", "ZoneLo", "ZoneHi", "EntryOff"]
    ref = {}
    for i, (label, val, note, fmt) in enumerate(rows):
        r = 5 + i
        inp.cell(r, 1, label)
        c = inp.cell(r, 2, val)
        c.font = BLUE
        c.fill = INPUT_FILL
        c.border = BOX
        if fmt:
            c.number_format = "yyyy-mm-dd" if isinstance(val, date) else fmt
        inp.cell(r, 3, note)
        ref[names[i]] = f"Inputs!$B${r}"
    dv = DataValidation(type="list", formula1='"Price,After-hours"', allow_blank=False)
    inp.add_data_validation(dv)
    dv.add("B6")
    inp.column_dimensions["A"].width = 38
    inp.column_dimensions["B"].width = 14
    inp.column_dimensions["C"].width = 95

    # ---------------- Holdings ----------------
    ws = wb.create_sheet("Holdings")
    wb.move_sheet("Holdings", offset=-1)
    wb.active = 0
    ws["A1"] = "Joint Account (••••5343) - Holdings, Price Targets and Sell Targets"
    ws["A1"].font = Font(bold=True, size=14)
    ws["A2"] = ("Blue columns are inputs (broker snapshot + routine targets). Green-header columns are formulas. "
                "Sell targets are guides for Ryan; the agent never trades the joint account.")
    ws["A3"] = "Price used:"
    ws["B3"] = f"={ref['PriceMode']}"
    ws["C3"] = data.get("price_label", "Prices as of:")
    ws["D3"] = f"={ref['AsOf']}"
    ws["D3"].number_format = "yyyy-mm-dd"

    in_cols = [
        ("Symbol", 8, None), ("Company", 22, None), ("Type", 11, None), ("Sector", 20, None),
        ("Shares", 10, "#,##0.0000"), ("Avg Cost", 10, "$#,##0.00"), ("Price", 10, "$#,##0.00"),
        ("After-hrs", 10, "$#,##0.00"), ("50-day SMA", 10, "$#,##0.00"), ("200-day SMA", 10, "$#,##0.00"),
        ("60-day Low", 10, "$#,##0.00"), ("60-day High", 10, "$#,##0.00"), ("52-wk High", 10, "$#,##0.00"),
        ("Tgt: Fundamental", 11, "$#,##0.00"), ("Tgt: Robinhood", 11, "$#,##0.00"),
        ("Tgt: Analysts", 11, "$#,##0.00"), ("FINAL Price Target", 12, "$#,##0.00"),
        ("Target Agreement", 12, None), ("Valuation", 18, None), ("Disruption", 12, None),
        ("Next Earnings", 13, "yyyy-mm-dd"),
    ]
    out_cols = [
        ("Price Used", 10, "$#,##0.00"), ("Market Value", 12, "$#,##0"), ("Cost Basis", 12, "$#,##0"),
        ("Unrealized P/L $", 12, "$#,##0;[Red]-$#,##0"), ("P/L %", 8, "0.0%;[Red]-0.0%"),
        ("Weight", 8, "0.0%"), ("After-hrs Move", 9, "0.0%;[Red]-0.0%"),
        ("vs 50-day", 8, "0.0%;[Red]-0.0%"), ("vs 200-day", 8, "0.0%;[Red]-0.0%"),
        ("Off 52-wk High", 9, "0.0%;[Red]-0.0%"), ("Upside to Target", 9, "0.0%;[Red]-0.0%"),
        ("SELL TARGET 1 (trim)", 12, "$#,##0.00"), ("SELL TARGET 2 (trim)", 12, "$#,##0.00"),
        ("Shares per Trim", 10, "#,##0.0000"), ("Proceeds at T1", 11, "$#,##0"),
        ("DOWNSIDE REVIEW LEVEL", 12, "$#,##0.00"), ("Cushion to Review", 9, "0.0%;[Red]-0.0%"),
        ("Trailing Stop (if green)", 12, "$#,##0.00"), ("Reward : Risk", 9, "0.0"),
        ("ACTION", 30, None),
    ]
    note_col = ("Notes", 60, None)
    headers = in_cols + out_cols + [note_col]
    HR = 5
    for j, (h, w, _) in enumerate(headers, start=1):
        c = ws.cell(HR, j, h)
        c.font = WHITE_BOLD
        c.fill = HEAD_IN if j <= len(in_cols) or j == len(headers) else HEAD_OUT
        c.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")
        c.border = BOX
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.row_dimensions[HR].height = 42

    col = {h: get_column_letter(j) for j, (h, _, _) in enumerate(headers, start=1)}
    first = HR + 1
    last = first + len(SNAPSHOT) - 1
    tot = last + 2
    L = col  # shorthand

    for i, row in enumerate(SNAPSHOT):
        r = first + i
        vals = list(row[:21])
        for j, v in enumerate(vals, start=1):
            c = ws.cell(r, j, v)
            c.font = BLUE
            c.fill = INPUT_FILL
            c.border = BOX
            fmt = in_cols[j - 1][2]
            if fmt:
                c.number_format = fmt
        ws.cell(r, len(headers), row[21]).font = BLUE

        def a(h):
            return f"{L[h]}{r}"

        lev = f'ISNUMBER(SEARCH("Lev",{a("Type")}))'
        P = a("Price Used")
        T = a("FINAL Price Target")
        f = {
            "Price Used": f'=IF(AND({ref["PriceMode"]}="After-hours",N({a("After-hrs")})>0),{a("After-hrs")},{a("Price")})',
            "Market Value": f"={a('Shares')}*{P}",
            "Cost Basis": f"={a('Shares')}*{a('Avg Cost')}",
            "Unrealized P/L $": f"={a('Market Value')}-{a('Cost Basis')}",
            "P/L %": f'=IFERROR({a("Unrealized P/L $")}/{a("Cost Basis")},"")',
            "Weight": f"={a('Market Value')}/${L['Market Value']}${tot}",
            "After-hrs Move": f'=IFERROR(IF(N({a("After-hrs")})>0,{a("After-hrs")}/{a("Price")}-1,""),"")',
            "vs 50-day": f'=IFERROR({P}/{a("50-day SMA")}-1,"")',
            "vs 200-day": f'=IFERROR({P}/{a("200-day SMA")}-1,"")',
            "Off 52-wk High": f'=IFERROR({P}/{a("52-wk High")}-1,"")',
            "Upside to Target": f'=IF(N({T})>0,{T}/{P}-1,"")',
            "SELL TARGET 1 (trim)": f'=IF(N({T})>0,{T}*{ref["Trim1"]},"")',
            "SELL TARGET 2 (trim)": f'=IF(N({T})>0,{T}*(1+{ref["Stretch"]}),"")',
            "Shares per Trim": f"={a('Shares')}*{ref['TrimSize']}",
            "Proceeds at T1": f'=IF(N({a("SELL TARGET 1 (trim)")})>0,{a("Shares per Trim")}*{a("SELL TARGET 1 (trim)")},"")',
            "DOWNSIDE REVIEW LEVEL": (f'=MAX({a("60-day Low")}*(1-{ref["Buffer"]}),'
                                      f'{a("Avg Cost")}*(1-IF({lev},{ref["MaxLossLev"]},{ref["MaxLoss"]})))'),
            "Cushion to Review": f'=IFERROR({P}/{a("DOWNSIDE REVIEW LEVEL")}-1,"")',
            "Trailing Stop (if green)": (f'=IF({P}>={a("Avg Cost")}/(1-{ref["Trail"]}),'
                                         f'MAX({a("Avg Cost")},{a("60-day High")}*(1-{ref["Trail"]})),"not green yet")'),
            "Reward : Risk": (f'=IF(AND(N({T})>0,{P}>{a("DOWNSIDE REVIEW LEVEL")},{a("SELL TARGET 1 (trim)")}>{P}),'
                              f'({a("SELL TARGET 1 (trim)")}-{P})/({P}-{a("DOWNSIDE REVIEW LEVEL")}),"")'),
            "ACTION": (
                f'=IF({a("Market Value")}<100,"DUST: clean up",'
                f'IF({P}<{a("DOWNSIDE REVIEW LEVEL")},"REVIEW: below support / max loss",'
                f'IF(AND(N({T})>0,{P}>={a("SELL TARGET 2 (trim)")}),"SELL 2nd TRIM, trail the rest",'
                f'IF(AND(N({T})>0,{P}>={a("SELL TARGET 1 (trim)")}),"TRIM 1/3 + thesis re-check",'
                f'IF({a("Weight")}>IF({lev},{ref["CapLev"]},{ref["Cap"]}),"OVERWEIGHT: trim to cap",'
                f'IF(IF(ISNUMBER({a("Next Earnings")}),AND({a("Next Earnings")}>{ref["AsOf"]},'
                f'{a("Next Earnings")}-{ref["AsOf"]}<={ref["ErnDays"]}),FALSE),"HOLD: earnings soon",'
                f'IF(N({T})=0,"HOLD: no target","HOLD")))))))'
            ),
        }
        for h, formula in f.items():
            c = ws[a(h)]
            c.value = formula
            c.number_format = next(x[2] for x in out_cols if x[0] == h) or "General"
            c.border = BOX

    # totals
    ws.cell(tot, 1, "TOTAL").font = BOLD
    for h in ("Market Value", "Cost Basis", "Unrealized P/L $", "Proceeds at T1"):
        c = ws[f"{L[h]}{tot}"]
        c.value = f"=SUM({L[h]}{first}:{L[h]}{last})"
        c.number_format = next(x[2] for x in out_cols if x[0] == h)
    ws[f"{L['P/L %']}{tot}"] = f"={L['Unrealized P/L $']}{tot}/{L['Cost Basis']}{tot}"
    ws[f"{L['P/L %']}{tot}"].number_format = "0.0%;[Red]-0.0%"
    ws[f"{L['Weight']}{tot}"] = f"=SUM({L['Weight']}{first}:{L['Weight']}{last})"
    ws[f"{L['Weight']}{tot}"].number_format = "0.0%"
    ws[f"{L['Upside to Target']}{tot}"] = (
        f'=SUMPRODUCT(--({L["FINAL Price Target"]}{first}:{L["FINAL Price Target"]}{last}>0),'
        f'{L["Shares"]}{first}:{L["Shares"]}{last},{L["FINAL Price Target"]}{first}:{L["FINAL Price Target"]}{last})'
        f'/SUMPRODUCT(--({L["FINAL Price Target"]}{first}:{L["FINAL Price Target"]}{last}>0),'
        f'{L["Market Value"]}{first}:{L["Market Value"]}{last})-1')
    ws[f"{L['Upside to Target']}{tot}"].number_format = "0.0%"
    ws[f"{L['ACTION']}{tot}"] = (f'=COUNTIF({L["ACTION"]}{first}:{L["ACTION"]}{last},"REVIEW*")&" review, "'
                                 f'&COUNTIF({L["ACTION"]}{first}:{L["ACTION"]}{last},"OVERWEIGHT*")&" overweight, "'
                                 f'&COUNTIF({L["ACTION"]}{first}:{L["ACTION"]}{last},"TRIM*")&" trim"')
    for j in range(1, len(headers) + 1):
        ws.cell(tot, j).fill = TOTAL_FILL
        ws.cell(tot, j).font = BOLD

    # conditional formatting
    act = f"{L['ACTION']}{first}:{L['ACTION']}{last}"
    ws.conditional_formatting.add(act, FormulaRule(formula=[f'LEFT({L["ACTION"]}{first},6)="REVIEW"'], fill=RED_FILL))
    ws.conditional_formatting.add(act, FormulaRule(formula=[f'LEFT({L["ACTION"]}{first},4)="OVER"'], fill=AMBER_FILL))
    ws.conditional_formatting.add(act, FormulaRule(formula=[f'OR(LEFT({L["ACTION"]}{first},4)="TRIM",LEFT({L["ACTION"]}{first},4)="SELL")'], fill=GREEN_FILL))
    ws.conditional_formatting.add(f"{L['After-hrs Move']}{first}:{L['After-hrs Move']}{last}",
                                  CellIsRule(operator="lessThan", formula=["-0.05"], fill=RED_FILL))
    ws.conditional_formatting.add(f"{L['Cushion to Review']}{first}:{L['Cushion to Review']}{last}",
                                  CellIsRule(operator="between", formula=["0", "0.05"], fill=AMBER_FILL))
    ws.conditional_formatting.add(f"{L['Target Agreement']}{first}:{L['Target Agreement']}{last}",
                                  CellIsRule(operator="equal", formula=['"LOW"'], fill=AMBER_FILL))
    ws.freeze_panes = ws.cell(first, 2)
    ws.auto_filter.ref = f"A{HR}:{get_column_letter(len(headers))}{last}"

    add_watchlist(wb, ref, WATCH)
    if skipped:
        ws.cell(3, 6, "Not priced (check in the app): " + ", ".join(skipped))

    # ---------------- Method ----------------
    m = wb.create_sheet("Method")
    lines = [
        ("How the numbers are set", True),
        ("FINAL PRICE TARGET: the Quality @ 200-day routine's 3-method target (joint_price_targets.json):", False),
        ("  1 Fundamental = next-year consensus EPS/EBITDA/sales x the stock's own 5-yr median multiples;", False),
        ("  2 Robinhood mean analyst target; 3 median of dated major-firm analyst targets (<=120 days old).", False),
        ("  Final = median of three, average of two, or one alone. Agreement HIGH/MED/LOW = how close the methods are.", False),
        ("  SOXL and AAOX have no analyst coverage: their target is the 50-day SMA (first overhead resistance).", False),
        ("SELL TARGET 1 = final target x Trim 1 %. Sell a third and re-check the thesis. A target hit is not an automatic exit.", False),
        ("SELL TARGET 2 = final target x (1 + stretch). Sell the second third; the last third rides the trailing stop.", False),
        ("DOWNSIDE REVIEW LEVEL = the higher of (60-day low less the buffer) and (cost less the max-loss %).", False),
        ("  Below it the trend has broken support: re-check the thesis and decide sell or hold. Not a stop order.", False),
        ("TRAILING STOP: shown once price >= cost / (1 - trail %), i.e. +17.6% at 15%. = 60-day high x (1 - trail), never below cost.", False),
        ("REWARD : RISK = (sell target 1 - price) / (price - review level). Above ~2 is a favourable hold.", False),
        ("WATCHLIST (Watchlist sheet): the Quality @ 200-day routine's buy-zone names (business grade >= 7/8, near the 200-day),", False),
        ("  ranked by pre-breakout chart setup (most pulled back first), plus the re-buy watch (MOD).", False),
        ("  BUY TARGET = 200-day SMA x (1 + entry offset). BUY ZONE = 200-day -8% to +5%. Below the zone = trend failed, wait for a reclaim.", False),
        ("  WATCH REVIEW LEVEL = bottom of the buy zone: where a new buy is wrong. UPSIDE / REWARD:RISK are measured from the buy target to the analyst mean target.", False),
        ("  STATUS is a prompt to research, not a buy order: every name still needs a news/thesis check and a wash-sale check before buying.", False),
        ("", False),
        ("Sources", True),
        ("Positions, quotes, 50/200-day SMA, 60-day range, 52-wk high, analyst ratings, earnings dates: Robinhood, via joint_tracker_data.json.", False),
        ("Targets: joint_price_targets.json. Valuation and disruption: valuation.json. Chart setups: setups.json. Re-buy: rebuy_watch.json. Wash-sale dates: wash_sale_watch.json.", False),
        ("", False),
        ("Not included", True),
        ("Holdings with no quote (e.g. EPIX^, 25 sh at $0 cost) are listed at the top of Holdings as Not priced.", False),
        ("Taxes: this is a taxable account. Check wash-sale lockouts (Robinhood list 'Wash-Sale Lockout') before selling at a loss and rebuying.", False),
        ("", False),
        ("Refresh", True),
        ("The Quality @ 200-day routine (step 4f) refreshes joint_tracker_data.json and rebuilds this file each weekday. Edit blue cells for what-ifs; a rebuild overwrites them.", False),
    ]
    for i, (t, b) in enumerate(lines, start=1):
        c = m.cell(i, 1, t)
        if b:
            c.font = Font(bold=True, size=12)
    m.column_dimensions["A"].width = 130

    wb.save(path)
    return path


def add_watchlist(wb, ref, WATCH):
    ws = wb.create_sheet("Watchlist")
    wb.move_sheet("Watchlist", offset=-(len(wb.sheetnames) - 2))
    ws["A1"] = "Joint Watchlist - Quality @ 200-day Buy Zone, Re-buy Watch, New Industries"
    ws["A1"].font = Font(bold=True, size=14)
    ws["A2"] = ("Ordered by pre-breakout chart setup (most pulled back first). Blue = inputs (10/29 close), "
                "green headers = formulas. A status is a prompt to research, never a buy order.")
    in_cols = [
        ("Symbol", 8, None), ("Company", 24, None), ("List", 12, None), ("Held?", 7, None),
        ("Quality Grade", 8, None), ("Quality Rank", 8, "0"), ("Chart Setup", 17, None), ("Valuation", 20, None),
        ("Disruption", 12, None), ("Price", 10, "$#,##0.00"), ("50-day SMA", 10, "$#,##0.00"),
        ("200-day SMA", 10, "$#,##0.00"), ("Analyst Mean Target", 11, "$#,##0.00"), ("# Buy", 6, "0"),
        ("# Hold", 6, "0"), ("# Sell", 6, "0"), ("Next Earnings", 16, "yyyy-mm-dd"), ("Wash-Sale Clear", 11, "yyyy-mm-dd"),
    ]
    out_cols = [
        ("vs 200-day", 8, "0.0%;[Red]-0.0%"), ("vs 50-day", 8, "0.0%;[Red]-0.0%"),
        ("Buy Zone Low", 10, "$#,##0.00"), ("Buy Zone High", 10, "$#,##0.00"), ("BUY TARGET", 10, "$#,##0.00"),
        ("Distance to Buy Target", 9, "0.0%;[Red]-0.0%"), ("Upside: Buy Tgt to Analyst", 10, "0.0%;[Red]-0.0%"),
        ("WATCH REVIEW LEVEL", 10, "$#,##0.00"), ("Reward : Risk at Buy Tgt", 9, "0.0"), ("% Buy Ratings", 8, "0%"),
        ("STATUS", 34, None),
    ]
    headers = in_cols + out_cols + [("Notes", 60, None)]
    HR = 4
    for j, (h, w, _) in enumerate(headers, start=1):
        c = ws.cell(HR, j, h)
        c.font = WHITE_BOLD
        c.fill = HEAD_IN if j <= len(in_cols) or j == len(headers) else HEAD_OUT
        c.alignment = Alignment(wrap_text=True, horizontal="center", vertical="center")
        c.border = BOX
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.row_dimensions[HR].height = 42
    L = {h: get_column_letter(j) for j, (h, _, _) in enumerate(headers, start=1)}
    first = HR + 1
    last = first + len(WATCH) - 1
    fmt_out = {h: f for h, _, f in out_cols}
    for i, row in enumerate(WATCH):
        r = first + i
        for j, v in enumerate(row[:18], start=1):
            c = ws.cell(r, j, v)
            c.font = BLUE
            c.fill = INPUT_FILL
            c.border = BOX
            if in_cols[j - 1][2] and v is not None:
                c.number_format = in_cols[j - 1][2]
        ws.cell(r, len(headers), row[18]).font = BLUE

        def a(h):
            return f"{L[h]}{r}"

        P, S200, T, B = a("Price"), a("200-day SMA"), a("Analyst Mean Target"), a("BUY TARGET")
        f = {
            "vs 200-day": f"={P}/{S200}-1",
            "vs 50-day": f"={P}/{a('50-day SMA')}-1",
            "Buy Zone Low": f"={S200}*(1+{ref['ZoneLo']})",
            "Buy Zone High": f"={S200}*(1+{ref['ZoneHi']})",
            "BUY TARGET": f"={S200}*(1+{ref['EntryOff']})",
            "Distance to Buy Target": f"={P}/{B}-1",
            "Upside: Buy Tgt to Analyst": f'=IF(N({T})>0,{T}/{B}-1,"")',
            "WATCH REVIEW LEVEL": f"={a('Buy Zone Low')}",
            "Reward : Risk at Buy Tgt": f'=IFERROR(IF(N({T})>{B},({T}-{B})/({B}-{a("WATCH REVIEW LEVEL")}),""),"")',
            "% Buy Ratings": f'=IFERROR({a("# Buy")}/({a("# Buy")}+{a("# Hold")}+{a("# Sell")}),"")',
            "STATUS": (
                f'=IF({a("Held?")}="HELD","HELD: see Holdings sheet",'
                f'IF(IF(ISNUMBER({a("Wash-Sale Clear")}),{ref["AsOf"]}<{a("Wash-Sale Clear")},FALSE),'
                f'"WASH-SALE LOCK until "&TEXT({a("Wash-Sale Clear")},"m/d"),'
                f'IF({P}<{a("Buy Zone Low")},"BELOW ZONE: wait for 200-day reclaim",'
                f'IF({P}>{a("Buy Zone High")},"ABOVE ZONE: extended, wait",'
                f'IF(IF(ISNUMBER({a("Next Earnings")}),AND({a("Next Earnings")}>{ref["AsOf"]},'
                f'{a("Next Earnings")}-{ref["AsOf"]}<={ref["ErnDays"]}),FALSE),"IN ZONE: earnings soon, wait",'
                f'IF(N({T})<={P},"IN ZONE: analysts see no upside",'
                f'IF({P}<={B},"IN ZONE: at/below buy target - research","IN ZONE: research")))))))'
            ),
        }
        for h, formula in f.items():
            c = ws[a(h)]
            c.value = formula
            if fmt_out[h]:
                c.number_format = fmt_out[h]
            c.border = BOX
    st = f"{L['STATUS']}{first}:{L['STATUS']}{last}"
    ws.conditional_formatting.add(st, FormulaRule(formula=[f'LEFT({L["STATUS"]}{first},7)="IN ZONE"'], fill=GREEN_FILL))
    ws.conditional_formatting.add(st, FormulaRule(formula=[f'OR(LEFT({L["STATUS"]}{first},4)="WASH",ISNUMBER(SEARCH("earnings",{L["STATUS"]}{first})),ISNUMBER(SEARCH("no upside",{L["STATUS"]}{first})))'], fill=AMBER_FILL))
    ws.conditional_formatting.add(st, FormulaRule(formula=[f'LEFT({L["STATUS"]}{first},5)="BELOW"'], fill=RED_FILL))
    ws.conditional_formatting.add(f"{L['Disruption']}{first}:{L['Disruption']}{last}",
                                  CellIsRule(operator="equal", formula=['"AT RISK"'], fill=AMBER_FILL))
    tot = last + 2
    ws.cell(tot, 1, "COUNT").font = BOLD
    ws[f"{L['STATUS']}{tot}"] = (f'=COUNTIF({st},"IN ZONE*")&" in zone, "&COUNTIF({st},"BELOW*")&" below, "'
                                 f'&COUNTIF({st},"ABOVE*")&" above"')
    for j in range(1, len(headers) + 1):
        ws.cell(tot, j).fill = TOTAL_FILL
        ws.cell(tot, j).font = BOLD
    ws.freeze_panes = ws.cell(first, 2)
    ws.auto_filter.ref = f"A{HR}:{get_column_letter(len(headers))}{last}"


if __name__ == "__main__":
    print(build())
