"""
Модуль для установки пакетов с помощью пакетного менеджера pacman.

Функции:
- install_package(package_names): Устанавливает указанные пакеты.
"""

from .utils import run_command
from .colors import color_text


def install_package(package_names):
    """Устанавливает указанные пакеты с помощью пакетного менеджера pacman.

    Args:
        package_names (list): Список имен пакетов, которые необходимо установить.

    Returns:
        None
    """
    if not package_names:
        print(color_text("❌ Названия пакетов не указаны.", "red"))
        return

    try:
        print(
            color_text(f"📦 Устанавливаем пакеты: {', '.join(package_names)}", "green")
        )
        # Запуск команды pacman для установки пакетов
        run_command(["sudo", "pacman", "-Sy", "--noconfirm"] + package_names)
        print(
            color_text(
                f"🎉 Установка {', '.join(package_names)} завершена успешно!", "green"
            )
        )

    except RuntimeError as e:
        print(color_text(f"❌ Ошибка при установке пакетов: {e}", "red"))
