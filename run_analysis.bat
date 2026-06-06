@echo off
REM Stock Autopilot - daily market analysis (read-only, no trading).
REM Runs analyze.py and appends console output to logs\cron.log.
REM analyze.py also writes its own timestamped analysis_*.json into logs\.

cd /d "C:\Users\Owner\OneDrive\Documents\Claude Code\stock-autopilot"
echo ==================== run %date% %time% ==================== >> "logs\cron.log"
"C:\Python314\python.exe" analyze.py --top 20 >> "logs\cron.log" 2>&1
echo. >> "logs\cron.log"
