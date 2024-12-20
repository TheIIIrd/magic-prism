"""
Модуль для отображения справочной информации о доступных командах пакетного менеджера.

Этот модуль содержит функции, которые предоставляют пользователю информацию о
доступных командах и их назначении, чтобы упростить использование пакетного менеджера.
"""

from .utils import detect_package_managers


def print_help_message():
    """Выводит справочное сообщение с описанием доступных команд.

    Эта функция отображает список команд, которые поддерживаются
    пакетным менеджером, вместе с кратким описанием каждой команды.
    Команды включают установку, удаление, обновление и другие операции
    с пакетами, что позволяет пользователю быстро ознакомиться с
    функциональностью приложения.

    Returns:
        None
    """
    print(
        "📋 Доступные команды:\n"
        "- help      : вывод справочного сообщения\n"
        "- install   : установка пакетов в систему\n"
        "- list      : вывод списка установленных пакетов\n"
        "- remove    : удаление установленных пакетов\n"
        "- repair    : проверка целостности пакетного менеджера и пакетов\n"
        "- search    : поиск пакетов\n"
        "- show      : отображение информации о пакете\n"
        "- update    : синхронизация репозиториев системы\n"
        "- upgrade   : обновление всех установленных пакетов\n"
    )

    package_managers = detect_package_managers()

    # Проверяем, есть ли пакетные менеджеры в списке
    if package_managers:
        print("📦 Доступные пакетные менеджеры:")
        for manager in package_managers:
            print(f"- {manager}")
    else:
        print("❌ Пакетные менеджеры не найдены.")
