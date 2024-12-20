"""
Модуль для вывода информации о пакетах с помощью различных пакетных менеджеров.

Функции:
- show_package(package_names): Выводит информацию о указанных пакетах.
"""

from .utils import process_packages, detect_package_managers


def show_package(package_names):
    """Выводит информацию о указанных пакетах с помощью доступных пакетных менеджеров.

    Args:
        package_names (list): Список имен пакетов для отображения информации.

    Returns:
        None
    """
    package_managers = detect_package_managers()

    if not package_managers:
        print("❌ Не удалось определить доступные пакетные менеджеры.")
        return

    # Словарь для сопоставления пакетных менеджеров с их командами
    show_commands = {
        "epm": ["epm", "-ql"],
        # "flatpak": ["flatpak", "info"],
        "snap": ["snap", "info"],
        "paru": ["paru", "-Qi"],
        "yay": ["yay", "-Qi"],
        "dnf": ["dnf", "info"],
        "pacman": ["pacman", "-Qi"],
        "apk": ["apk", "info"],
        "xbps": ["xbps-install", "-Qi"],
        "apt": ["apt", "show"],
        "apt-get": ["apt-get", "show"],
    }

    for manager in package_managers:
        if manager in show_commands:
            try:
                print(f"📋 Получаем информацию о пакетах с помощью {manager}...\n")
                process_packages(
                    show_commands[manager], package_names, "📋 Создаем сводку о пакете:"
                )
            except RuntimeError as e:
                print(
                    f"\n❌ Ошибка при получении информации о пакетах для {manager}: {e}"
                )
