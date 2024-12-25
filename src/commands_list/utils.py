"""
Этот модуль предоставляет функции для выполнения команд в системе и управления
пакетами с помощью различных пакетных менеджеров.

Функции:
- run_command(command): Запускает указанную команду и возвращает ее вывод.
- process_pkgs(command, pkg_names, comment): Обрабатывает список пакетов, вызывая
  `run_command` для каждого пакета с указанной командой и выводя комментарий.
- detect_pkg_managers(should_filter=True): Определяет, какие пакетные менеджеры
  установлены в системе.
- check_pkg_managers(pkg_managers): Проверяет доступные пакетные менеджеры и выводит
  сообщение об ошибке, если их нет.
- check_pkg_names(pkg_names): Проверяет, указаны ли названия пакетов.
- is_command_available(command): Проверяет, доступна ли команда в системе.
- prepare_pkg_managers(pkg_names): Подготавливает список пакетных менеджеров для
  установки или удаления пакетов.

Использование:
    output = run_command(["команда", "аргумент1", "аргумент2"])
    print(output)

    process_pkgs("команда", ["пакет1", "пакет2"], "Комментарий:")
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
            f"\n\033[31m❌ Ошибка при выполнении команды:\033[0m\n{e.stderr.decode().strip()}"
        ) from e


def process_pkgs(command, pkg_names, comment):
    """Обрабатывает список пакетов с указанной командой,
    выводя комментарий для каждого пакета.

    Args:
        command (str): Команда, которую нужно выполнить.
        pkg_names (list): Список имен пакетов для обработки.
        comment (str): Комментарий, отображаемый для каждого пакета.

    Returns:
        None
    """
    if not pkg_names:
        print(color_text("❌ Название пакета не указано.", "red"))
        return

    for pkg in pkg_names:
        try:
            print(comment, pkg)
            # Запуск команды для каждого пакета
            run_command(command + [pkg])

        except RuntimeError as e:
            print(e)


def detect_pkg_managers(should_filter=True):
    """Определяет установленные пакетные менеджеры.

    Returns:
        list: Список названий пакетных менеджеров
        ('flatpak', 'nix', 'epm', 'apt-get', ...)
        или пустой список, если ни один не найден.
    """
    pkg_managers = {
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

    for manager, command in pkg_managers.items():
        if is_command_available(command):
            found_managers.append(manager)

    if should_filter:
        # Фильтруем ненужные пакетные менеджеры
        return filter_pkg_managers(found_managers)
    return found_managers


def filter_pkg_managers(found_managers):
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
            if m
            not in [
                "flatpak",
                "dnf",
                "apt",
                "apt-get",
                "rpm",
                "dpkg",
            ]
        ]

    if "apt" in found_managers:
        found_managers = [
            m
            for m in found_managers
            if m
            not in [
                "apt-get",
                "dpkg",
            ]
        ]

    if "paru" in found_managers:
        found_managers = [
            m
            for m in found_managers
            if m
            not in [
                "yay",
                "pacman",
            ]
        ]

    if "yay" in found_managers:
        found_managers = [
            m
            for m in found_managers
            if m
            not in [
                "pacman",
            ]
        ]

    return found_managers


def check_pkg_managers(pkg_managers):
    """Проверяет доступные пакетные менеджеры в системе.

    Если список пуст, выводит сообщение об ошибке и возвращает False.
    В противном случае возвращает True.

    Returns:
        bool: True, если пакетные менеджеры найдены, иначе False.
    """

    if not pkg_managers:
        print(
            color_text("❌ Не удалось определить доступные пакетные менеджеры.", "red")
        )
        return False
    return True


def check_pkg_names(pkg_names):
    """Проверяет, указаны ли названия пакетов.

    Args:
        pkg_names (list): Список имен пакетов.

    Returns:
        bool: True, если названия пакетов указаны, иначе False.
    """
    if not pkg_names:
        print(color_text("❌ Названия пакетов не указаны.", "red"))
        return False
    return True


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


def prepare_pkg_managers(pkg_names):
    """Подготавливает список пакетных менеджеров для установки или удаления пакетов.

    Args:
        pkg_names (list): Список имен пакетов.

    Returns:
        list: Список доступных пакетных менеджеров, или None, если есть ошибка.
    """
    if not check_pkg_names(pkg_names):
        return None

    pkg_managers = detect_pkg_managers()

    if not check_pkg_managers(pkg_managers):
        return None

    return pkg_managers
