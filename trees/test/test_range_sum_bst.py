import unittest

from trees.RangeSumOfBST import range_sum_bst, range_sum_bst_iterative
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_range_sum_bst(self):
        root = TreeNode(
            val=10,
            left=TreeNode(
                val=5,
                left=TreeNode(val=3),
                right=TreeNode(val=7)
            ),
            right=TreeNode(
                val=15,
                right=TreeNode(18)
            )
        )

        self.assertEqual(32, range_sum_bst(self, root, 7, 15))
        self.assertEqual(32, range_sum_bst_iterative(self, root, 7, 15))

    def test_range_sum_bst_1(self):
        root = TreeNode(
            val=10,
            left=TreeNode(
                val=5,
                left=TreeNode(val=3, left=TreeNode(1)),
                right=TreeNode(val=7, left=TreeNode(6))
            ),
            right=TreeNode(
                val=15,
                left=TreeNode(13),
                right=TreeNode(18)
            )
        )

        self.assertEqual(23, range_sum_bst(self, root, 6, 10))
        self.assertEqual(23, range_sum_bst_iterative(self, root, 6, 10))


if __name__ == '__main__':
    unittest.main()
