import unittest

from trees.MinimumDepthOfBinaryTree import min_depth_recursive, min_depth_dfs
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_min_depth(self):
        root = TreeNode(3)
        left, right = TreeNode(9), TreeNode(20)
        r_left, r_right = TreeNode(15), TreeNode(7)
        right.left, right.right = r_left, r_right
        root.left, root.right = left, right

        self.assertEqual(2, min_depth_recursive(self, root))
        self.assertEqual(2, min_depth_dfs(self, root))


if __name__ == '__main__':
    unittest.main()
