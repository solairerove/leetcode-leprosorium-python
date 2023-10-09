import unittest

from binary_search.FindFirstAndLastPositionOfElementInSortedArray import search_range


class MyTestCase(unittest.TestCase):
    def test_search_range(self):
        self.assertEqual([3, 4], search_range(self, nums=[5, 7, 7, 8, 8, 10], target=8))

    def test_search_range_1(self):
        self.assertEqual([-1, -1], search_range(self, nums=[5, 7, 7, 8, 8, 10], target=6))

    def test_search_range_2(self):
        self.assertEqual([-1, -1], search_range(self, nums=[], target=0))


if __name__ == '__main__':
    unittest.main()
