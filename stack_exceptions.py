class StackExceptions(Exception):
    """Класс исключений для стэка"""

class EmptyStackException(StackExceptions):
    """Исключение для пустого стэка"""

class StackOverflowException(StackExceptions):
    """Исключение для переполнения стэка"""
