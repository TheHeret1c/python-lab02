import unittest

from tree import gen_bin_tree


class TestGenBinTree(unittest.TestCase):
    """Тесты для функции gen_bin_tree."""

    def test_height_zero_returns_leaf(self):
        """height=0 — только корень без потомков."""
        result = gen_bin_tree(0, 5)
        expected = {'value': 5, 'left': None, 'right': None}
        self.assertEqual(result, expected)

    def test_negative_height_returns_leaf(self):
        """height<0 обрабатывается так же, как height=0."""
        result = gen_bin_tree(-3, 5)
        expected = {'value': 5, 'left': None, 'right': None}
        self.assertEqual(result, expected)

    def test_height_one_default_lambdas(self):
        """height=1 — корень и два потомка по дефолтным лямбдам."""
        result = gen_bin_tree(1, 1)
        self.assertEqual(result['value'], 1)
        self.assertEqual(result['left']['value'], 2)   # 1 * 2
        self.assertEqual(result['right']['value'], 4)  # 1 + 3
        self.assertIsNone(result['left']['left'])
        self.assertIsNone(result['left']['right'])
        self.assertIsNone(result['right']['left'])
        self.assertIsNone(result['right']['right'])

    def test_height_two_full_structure(self):
        """height=2 — сверяем всё дерево целиком."""
        expected = {
            'value': 1,
            'left': {
                'value': 2,
                'left': {'value': 4, 'left': None, 'right': None},
                'right': {'value': 5, 'left': None, 'right': None},
            },
            'right': {
                'value': 4,
                'left': {'value': 8, 'left': None, 'right': None},
                'right': {'value': 7, 'left': None, 'right': None},
            },
        }
        self.assertEqual(gen_bin_tree(2, 1), expected)

    def test_custom_lambdas_override_defaults(self):
        """Переданные лямбды используются вместо дефолтных."""
        result = gen_bin_tree(
            1, 10,
            left_leaf=lambda x: x + 1,
            right_leaf=lambda x: x - 1,
        )
        self.assertEqual(result['left']['value'], 11)
        self.assertEqual(result['right']['value'], 9)

    def test_root_preserved_at_top(self):
        """Значение корня не меняется, что бы ни передали."""
        result = gen_bin_tree(3, 42)
        self.assertEqual(result['value'], 42)

    def test_leaf_has_none_children(self):
        """Лист на максимальной глубине имеет left=None и right=None."""
        tree = gen_bin_tree(2, 1)
        leaf = tree['left']['left']
        self.assertIsNone(leaf['left'])
        self.assertIsNone(leaf['right'])


if __name__ == '__main__':
    unittest.main()