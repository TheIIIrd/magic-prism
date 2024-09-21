"""
Модуль для вывода информации о пакете с помощью пакетного менеджера pacman.

Функции:
- show_package(package_name): Выводит информацию о пакете.
"""

from .utils import run_command


def show_package(package_name):
    """Вывод информации о пакете."""
    if not package_name:
        print("❌ Название пакета не указано.")
        return

    try:
        print(f"🗒️ Создаем сводку о пакете: {package_name}")
        run_command(["pacman", "-Qii", package_name])

    except RuntimeError as e:
        print(e)
