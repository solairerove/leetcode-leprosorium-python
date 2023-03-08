import unittest

from trees.SameTree import is_same_tree, is_same_tree_dfs, is_same_tree_bfs
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_is_same_tree(self):
        root = TreeNode(1)
        left, right = TreeNode(2), TreeNode(3)
        root.left, root.right = left, right

        root1 = TreeNode(1)
        left1, right1 = TreeNode(2), TreeNode(3)
        root1.left, root1.right = left1, right1
        self.assertEqual(True, is_same_tree(self, root, root1))
        self.assertEqual(True, is_same_tree_dfs(self, root, root1))
        self.assertEqual(True, is_same_tree_bfs(self, root, root1))

    def test_is_same_tree_1(self):
        root = TreeNode(1)
        left = TreeNode(2)
        root.left = left

        root1 = TreeNode(1)
        right1 = TreeNode(2)
        root1.right1 = right1
        self.assertEqual(False, is_same_tree(self, root, root1))
        self.assertEqual(False, is_same_tree_dfs(self, root, root1))
        self.assertEqual(False, is_same_tree_bfs(self, root, root1))

    def test_is_same_tree_2(self):
        root = TreeNode(1)
        left, right = TreeNode(2), TreeNode(1)
        root.left, root.right = left, right

        root1 = TreeNode(1)
        left1, right1 = TreeNode(1), TreeNode(3)
        root1.left1, root1.right1 = left1, right1
        self.assertEqual(False, is_same_tree(self, root, root1))
        self.assertEqual(False, is_same_tree_dfs(self, root, root1))
        self.assertEqual(False, is_same_tree_bfs(self, root, root1))


if __name__ == '__main__':
    unittest.main()
