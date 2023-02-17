import unittest

from trees.MinimumDistanceBetweenBSTNodes import min_diff_in_bst
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_min_diff_in_bst(self):
        root = TreeNode(4)
        left = TreeNode(2)
        l_left, l_right = TreeNode(1), TreeNode(3)
        left.left = l_left
        left.right = l_right
        right = TreeNode(6)
        root.left = left
        root.right = right

        self.assertEqual(1, min_diff_in_bst(self, root))

    def test_min_diff_in_bst_1(self):
        root = TreeNode(1)
        left = TreeNode(0)
        right = TreeNode(48)
        r_left = TreeNode(12)
        r_right = TreeNode(49)
        right.left = r_left
        right.right = r_right
        root.left = left
        root.right = right

        self.assertEqual(1, min_diff_in_bst(self, root))


if __name__ == '__main__':
    unittest.main()
