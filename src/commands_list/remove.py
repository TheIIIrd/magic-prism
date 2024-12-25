"""
Модуль для удаления пакетов с помощью различных пакетных менеджеров.

Функции:
- remove_pkg(pkg_names): Удаляет указанные пакеты.
- is_pkg_installed(pkg_name, pkg_manager) Проверяет, установлен ли пакет.
"""

from .utils import run_command, detect_pkg_managers, check_pkg_managers
from .colors import color_text


def remove_pkg(pkg_names):
    """Удаляет указанные пакеты с помощью поддерживаемых пакетных менеджеров.

    Args:
        pkg_names (list): Список имен пакетов, которые необходимо удалить.

    Returns:
        None
    """
    if not pkg_names:
        print(color_text("❌ Названия пакетов не указаны.", "red"))
        return

    pkg_managers = detect_pkg_managers()

    if not check_pkg_managers(pkg_managers):
        return

    # Словарь для сопоставления пакетных менеджеров с их командами удаления
    remove_commands = {
        "epm": [["sudo", "epme"]],
        "flatpak": [["flatpak", "uninstall", "--remove-data"]],
        "snap": [["snap", "remove"]],
        "paru": [["paru", "-Rsn"]],
        "yay": [["yay", "-Rsn"]],
        "dnf": [["dnf", "remove"]],
        "pacman": [["sudo", "pacman", "-Rsn", "--noconfirm"]],
        "apk": [["sudo", "apk", "del"]],
        "xbps": [["sudo", "xbps-remove", "-r"]],
        "apt": [["sudo", "apt", "remove"]],
        "apt-get": [["sudo", "apt-get", "remove"]],
    }

    # Словарь для хранения пакетов по пакетным менеджерам
    pkgs_to_remove = {manager: [] for manager in pkg_managers}

    # Проверяем, какие пакеты установлены в каких менеджерах
    for pkg in pkg_names:
        for manager in pkg_managers:
            if is_pkg_installed(pkg, manager):
                pkgs_to_remove[manager].append(pkg)

    # Удаляем пакеты в зависимости от их менеджера
    for manager, pkgs in pkgs_to_remove.items():
        if pkgs:
            try:
                print(
                    color_text(
                        f"🗑 Удаляем пакеты: {', '.join(pkgs)} с помощью {manager}...",
                        "yellow",
                    )
                )

                for command in remove_commands[manager]:
                    run_command(command + pkgs)  # Запуск команды для удаления пакетов

                print(
                    color_text(
                        f"🎉 Удаление {', '.join(pkgs)} завершено успешно для {manager}!",
                        "green",
                    )
                )
            except RuntimeError as e:
                print(
                    color_text(
                        f"❌ Ошибка при удалении пакетов с {manager}: {e}", "red"
                    )
                )
        else:
            print(color_text(f"👁️‍🗨️ Нет пакетов для удаления в {manager}.", "blue"))


def is_pkg_installed(pkg_name, pkg_manager):
    """Проверяет, установлен ли пакет в указанном пакетном менеджере.

    Args:
        pkg_name (str): Имя пакета.
        pkg_manager (str): Имя пакетного менеджера.

    Returns:
        bool: True, если пакет установлен, иначе False.
    """

    # Словарь с командами для проверки установки пакетов
    commands = {
        "epm": ["rpm", "-q", pkg_name],
        "flatpak": ["flatpak", "info", pkg_name],
        "snap": ["snap", "list", pkg_name],
        "paru": ["pacman", "-Q", pkg_name],  # основа на pacman
        "yay": ["pacman", "-Q", pkg_name],  # основа на pacman
        "dnf": ["dnf", "list", "installed", pkg_name],
        "pacman": ["pacman", "-Q", pkg_name],
        "apk": ["apk", "info", pkg_name],
        "xbps": ["xbps-query", "-e", pkg_name],
        "apt": ["dpkg", "-s", pkg_name],
        "apt-get": ["dpkg", "-s", pkg_name],
    }

    # Получаем команду для заданного пакетного менеджера
    command = commands.get(pkg_manager)

    if command:
        try:
            run_command(command)
            return True
        except RuntimeError:
            return False

    # Если пакетный менеджер не распознан, возвращаем False
    return False
