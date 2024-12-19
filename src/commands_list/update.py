"""
Модуль для синхронизации репозиториев системы с помощью различных пакетных менеджеров.

Функции:
- update_system(): Синхронизирует репозитории системы.
"""

from .utils import run_command, detect_package_managers


def update_system():
    """Синхронизация репозиториев системы с помощью доступных пакетных менеджеров.

    Эта функция проверяет, какие пакетные менеджеры установлены в системе,
    и выполняет соответствующие команды для синхронизации репозиториев.

    Возвращает:
        None
    """
    package_managers = detect_package_managers()

    if not package_managers:
        print("❌ Не удалось определить доступные пакетные менеджеры.")
        return

    # Словарь для сопоставления пакетных менеджеров с их командами
    update_commands = {
        "epm": [["epm", "update"]],
        "flatpak": [["flatpak", "update"]],
        "snap": [["sudo", "snap", "refresh"]],
        "paru": [["paru", "-Sy"]],
        "yay": [["yay", "-Sy"]],
        "dnf": [["sudo", "dnf", "makecache"], ["sudo", "dnf", "check-update"]],
        "pacman": [["sudo", "pacman", "-Syy"], ["sudo", "pacman", "-Fy"]],
        "apk": [["sudo", "apk", "update"]],
        "xbps": [["sudo", "xbps-install", "-Syu"]],
        "apt": [["sudo", "apt", "update"]],
        "apt-get": [["sudo", "apt-get", "update"]],
    }

    for manager in package_managers:
        if manager in update_commands:
            try:
                print(f"🔄 Синхронизируем репозитории с помощью {manager}...")
                for command in update_commands[manager]:
                    run_command(command)
                print(f"🎉 Синхронизация репозиториев завершена успешно для {manager}!")
            except RuntimeError as e:
                print(f"❌ Ошибка при синхронизации для {manager}: {e}")
        else:
            print(f"❌ Неизвестный пакетный менеджер: {manager}")
