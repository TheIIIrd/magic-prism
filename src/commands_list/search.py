"""
Модуль для поиска пакетов с помощью различных пакетных менеджеров.

Функции:
- search_package(package_names): Ищет указанные пакеты.
"""

from .utils import process_packages, detect_package_managers
from .colors import color_text


def search_package(package_names):
    """Ищет указанные пакеты с помощью доступных пакетных менеджеров.

    Args:
        package_names (list): Список имен пакетов для поиска.

    Returns:
        None
    """
    package_managers = detect_package_managers()

    if not package_managers:
        print(
            color_text("❌ Не удалось определить доступные пакетные менеджеры.", "red")
        )
        return

    # Словарь для сопоставления пакетных менеджеров с их командами
    search_commands = {
        "epm": [["epm", "-s"]],
        "flatpak": [["flatpak", "search"]],
        "snap": [["snap", "find"]],
        "paru": [["paru", "-Ss"]],
        "yay": [["yay", "-Ss"]],
        "dnf": [["dnf", "search"]],
        "pacman": [["pacman", "-Ss"]],
        "apk": [["apk", "search"]],
        "xbps": [["xbps-install", "-Ss"]],
        "apt": [["apt", "search"]],
        "apt-get": [["apt-get", "search"]],
    }

    for manager in package_managers:
        if manager in search_commands:
            try:
                print(color_text(f"🔍 Ищем пакеты с помощью {manager}...", "magenta"))
                for command in search_commands[manager]:
                    process_packages(
                        command,
                        package_names,
                        color_text("\n🔍 Ищем пакет:", "magenta"),
                    )
                    print()
            except RuntimeError as e:
                print(
                    color_text(
                        f"\n❌ Ошибка при поиске пакетов для {manager}: {e}", "red"
                    )
                )
