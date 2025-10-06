#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks with environment-specific settings."""
    # Si no está definido, usar dev por defecto
    settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', 'labmedic.settings.dev')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y activado tu entorno virtual?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
