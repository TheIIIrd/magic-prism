"""
Модуль для удаления пакетов с помощью различных пакетных менеджеров.

Функции:
- remove_package(package_names): Удаляет указанные пакеты.
- is_package_installed(package_name, package_manager) Проверяет, установлен ли пакет.
"""

from .utils import run_command, detect_package_managers, check_package_managers
from .colors import color_text


def remove_package(package_names):
    """Удаляет указанные пакеты с помощью поддерживаемых пакетных менеджеров.

    Args:
        package_names (list): Список имен пакетов, которые необходимо удалить.

    Returns:
        None
    """
    if not package_names:
        print(color_text("❌ Названия пакетов не указаны.", "red"))
        return

    package_managers = detect_package_managers()

    if not check_package_managers(package_managers):
        return

    # Словарь для сопоставления пакетных менеджеров с их командами удаления
    remove_commands = {
        "epm": [["epme"]],
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
    packages_to_remove = {manager: [] for manager in package_managers}

    # Проверяем, какие пакеты установлены в каких менеджерах
    for package in package_names:
        for manager in package_managers:
            if is_package_installed(package, manager):
                packages_to_remove[manager].append(package)

    # Удаляем пакеты в зависимости от их менеджера
    for manager, packages in packages_to_remove.items():
        if packages:
            try:
                print(
                    color_text(
                        f"🗑 Удаляем пакеты: {', '.join(packages)} с помощью {manager}...",
                        "yellow",
                    )
                )
                command = remove_commands[manager]
                run_command(command + packages)  # Запуск команды для удаления
                print(
                    color_text(
                        f"🎉 Удаление {', '.join(packages)} завершено успешно для {manager}!",
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


def is_package_installed(package_name, package_manager):
    """Проверяет, установлен ли пакет в указанном пакетном менеджере.

    Args:
        package_name (str): Имя пакета.
        package_manager (str): Имя пакетного менеджера.

    Returns:
        bool: True, если пакет установлен, иначе False.
    """

    # Словарь с командами для проверки установки пакетов
    commands = {
        "epm": [["rpm", "-q"]],
        "flatpak": ["flatpak", "info", package_name],
        "snap": ["snap", "list", package_name],
        "paru": ["pacman", "-Q", package_name],  # основа на pacman
        "yay": ["pacman", "-Q", package_name],  # основа на pacman
        "dnf": ["dnf", "list", "installed", package_name],
        "pacman": ["pacman", "-Q", package_name],
        "apk": ["apk", "info", package_name],
        "xbps": ["xbps-query", "-e", package_name],
        "apt": ["dpkg", "-s", package_name],
        "apt-get": ["dpkg", "-s", package_name],
    }

    # Получаем команду для заданного пакетного менеджера
    command = commands.get(package_manager)

    if command:
        try:
            run_command(command)
            return True
        except RuntimeError:
            return False

    # Если пакетный менеджер не распознан, возвращаем False
    return False
