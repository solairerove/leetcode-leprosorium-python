import unittest

from trees.SubtreeOfAnotherTree import is_subtree
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_is_subtree(self):
        root = TreeNode(
            val=3,
            left=TreeNode(
                val=4,
                left=TreeNode(1),
                right=TreeNode(2)
            ),
            right=TreeNode(val=5)
        )

        sub_root = TreeNode(
            val=4,
            left=TreeNode(1),
            right=TreeNode(2)
        )

        self.assertEqual(True, is_subtree(self, root, sub_root))

    def test_is_subtree_1(self):
        root = TreeNode(
            val=3,
            left=TreeNode(
                val=4,
                left=TreeNode(1),
                right=TreeNode(2, left=TreeNode(0))
            ),
            right=TreeNode(val=5)
        )

        sub_root = TreeNode(
            val=4,
            left=TreeNode(1),
            right=TreeNode(2)
        )

        self.assertEqual(False, is_subtree(self, root, sub_root))


if __name__ == '__main__':
    unittest.main()
