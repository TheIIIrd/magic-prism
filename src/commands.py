import sys
from commands_list.install import install_package
from commands_list.search import search_package
from commands_list.remove import remove_package
from commands_list.update import update_system
from commands_list.upgrade import upgrade_system


def handle_arguments():
    """Обрабатывает аргументы командной строки и вызывает соответствующие функции."""
    if len(sys.argv) < 2:
        print("Использование: python main.py <команда> [<название_пакета>]")
        return 1

    command = sys.argv[1]
    command_handlers = {
        "install": install_package,
        "search": search_package,
        "remove": remove_package,
        "update": update_system,
        "upgrade": upgrade_system,
    }

    if command in command_handlers:
        if command in ["update", "upgrade"]:
            command_handlers[command]()

        elif len(sys.argv) != 3:
            print(f"Использование: python main.py {command} <название_пакета>")
            return 1

        else:
            package_name = sys.argv[2]
            command_handlers[command](package_name)

    else:
        print(
            "Неизвестная команда. Используйте: install, search, remove, update, upgrade."
        )
        return 1

    return 0
