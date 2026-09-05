@echo off
echo ========================================
echo    DESA ADMIN PANEL - QUICK START
echo ========================================
echo.

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Start the server
echo 🚀 Starting Desa Admin Panel...
echo.
echo 🌐 Website: http://localhost:8000
echo 🔧 Admin Panel: http://localhost:8000/admin
echo 👤 Username: admin
echo 🔑 Password: admin
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 0.0.0.0:8000

pause
