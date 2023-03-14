import unittest

from trees.SumRootToLeafNumbers import sum_numbers, sum_numbers_rec
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_sum_numbers(self):
        root = TreeNode(
            val=1,
            left=TreeNode(2),
            right=TreeNode(3)
        )

        self.assertEqual(25, sum_numbers(self, root))
        self.assertEqual(25, sum_numbers_rec(self, root))

    def test_sum_numbers_1(self):
        root = TreeNode(
            val=4,
            left=TreeNode(
                val=9,
                left=TreeNode(5),
                right=TreeNode(1)
            ),
            right=TreeNode(0)
        )

        self.assertEqual(1026, sum_numbers(self, root))
        self.assertEqual(1026, sum_numbers_rec(self, root))


if __name__ == '__main__':
    unittest.main()
