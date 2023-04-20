import unittest

from dynamic_programming.UniqueBinarySearchTrees import num_trees_top_down, num_trees_bottom_up, \
    num_trees_catalan_numbers


class MyTestCase(unittest.TestCase):
    def test_num_trees(self):
        self.assertEqual(5, num_trees_top_down(self, 3))
        self.assertEqual(5, num_trees_bottom_up(self, 3))
        self.assertEqual(5, num_trees_catalan_numbers(self, 3))

    def test_num_trees_1(self):
        self.assertEqual(1, num_trees_top_down(self, 1))
        self.assertEqual(1, num_trees_bottom_up(self, 1))
        self.assertEqual(1, num_trees_catalan_numbers(self, 1))


if __name__ == '__main__':
    unittest.main()
