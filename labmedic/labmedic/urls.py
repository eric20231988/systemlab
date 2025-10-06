from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticación y cuentas
    path('accounts/', include('accounts.urls')),         # login, logout, registro

    # Gestión de usuarios
    #path('usuarios/', include('usuarios.urls')),         # perfiles, roles
    
    path('analitos/', include('analitos.urls')),         # gestión de analitos
    path('analisis/', include('analisis.urls')),         # gestión de análisis
    path('examenes/', include('examen.urls')),         # gestión de exámenes
    

    # Gestión de pacientes
    path('pacientes/', include('pacientes.urls')),       # ficha clínica, historial

    # Especialidades médicas
    path('especialidad/', include('especialidad.urls')), # urología, cardiología, etc.

    # Exámenes y órdenes
    path('registrar_examenes/', include('registrar_examenes.urls')),

    # Analitos y resultados
    path('resultados_analitos/', include('resultados_analitos.urls')),

    # Informes clínicos
    path('informes/', include('informes.urls')),

    # Precios y tarifas
    path('precios/', include('precios.urls')),

    # Citas médicas (si existe)
    #path('citas/', include('citas.urls')),

    # Dashboard o panel principal
    path('', include('dashboard.urls')),                 # vista principal del sistema
]
