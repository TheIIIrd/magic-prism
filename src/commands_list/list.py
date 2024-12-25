"""
Модуль для вывода списка установленных пакетов с использованием различных пакетных менеджеров.

Функции:
- list_pkgs(): Выводит список установленных пакетов.
"""

from .utils import run_command, detect_pkg_managers, check_pkg_managers
from .colors import color_text


def list_pkgs():
    """Выводит список установленных пакетов с помощью доступных пакетных менеджеров.

    Returns:
        None
    """
    pkg_managers = detect_pkg_managers()

    if not check_pkg_managers(pkg_managers):
        return

    # Словарь для сопоставления пакетных менеджеров с их командами
    list_commands = {
        "epm": [["epm", "-qa"], ["epm", "programs"]],
        "flatpak": [["flatpak", "list"]],
        "snap": [["snap", "list"]],
        "paru": [["paru", "-Q"]],
        "yay": [["yay", "-Q"]],
        "dnf": [["dnf", "list", "installed"]],
        "pacman": [["pacman", "-Q"]],
        "apk": [["apk", "info"]],
        "xbps": [["xbps-query", "-l"]],
        "apt": [["apt", "list", "--installed"]],
        "apt-get": [["apt-get", "list", "--installed"]],
    }

    for manager in pkg_managers:
        if manager in list_commands:
            try:
                print(
                    color_text(
                        f"📋 Создаем список установленных пакетов с помощью {manager}...",
                        "magenta",
                    )
                )

                for command in list_commands[manager]:
                    # Запуск команды для вывода списка установленных пакетов
                    run_command(command)
                    print()

            except RuntimeError as e:
                print(
                    color_text(
                        f"\n❌ Ошибка при получении списка установленных пакетов для {manager}: {e}",
                        "red",
                    )
                )

        else:
            print(color_text(f"\n❌ Неизвестный пакетный менеджер: {manager}", "red"))
