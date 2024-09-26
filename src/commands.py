"""
Этот модуль предоставляет интерфейс командной строки для управления пакетами.
Поддерживаемые команды включают установку, поиск, удаление,
обновление и апгрейд пакетов.

Использование:
    python main.py <команда> [<название_пакета>]

Где команда может быть одной из следующих:
- install: Устанавливает указанный пакет
- search: Ищет указанный пакет
- remove: Удаляет указанный пакет
- update: Обновляет систему
- upgrade: Апгрейд системы
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
    """Обрабатывает аргументы командной строки и вызывает соответствующие функции."""
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
        if command in ["list", "repair", "update", "upgrade"]:
            command_handlers[command]()

        # Для установки и удаления пакетов нам нужно больше аргументов
        elif command in ["install", "remove", "search", "show"]:
            package_names = sys.argv[2:]
            if not package_names:
                print(f"Использование: python main.py {command} <название_пакета>...")
                return 1

            command_handlers[command](package_names)

        else:
            print(f"Использование: python main.py {command} <название_пакета>")
            return 1

    else:
        print(
            "=============================\n"
            "Ошибка: команда не распознана\n"
            "=============================\n"
            "Доступные команды:\n"
            "- install   : установка пакетов в систему\n"
            "- list      : вывод списка установленных пакетов\n"
            "- remove    : удаление установленных пакетов\n"
            "- search    : поиск пакетов\n"
            "- show      : отображение информации о пакете\n"
            "- update    : синхронизация репозиториев системы\n"
            "- upgrade   : обновление всех установленных пакетов\n"
            "============================="
        )

        return 1

    return 0
