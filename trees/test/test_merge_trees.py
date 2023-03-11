import unittest

from trees.MergeTwoBinaryTrees import merge_trees_rec, merge_trees
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_merge_trees_rec(self):
        root1 = TreeNode(
            val=1,
            left=TreeNode(
                val=3,
                left=TreeNode(
                    val=5
                )
            ),
            right=TreeNode(
                val=2
            )
        )
        root2 = TreeNode(
            val=2,
            left=TreeNode(
                val=1,
                right=TreeNode(
                    val=4
                )
            ),
            right=TreeNode(
                val=3,
                right=TreeNode(
                    val=7
                )
            )
        )
        actual = merge_trees_rec(self, root1, root2)
        self.assertEqual(3, actual.val)
        self.assertEqual(4, actual.left.val)
        self.assertEqual(5, actual.left.left.val)
        self.assertEqual(4, actual.left.right.val)
        self.assertEqual(5, actual.right.val)
        self.assertEqual(7, actual.right.right.val)

    def test_merge_trees_stack(self):
        root1 = TreeNode(
            val=1,
            left=TreeNode(
                val=3,
                left=TreeNode(
                    val=5
                )
            ),
            right=TreeNode(
                val=2
            )
        )
        root2 = TreeNode(
            val=2,
            left=TreeNode(
                val=1,
                right=TreeNode(
                    val=4
                )
            ),
            right=TreeNode(
                val=3,
                right=TreeNode(
                    val=7
                )
            )
        )

        actual = merge_trees(self, root1, root2)
        self.assertEqual(3, actual.val)
        self.assertEqual(4, actual.left.val)
        self.assertEqual(5, actual.left.left.val)
        self.assertEqual(4, actual.left.right.val)
        self.assertEqual(5, actual.right.val)
        self.assertEqual(7, actual.right.right.val)


if __name__ == '__main__':
    unittest.main()
