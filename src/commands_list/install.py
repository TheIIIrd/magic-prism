"""
Модуль для установки пакетов с помощью пакетного менеджера pacman.

Функции:
- install_package(package_name): Устанавливает указанный пакет.
"""

from .utils import run_command


def install_package(package_name):
    """Устанавливает указанный пакет с помощью пакетного менеджера pacman."""
    if not package_name:
        print("❌ Название пакета не указано.")
        return

    try:
        output = run_command(["sudo", "pacman", "-Sy", "--noconfirm", package_name])
        print(f"🎉 Установка {package_name} завершена успешно!\n{output}")

    except RuntimeError as e:
        print(f"❌ {e}")
