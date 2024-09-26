"""
Модуль для проверки целостности системных пакетов и пакетного менеджера.

Функции:
- repair_package(): Проверяет целостность системы.
"""

from .utils import process_packages


def repair_package():
    """Проверка целостности системы."""
    try:
        print("🛠️ Проверяет целостность системы...")
        run_command(
            ["sudo", "pacman", "-Sy", "--needed", "--noconfirm", "archlinux-keyring"]
        )
        run_command(["sudo", "pacman", "-Su", "--noconfirm", "pacman-contrib"])
        run_command(["sudo", "pacman", "-Fy"])
        run_command(["sudo", "paccache", "-r"])
        print("🎉 Проверка завершена успешно!")

    except RuntimeError as e:
        print(e)
