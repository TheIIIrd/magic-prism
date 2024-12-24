"""
Модуль для поиска пакетов с помощью различных пакетных менеджеров.

Функции:
- search_package(package_names): Ищет указанные пакеты.
"""

from .utils import process_packages, detect_package_managers


def search_package(package_names):
    """Ищет указанные пакеты с помощью доступных пакетных менеджеров.

    Args:
        package_names (list): Список имен пакетов для поиска.

    Returns:
        None
    """
    package_managers = detect_package_managers()

    if not package_managers:
        print("❌ Не удалось определить доступные пакетные менеджеры.")
        return

    # Словарь для сопоставления пакетных менеджеров с их командами
    search_commands = {
        "epm": ["epm", "-s"],
        "flatpak": ["flatpak", "search"],
        "snap": ["snap", "find"],
        "paru": ["paru", "-Ss"],
        "yay": ["yay", "-Ss"],
        "dnf": ["dnf", "search"],
        "pacman": ["pacman", "-Ss"],
        "apk": ["apk", "search"],
        "xbps": ["xbps-install", "-Ss"],
        "apt": ["apt", "search"],
        "apt-get": ["apt-get", "search"],
    }

    for manager in package_managers:
        if manager in search_commands:
            try:
                print(f"🔍 Ищем пакеты с помощью {manager}...")
                process_packages(
                    search_commands[manager], package_names, "\n🔍 Ищем пакет:"
                )
            except RuntimeError as e:
                print(f"\n❌ Ошибка при поиске пакетов для {manager}: {e}")
