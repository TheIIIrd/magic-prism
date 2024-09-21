"""
Модуль для поиска пакетов с помощью пакетного менеджера pacman.

Функции:
- search_package(package_name): Ищет указанный пакет.
"""

from .utils import run_command


def search_package(package_name):
    """Поиск указанного пакета."""
    if not package_name:
        print("❌ Название пакета не указано.")
        return

    try:
        print(f"🔍 Ищем пакет: {package_name}")
        run_command(["pacman", "-Ss", package_name])

    except RuntimeError as e:
        print(e)
