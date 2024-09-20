"""
Magic Prism Package Manager written in Python that helps unify the way utilities
are installed across platforms. This is an abstraction for different package
managers so that all commands have a common interface.
"""

import subprocess
import sys


def install_package(package_name):
    """
    Устанавливает указанный пакет с помощью пакетного менеджера pacman.

    Параметры:
    package_name (str): Название пакета, который нужно установить.

    Исключения:
    subprocess.CalledProcessError: Если установка пакета завершилась с ошибкой.
    """

    if not package_name:
        print("❌ Название пакета не указано.")
        return

    try:
        subprocess.run(
            ["sudo", "pacman", "-Sy", "--noconfirm", package_name],
            check=True,
            stderr=subprocess.PIPE,
        )
        print(f"🎉 Установка {package_name} завершена успешно!")

    except subprocess.CalledProcessError as e:
        print(
            f"❌ Произошла ошибка при установке {package_name}. Ошибка:\n{e.stderr.decode().strip()}"
        )


def search_package(package_name):
    """Поиск указанного пакета (пока заглушка)."""
    print(f"🔍 Ищем пакет: {package_name}")


def remove_package(package_name):
    """Удаление указанного пакета (пока заглушка)."""
    print(f"🗑 Удаляем пакет: {package_name}")


def update_system():
    """Обновление системы (пока заглушка)."""
    print("🔄 Обновляем систему...")


def upgrade_system():
    """Обновление пакетов системы (пока заглушка)."""
    print("🔄 Обновляем установленные пакеты...")


def handle_arguments():
    """
    Обрабатывает аргументы командной строки и вызывает соответствующие функции.

    Возвращает:
    int: Код завершения (0 если успешно, 1 если произошла ошибка).
    """

    if len(sys.argv) < 2:
        print("Использование: python main.py <команда> [<название_пакета>]")
        return 1

    command = sys.argv[1]

    # Словарь с командами и соответствующими обработчиками
    command_handlers = {
        "install": install_package,
        "search": search_package,
        "remove": remove_package,
        "update": update_system,
        "upgrade": upgrade_system,
    }

    if command in command_handlers:
        if command in ["update", "upgrade"]:
            # Для команд update и upgrade не нужен аргумент
            command_handlers[command]()

        elif len(sys.argv) != 3:
            print(f"Использование: python main.py {command} <название_пакета>")
            return 1

        else:
            package_name = sys.argv[2]
            command_handlers[command](package_name)

    else:
        print(
            "Неизвестная команда. Используйте: install, search, remove, update, upgrade."
        )
        return 1

    return 0


def main():
    """Основная функция программы."""
    return handle_arguments()


if __name__ == "__main__":
    main()
