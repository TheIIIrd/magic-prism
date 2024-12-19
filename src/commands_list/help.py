"""
Модуль для отображения справочной информации о доступных командах пакетного менеджера.

Этот модуль содержит функции, которые предоставляют пользователю информацию о
доступных командах и их назначении, чтобы упростить использование пакетного менеджера.
"""


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
        "Доступные команды:\n"
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