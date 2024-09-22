"""
Модуль для поиска пакетов с помощью пакетного менеджера pacman.

Функции:
- search_package(package_names): Ищет указанный пакет.
"""

from .utils import run_command


def search_package(package_names):
    """Поиск указанного пакета."""
    if not package_names:
        print("❌ Название пакета не указано.")
        return

    for package in package_names:
        try:
            print(f"🔍 Ищем пакет: {package}")
            run_command(["pacman", "-Ss", package])

        except RuntimeError as e:
            print(e)
