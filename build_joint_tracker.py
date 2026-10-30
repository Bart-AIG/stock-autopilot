"""Build joint_portfolio_tracker.xlsx: the joint account's holdings, price targets and sell targets.

Inputs (blue) are a snapshot pasted from the broker and the repo's routine files.
Every output column is an Excel formula, so editing an input (price, target,
an assumption on the Inputs sheet) recalculates the sheet.

Refresh: update SNAPSHOT below (or edit the cells in Excel) and run
    python3 build_joint_tracker.py
"""
from datetime import date

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

AS_OF = date(2026, 10, 29)  # official close used for "Close" prices

# Sources: Robinhood joint account positions + quotes + daily SMA/Donchian/fundamentals
# (pulled 2026-10-30 ~04:50Z); targets from joint_price_targets.json (2026-10-29T19:29Z);
# valuation/disruption from valuation.json (2026-10-28/29); earnings from Robinhood calendar.
# Columns: sym, name, type, sector, shares, avg_cost, close, after_hours, sma50, sma200,
#          low60, high60, high52, tgt_fund, tgt_rh, tgt_analysts, final_tgt, agreement,
#          valuation, disruption, next_earnings, note
SNAPSHOT = [
    ("META", "Meta Platforms", "Stock", "Internet", 25.982426, 631.15, 624.52, 618.49, 668.60, 632.11,
     537.27, 779.82, 779.82, 890.02, 850.51, 840.00, 850.51, "HIGH", "RICH", "INNOVATING", "Not in next 30d", ""),
    ("AMZN", "Amazon", "Stock", "Internet retail / cloud", 61.916672, 229.20, 243.79, 226.96, 254.89, 243.44,
     244.30, 280.14, 287.20, 440.05, 333.68, 350.00, 350.00, "MED", "DEEP VALUE (low conf.)", "INNOVATING",
     date(2026, 10, 29), "Q3 EPS 1.89 vs 1.97 est (miss); -6.9% after hours. Below 60-day low AH."),
    ("SOXL", "Direxion Semis 3x Bull", "3x Lev ETF", "Semiconductors", 145, 86.37, 102.39, 87.39, 122.07, 124.17,
     80.22, 169.83, 302.00, None, None, None, 122.07, "TECH (50-day)", "n/a", "n/a", "n/a",
     "3x daily leverage, decays in chop. No analyst target: target = 50-day SMA (first resistance). -14.6% AH."),
    ("SPCX", "SpaceX", "Stock", "Space / telecom / AI", 65, 154.95, 143.89, 140.71, 149.57, 147.94,
     105.11, 176.42, 225.64, None, 256.00, 240.00, 248.00, "MED", "n/a", "n/a", "Not in next 30d", ""),
    ("NBIS", "Nebius Group", "Stock", "AI cloud", 46, 162.87, 171.99, 164.33, 211.23, 177.28,
     149.48, 280.83, 299.86, None, 286.71, 250.00, 268.36, "MED", "EXPENSIVE (low conf.)", "DISRUPTOR",
     date(2026, 11, 10), "Earnings date unverified."),
    ("MPWR", "Monolithic Power", "Stock", "Semiconductors", 6, 1165.40, 1198.81, 1190.01, 1276.92, 1315.16,
     1126.57, 1491.64, 1714.09, 1870.20, 1807.46, None, 1838.83, "HIGH", "EXPENSIVE", "INNOVATING",
     date(2026, 10, 29), "Q3 EPS 8.19 vs 7.56 est (beat)."),
    ("CDNS", "Cadence Design", "Stock", "EDA software", 20, 316.43, 342.75, 337.94, 320.24, 327.46,
     273.07, 361.91, 416.69, 593.26, 415.04, None, 504.15, "LOW", "RICH", "INNOVATING", "Not in next 30d",
     "Target agreement LOW: fundamental and Robinhood targets 35% apart."),
    ("ASND", "Ascendis Pharma", "Stock", "Biotech", 20, 226.14, 253.00, 253.00, 242.38, 237.93,
     219.52, 272.47, 282.15, None, 302.81, 302.00, 302.40, "MED", "n/a", "DISRUPTOR",
     date(2026, 11, 11), "Earnings date unverified."),
    ("NOW", "ServiceNow", "Stock", "Software", 46.881838, 103.90, 109.67, 109.23, 139.99, 115.34,
     111.80, 159.50, 192.97, None, 158.78, 195.50, 177.14, "MED", "DEEP VALUE (low conf.)", "DISRUPTOR",
     "Not in next 30d", "Closed below its 60-day low on 10/29."),
    ("VST", "Vistra", "Stock", "Power generation", 35, 140.54, 140.95, 137.85, 145.12, 153.77,
     133.44, 168.75, 198.82, 234.71, 207.86, 224.00, 224.00, "HIGH", "EXPENSIVE", "STABLE",
     date(2026, 11, 6), ""),
    ("CRDO", "Credo Technology", "Stock", "Semiconductors", 25, 164.53, 165.29, 155.65, 190.17, 181.14,
     142.89, 286.24, 308.67, 189.97, 281.59, 292.00, 281.59, "LOW", "EXPENSIVE", "DISRUPTOR",
     "Not in next 30d", "-5.8% after hours."),
    ("SNDK", "Sandisk", "Stock", "Memory", 3, 1278.16, 1330.05, 1309.34, 1568.40, 1255.73,
     1163.09, 1909.48, 2354.39, None, 2287.38, 1737.50, 2012.44, "MED", "EXPENSIVE (low conf.)", "INNOVATING",
     date(2026, 10, 29), "FQ1 EPS 49.51 vs 46.36 est (beat)."),
    ("OKLO", "Oklo", "Stock", "Nuclear (pre-revenue)", 100, 26.73, 26.81, 25.78, 35.86, 54.21,
     25.39, 49.48, 145.30, None, 62.83, 37.00, 49.91, "LOW", "n/a", "n/a", date(2026, 11, 6),
     "At 52-week low. Targets disagree (52% spread)."),
    ("AAOX", "AAOI 2x Leveraged ETF", "2x Lev ETF", "Optical networking", 500, 3.84, 5.10, 4.49, 9.57, 28.89,
     3.60, 27.57, 103.00, None, None, None, 9.57, "TECH (50-day)", "n/a", "n/a", "n/a",
     "2x daily leverage on one stock; -95% from 52-wk high. Target = 50-day SMA."),
    ("GOOGL", "Alphabet", "Stock", "Internet", 6.848872, 297.58, 283.82, 282.23, 341.11, 341.14,
     316.60, 364.17, 408.61, 367.54, 405.31, 425.00, 405.31, "HIGH", "RICH", "DISRUPTOR", "Not in next 30d",
     "Well below 60-day low and both moving averages."),
    ("IONQ", "IonQ", "Stock", "Quantum computing", 30, 33.21, 31.72, 30.81, 38.44, 42.15,
     29.94, 47.95, 73.65, None, 65.77, None, 65.77, "LOW", "n/a", "n/a", date(2026, 11, 5),
     "Only one target method available."),
    ("AUR", "Aurora Innovation", "Stock", "Autonomous trucking", 200, 4.91, 4.405, 4.37, 5.73, 5.63,
     4.40, 7.16, 8.57, None, 11.33, 12.50, 11.91, "MED", "n/a", "INNOVATING", "Not in next 30d",
     "Sitting on its 60-day low."),
    ("HOOD", "Robinhood Markets", "Stock", "Brokerage", 0.010482, 90.63, 91.59, 87.37, 108.69, 92.76,
     89.15, 126.74, 150.47, None, 133.63, 145.00, 139.31, "MED", "n/a", "DISRUPTOR", "Not in next 30d",
     "Fractional leftover (<$1)."),
    ("QQQ", "Invesco QQQ", "ETF", "Nasdaq-100", 0.04204, 713.61, 715.34, 702.61, 725.61, 679.22,
     700.00, 762.86, 762.86, None, None, None, None, "n/a", "n/a", "n/a", "n/a", "Fractional leftover (~$30)."),
    ("QQQI", "NEOS Nasdaq-100 Income", "ETF", "Nasdaq-100 covered call", 0.567476, 53.83, 53.42, 52.61, 54.72, 54.18,
     52.36, 56.84, 57.84, None, None, None, None, "n/a", "n/a", "n/a", "n/a", "Fractional leftover (~$30)."),
]

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


def build(path="joint_portfolio_tracker.xlsx"):
    wb = Workbook()

    # ---------------- Inputs (assumptions) ----------------
    inp = wb.active
    inp.title = "Inputs"
    inp["A1"] = "Joint Portfolio Tracker - Assumptions"
    inp["A1"].font = Font(bold=True, size=14)
    inp["A2"] = "Blue on yellow = input. Change any of these and the Holdings sheet recalculates."
    rows = [
        ("As-of date (close used)", AS_OF, "Date of the official close in the Close column.", "0"),
        ("Price to use", "Close", "Close or After-hours. After-hours falls back to Close when blank.", None),
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
    dv = DataValidation(type="list", formula1='"Close,After-hours"', allow_blank=False)
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
    ws["C3"] = "Close date:"
    ws["D3"] = f"={ref['AsOf']}"
    ws["D3"].number_format = "yyyy-mm-dd"

    in_cols = [
        ("Symbol", 8, None), ("Company", 22, None), ("Type", 11, None), ("Sector", 20, None),
        ("Shares", 10, "#,##0.0000"), ("Avg Cost", 10, "$#,##0.00"), ("Close", 10, "$#,##0.00"),
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
            "Price Used": f'=IF(AND({ref["PriceMode"]}="After-hours",N({a("After-hrs")})>0),{a("After-hrs")},{a("Close")})',
            "Market Value": f"={a('Shares')}*{P}",
            "Cost Basis": f"={a('Shares')}*{a('Avg Cost')}",
            "Unrealized P/L $": f"={a('Market Value')}-{a('Cost Basis')}",
            "P/L %": f'=IFERROR({a("Unrealized P/L $")}/{a("Cost Basis")},"")',
            "Weight": f"={a('Market Value')}/${L['Market Value']}${tot}",
            "After-hrs Move": f'=IFERROR(IF(N({a("After-hrs")})>0,{a("After-hrs")}/{a("Close")}-1,""),"")',
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

    add_watchlist(wb, ref)

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
        ("Positions, quotes, 50/200-day SMA, 60-day range, 52-wk high, earnings dates: Robinhood (pulled 2026-10-30).", False),
        ("Targets: joint_price_targets.json (2026-10-29). Valuation and disruption grades: valuation.json (2026-10-28/29).", False),
        ("", False),
        ("Not included", True),
        ("EPIX^ (25 sh, $0 cost) has no quote: likely a delisted or escrowed position. Check it in the app.", False),
        ("Taxes: this is a taxable account. Check wash-sale lockouts (Robinhood list 'Wash-Sale Lockout') before selling at a loss and rebuying.", False),
        ("", False),
        ("Refresh", True),
        ("Edit the blue cells, or update SNAPSHOT in build_joint_tracker.py and re-run it.", False),
    ]
    for i, (t, b) in enumerate(lines, start=1):
        c = m.cell(i, 1, t)
        if b:
            c.font = Font(bold=True, size=12)
    m.column_dimensions["A"].width = 130

    wb.save(path)
    return path


# Watchlist: Quality @ 200-day buy-zone names (quality_watch_report.md, 2026-10-29T19:30Z), ordered by
# pre-breakout setup, plus the re-buy watch (rebuy_watch.json). Prices, SMAs and analyst targets: Robinhood,
# 10/29 close. Columns: sym, company, list, held, grade, q_rank, setup, valuation, disruption, close, sma50,
# sma200, analyst_mean, n_buy, n_hold, n_sell, next_earnings, wash_clear, note
WATCH = [
    ("AEM", "Agnico Eagle Mines", "Buy Zone", "", "A+", 3, "57 PULLING BACK", "RICH -23% (low)", "STABLE", 175.92, 193.80, 189.53, 225.40, 19, 4, 1, "Feb 11 (unverified)", None, "Falling wedge forming; tracks gold."),
    ("STX", "Seagate", "Buy Zone", "", "A+", 4, "57 PULLING BACK", "EXPENSIVE -50% (low)", "DISRUPTOR", 700.47, 803.15, 690.92, 1062.55, 25, 5, 0, "Jan 26 (unverified)", None, "Falling wedge forming; -4.1% after hours."),
    ("AVGO", "Broadcom", "Buy Zone", "", "A+", 7, "57 PULLING BACK", "EXPENSIVE -50% (med)", "DISRUPTOR", 345.00, 353.70, 367.78, 532.31, 53, 2, 0, date(2026, 12, 9), None, "Falling wedge forming; thesis intact 9/30. -3.7% after hours."),
    ("NVDA", "NVIDIA", "Buy Zone", "", "A+", 1, "43 PULLING BACK", "FAIR +5% (med)", "DISRUPTOR", 213.66, 221.99, 204.28, 334.45, 69, 2, 1, date(2026, 11, 17), None, "#1 on business quality."),
    ("WES", "Western Midstream", "Buy Zone", "", "A+", 6, "43 PULLING BACK", "RICH -19% (high)", "STABLE", 45.82, 46.50, 44.12, 49.54, 5, 10, 2, date(2026, 11, 4), None, "Double bottom near trigger 46.42. Analysts mostly Hold."),
    ("SCCO", "Southern Copper", "Buy Zone", "", "A+", 8, "43 PULLING BACK", "EXPENSIVE -40% (high)", "INNOVATING", 191.75, 201.33, 189.09, 176.66, 1, 8, 10, "Jan 26 (unverified)", None, "Analyst mean target is BELOW price; 10 Sells."),
    ("ASML", "ASML Holding", "Buy Zone", "", "A+", 9, "43 PULLING BACK", "EXPENSIVE -36% (med)", "DISRUPTOR", 1675.70, 1708.14, 1595.65, 2408.50, 37, 4, 2, date(2027, 1, 27), None, "Double bottom forming; -3.6% after hours."),
    ("FNV", "Franco-Nevada", "Buy Zone", "", "A", 11, "43 PULLING BACK", "FAIR -3% (med)", "STABLE", 231.60, 252.44, 240.07, 287.68, 7, 3, 1, date(2026, 11, 11), None, "Gold royalty."),
    ("HOOD", "Robinhood Markets", "Buy Zone", "HELD", "A", 14, "43 PULLING BACK", "N/A", "DISRUPTOR", 91.59, 108.69, 92.76, 133.63, 30, 5, 2, "Feb 9 (unverified)", None, "Held as a fractional leftover."),
    ("NBIX", "Neurocrine Biosciences", "Buy Zone", "", "A", 18, "43 PULLING BACK", "DEEP VALUE +100% (low)", "DISRUPTOR", 146.38, 146.75, 147.32, 207.37, 27, 4, 0, date(2026, 11, 2), None, "Reports 11/2."),
    ("ADBE", "Adobe", "Buy Zone", "", "A", 22, "43 PULLING BACK", "DEEP VALUE +100% (low)", "AT RISK", 248.12, 254.84, 250.71, 269.50, 11, 25, 5, "Dec 10 (unverified)", None, "VALUE TRAP? flag: AI design tools pressure; thesis weakened 10/23."),
    ("META", "Meta Platforms", "Buy Zone", "HELD", "A+", 5, "29 MIXED", "RICH -14% (low)", "DISRUPTOR", 624.52, 668.60, 632.11, 850.51, 65, 6, 1, "Jan 27 (unverified)", None, "Already held (~15% of the joint account)."),
    ("NEM", "Newmont", "Buy Zone", "", "A", 15, "29 MIXED", "EXPENSIVE -28% (low)", "STABLE", 111.80, 121.10, 112.49, 137.61, 24, 4, 2, "Feb 19 (unverified)", None, ""),
    ("AMAT", "Applied Materials", "Buy Zone", "", "A", 17, "29 MIXED", "EXPENSIVE -50% (low)", "INNOVATING", 421.66, 459.67, 444.04, 651.64, 35, 5, 0, date(2026, 11, 12), None, "-4.5% after hours."),
    ("RGLD", "Royal Gold", "Buy Zone", "", "A", 12, "14 EXTENDED", "FAIR +3% (high)", "STABLE", 236.83, 246.65, 241.42, 310.08, 11, 3, 1, "Nov 5 (unverified)", None, ""),
    ("WDC", "Western Digital", "Buy Zone", "", "A", 13, "14 EXTENDED", "EXPENSIVE -50% (low)", "DISRUPTOR", 395.41, 423.52, 418.23, 621.78, 22, 8, 0, "Jan 28 (unverified)", None, "-4.5% after hours."),
    ("PAC", "Grupo Aeroportuario del Pacifico", "Buy Zone", "", "A", 10, "0 EXTENDED", "DEEP VALUE +58% (med)", "DISRUPTOR", 227.47, 208.31, 236.65, 232.50, 6, 7, 0, "Feb 22 (unverified)", None, "Analyst target last updated 2020: stale."),
    ("CDNS", "Cadence Design", "Buy Zone", "HELD", "A", 19, "0 EXTENDED", "RICH -13% (med)", "DISRUPTOR", 342.75, 320.24, 327.46, 415.04, 25, 3, 0, "Feb 17 (unverified)", None, "Already held (20 sh)."),
    ("ISRG", "Intuitive Surgical", "Buy Zone", "", "A", 20, "0 EXTENDED", "DEEP VALUE +43% (high)", "AT RISK", 448.76, 400.30, 433.61, 489.57, 21, 8, 2, "Jan 22 (unverified)", None, "VALUE TRAP? flag from the quant grade; research says innovating."),
    ("TROW", "T. Rowe Price", "Buy Zone", "", "A", 21, "0 EXTENDED", "DEEP VALUE +40% (med)", "AT RISK", 106.63, 105.77, 103.68, 102.83, 0, 10, 5, "Reported 10/29", None, "VALUE TRAP? Losing assets to passive funds. No Buy ratings."),
    ("SKHY", "SK hynix (ADR)", "Buy Zone", "", "A+", 2, "n/a", "DEEP VALUE +100% (low)", "DISRUPTOR", 162.09, 169.17, 154.83, 263.91, 12, 2, 0, "Feb 13 (unverified)", None, "-5.3% after hours."),
    ("PSA", "Public Storage", "Buy Zone", "", "A", 16, "n/a", "n/a", "n/a", 317.06, 298.61, 302.64, 330.06, 7, 16, 0, "Feb 11 (unverified)", None, ""),
    ("KEYS", "Keysight", "Buy Zone", "", "A", 23, "n/a", "EXPENSIVE -40% (med)", "n/a", 329.84, 341.12, 316.26, 424.18, 13, 2, 0, date(2026, 11, 19), None, ""),
    ("MOD", "Modine Manufacturing", "Re-buy", "", "n/a", None, "WAIT (re-buy stage)", "n/a", "n/a", 138.79, 175.88, 216.14, 282.48, 12, 0, 0, "check", date(2026, 11, 14), "Sold 10/14 @ 162.10 at a loss: do not rebuy before the wash-sale date."),
]


def add_watchlist(wb, ref):
    ws = wb.create_sheet("Watchlist")
    wb.move_sheet("Watchlist", offset=-(len(wb.sheetnames) - 2))
    ws["A1"] = "Joint Watchlist - Quality @ 200-day Buy Zone + Re-buy Watch"
    ws["A1"].font = Font(bold=True, size=14)
    ws["A2"] = ("Ordered by pre-breakout chart setup (most pulled back first). Blue = inputs (10/29 close), "
                "green headers = formulas. A status is a prompt to research, never a buy order.")
    in_cols = [
        ("Symbol", 8, None), ("Company", 24, None), ("List", 9, None), ("Held?", 7, None),
        ("Quality Grade", 8, None), ("Quality Rank", 8, "0"), ("Chart Setup", 17, None), ("Valuation", 20, None),
        ("Disruption", 12, None), ("Close", 10, "$#,##0.00"), ("50-day SMA", 10, "$#,##0.00"),
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

        P, S200, T, B = a("Close"), a("200-day SMA"), a("Analyst Mean Target"), a("BUY TARGET")
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
