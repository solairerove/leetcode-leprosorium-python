import unittest

from trees.PathSumII import path_sum_rec, path_sum_dfs
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_path_sum(self):
        root = TreeNode(
            val=5,
            left=TreeNode(
                val=4,
                left=TreeNode(
                    val=11,
                    left=TreeNode(7),
                    right=TreeNode(2)
                )
            ),
            right=TreeNode(
                val=8,
                left=TreeNode(13),
                right=TreeNode(
                    val=4,
                    left=TreeNode(5),
                    right=TreeNode(1)
                )
            )
        )
        self.assertEqual([[5, 4, 11, 2], [5, 8, 4, 5]], path_sum_rec(self, root, 22))
        self.assertEqual([[5, 8, 4, 5], [5, 4, 11, 2]], path_sum_dfs(self, root, 22))

    def test_path_sum_1(self):
        root = TreeNode(
            val=1,
            left=TreeNode(2),
            right=TreeNode(3)
        )

        self.assertEqual([], path_sum_rec(self, root, 0))
        self.assertEqual([], path_sum_dfs(self, root, 0))


if __name__ == '__main__':
    unittest.main()
