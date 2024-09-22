"""
Модуль для вывода информации о пакете с помощью пакетного менеджера pacman.

Функции:
- show_package(package_names): Выводит информацию о пакете.
"""

from .utils import run_command


def show_package(package_names):
    """Вывод информации о пакете."""
    if not package_names:
        print("❌ Название пакета не указано.")
        return

    for package in package_names:
        try:
            for package in package_names:
                print(f"🗒️ Создаем сводку о пакете: {package}")
                run_command(["pacman", "-Qii", package])

        except RuntimeError as e:
            print(e)
