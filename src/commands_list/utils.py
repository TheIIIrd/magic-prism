"""
Этот модуль предоставляет функции для выполнения команд в системе.
Функция `run_command` запускает указанную команду и возвращает ее вывод.
Функция `process_packages` обрабатывает список пакетов, вызывая `run_command` для каждого пакета.
Функция `detect_package_managers` определяет, какие пакетные менеджеры используются в системе.

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


def detect_package_managers():
    """Определяет установленные пакетные менеджеры.

    Returns:
        list: Список названий пакетных менеджеров ('apt', 'dnf', 'pacman') или пустой список, если ни один не найден.
    """
    package_managers = {
        "flatpak": ["flatpak"],
        "snap": ["snap"],
        "nix": ["nix"],
        "gnu_guix": ["guix"],
        "epm": ["epm"],
        "paru": ["paru"],
        "yay": ["yay"],
        "zypper": ["zypper"],
        "dnf": ["dnf"],
        "pacman": ["pacman"],
        "apk-tools": ["apk-tools"],
        "portage": ["portage"],
        "xbps": ["xbps"],
        "apt": ["apt", "apt-get"],
        "rpm": ["rpm"],
        "dpkg": ["dpkg"],
    }

    found_managers = []

    for manager, commands in package_managers.items():
        for command in commands:
            if is_command_available(command):
                found_managers.append(manager)

    return found_managers


def is_command_available(command):
    """Проверяет, доступна ли команда в системе.

    Args:
        command (str): Название команды для проверки.

    Returns:
        bool: True, если команда доступна, иначе False.
    """
    try:
        subprocess.run(
            [command, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return True
    except FileNotFoundError:
        return False
