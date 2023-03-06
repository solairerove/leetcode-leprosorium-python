import unittest

from trees.AverageOfLevelsInBinaryTree import average_of_levels
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_average_of_levels(self):
        root = TreeNode(3)
        left, right = TreeNode(9), TreeNode(20)

        r_left, r_right = TreeNode(15), TreeNode(7)
        right.left, right.right = r_left, r_right

        root.left, root.right = left, right

        self.assertEqual([3.00000, 14.50000, 11.00000], average_of_levels(self, root))

    def test_average_of_levels_1(self):
        root = TreeNode(3)
        left, right = TreeNode(9), TreeNode(20)

        l_left, l_right = TreeNode(15), TreeNode(7)
        left.left, right.right = l_left, l_right

        root.left, root.right = left, right

        self.assertEqual([3.00000, 14.50000, 11.00000], average_of_levels(self, root))


if __name__ == '__main__':
    unittest.main()
