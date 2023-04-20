import unittest

from trees.MaximumWidthOfBinaryTree import width_of_binary_tree_bfs
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_width_of_binary_tree(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=3,
                left=TreeNode(5),
                right=TreeNode(3)
            ),
            right=TreeNode(val=2, right=TreeNode(9))
        )

        self.assertEqual(4, width_of_binary_tree_bfs(self, root))

    def test_width_of_binary_tree_1(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=3,
                left=TreeNode(val=5, left=TreeNode(6)),
            ),
            right=TreeNode(val=2, right=TreeNode(val=9, left=TreeNode(7)))
        )

        self.assertEqual(7, width_of_binary_tree_bfs(self, root))

    def test_width_of_binary_tree_2(self):
        root = TreeNode(
            val=1,
            left=TreeNode(val=3, left=TreeNode(5)),
            right=TreeNode(2)
        )

        self.assertEqual(2, width_of_binary_tree_bfs(self, root))


if __name__ == '__main__':
    unittest.main()
