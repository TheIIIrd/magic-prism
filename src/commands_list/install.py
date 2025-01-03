"""
Модуль для установки пакетов с помощью различных пакетных менеджеров.

Функции:
- install_pkg(pkg_names): Устанавливает указанные пакеты.
"""

from .utils import run_command, prepare_pkg_managers
from .colors import color_text


def install_pkg(pkg_names):
    """Устанавливает указанные пакеты с помощью поддерживаемых пакетных менеджеров.

    Args:
        pkg_names (list): Список имен пакетов, которые необходимо установить.

    Returns:
        None
    """
    pkg_managers = prepare_pkg_managers(pkg_names)
    if pkg_managers is None:
        return

    # Словарь для сопоставления пакетных менеджеров с их командами установки
    install_commands = {
        "epm": [["sudo", "epmi"]],
        "flatpak": [["flatpak", "install", "--assumeyes"]],
        "snap": [["snap", "install"]],
        "paru": [["paru", "-Sy"]],
        "yay": [["yay", "-Sy"]],
        "dnf": [["sudo", "dnf", "install", "-y"]],
        "pacman": [["sudo", "pacman", "-Sy", "--noconfirm"]],
        "apk": [["sudo", "apk", "add"]],
        "xbps": [["sudo", "xbps-install"]],
        "apt": [["sudo", "apt", "install", "-y"]],
        "apt-get": [["sudo", "apt-get", "install", "-y"]],
    }

    for manager in pkg_managers:
        if manager in install_commands:
            try:
                print(
                    color_text(
                        f"📦 Устанавливаем пакеты: {', '.join(pkg_names)} с помощью {manager}...",
                        "green",
                    )
                )

                for command in install_commands[manager]:
                    # Запуск команды для установки пакетов
                    run_command(command + pkg_names)

                print(
                    color_text(
                        f"🎉 Установка {', '.join(pkg_names)} завершена успешно для {manager}!\n",
                        "green",
                    )
                )
                return

            except RuntimeError as e:
                print(
                    color_text(
                        f"❌ Ошибка при установке пакетов с {manager}: {e}", "red"
                    )
                )

        else:
            print(color_text(f"❌ Неизвестный пакетный менеджер: {manager}", "red"))
