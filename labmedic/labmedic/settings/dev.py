from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# Configuración de base de datos para desarrollo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'labmedica',       # Nombre de tu base de datos local
        'USER': 'postgres',        # Usuario de PostgreSQL
        'PASSWORD': 'root',        # Contraseña
        'HOST': 'localhost',       # Servidor
        'PORT': '5432',            # Puerto por defecto
    }
}

# En desarrollo, los correos se muestran en consola
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
