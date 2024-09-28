"""
Этот модуль предоставляет интерфейс командной строки для управления пакетами. 
Поддерживаемые команды включают установку, поиск, удаление, обновление и апгрейд пакетов.

Использование:
    python main.py <команда> [<название_пакета>]

Команды:
- install : Устанавливает указанный пакет.
- list    : Выводит список установленных пакетов.
- remove  : Удаляет указанный пакет.
- repair  : Проверяет целостность пакетного менеджера и пакетов.
- search  : Ищет указанный пакет.
- show    : Отображает информацию о пакете.
- update  : Обновляет систему, синхронизируя репозитории.
- upgrade : Апгрейд системы, обновляя все установленные пакеты.
"""

import sys
from commands_list.install import install_package
from commands_list.list import list_package
from commands_list.remove import remove_package
from commands_list.repair import repair_package
from commands_list.search import search_package
from commands_list.show import show_package
from commands_list.update import update_system
from commands_list.upgrade import upgrade_system


def handle_arguments():
    """Обрабатывает аргументы командной строки
    и вызывает соответствующие функции для выполнения команд.

    Проверяет количество аргументов на входе и определяет, какую команду
    нужно выполнить. Если команда требует имя пакета, проверяет его наличие
    и передает управление соответствующей функции.

    Возвращает:
        int: Код завершения (0 при успешном выполнении, 1 при ошибке).
    """
    if len(sys.argv) < 2:
        print("Использование: python main.py <команда> [<название_пакета>...]")
        return 1

    command = sys.argv[1]
    command_handlers = {
        "install": install_package,
        "list": list_package,
        "remove": remove_package,
        "repair": repair_package,
        "search": search_package,
        "show": show_package,
        "update": update_system,
        "upgrade": upgrade_system,
    }

    if command in command_handlers:
        # Для команд, которые не требуют указания пакета, просто вызываем их
        if command in ["list", "repair", "update", "upgrade"]:
            command_handlers[command]()

        elif command in ["install", "remove", "search", "show"]:
            # Для команд, требующих указания имени пакета
            package_names = sys.argv[2:]

            if not package_names:
                print(f"Использование: python main.py {command} <название_пакета>...")
                return 1

            command_handlers[command](package_names)

    else:
        # Если команда не распознана, выводим сообщение об ошибке
        print(
            "=============================\n"
            "Ошибка: команда не распознана\n"
            "=============================\n"
            "Доступные команды:\n"
            "- install   : установка пакетов в систему\n"
            "- list      : вывод списка установленных пакетов\n"
            "- remove    : удаление установленных пакетов\n"
            "- repair    : проверка целостности пакетного менеджера и пакетов\n"
            "- search    : поиск пакетов\n"
            "- show      : отображение информации о пакете\n"
            "- update    : синхронизация репозиториев системы\n"
            "- upgrade   : обновление всех установленных пакетов\n"
            "============================="
        )
        return 1

    return 0
