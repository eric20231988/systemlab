#!/bin/bash
# Script de arranque para entorno de producción

echo "🚀 Iniciando servidor Django en modo PRODUCCIÓN..."

# Si quieres que active el entorno virtual automáticamente, ajusta la ruta:
# source ../lab_env/bin/activate

# Exportar settings de producción
export DJANGO_SETTINGS_MODULE=labmedic.settings.prod

# Ejecutar migraciones y arrancar con Gunicorn en localhost:8000
python manage.py migrate
gunicorn labmedic.wsgi:application --bind 127.0.0.1:8000 --workers 3

