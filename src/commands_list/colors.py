"""Модуль для окрашивания текста в различные цвета с использованием ANSI escape codes."""


class ColorText:
    """Класс для окрашивания текста в различные цвета."""

    # ANSI escape codes для цветов
    COLORS = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m",
    }

    def color_text(self, text: str, color: str) -> str:
        """Возвращает текст, окрашенный в указанный цвет.

        Args:
            text (str): Текст для окрашивания.
            color (str): Цвет, в который нужно окрасить текст.

        Returns:
            str: Окрашенный текст.
        """
        if color.lower() not in self.COLORS:
            raise ValueError(
                f"\n❌Некорректный цвет: {color}. Доступные цвета: {', '.join(self.COLORS.keys())}"
            )

        color_code = self.COLORS[color.lower()]
        return f"{color_code}{text}{self.COLORS['reset']}"

    def list_colors(self) -> list:
        """Возвращает список доступных цветов.

        Returns:
            list: Список доступных цветов.
        """
        return list(self.COLORS.keys())


# Создаем экземпляр класса
color_text_instance = ColorText()

# Экспортируем метод color_text
color_text = color_text_instance.color_text
