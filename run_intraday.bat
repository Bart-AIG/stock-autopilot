@echo off
REM Stock Autopilot - INTRADAY combined report (read-only, no trading).
REM Reuses the morning history cache, overlays live prices, rechecks swing triggers.
cd /d "C:\Users\Owner\OneDrive\Documents\Claude Code\stock-autopilot"
echo ==================== INTRADAY %date% %time% ==================== >> "logs\cron.log"
"C:\Python314\python.exe" report.py --mode intraday >> "logs\cron.log" 2>&1
echo. >> "logs\cron.log"
