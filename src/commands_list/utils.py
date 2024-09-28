"""
Этот модуль предоставляет функции для выполнения команд в системе.
Функция `run_command` запускает указанную команду и возвращает ее вывод.
Функция `process_packages` обрабатывает список пакетов, вызывая `run_command` для каждого пакета.

Использование:
    output = run_command(["команда", "аргумент1", "аргумент2"])
    print(output)

    process_packages("команда", ["пакет1", "пакет2"], "Комментарий:")
"""

import subprocess


def run_command(command):
    """Запускает указанную команду и возвращает ее вывод.

    Args:
        command (list): Список, содержащий команду и её аргументы.

    Raises:
        RuntimeError: Если выполнение команды завершилось с ошибкой,
        возвращает сообщение с деталями ошибки.

    Returns:
        bytes: Вывод команды в байтах.
    """
    try:
        result = subprocess.run(
            command,
            check=True,
            # stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.stdout

    except subprocess.CalledProcessError as e:
        # Явно перекидываем исключение с указанием на оригинальную ошибку
        raise RuntimeError(
            f"❌ Ошибка при выполнении команды:\n{e.stderr.decode().strip()}"
        ) from e


def process_packages(command, package_names, comment):
    """Обрабатывает список пакетов с указанной командой,
    выводя комментарий для каждого пакета.

    Args:
        command (str): Команда, которую нужно выполнить.
        package_names (list): Список имен пакетов для обработки.
        comment (str): Комментарий, отображаемый для каждого пакета.

    Returns:
        None
    """
    if not package_names:
        print("❌ Название пакета не указано.")
        return

    for package in package_names:
        try:
            print(comment, package)
            run_command(command + [package])  # Запуск команды для каждого пакета

        except RuntimeError as e:
            print(e)
