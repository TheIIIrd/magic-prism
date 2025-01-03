"""
Модуль для обновления пакетов системы с помощью различных пакетных менеджеров.

Функции:
- upgrade_system(): Обновляет пакеты системы.
"""

from .utils import run_command, detect_pkg_managers, check_pkg_managers
from .colors import color_text


def upgrade_system():
    """Обновление пакетов системы с помощью доступных пакетных менеджеров.

    Эта функция проверяет, какие пакетные менеджеры установлены в системе,
    и выполняет соответствующие команды для обновления пакетов.

    Возвращает:
        None
    """
    pkg_managers = detect_pkg_managers()

    if not check_pkg_managers(pkg_managers):
        return

    # Словарь для сопоставления пакетных менеджеров с их командами
    upgrade_commands = {
        "epm": [["sudo", "epm", "full-upgrade"]],
        "flatpak": [["flatpak", "update"]],
        "snap": [["sudo", "snap", "refresh"]],
        "paru": [["paru", "-Syu"]],
        "yay": [["yay", "-Syu"]],
        "dnf": [["sudo", "dnf", "upgrade"]],
        "pacman": [["sudo", "pacman", "-Syu", "--noconfirm"]],
        "apk": [["sudo", "apk", "upgrade"]],
        "xbps": [["sudo", "xbps-install", "-Su"]],
        "apt": [["sudo", "apt", "full-upgrade"]],
        "apt-get": [["sudo", "apt-get", "dist-upgrade"]],
    }

    for manager in pkg_managers:
        if manager in upgrade_commands:
            try:
                print(
                    color_text(
                        f"🔄 Обновляем установленные пакеты с помощью {manager}...",
                        "magenta",
                    )
                )

                for command in upgrade_commands[manager]:
                    # Запуск команды для обновления пакетов
                    run_command(command)

                print(
                    color_text(
                        f"🎉 Обновление пакетов завершено успешно для {manager}!\n",
                        "green",
                    )
                )

            except RuntimeError as e:
                print(
                    color_text(
                        f"\n❌ Ошибка при обновлении пакетов для {manager}: {e}", "red"
                    )
                )

        else:
            print(color_text(f"\n❌ Неизвестный пакетный менеджер: {manager}", "red"))
