"""Проверяем обход дерева через deque."""

import unittest

from tree import gen_bin_tree
from tree_containers import bfs


class TestBfs(unittest.TestCase):

    def test_bfs_order(self):
        """height=2, root=1 → обход по уровням: 1; 2,4; 4,5,8,7."""
        tree = gen_bin_tree(2, 1)
        self.assertEqual(bfs(tree), [1, 2, 4, 4, 5, 8, 7])

    def test_bfs_single_node(self):
        """height=0 → только корень."""
        self.assertEqual(bfs(gen_bin_tree(0, 5)), [5])

    def test_bfs_none(self):
        """Пустое дерево → пустой список."""
        self.assertEqual(bfs(None), [])


if __name__ == "__main__":
    unittest.main()