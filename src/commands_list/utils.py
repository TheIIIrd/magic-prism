"""
Этот модуль предоставляет функцию для выполнения команд в системе.
Функция `run_command` запускает указанную команду и возвращает ее вывод.

Использование:
    output = run_command(["команда", "аргумент1", "аргумент2"])
    print(output)
"""

import subprocess


def run_command(command):
    """Запускает команду и возвращает ее вывод."""
    try:
        result = subprocess.run(
            command,
            check=True,
            stderr=subprocess.PIPE,
        )
        return result.stdout

    except subprocess.CalledProcessError as e:
        # Явно перекидываем исключение с указанием на оригинальную ошибку
        raise RuntimeError(f"❌ Ошибка при выполнении команды:\n{e.stderr.strip()}") from e
