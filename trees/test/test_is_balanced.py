import unittest

from trees.BalancedBinaryTree import is_balanced
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_is_balanced(self):
        root = TreeNode(
            val=3,
            left=TreeNode(9),
            right=TreeNode(
                val=20,
                left=TreeNode(15),
                right=TreeNode(7)
            )
        )
        self.assertEqual(True, is_balanced(self, root))

    def test_is_balanced_1(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=2,
                left=TreeNode(
                    val=3,
                    left=TreeNode(4),
                    right=TreeNode(4)
                ),
                right=TreeNode(3)
            ),
            right=TreeNode(2)
        )
        self.assertEqual(False, is_balanced(self, root))


if __name__ == '__main__':
    unittest.main()
