"""
Модуль для синхронизации репозиториев системы с помощью пакетного менеджера pacman.

Функции:
- update_system(): Синхронизирует репозитории системы.
"""

from .utils import run_command


def update_system():
    """Синхронизация репозиториев системы с помощью пакетного менеджера pacman.

    Эта функция выполняет следующие действия:
    1. Синхронизирует базы данных пакетов с помощью команды `pacman -Syy`.
    2. Обновляет базы данных файлов с помощью команды `pacman -Fy`.

    Возвращает:
        None
    """
    try:
        print("🔄 Синхронизируем репозитории системы...")

        # Исполняем команду для синхронизации баз данных пакетов
        run_command(["sudo", "pacman", "-Syy"])

        # Исполняем команду для обновления баз данных файлов
        run_command(["sudo", "pacman", "-Fy"])

        print("🎉 Синхронизация репозиториев завершена успешно!")

    except RuntimeError as e:
        print(f"❌ Ошибка при синхронизации: {e}")
