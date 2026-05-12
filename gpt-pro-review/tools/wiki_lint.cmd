@echo off
setlocal

set "SCRIPT=%~dp0wiki_lint.py"
set "BUNDLED=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python "%SCRIPT%" %*
    exit /b
)

if exist "%BUNDLED%" (
    "%BUNDLED%" "%SCRIPT%" %*
    exit /b
)

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    py "%SCRIPT%" %*
    exit /b
)

echo Could not find Python. Install Python, add it to PATH, or run wiki_lint.py with a known interpreter.
exit /b 127
