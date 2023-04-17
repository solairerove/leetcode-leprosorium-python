import unittest

from arrays.MergeIntervals import merge


class MyTestCase(unittest.TestCase):
    def test_merge(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], merge(self, [[1, 3], [2, 6], [8, 10], [15, 18]]))

    def test_merge_1(self):
        self.assertEqual([[1, 5]], merge(self, [[1, 4], [4, 5]]))


if __name__ == '__main__':
    unittest.main()
