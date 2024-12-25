"""
Этот модуль предоставляет функции для выполнения команд в системе.
Функция `run_command` запускает указанную команду и возвращает ее вывод.
Функция `process_packages` обрабатывает список пакетов, вызывая `run_command` для каждого пакета.
Функция `detect_package_managers` определяет, какие пакетные менеджеры используются в системе.
Функция `is_command_available` проверяет, доступна ли команда в системе.

Использование:
    output = run_command(["команда", "аргумент1", "аргумент2"])
    print(output)

    process_packages("команда", ["пакет1", "пакет2"], "Комментарий:")
"""

import subprocess
from .colors import color_text


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
            f"\n{color_text("❌ Ошибка при выполнении команды:", "red")}\n{e.stderr.decode().strip()}"
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
        print(color_text("❌ Название пакета не указано.", "red"))
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
        list: Список названий пакетных менеджеров
        ('flatpak', 'nix', 'epm', 'apt-get', ...)
        или пустой список, если ни один не найден.
    """
    package_managers = {
        "epm": ["epm", "--version"],
        "flatpak": ["flatpak", "--version"],
        "snap": ["snap", "version"],
        "nix": ["nix", "--version"],
        "guix": ["guix", "--version"],
        "paru": ["paru", "--version"],
        "yay": ["yay", "--version"],
        "zypper": ["zypper", "--version"],
        "dnf": ["dnf", "--version"],
        "pacman": ["pacman", "--version"],
        "apk": ["apk", "--version"],
        "emerge": ["emerge", "--version"],
        "xbps": ["xbps-install", "--version"],
        "apt": ["apt", "version"],
        "apt-get": ["apt-get", "--version"],
        "rpm": ["rpm", "--version"],
        "dpkg": ["dpkg", "--version"],
    }

    found_managers = []

    for manager, command in package_managers.items():
        if is_command_available(command):
            found_managers.append(manager)

    # Фильтруем ненужные пакетные менеджеры
    return filter_package_managers(found_managers)


def filter_package_managers(found_managers):
    """Фильтрует ненужные пакетные менеджеры из списка.

    Args:
        found_managers (list): Список найденных пакетных менеджеров.

    Returns:
        list: Отфильтрованный список пакетных менеджеров.
    """
    if "epm" in found_managers:
        found_managers = [
            m
            for m in found_managers
            if m not in ["flatpak", "dnf", "apt", "apt-get", "rpm", "dpkg"]
        ]

    if "apt" in found_managers:
        found_managers = [m for m in found_managers if m not in ["apt-get", "dpkg"]]

    if "paru" in found_managers:
        found_managers = [m for m in found_managers if m not in ["yay", "pacman"]]

    if "yay" in found_managers:
        found_managers = [m for m in found_managers if m not in ["pacman"]]

    return found_managers


def is_command_available(command):
    """Проверяет, доступна ли команда в системе.

    Args:
        command (str): Название команды для проверки.

    Returns:
        bool: True, если команда доступна, иначе False.
    """
    try:
        # Запускаем команду с флагом --version для проверки доступности
        subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        # Если команда не найдена или завершилась с ошибкой, возвращаем False
        return False
