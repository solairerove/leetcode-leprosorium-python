import unittest

from trees.PathSum import has_path_sum_recursive, has_path_sum_dfs
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_has_path_sum(self):
        root = TreeNode(5)
        left, right = TreeNode(4), TreeNode(8)
        l_left, r_left, r_right = TreeNode(11), TreeNode(13), TreeNode(4)
        l_l_left, l_l_right, r_r_right = TreeNode(7), TreeNode(2), TreeNode(1)

        root.left, root.right = left, right
        left.left, right.left, right.right = l_left, r_left, r_right
        l_left.left, l_left.right, r_right.right = l_l_left, l_l_right, r_r_right

        self.assertEqual(True, has_path_sum_recursive(self, root, 22))
        self.assertEqual(True, has_path_sum_dfs(self, root, 22))

    def test_has_path_sum_1(self):
        root = TreeNode(1)
        left, right = TreeNode(2), TreeNode(3)

        root.left, root.right = left, right

        self.assertEqual(False, has_path_sum_recursive(self, root, 5))
        self.assertEqual(False, has_path_sum_dfs(self, root, 5))


if __name__ == '__main__':
    unittest.main()
