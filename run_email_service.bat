@echo off
REM Generic launcher for the SMTP Email Service

REM Path to your Python executable
set PY_EXE="C:\Path\To\Your\Python\python.exe"

REM Path to the directory containing your FastAPI app (mail_service.py)
set APP_DIR="C:\Path\To\Your\EmailTool"

cd /d %APP_DIR%

%PY_EXE% mail_service.py
pause
