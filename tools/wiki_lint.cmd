@echo off
setlocal

set "SCRIPT=%~dp0wiki_lint.py"
set "BUNDLED=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 goto run_python

if exist "%BUNDLED%" goto run_bundled

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 goto run_py

echo Could not find Python. Install Python, add it to PATH, or run wiki_lint.py with a known interpreter.
exit /b 127

:run_python
python "%SCRIPT%" %*
exit /b %ERRORLEVEL%

:run_bundled
"%BUNDLED%" "%SCRIPT%" %*
exit /b %ERRORLEVEL%

:run_py
py "%SCRIPT%" %*
exit /b %ERRORLEVEL%
