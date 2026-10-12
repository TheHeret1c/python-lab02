from typing import Callable

def gen_bin_tree(height: int, root: int, 
                 left_leaf: Callable = lambda x: x * 2, 
                 right_leaf: Callable = lambda x: x + 3) -> dict:
    """Рекурсивно строит бинарное дерево заданной высоты.

    Значение потомка вычисляется из значения родителя с помощью лямбда-функций left_leaf и right_leaf. 
    Если функции не переданы, используются значения по умолчанию.

    Параметры:
        height: Высота дерева
        root: Значение в корне дерева
        left_leaf: вычисление значения левого потомка из значения родителя
        right_leaf: вычисление значения правого потомка из значения родителя

    Возврат:
        Словарь с ключами 'value', 'left', 'right'. 'left' и 'right' те же словари, либо None, если дерево закончилось
    """
    
    if height <= 0:
        return {'value': root, 'left': None, 'right': None}

    left_val = left_leaf(root)
    right_val = right_leaf(root)

    return {
        'value': root,
        'left': gen_bin_tree(height - 1, left_val, left_leaf, right_leaf),
        'right': gen_bin_tree(height - 1, right_val, left_leaf, right_leaf),
    }

def print_horizontal(node, prefix='', is_last=True, max_depth=10, depth=0):
    """
    Выводит дерево в консоль в горизонтальном виде
    Позаимствована
    """
    if node is None or depth > max_depth:
        return
    connector = '└── ' if is_last else '├── '
    print(prefix + connector + str(node['value']))
    children = [c for c in (node['left'], node['right']) if c is not None]
    for i, child in enumerate(children):
        last = (i == len(children) - 1)
        extension = '    ' if is_last else '│   '
        print_horizontal(child, prefix + extension, last, max_depth, depth + 1)

if __name__ == "__main__":
    print_horizontal(gen_bin_tree(5, 1), max_depth=5)
