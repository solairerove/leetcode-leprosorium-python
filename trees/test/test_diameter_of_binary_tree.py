import unittest

from trees.DiameterOfBinaryTree import diameter_of_binary_tree_recursive_dfs, diameter_of_binary_tree_dfs
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_diameter_of_binary_tree(self):
        root = TreeNode(1)
        left, right = TreeNode(2), TreeNode(3)
        l_left, l_right = TreeNode(4), TreeNode(5)
        left.left, left.right = l_left, l_right
        root.left, root.right = left, right

        self.assertEqual(3, diameter_of_binary_tree_recursive_dfs(self, root))
        self.assertEqual(3, diameter_of_binary_tree_dfs(self, root))

    def test_diameter_of_binary_tree_1(self):
        root = TreeNode(1)
        left = TreeNode(2)
        root.left = left

        self.assertEqual(1, diameter_of_binary_tree_recursive_dfs(self, root))
        self.assertEqual(1, diameter_of_binary_tree_dfs(self, root))


if __name__ == '__main__':
    unittest.main()
