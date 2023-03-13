import unittest

from trees.SymmetricTree import is_symmetric_rec, is_symmetric
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_is_symmetric(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=2,
                left=TreeNode(3),
                right=TreeNode(4)
            ),
            right=TreeNode(
                val=2,
                left=TreeNode(4),
                right=TreeNode(3)
            )
        )

        self.assertEqual(True, is_symmetric(self, root))
        self.assertEqual(True, is_symmetric_rec(self, root))

    def test_is_symmetric_1(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=2,
                right=TreeNode(3)
            ),
            right=TreeNode(
                val=2,
                right=TreeNode(3)
            )
        )

        self.assertEqual(False, is_symmetric(self, root))
        self.assertEqual(False, is_symmetric_rec(self, root))


if __name__ == '__main__':
    unittest.main()
