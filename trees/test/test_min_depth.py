import unittest

from trees.MinimumDepthOfBinaryTree import min_depth_recursive_dfs, \
    min_depth_iterative_dfs, min_depth_iterative_bfs
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_min_depth(self):
        root = TreeNode(
            val=3,
            left=TreeNode(9),
            right=TreeNode(
                val=20,
                left=TreeNode(15),
                right=TreeNode(7)
            )
        )

        self.assertEqual(2, min_depth_recursive_dfs(self, root))
        self.assertEqual(2, min_depth_iterative_dfs(self, root))
        self.assertEqual(2, min_depth_iterative_bfs(self, root))


if __name__ == '__main__':
    unittest.main()
