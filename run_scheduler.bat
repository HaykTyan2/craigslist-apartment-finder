@echo off
REM ===============================================
REM E-Commerce Tracker - Scheduler Runner
REM ===============================================
cd /d "%~dp0"


REM Run the Python scheduler script
python scheduler.py

REM Keep window open so we can see output or errors
pause
