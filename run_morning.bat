@echo off
REM Stock Autopilot - MORNING combined report (read-only, no trading).
REM Full scan: 12-1 momentum + Connors RSI(2) swing. Caches history for the intraday run.
cd /d "C:\Users\Owner\OneDrive\Documents\Claude Code\stock-autopilot"
echo ==================== MORNING %date% %time% ==================== >> "logs\cron.log"
"C:\Python314\python.exe" report.py --mode morning >> "logs\cron.log" 2>&1
echo. >> "logs\cron.log"
