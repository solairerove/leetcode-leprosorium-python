import unittest

from trees.BinaryTreeInorderTraversal import inorder_traversal, inorder_traversal_stack
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_inorder_traversal(self):
        root = TreeNode(1)
        right = TreeNode(2)
        r_left = TreeNode(3)
        right.left = r_left
        root.right = right

        self.assertEqual([1, 3, 2], inorder_traversal(self, root))
        self.assertEqual([1, 3, 2], inorder_traversal_stack(self, root))

    def test_inorder_traversal_1(self):
        self.assertEqual([], inorder_traversal(self, None))
        self.assertEqual([], inorder_traversal_stack(self, None))

    def test_inorder_traversal_2(self):
        self.assertEqual([1], inorder_traversal(self, TreeNode(1)))
        self.assertEqual([1], inorder_traversal_stack(self, TreeNode(1)))


if __name__ == '__main__':
    unittest.main()
