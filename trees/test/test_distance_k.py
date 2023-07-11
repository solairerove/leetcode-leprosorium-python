import unittest

from trees.AllNodesDistanceKInBinaryTree import distance_k
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_distance_k(self):
        target = TreeNode(
            val=5,
            left=TreeNode(6),
            right=TreeNode(
                val=2,
                left=TreeNode(7),
                right=TreeNode(4)
            )
        )
        root = TreeNode(
            val=3,
            left=target,
            right=TreeNode(
                val=1,
                left=TreeNode(0),
                right=TreeNode(8)
            )
        )

        self.assertEqual([1, 4, 7], distance_k(self, root=root, target=target, k=2))


if __name__ == '__main__':
    unittest.main()
