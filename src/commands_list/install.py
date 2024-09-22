"""
Модуль для установки пакетов с помощью пакетного менеджера pacman.

Функции:
- install_package(package_name): Устанавливает указанный пакет.
"""

from .utils import run_command


def install_package(package_names):
    """Устанавливает указанные пакеты с помощью пакетного менеджера."""
    if not package_names:
        print("❌ Названия пакетов не указаны.")
        return

    try:
        print(f"📦 Устанавливаем пакеты: {', '.join(package_names)}")
        run_command(["sudo", "pacman", "-Sy", "--noconfirm"] + package_names)
        print(f"🎉 Установка {', '.join(package_names)} завершена успешно!")

    except RuntimeError as e:
        print(e)
