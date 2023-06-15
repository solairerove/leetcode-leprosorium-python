import unittest

from trees.MaximumLevelSumOfABinaryTree import max_level_sum
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_max_level_sum(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=7,
                left=TreeNode(7),
                right=TreeNode(-8)
            ),
            right=TreeNode(val=0)
        )

        self.assertEqual(2, max_level_sum(self, root))


if __name__ == '__main__':
    unittest.main()
