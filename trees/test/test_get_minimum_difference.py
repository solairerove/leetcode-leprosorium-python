import unittest

from trees.MinimumAbsoluteDifferenceInBST import get_minimum_difference, get_minimum_difference_rec
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_get_minimum_difference(self):
        root = TreeNode(4)
        left = TreeNode(2)
        right = TreeNode(6)
        l_left = TreeNode(1)
        l_right = TreeNode(3)

        left.left = l_left
        left.right = l_right

        root.left = left
        root.right = right
        self.assertEqual(1, get_minimum_difference(self, root))
        self.assertEqual(1, get_minimum_difference_rec(self, root))

    def test_get_minimum_difference_1(self):
        root = TreeNode(1)
        left = TreeNode(0)
        right = TreeNode(48)
        r_left = TreeNode(12)
        r_right = TreeNode(49)

        right.left = r_left
        right.right = r_right

        root.left = left
        root.right = right
        self.assertEqual(1, get_minimum_difference(self, root))
        self.assertEqual(1, get_minimum_difference_rec(self, root))


if __name__ == '__main__':
    unittest.main()
