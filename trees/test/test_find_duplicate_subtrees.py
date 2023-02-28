import unittest

from trees.FindDuplicateSubtrees import find_duplicate_subtrees
from trees.TreeNode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_find_duplicate_subtrees(self):
        root = TreeNode(1)
        left, right = TreeNode(2), TreeNode(3)

        l_left = TreeNode(4)
        left.left = l_left

        r_left, r_right = TreeNode(2), TreeNode(4)
        r_l_left = TreeNode(4)
        r_left.left = r_l_left
        right.left, right.right = r_left, r_right

        root.left, root.right = left, right

        duplicates = find_duplicate_subtrees(self, root)
        self.assertEqual(4, duplicates[0].val)
        self.assertEqual(2, duplicates[1].val)
        self.assertEqual(4, duplicates[1].left.val)

    def test_find_duplicate_subtrees_1(self):
        root = TreeNode(2)
        left, right = TreeNode(1), TreeNode(1)

        root.left, root.right = left, right

        duplicates = find_duplicate_subtrees(self, root)
        self.assertEqual(1, duplicates[0].val)

    def test_find_duplicate_subtrees_2(self):
        root = TreeNode(2)
        left, right = TreeNode(2), TreeNode(2)

        l_left = TreeNode(3)
        left.left = l_left

        r_left = TreeNode(3)
        right.left = r_left

        root.left, root.right = left, right

        duplicates = find_duplicate_subtrees(self, root)
        self.assertEqual(3, duplicates[0].val)
        self.assertEqual(2, duplicates[1].val)
        self.assertEqual(3, duplicates[1].left.val)


if __name__ == '__main__':
    unittest.main()
