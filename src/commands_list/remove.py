"""
Модуль для удаления пакетов с помощью пакетного менеджера pacman.

Функции:
- remove_package(package_names): Удаляет указанный пакет.
"""

from .utils import run_command


def remove_package(package_names):
    """Удаление указанного пакета."""
    if not package_names:
        print("❌ Названия пакетов не указаны.")
        return

    try:
        print(f"🗑 Удаляем пакеты: {', '.join(package_names)}")
        run_command(["sudo", "pacman", "-Rsn", "--noconfirm"] + package_names)
        print(f"🎉 Удаление {', '.join(package_names)} завершено успешно!")

    except RuntimeError as e:
        print(e)
