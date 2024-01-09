import unittest

from trees.LeafSimilarTrees import leaf_similar
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_leaf_similar(self):
        root1 = TreeNode(
            val=3,
            left=TreeNode(
                val=5,
                left=TreeNode(val=6),
                right=TreeNode(
                    val=2,
                    left=TreeNode(val=7),
                    right=TreeNode(val=4)
                )
            ),
            right=TreeNode(
                val=1,
                left=TreeNode(val=9),
                right=TreeNode(val=8)
            )
        )

        root2 = TreeNode(
            val=3,
            left=TreeNode(
                val=5,
                left=TreeNode(val=6),
                right=TreeNode(val=7)
            ),
            right=TreeNode(
                val=1,
                left=TreeNode(val=4),
                right=TreeNode(
                    val=2,
                    left=TreeNode(val=9),
                    right=TreeNode(val=8)
                )
            )
        )

        self.assertEqual(True, leaf_similar(self, root1, root2))

    def test_leaf_similar_1(self):
        root1 = TreeNode(
            val=1,
            left=TreeNode(val=2),
            right=TreeNode(val=3)
        )

        root2 = TreeNode(
            val=1,
            left=TreeNode(val=3),
            right=TreeNode(val=2)
        )

        self.assertEqual(False, leaf_similar(self, root1, root2))


if __name__ == '__main__':
    unittest.main()
