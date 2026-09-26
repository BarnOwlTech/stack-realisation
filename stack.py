from typing import Iterator

import stack_exceptions

class Stack:
    """Реализация стэка на основе списка Python"""
    def __init__(self, *args) -> None:
        self.stack = []
        for arg in args:
            self.stack.append(arg)

    def __iter__(self) -> Iterator:
        """Итератор стэка"""
        return iter(self.stack)

    def __reversed__(self) -> Iterator:
        """Обратный итератор стэка"""
        return reversed(self.stack)

    def __len__(self) -> int:
        """Длина стэка"""
        return len(self.stack)

    def __repr__(self) -> str:
        """Строковое представление стэка для разработчика"""
        return f"Stack({self.stack})"

    def __str__(self) -> str:
        """Строковое представление стэка для пользователя"""
        if self.is_empty():
            return "Stack empty"
        return f"Stack: {self.stack}\n> Size {self.size()}"

    def size(self) -> int:
        """Размер стэка"""
        return len(self.stack)

    def is_empty(self) -> bool:
        """Проверка, является ли стэк пустым"""
        return len(self.stack) == 0

    def push(self, *items) -> None:
        """Добавление элементов в стэк"""
        for item in items:
            self.stack.append(item)

    def pop(self) -> object:
        """Извлечение элемента из стэка"""
        if self.is_empty():
            raise stack_exceptions.EmptyStackException("Попытка удалить элемент из пустого стэка")
        else:
            answer = self.stack[-1]
            del self.stack[-1]
            return answer

    def peek(self) -> object:
        """Получить первый элемент стэка без удаления"""
        if self.is_empty():
            raise stack_exceptions.EmptyStackException("Попытка получить первый элемент из пустого стэка")
        return self.stack[-1]

    def clear(self) -> None:
        """Очистка стэка"""
        self.stack.clear()

    def contains(self, item) -> bool:
        """Проверка, содержится ли элемент в стэке"""
        return item in self.stack

class LimitedStack(Stack):
    """Реализация ограниченного стэка на основе списка Python"""
    def __init__(self, limit: int, *args) -> None:
        if limit <= 0:
            raise ValueError("Попыка указать некорректный лимит для стэка")
        elif len(args) > limit:
            raise stack_exceptions.StackOverflowException("Попытка создать стэк с количеством элементов, превышающим лимит")
        super().__init__(*args)
        self.limit = limit

    def push(self, *items) -> None:
        """Добавление элементов в стэк"""
        if len(self.stack) + len(items) > self.limit:
            raise stack_exceptions.StackOverflowException("Попытка добавить элемент в переполненный стэк")
        super().push(*items)

    def pop_multiple(self, count: int) -> list:
        """Извлечение нескольких элементов из стэка"""
        if self.is_empty():
            raise stack_exceptions.EmptyStackException("Попытка удалить элемент из пустого стэка")
        if count > len(self.stack):
            raise stack_exceptions.StackOverflowException("Попытка удалить больше элементов, чем есть в стэке")
        result = []
        for _ in range(count):
            result.append(self.pop())
        return result

    def search(self, item) -> int:
        """Поиск элемента в стэке"""
        if self.is_empty():
            raise stack_exceptions.EmptyStackException("Попытка поиска элемента в пустом стэке")
        if item not in self.stack:
            return -1
        return self.stack.index(item)
