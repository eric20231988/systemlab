#!/bin/bash
# Script de arranque para entorno de desarrollo

echo "🚀 Iniciando servidor Django en modo DESARROLLO..."

# Si ya activas el entorno manualmente, no necesitas esta línea.
# Si quieres que el script lo active, ajusta la ruta real de tu venv.
# source ../lab_env/bin/activate

# Exportar settings de desarrollo
export DJANGO_SETTINGS_MODULE=labmedic.settings.dev

# Ejecutar migraciones y arrancar servidor en localhost:8000
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
