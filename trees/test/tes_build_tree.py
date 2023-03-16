import unittest

from trees.ConstructBinaryTreeFromInorderAndPostorderTraversal import build_tree


class MyTestCase(unittest.TestCase):
    def test_build_tree(self):
        root = build_tree(self, [9, 3, 15, 20, 7], [9, 15, 7, 20, 3])

        self.assertEqual(3, root.val)
        self.assertEqual(9, root.left.val)
        self.assertEqual(20, root.right.val)
        self.assertEqual(15, root.right.left.val)
        self.assertEqual(7, root.right.right.val)


if __name__ == '__main__':
    unittest.main()
