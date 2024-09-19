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

    try:
        # Выполняем команду pacman для установки пакета
        subprocess.run(
            ["sudo", "pacman", "-Syy", "--noconfirm", package_name],
            check=True,
            # stdout=subprocess.PIPE,  # Подавляем стандартный вывод
            # stderr=subprocess.PIPE   # Подавляем стандартный вывод ошибок
        )
        print(f"Установка {package_name} завершена успешно! 🎉")

    except subprocess.CalledProcessError as e:
        print(
            f"Произошла ошибка при установке {package_name}. Ошибка: {e.stderr.decode().strip()} ❌"
        )


def main():
    """
    Главная функция, которая запускает процесс установки пакета.

    Аргументы:
    package_name (str): Название пакета для установки (принимается из командной строки).

    Возвращает:
    int: Код завершения (0 если успешно).
    """

    # Проверяем, передано ли имя пакета
    if len(sys.argv) != 2:
        print("Использование: python main.py <название_пакета>")
        return 1

    package_name = sys.argv[1]
    install_package(package_name)
    return 0


if __name__ == "__main__":
    main()
