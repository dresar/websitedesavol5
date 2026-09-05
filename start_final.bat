@echo off
echo ========================================
echo    DESA ADMIN PANEL - FINAL START
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.11+ first.
    pause
    exit /b 1
)

echo ✅ Python detected

REM Create virtual environment if not exists
if not exist ".venv" (
    echo 🔄 Creating virtual environment...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment already exists
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✅ Virtual environment activated

REM Upgrade pip
echo 🔄 Upgrading pip...
python -m pip install --upgrade pip

REM Install all required packages
echo 🔄 Installing all required packages...
pip install Django==4.2.7 python-decouple==3.8 Pillow djangorestframework django-cors-headers django-filter dj-database-url
if %errorlevel% neq 0 (
    echo ❌ Failed to install packages
    pause
    exit /b 1
)
echo ✅ All packages installed successfully

REM Run migrations
echo 🔄 Running database migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ❌ Failed to run migrations
    pause
    exit /b 1
)
echo ✅ Database migrations completed

REM Collect static files
echo 🔄 Collecting static files...
python manage.py collectstatic --noinput
if %errorlevel% neq 0 (
    echo ❌ Failed to collect static files
    pause
    exit /b 1
)
echo ✅ Static files collected

REM Check if superuser exists, if not create one
echo 🔄 Checking for superuser...
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print('Superuser exists:', User.objects.filter(username='admin').exists())" 2>nul | findstr "True" >nul
if %errorlevel% neq 0 (
    echo 🔄 Creating superuser...
    echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None | python manage.py shell
    echo ✅ Superuser created (username: admin, password: admin123)
) else (
    echo ✅ Superuser already exists
)

echo.
echo ========================================
echo    🚀 DESA ADMIN PANEL IS RUNNING!
echo ========================================
echo.
echo 🌐 Website: http://localhost:8000
echo 🔧 Admin Panel: http://localhost:8000/admin
echo 👤 Username: admin
echo 🔑 Password: admin123
echo.
echo 📊 Features Available:
echo    - Dashboard with statistics
echo    - Penduduk Management
echo    - Surat Menyurat System
echo    - Keuangan Management
echo    - Laporan & Monitoring
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the server
python manage.py runserver 0.0.0.0:8000

pause
