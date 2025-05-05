@echo off
if "%1"=="run" (
    python main.py
) else if "%1"=="test" (
    pytest
) else if "%1"=="lint" (
    flake8 .
) else (
    echo Unknown command: %1
)
