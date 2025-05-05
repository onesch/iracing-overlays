@echo off
if "%1"=="run" (
    call .\venv\Scripts\activate
    python main.py
) else if "%1"=="test" (
    call .\venv\Scripts\activate
    pytest
) else if "%1"=="lint" (
    call .\venv\Scripts\activate
    flake8 .
) else (
    echo Unknown command: %1
)
