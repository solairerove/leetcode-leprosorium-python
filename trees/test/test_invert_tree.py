import unittest

from trees.BinaryTreeInorderTraversal import inorder_traversal
from trees.InvertBinaryTree import invert_tree, invert_tree_stack
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_invert_tree(self):
        root = TreeNode(4)
        r_left, r_right = TreeNode(2), TreeNode(7)
        r_l_left, r_l_right = TreeNode(1), TreeNode(3)
        r_r_left, r_r_right = TreeNode(6), TreeNode(9)
        r_left.left, r_left.right = r_l_left, r_l_right
        r_right.left, r_right.right = r_r_left, r_r_right
        root.left, root.right = r_left, r_right

        res = invert_tree(self, root)
        actual = inorder_traversal(self, res)

        self.assertEqual([9, 7, 6, 4, 3, 2, 1], actual)

    def test_invert_tree_1(self):
        root = TreeNode(2)
        r_left, r_right = TreeNode(1), TreeNode(3)
        root.left, root.right = r_left, r_right

        res = invert_tree(self, root)
        actual = inorder_traversal(self, res)

        self.assertEqual([3, 2, 1], actual)

    def test_invert_tree_2(self):
        actual = inorder_traversal(self, None)

        self.assertEqual([], actual)

    def test_invert_tree_4(self):
        root = TreeNode(4)
        r_left, r_right = TreeNode(2), TreeNode(7)
        r_l_left, r_l_right = TreeNode(1), TreeNode(3)
        r_r_left, r_r_right = TreeNode(6), TreeNode(9)
        r_left.left, r_left.right = r_l_left, r_l_right
        r_right.left, r_right.right = r_r_left, r_r_right
        root.left, root.right = r_left, r_right

        res = invert_tree_stack(self, root)
        actual = inorder_traversal(self, res)

        self.assertEqual([9, 7, 6, 4, 3, 2, 1], actual)

    def test_invert_tree_5(self):
        root = TreeNode(2)
        r_left, r_right = TreeNode(1), TreeNode(3)
        root.left, root.right = r_left, r_right

        res = invert_tree_stack(self, root)
        actual = inorder_traversal(self, res)

        self.assertEqual([3, 2, 1], actual)


if __name__ == '__main__':
    unittest.main()
