import unittest

from trees.LowestCommonAncestorOfABinaryTree import lowest_common_ancestor
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_lowest_common_ancestor(self):
        p = TreeNode(
            val=5,
            left=TreeNode(6),
            right=TreeNode(
                val=2,
                left=TreeNode(7),
                right=TreeNode(4)
            )
        )

        q = TreeNode(
            val=1,
            left=TreeNode(0),
            right=TreeNode(8)
        )

        root = TreeNode(
            val=3,
            left=p,
            right=q
        )

        self.assertEqual(3, lowest_common_ancestor(self, root, p, q).val)

    def test_lowest_common_ancestor_1(self):
        q = TreeNode(4)

        p = TreeNode(
            val=5,
            left=TreeNode(6),
            right=TreeNode(
                val=2,
                left=TreeNode(7),
                right=q
            )
        )

        root = TreeNode(
            val=3,
            left=p,
            right=TreeNode(
                val=1,
                left=TreeNode(0),
                right=TreeNode(8)
            )
        )

        self.assertEqual(5, lowest_common_ancestor(self, root, p, q).val)


if __name__ == '__main__':
    unittest.main()
