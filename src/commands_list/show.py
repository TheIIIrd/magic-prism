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
        "epm": [["epmqi"]],
        # "flatpak": [["flatpak", "info"]],
        "snap": [["snap", "info"]],
        "paru": [["paru", "-Qi"]],
        "yay": [["yay", "-Qi"]],
        "dnf": [["dnf", "info"]],
        "pacman": [["pacman", "-Qii"]],
        "apk": [["apk", "info"]],
        "xbps": [["xbps-install", "-Qi"]],
        "apt": [["apt", "show"]],
        "apt-get": [["apt-get", "show"]],
    }

    for manager in package_managers:
        if manager in show_commands:
            try:
                print(f"📋 Получаем информацию о пакетах с помощью {manager}...")
                for command in show_commands[manager]:
                    process_packages(
                        command, package_names, "\n📋 Создаем сводку о пакете:"
                    )
            except RuntimeError as e:
                print(
                    f"\n❌ Ошибка при получении информации о пакетах для {manager}: {e}"
                )
