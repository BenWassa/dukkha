@echo off
REM Wrapper to run the PowerShell QA script from Explorer or cmd.
REM Usage: run_qa_check.bat [-CheckUrls]

SET SCRIPT_DIR=%~dp0
SET PS1_PATH=%SCRIPT_DIR%qa_check.ps1

REM Forward all args to the PowerShell script
powershell -NoProfile -ExecutionPolicy Bypass -File "%PS1_PATH%" %*
IF %ERRORLEVEL% NEQ 0 (
    echo QA script exited with code %ERRORLEVEL%
    EXIT /B %ERRORLEVEL%
)
EXIT /B 0
