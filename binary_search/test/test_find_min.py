import unittest

from binary_search.FindMinimumInRotatedSortedArray import find_min


class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(1, find_min(self, nums=[3, 4, 5, 1, 2]))

    def test_find_min_1(self):
        self.assertEqual(0, find_min(self, nums=[4, 5, 6, 7, 0, 1, 2]))

    def test_find_min_2(self):
        self.assertEqual(11, find_min(self, nums=[11, 13, 15, 17]))


if __name__ == '__main__':
    unittest.main()
