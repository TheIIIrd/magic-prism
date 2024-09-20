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
        raise RuntimeError(f"Ошибка при выполнении команды: {e.stderr.strip()}") from e
