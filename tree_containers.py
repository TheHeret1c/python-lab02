"""Другой способ обойти дерево — через deque из collections."""

from collections import deque


def bfs(tree):
    """Обходит дерево в ширину и возвращает список значений.

    Обычная рекурсия идёт «вглубь», а здесь идёт "по уровням": сначала корень, потом его детей, потом внуков и так далее.
    deque — это очередь: кладём в конец, берём из начала.
    """
    if tree is None:
        return []

    result = []
    queue = deque([tree])

    while queue:
        node = queue.popleft()      # берём первый узел из очереди
        if node is None:
            continue
        result.append(node["value"])
        queue.append(node["left"])  # добавляем детей в конец
        queue.append(node["right"])

    return result


if __name__ == "__main__":
    from tree import gen_bin_tree

    tree = gen_bin_tree(2, 1)
    print("BFS:", bfs(tree))