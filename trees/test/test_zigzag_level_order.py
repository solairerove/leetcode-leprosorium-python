import unittest

from dynamic_programming.HouseRobberIII import TreeNode
from trees.BinaryTreeZigzagLevelOrderTraversal import zigzag_level_order


class MyTestCase(unittest.TestCase):
    def test_zigzag_level_order(self):
        root = TreeNode(3)
        left = TreeNode(9)
        right = TreeNode(20)
        r_left = TreeNode(15)
        r_right = TreeNode(7)
        right.left, right.right = r_left, r_right
        root.left, root.right = left, right

        self.assertEqual([[3], [20, 9], [15, 7]], zigzag_level_order(self, root))


if __name__ == '__main__':
    unittest.main()
