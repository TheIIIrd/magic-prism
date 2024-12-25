"""
Модуль для удаления пакетов с помощью пакетного менеджера pacman.

Функции:
- remove_package(package_names): Удаляет указанные пакеты.
"""

from .utils import run_command
from .colors import color_text


def remove_package(package_names):
    """Удаляет указанные пакеты с помощью пакетного менеджера pacman.

    Args:
        package_names (list): Список имен пакетов, которые необходимо удалить.

    Returns:
        None
    """
    if not package_names:
        print(color_text("❌ Названия пакетов не указаны.", "red"))
        return

    try:
        print(color_text(f"🗑 Удаляем пакеты: {', '.join(package_names)}", "yellow"))
        # Запуск команды pacman для удаления пакетов с указанием параметров
        run_command(["sudo", "pacman", "-Rsn", "--noconfirm"] + package_names)
        print(
            color_text(
                f"🎉 Удаление {', '.join(package_names)} завершено успешно!", "green"
            )
        )

    except RuntimeError as e:
        print(color_text(f"❌ Ошибка при удалении пакетов: {e}", "red"))
