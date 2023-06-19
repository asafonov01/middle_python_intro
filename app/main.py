"""Генератор приветствий."""
import sys


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name(str): Имя пользователя

    Returns:
        str: Текст приветствия
    """
    return 'Привет, {0}'.format(name.title())


if __name__ == '__main__':
    greeting(str(sys.argv[1]))
