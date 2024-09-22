"""
Модуль для поиска пакетов с помощью пакетного менеджера pacman.

Функции:
- search_package(package_names): Ищет указанный пакет.
"""

from .utils import process_packages


def search_package(package_names):
    """Поиск указанного пакета."""
    process_packages(["pacman", "-Ss"], package_names, "🔍 Ищем пакет:")
