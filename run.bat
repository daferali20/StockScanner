@echo off
REM تشغيل Backend أولاً
echo Starting Backend...
start cmd /k "python server/main.py"

REM الانتظار 5 ثواني ثم تشغيل Frontend
timeout /t 5
echo Starting Frontend...
start cmd /k "cd client && npm start"

pause
