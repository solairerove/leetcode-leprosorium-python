import unittest

from trees.MaximumDepthOfBinaryTree import max_depth_recursive_dfs, max_depth_iterative_dfs
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_max_depth(self):
        root = TreeNode(
            val=3,
            left=TreeNode(9),
            right=TreeNode(
                val=20,
                left=TreeNode(15),
                right=TreeNode(7)
            )
        )

        self.assertEqual(3, max_depth_recursive_dfs(self, root))
        self.assertEqual(3, max_depth_iterative_dfs(self, root))

    def test_max_depth_1(self):
        root = TreeNode(1)

        right = TreeNode(2)

        root.right = right

        self.assertEqual(2, max_depth_recursive_dfs(self, root))
        self.assertEqual(2, max_depth_iterative_dfs(self, root))


if __name__ == '__main__':
    unittest.main()
