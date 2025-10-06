from pathlib import Path
import os

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Seguridad
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'clave-segura-en-desarrollo')

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # 👈 agrega aquí tus dominios o IPs en producción

# Aplicaciones instaladas
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceros
    'django_filters',
    'django_select2',
    'widget_tweaks',

    # Apps del proyecto
    'dashboard',
    'accounts',
    'pacientes.apps.PacientesConfig',
    'analisis',
    'examen',
    'especialidad',
    'laboratorio',
    'informes',
    'precios',
    'analitos',
    'registrar_examenes',
    'resultados_analitos',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Rutas principales
ROOT_URLCONF = 'labmedic.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Carpeta global de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'labmedic.wsgi.application'

# Base de datos: se define en dev.py o prod.py
# Ejemplo de configuración PostgreSQL (puedes moverlo a dev/prod):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('POSTGRES_DB', 'labmedic'),
#         'USER': os.environ.get('POSTGRES_USER', 'postgres'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'password'),
#         'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
#         'PORT': os.environ.get('POSTGRES_PORT', '5432'),
#     }
# }

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Archivos subidos por usuarios
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración por defecto de IDs
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Autenticación
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'dashboard:panel'
LOGOUT_REDIRECT_URL = 'accounts:login'
LOGIN_URL = 'accounts:login'
