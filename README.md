# stack-realisation
Реализация стэка.

### Требования
 
- Python 3.7+
- Нет внешних зависимостей
---

## Установка
 
### Из исходного кода
 
```bash
# Клонируйте репозиторий
git clone https://github.com/BarnOwlTech/stack-realisation.git
cd stack-realisation
 
# Установите пакет в режиме разработки
pip install -e .
```
---

### Базовые операции
 
```python
from stack import Stack
 
# Создание
s = Stack()                    # Обычный стек
s = Stack(max_size=100)        # С ограничением размера
 
# Добавление
s.push(42)                     # Добавить элемент
 
# Удаление
value = s.pop()                # Удалить и получить верхний элемент
 
# Просмотр
top = s.peek()                 # Получить верхний элемент без удаления
 
# Проверка
if not s.is_empty():           # Проверить, пуст ли стек
    size = s.size()            # Получить размер
 
# Очистка
s.clear()                      # Очистить стек
```
 
### Расширенные методы
 
```python
from stack import LimitedStack
 
s = LimitedStack(max_size=10)
 
# Добавить несколько элементов
s.push_multiple([1, 2, 3, 4, 5])
 
# Удалить несколько элементов
items = s.pop_multiple(3)      # [5, 4, 3]
 
# Поиск
if s.contains(2):              # Содержит элемент?
    pos = s.search(2)          # Найти позицию (с верха)
```
 
### Обработка ошибок
 
```python
from stack import Stack, EmptyStackException, StackOverflowException
 
s = Stack(max_size=5)
 
try:
    s.push(1)
except StackOverflowException as e:
    print(f"Ошибка: {e}")
 
try:
    s.pop()
except EmptyStackException as e:
    print(f"Ошибка: {e}")
```
 
---
 
## API Документация
 
### Класс `Stack`
 
#### `__init__(max_size: int = -1)`
Создать новый стек.
- **max_size**: Максимальный размер (-1 = неограниченный)
#### `push(item: Any) -> None`
Добавить элемент в стек.
- **Time Complexity**: O(1) amortized
#### `pop() -> Any`
Удалить и вернуть верхний элемент.
- **Time Complexity**: O(1)
- **Raises**: `EmptyStackException` если стек пуст
#### `peek() -> Any`
Получить верхний элемент без удаления.
- **Time Complexity**: O(1)
- **Raises**: `EmptyStackException` если стек пуст
#### `is_empty() -> bool`
Проверить, пуст ли стек.
- **Time Complexity**: O(1)
#### `size() -> int`
Получить количество элементов.
- **Time Complexity**: O(1)
#### `clear() -> None`
Очистить стек.
- **Time Complexity**: O(n)
#### `to_list() -> List[Any]`
Получить копию элементов в виде списка.
- **Time Complexity**: O(n)
### Класс `LimitedStack` (наследуется от Stack)
 
#### `push_multiple(items: List[Any]) -> None`
Добавить несколько элементов.
 
#### `pop_multiple(count: int) -> List[Any]`
Удалить несколько элементов.
 
#### `contains(item: Any) -> bool`
Проверить, содержит ли стек элемент.
- **Time Complexity**: O(n)
#### `search(item: Any) -> int`
Найти позицию элемента (с верха, начиная с 1).
- **Time Complexity**: O(n)
- **Returns**: Позиция или -1 если не найден
### Модуль `stack.utils`
 
#### `check_parentheses(text: str) -> bool`
Проверить корректность парных скобок.
 
#### `reverse_string(s: str) -> str`
Развернуть строку используя стек.
 
#### `decimal_to_binary(num: int) -> str`
Преобразовать число в двоичное представление.
 
#### `evaluate_rpn(tokens: List[str]) -> float`
Вычислить выражение в обратной польской нотации.
