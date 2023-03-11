import unittest

from linked_list.test.utils import transform_array_to_list_node
from trees.ConvertSortedListToBinarySearchTree import sorted_list_to_bst


class MyTestCase(unittest.TestCase):
    def test_sorted_list_to_bst(self):
        linked_list = transform_array_to_list_node(self, [-10, -3, 0, 5, 9])
        root = sorted_list_to_bst(self, linked_list)
        self.assertEqual(0, root.val)
        self.assertEqual(-3, root.left.val)
        self.assertEqual(9, root.right.val)
        self.assertEqual(-10, root.left.left.val)
        self.assertEqual(5, root.right.left.val)


if __name__ == '__main__':
    unittest.main()
