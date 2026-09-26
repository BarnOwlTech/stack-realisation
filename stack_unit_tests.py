"""
Юнит-тесты для проверки реализации Stack.
Использует встроенный модуль unittest.
"""

import unittest
from stack import (
    Stack,
    LimitedStack,
)
from stack_exceptions import EmptyStackException, StackOverflowException
import stack_exceptions


class TestStackBasicOperations(unittest.TestCase):
    """Тесты базовых операций стека"""

    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.stack = Stack()

    def test_empty_stack_creation(self):
        """Проверка создания пустого стека"""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_push_single_element(self):
        """Проверка добавления одного элемента"""
        self.stack.push(42)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)

    def test_push_multiple_elements(self):
        """Проверка добавления нескольких элементов"""
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            self.stack.push(elem)
        self.assertEqual(self.stack.size(), 5)

    def test_pop_element(self):
        """Проверка удаления и получения элемента"""
        self.stack.push(10)
        self.stack.push(20)
        result = self.stack.pop()
        self.assertEqual(result, 20)
        self.assertEqual(self.stack.size(), 1)

    def test_lifo_order(self):
        """Проверка порядка LIFO (Last In First Out)"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_peek(self):
        """Проверка просмотра верхнего элемента без удаления"""
        self.stack.push(100)
        self.stack.push(200)

        # Peek не должен менять размер
        result = self.stack.peek()
        self.assertEqual(result, 200)
        self.assertEqual(self.stack.size(), 2)

        # Значение должно остаться тем же
        self.assertEqual(self.stack.peek(), 200)

    def test_clear(self):
        """Проверка очистки стека"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.stack.clear()
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)


class TestStackExceptions(unittest.TestCase):
    """Тесты обработки исключений"""

    def setUp(self):
        self.stack = Stack()

    def test_pop_from_empty_stack(self):
        """Проверка исключения при pop из пустого стека"""
        with self.assertRaises(EmptyStackException):
            self.stack.pop()

    def test_peek_from_empty_stack(self):
        """Проверка исключения при peek из пустого стека"""
        with self.assertRaises(EmptyStackException):
            self.stack.peek()

    def test_stack_overflow(self):
        """Проверка исключения переполнения стека"""
        limited_stack = LimitedStack(limit=3)

        limited_stack.push(1)
        limited_stack.push(2)
        limited_stack.push(3)

        with self.assertRaises(StackOverflowException):
            limited_stack.push(4)


class TestStackWithDifferentTypes(unittest.TestCase):
    """Тесты со стеком элементов разных типов"""

    def setUp(self):
        self.stack = Stack()

    def test_integers(self):
        """Проверка работы с целыми числами"""
        for i in range(5):
            self.stack.push(i)
        self.assertEqual(self.stack.pop(), 4)

    def test_strings(self):
        """Проверка работы со строками"""
        self.stack.push("Hello")
        self.stack.push("World")
        self.assertEqual(self.stack.pop(), "World")

    def test_floats(self):
        """Проверка работы с вещественными числами"""
        self.stack.push(3.14)
        self.stack.push(2.71)
        self.assertEqual(self.stack.pop(), 2.71)

    def test_mixed_types(self):
        """Проверка работы со смешанными типами"""
        self.stack.push(42)
        self.stack.push("string")
        self.stack.push([1, 2, 3])
        self.stack.push({'key': 'value'})

        self.assertEqual(self.stack.pop(), {'key': 'value'})
        self.assertEqual(self.stack.pop(), [1, 2, 3])
        self.assertEqual(self.stack.pop(), "string")
        self.assertEqual(self.stack.pop(), 42)

    def test_none_value(self):
        """Проверка работы со значением None"""
        self.stack.push(None)
        self.assertIsNone(self.stack.pop())

    def test_complex_objects(self):
        """Проверка работы со сложными объектами"""
        obj1 = {'name': 'Alice', 'age': 30}
        obj2 = [1, 2, [3, 4, 5]]

        self.stack.push(obj1)
        self.stack.push(obj2)

        self.assertEqual(self.stack.pop(), obj2)
        self.assertEqual(self.stack.pop(), obj1)


class TestLimitedStack(unittest.TestCase):
    """Тесты расширенной версии стека с ограничениями"""

    def setUp(self):
        self.limited = LimitedStack(limit=5)

    def test_push_multiple(self):
        """Проверка добавления нескольких элементов"""
        self.limited.push(1, 2, 3, 4, 5)
        self.assertEqual(self.limited.size(), 5)

    def test_pop_multiple(self):
        """Проверка удаления нескольких элементов"""
        items = [1, 2, 3, 4, 5]
        for item in items:
            self.limited.push(item)

        popped = self.limited.pop_multiple(3)
        self.assertEqual(popped, [5, 4, 3])
        self.assertEqual(self.limited.size(), 2)

    def test_contains(self):
        """Проверка поиска элемента"""
        self.limited.push(10, 20, 30)

        self.assertTrue(self.limited.contains(20))
        self.assertFalse(self.limited.contains(40))

    def test_search(self):
        """Проверка поиска позиции элемента"""
        self.limited.push(10, 20, 30, 40, 50)

        # 50 находится на позиции 1 (с верхушки)
        self.assertEqual(self.limited.search(50), 4)
        # 10 находится на позиции 5 (с верхушки)
        self.assertEqual(self.limited.search(10), 0)
        # 99 не найден
        self.assertEqual(self.limited.search(99), -1)

    def test_pop_multiple_more_than_size(self):
        """Проверка исключения при попытке удалить больше элементов чем есть"""
        self.limited.push([1, 2, 3])

        with self.assertRaises(stack_exceptions.StackOverflowException):
            self.limited.pop_multiple(5)


class TestStackUtilityFunctions(unittest.TestCase):
    """Тесты служебных функций"""
    def test_stack_len(self):
        """Проверка функции len()"""
        stack = Stack()
        self.assertEqual(len(stack), 0)

        stack.push(1)
        stack.push(2)
        self.assertEqual(len(stack), 2)

    def test_stack_representation(self):
        """Проверка строкового представления"""
        stack = Stack()
        self.assertIn("empty", str(stack))

        stack.push(1)
        stack.push(2)
        self.assertIn("Stack:", str(stack))
        self.assertIn("Size 2", str(stack))

    def test_stack_iteration(self):
        """Проверка итерации по стеку"""
        stack = Stack()
        for i in [1, 2, 3, 4, 5]:
            stack.push(i)

        result = list(stack)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_stack_reverse_iteration(self):
        """Проверка обратной итерации"""
        stack = Stack()
        for i in [1, 2, 3, 4, 5]:
            stack.push(i)

        result = list(reversed(stack))
        self.assertEqual(result, [5, 4, 3, 2, 1])



class TestStackPerformance(unittest.TestCase):
    """Тесты производительности стека"""

    def test_push_pop_large_volume(self):
        """Проверка работы со большим количеством элементов"""
        stack = Stack()
        n = 10000

        # Push
        for i in range(n):
            stack.push(i)
        self.assertEqual(stack.size(), n)

        # Pop
        for i in range(n - 1, -1, -1):
            self.assertEqual(stack.pop(), i)
        self.assertTrue(stack.is_empty())


def run_tests():
    """Запуск всех тестов"""
    # Создаем набор тестов
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Добавляем все тесты
    suite.addTests(loader.loadTestsFromTestCase(TestStackBasicOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestStackExceptions))
    suite.addTests(loader.loadTestsFromTestCase(TestStackWithDifferentTypes))
    suite.addTests(loader.loadTestsFromTestCase(TestLimitedStack))
    suite.addTests(loader.loadTestsFromTestCase(TestStackUtilityFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestStackPerformance))

    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result


if __name__ == "__main__":
    run_tests()
