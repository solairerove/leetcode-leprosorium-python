import unittest

from dynamic_programming.AllPossibleFullBinaryTrees import all_possible_fbt


class MyTestCase(unittest.TestCase):
    def test_all_possible_fbt(self):
        root = all_possible_fbt(self, 7)
        self.assertEqual(0, root[0].right.right.right.val)
        self.assertEqual(0, root[4].left.left.left.val)


if __name__ == '__main__':
    unittest.main()
