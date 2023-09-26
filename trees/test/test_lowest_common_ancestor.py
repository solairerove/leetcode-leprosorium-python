import unittest

from trees.LowestCommonAncestorOfABinarySearchTree import lowest_common_ancestor
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_lowest_common_ancestor(self):
        p = TreeNode(
            val=2,
            left=TreeNode(0),
            right=TreeNode(
                val=4,
                left=TreeNode(3),
                right=TreeNode(5)
            )
        )

        q = TreeNode(
            val=8,
            left=TreeNode(7),
            right=TreeNode(9)
        )

        root = TreeNode(
            val=6,
            left=p,
            right=q
        )

        self.assertEqual(6, lowest_common_ancestor(self, root, p, q).val)

    def test_lowest_common_ancestor_1(self):
        q = TreeNode(
            val=4,
            left=TreeNode(3),
            right=TreeNode(5)
        )

        p = TreeNode(
            val=2,
            left=TreeNode(0),
            right=q
        )

        root = TreeNode(
            val=6,
            left=p,
            right=TreeNode(
                val=8,
                left=TreeNode(7),
                right=TreeNode(9)
            )
        )

        self.assertEqual(2, lowest_common_ancestor(self, root, p, q).val)


if __name__ == '__main__':
    unittest.main()
