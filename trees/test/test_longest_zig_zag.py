import unittest

from trees.LongestZigZagPathInABinaryTree import longest_zig_zag
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_longest_zig_zag(self):
        root = TreeNode(
            val=1,
            right=TreeNode(
                val=1,
                left=TreeNode(1),
                right=TreeNode(
                    val=1,
                    left=TreeNode(
                        val=1,
                        right=TreeNode(
                            val=1,
                            right=TreeNode(
                                val=1,
                                right=TreeNode(
                                    val=1,
                                    right=TreeNode(1)
                                )
                            )
                        )
                    ),
                    right=TreeNode(1)
                )
            )
        )
        self.assertEqual(3, longest_zig_zag(self, root))

    def test_longest_zig_zag_1(self):
        root = TreeNode(
            val=1,
            left=TreeNode(
                val=1,
                right=TreeNode(
                    val=1,
                    left=TreeNode(
                        val=1,
                        right=TreeNode(1)
                    ),
                    right=TreeNode(1)
                )
            ),
            right=TreeNode(1)
        )
        self.assertEqual(4, longest_zig_zag(self, root))


if __name__ == '__main__':
    unittest.main()
