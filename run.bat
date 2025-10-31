@echo off
title Entrenamiento y Ejecución del Modelo de Casas 🏡
color 0A

echo ==============================================
echo     Verificando entorno de Python...
echo ==============================================

REM Verificar si Python está instalado
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ Python no está instalado o no está en el PATH.
    echo Por favor instala Python 3.9 o superior desde https://www.python.org/downloads/
    pause
    exit /b
)

echo ✅ Python detectado correctamente.
echo.

REM Crear entorno virtual (opcional pero recomendado)
if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv
    echo ✅ Entorno virtual creado.
)
echo Activando entorno virtual...
call venv\Scripts\activate
echo ✅ Entorno activado.
echo.

REM Verificar e instalar librerías necesarias
echo ==============================================
echo     Verificando e instalando dependencias...
echo ==============================================

REM Archivo de requisitos temporal
echo pandas>requirements.txt
echo tensorflow>>requirements.txt
echo scikit-learn>>requirements.txt
echo numpy>>requirements.txt
echo tk>>requirements.txt

pip install --upgrade pip >nul
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Ocurrió un error instalando las dependencias.
    pause
    exit /b
)

del requirements.txt >nul 2>&1
echo ✅ Todas las dependencias están instaladas correctamente.
echo.

REM Ejecutar el programa principal
echo ==============================================
echo     Iniciando el programa algoritmo.py
echo ==============================================

python algoritmo.py

echo.
echo ==============================================
echo     Ejecución finalizada.
echo ==============================================
pause
