# Лабораторная работа №3 «Построение бинарного дерева»

## 1. Цель работы
Написать рекурсивную функцию `gen_bin_tree`, которая строит бинарное дерево по параметрам `height`, `root`, `left_leaf`, `right_leaf`. Результат — словарь с ключами `value`, `left`, `right`. Дополнительно — исследовать другие структуры для хранения/обхода дерева, в том числе из модуля `collections`.

## 2. Вариант
Использован вариант №1:
- `root = 1`
- `height = 5`
- `left_leaf = root * 2`
- `right_leaf = root + 3`

Эти значения заданы по умолчанию в виде `lambda`-функций в сигнатуре `gen_bin_tree`.

## 3. Реализация

### `tree.py`
```python
from typing import Callable


def gen_bin_tree(height: int, root: int,
                 left_leaf: Callable = lambda x: x * 2,
                 right_leaf: Callable = lambda x: x + 3) -> dict:
    """Рекурсивно строит бинарное дерево заданной высоты.

    Args:
        height: Высота дерева.
        root: Значение в корне.
        left_leaf: Функция для левого потомка.
        right_leaf: Функция для правого потомка.

    Returns:
        Словарь с ключами 'value', 'left', 'right'.
    """
    if height <= 0:
        return {'value': root, 'left': None, 'right': None}

    return {
        'value': root,
        'left': gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
        'right': gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf),
    }
```

### `tree_containers.py`
Дополнительный обход дерева через `deque` из `collections` (BFS — по уровням):

```python
from collections import deque


def bfs(tree):
    """Обходит дерево в ширину и возвращает список значений."""
    if tree is None:
        return []

    result = []
    queue = deque([tree])

    while queue:
        node = queue.popleft()
        if node is None:
            continue
        result.append(node['value'])
        queue.append(node['left'])
        queue.append(node['right'])

    return result
```

## 4. Алгоритм работы
- если `height <= 0` — возвращаем лист `{'value': root, 'left': None, 'right': None}`.
- шаг: вычисляем значения потомков через `left_leaf(root)` и `right_leaf(root)`, затем рекурсивно строим левое и правое поддеревья с `height - 1`.
- BFS: кладём корень в `deque`, берём узлы с начала, добавляем их детей в конец. Порядок обхода — по уровням.

## 5. Тестирование

### `test_tree.py` (7 тестов)
- `height = 0` → только корень
- отрицательная высота → только корень
- `height = 1` с дефолтными лямбдами
- `height = 2` — полная сверка дерева
- переопределение лямбд пользователем
- значение корня сохраняется
- листья без потомков

### `test_tree_containers.py` (3 теста)
- BFS-обход полного дерева
- дерево из одного узла
- пустое дерево (`None`)

### Запуск
```bash
python -m unittest test_tree.py test_tree_containers.py
```

Ожидаемый результат:
```text
..........
----------------------------------------------------------------------
Ran 10 tests in 0.000s

OK
```

## 6. Исследование других контейнеров
Помимо словаря и рекурсии, дерево можно обходить с помощью контейнеров из `collections`. В файле `tree_containers.py` реализован обход в ширину (BFS) через `deque`.

`deque` — двусторонняя очередь. Мы кладём узлы в неё с одного конца, а берём с другого. Это позволяет обходить дерево по уровням: сначала корень, потом его детей, потом внуков.

Результат для `gen_bin_tree(2, 1)`:
- рекурсия (pre-order): `1, 2, 4, 5, 4, 8, 7`
- BFS через `deque`: `1, 2, 4, 4, 5, 8, 7`

## 7. Вывод
Функция `gen_bin_tree` корректно и рекурсивно строит бинарное дерево, поддерживает переопределение лямбд и обрабатывает граничные случаи. Документация соответствует PEP-257, аннотации типов присутствуют. Дополнительно реализован обход через `deque` из `collections`. Все 10 тестов проходят.