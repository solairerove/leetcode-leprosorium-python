import unittest

from dynamic_programming.HouseRobberIII import rob, TreeNode


class MyTestCase(unittest.TestCase):
    def test_rob(self):
        root = TreeNode(3)
        left = TreeNode(2)
        right = TreeNode(3)
        left1 = TreeNode(3)
        right1 = TreeNode(1)

        root.left, root.right = left, right
        left.right = left1
        right.right = right1

        self.assertEqual(7, rob(self, root))

    def test_rob_1(self):
        root = TreeNode(3)
        left = TreeNode(4)
        right = TreeNode(5)
        l_left1 = TreeNode(1)
        l_right1 = TreeNode(3)
        r_right1 = TreeNode(1)

        root.left, root.right = left, right
        left.left, left.right = l_left1, l_right1
        right.right = r_right1

        self.assertEqual(9, rob(self, root))


if __name__ == '__main__':
    unittest.main()
