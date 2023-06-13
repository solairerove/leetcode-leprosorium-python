import unittest

from arrays.EqualRowAndColumnPairs import equal_pairs


class MyTestCase(unittest.TestCase):
    def test_equal_pairs(self):
        self.assertEqual(1, equal_pairs(self, [[3, 2, 1], [1, 7, 6], [2, 7, 7]]))

    def test_equal_pairs_1(self):
        self.assertEqual(3, equal_pairs(self, [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))


if __name__ == '__main__':
    unittest.main()
