import unittest

from trees.MaximumDepthOfBinaryTree import max_depth_rec, max_depth_dfs
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_max_depth(self):
        root = TreeNode(3)
        left = TreeNode(9)
        right = TreeNode(20)
        r_right1 = TreeNode(7)
        r_left1 = TreeNode(15)

        right.right = r_right1
        right.left = r_left1

        root.left = left
        root.right = right

        self.assertEqual(3, max_depth_rec(self, root))
        self.assertEqual(3, max_depth_dfs(self, root))

    def test_max_depth_1(self):
        root = TreeNode(1)

        right = TreeNode(2)

        root.right = right

        self.assertEqual(2, max_depth_rec(self, root))
        self.assertEqual(2, max_depth_dfs(self, root))


if __name__ == '__main__':
    unittest.main()
