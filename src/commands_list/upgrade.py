"""
Модуль для обновления пакетов системы с помощью различных пакетных менеджеров.

Функции:
- upgrade_system(): Обновляет пакеты системы.
"""

from .utils import run_command, detect_package_managers


def upgrade_system():
    """Обновление пакетов системы с помощью доступных пакетных менеджеров.

    Эта функция проверяет, какие пакетные менеджеры установлены в системе,
    и выполняет соответствующие команды для обновления пакетов.

    Возвращает:
        None
    """
    package_managers = detect_package_managers()

    if not package_managers:
        print("❌ Не удалось определить доступные пакетные менеджеры.")
        return

    # Словарь для сопоставления пакетных менеджеров с их командами
    upgrade_commands = {
        "epm": [["epm", "update"]],
        "flatpak": [["flatpak", "update"]],
        "snap": [["sudo", "snap", "refresh"]],
        "paru": [["paru", "-Syu"]],
        "yay": [["yay", "-Syu"]],
        "dnf": [["sudo", "dnf", "upgrade"]],
        "pacman": [["sudo", "pacman", "-Syu", "--noconfirm"]],
        "apk": [["sudo", "apk", "upgrade"]],
        "xbps": [["sudo", "xbps-install", "-Su"]],
        "apt": [["sudo", "apt", "upgrade"]],
        "apt-get": [["sudo", "apt-get", "upgrade"]],
    }

    for manager in package_managers:
        if manager in upgrade_commands:
            try:
                print(f"🔄 Обновляем установленные пакеты с помощью {manager}...\n")
                for command in upgrade_commands[manager]:
                    run_command(command)
                print(f"🎉 Обновление пакетов завершено успешно для {manager}!\n")
            except RuntimeError as e:
                print(f"\n❌ Ошибка при обновлении пакетов для {manager}: {e}")
        # else:
        #     print(f"\n❌ Неизвестный пакетный менеджер: {manager}")
