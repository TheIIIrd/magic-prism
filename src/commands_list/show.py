"""
Модуль для вывода информации о пакетах с помощью различных пакетных менеджеров.

Функции:
- show_pkg(pkg_names): Выводит информацию о указанных пакетах.
"""

from .utils import process_pkgs, detect_pkg_managers, check_pkg_managers
from .colors import color_text


def show_pkg(pkg_names):
    """Выводит информацию о указанных пакетах с помощью доступных пакетных менеджеров.

    Args:
        pkg_names (list): Список имен пакетов для отображения информации.

    Returns:
        None
    """
    pkg_managers = detect_pkg_managers()

    if not check_pkg_managers(pkg_managers):
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

    for manager in pkg_managers:
        if manager in show_commands:
            try:
                print(
                    color_text(
                        f"📋 Получаем информацию о пакетах с помощью {manager}...",
                        "magenta",
                    )
                )

                for command in show_commands[manager]:
                    # Запуск команды для вывода информации о пакетах
                    process_pkgs(
                        command,
                        pkg_names,
                        color_text("\n📋 Создаем сводку о пакете:", "magenta"),
                    )
                    print()

            except RuntimeError as e:
                print(
                    color_text(
                        f"\n❌ Ошибка при получении информации о пакетах для {manager}: {e}",
                        "red",
                    )
                )
