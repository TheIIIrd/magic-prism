"""
Magic Prism Package Manager written in Python that helps unify the way utilities
are installed across platforms. This is an abstraction for different package
managers so that all commands have a common interface.
"""

from commands import handle_arguments


def main():
    """Основная функция программы."""
    return handle_arguments()


if __name__ == "__main__":
    main()
