"""
Этот модуль предоставляет функции для проверки целостности системы и обновления пакетов.
Функция `repair_pkg` выполняет обновление ключей, пакетов и очистку неиспользуемых версий пакетов
для различных пакетных менеджеров, таких как apt, dnf, pacman, flatpak, snap и другие.
Функция `detect_pkg_managers` определяет, какие пакетные менеджеры используются в системе.
Функция `check_pkg_managers` проверяет доступные пакетные менеджеры.
Функция `run_command` запускает указанную команду и обрабатывает возможные ошибки.

Использование:
    repair_pkg()
"""

from .utils import run_command, detect_pkg_managers, check_pkg_managers
from .colors import color_text


def repair_pkg():
    """Проверяет целостность системы и обновляет ключи и пакеты для доступных пакетных менеджеров.

    Эта функция выполняет следующие действия для каждого поддерживаемого пакетного менеджера:
    - Обновляет ключи.
    - Обновляет необходимые пакеты.
    - Очищает неиспользуемые версии пакетов.

    Returns:
        None
    """
    print(color_text("🛠️ Проверяем целостность системы...", "blue"))

    # Определяем доступные пакетные менеджеры
    pkg_managers = detect_pkg_managers()

    if not check_pkg_managers(pkg_managers):
        return

    # Словарь с командами для каждого пакетного менеджера
    commands = {
        "epm": [
            (
                ["sudo", "epm", "check"],
                "Проверка целостности локальной базы пакетов...",
            ),
            (["sudo", "epm", "clean"], "Очистка кэша пакетов..."),
            (["sudo", "epm", "update"], "Обновление списка пакетов..."),
        ],
        "flatpak": [
            (["flatpak", "update"], "Обновление установленных Flatpak пакетов..."),
            (["flatpak", "repair"], "Проверка и восстановление Flatpak пакетов..."),
        ],
        "snap": [
            (["sudo", "snap", "refresh"], "Обновление установленных Snap пакетов..."),
            (
                ["sudo", "snap", "remove", "--purge"],
                "Очистка неиспользуемых Snap пакетов...",
            ),
        ],
        "dnf": [
            (["sudo", "dnf", "makecache"], "Обновление кэша DNF..."),
            (
                ["sudo", "dnf", "upgrade", "--assumeyes"],
                "Обновление установленных пакетов...",
            ),
            (
                ["sudo", "dnf", "autoremove", "--assumeyes"],
                "Очистка неиспользуемых пакетов...",
            ),
        ],
        "pacman": [
            (
                [
                    "sudo",
                    "pacman",
                    "-Sy",
                    "--needed",
                    "--noconfirm",
                    "archlinux-keyring",
                ],
                "Обновление ключей Arch Linux...",
            ),
            (
                ["sudo", "pacman", "-Su", "--noconfirm", "pacman-contrib"],
                "Обновление pacman-contrib...",
            ),
            (["sudo", "pacman", "-Fy"], "Обновление базы данных пакетов..."),
            (["sudo", "paccache", "-r"], "Очистка неиспользуемых версий пакетов..."),
        ],
        "apk": [
            (["sudo", "apk", "update"], "Обновление списка пакетов..."),
            (["sudo", "apk", "upgrade"], "Обновление установленных пакетов..."),
            (["sudo", "apk", "cache", "clean"], "Очистка кэша пакетов..."),
        ],
        "xbps": [
            (["sudo", "xbps-install", "-S"], "Обновление списка пакетов..."),
            (["sudo", "xbps-install", "-u"], "Обновление установленных пакетов..."),
            (["sudo", "xbps-remove", "-o"], "Очистка неиспользуемых пакетов..."),
        ],
        "apt": [
            (["sudo", "apt", "update"], "Обновление списка пакетов..."),
            (
                ["sudo", "apt", "upgrade", "--yes"],
                "Обновление установленных пакетов...",
            ),
            (
                ["sudo", "apt", "autoremove", "--yes"],
                "Очистка неиспользуемых пакетов...",
            ),
        ],
        "apt-get": [
            (["sudo", "apt-get", "update"], "Обновление списка пакетов..."),
            (
                ["sudo", "apt-get", "upgrade", "--yes"],
                "Обновление установленных пакетов...",
            ),
            (
                ["sudo", "apt-get", "autoremove", "--yes"],
                "Очистка неиспользуемых пакетов...",
            ),
        ],
    }

    for manager in pkg_managers:
        if manager in commands:
            print(color_text(f"🔧 Выполняем проверку для {manager}...", "cyan"))
            for command, message in commands[manager]:
                try:
                    print(color_text(message, "cyan"))
                    run_command(command)
                except RuntimeError as e:
                    print(
                        color_text(
                            f"❌ Ошибка при выполнении команды '{' '.join(command)}': {e}",
                            "red",
                        )
                    )
                    return  # Завершаем выполнение, если произошла ошибка

    print(color_text("🎉 Проверка завершена успешно!", "green"))
