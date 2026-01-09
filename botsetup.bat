@echo off
setlocal EnableDelayedExpansion 
mode 120, 30

echo Type 1 to install needed libraries...
echo.
echo Type 9 to exit...
echo. 

set /p ola=

if /I "!ola!"=="1" goto inst 
if /I "!ola!"=="9" exit 


:inst 

pip install python-telegram-bot 

timeout /t 1 >nul 

pip install python-dotenv

echo ------------------------------------------------------------------------------------------------------------------------

echo Press any key to exit 
echo.
pause >nul 
exit 
