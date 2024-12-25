"""
Модуль для проверки целостности системных пакетов и пакетного менеджера.

Функции:
- repair_package(): Проверяет целостность системы и обновляет необходимые ключи и пакеты.
"""

from .utils import run_command
from .colors import color_text


def repair_package():
    """Проверяет целостность системы и обновляет ключи и пакеты pacman.

    Returns:
        None
    """
    try:
        print(color_text("🛠️ Проверяем целостность системы...", "blue"))

        # Обновление ключей Arch Linux
        run_command(
            ["sudo", "pacman", "-Sy", "--needed", "--noconfirm", "archlinux-keyring"]
        )

        # Обновление pacman-contrib, если это необходимо
        run_command(["sudo", "pacman", "-Su", "--noconfirm", "pacman-contrib"])

        # Обновление базы данных пакетов
        run_command(["sudo", "pacman", "-Fy"])

        # Очистка неиспользуемых версий пакетов при помощи paccache
        run_command(["sudo", "paccache", "-r"])

        print(color_text("🎉 Проверка завершена успешно!", "green"))

    except RuntimeError as e:
        print(color_text(f"❌ Ошибка при проверке целостности системы: {e}", "red"))
