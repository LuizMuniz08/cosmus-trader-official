#!/usr/bin/env python
import sys
import os

# Obtém o diretório base do projeto (onde manage.py está localizado)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Adiciona o diretório base ao sys.path se ele ainda não estiver lá
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Obtém o diretório do projeto 'cosmos_trader_backend'
PROJECT_DIR = os.path.join(BASE_DIR, 'cosmos_trader_backend')

# Adiciona o diretório do projeto ao sys.path se ele ainda não estiver lá
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cosmos_trader_backend.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your"
            "PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
            "Available packages in this Python installation: {}".format(sys.path)
        ) from exc
    execute_from_command_line(sys.argv)