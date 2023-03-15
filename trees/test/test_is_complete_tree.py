import unittest

from trees.CheckCompletenessOfABinaryTree import is_complete_tree
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_is_complete_tree(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=2,
                left=TreeNode(4),
                right=TreeNode(5)
            ),
            right=TreeNode(
                val=3,
                left=TreeNode(6)
            )
        )

        self.assertEqual(True, is_complete_tree(self, root))

    def test_is_complete_tree_1(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=2,
                left=TreeNode(4),
                right=TreeNode(5)
            ),
            right=TreeNode(
                val=3,
                right=TreeNode(7)
            )
        )

        self.assertEqual(False, is_complete_tree(self, root))


if __name__ == '__main__':
    unittest.main()
