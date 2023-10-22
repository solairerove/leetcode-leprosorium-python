import unittest

from binary_search.SearchInRotatedSortedArray import search


class MyTestCase(unittest.TestCase):
    def test_search_in_rotated_sorted_array(self):
        self.assertEqual(4, search(self, nums=[4, 5, 6, 7, 0, 1, 2], target=0))

    def test_search_in_rotated_sorted_array_1(self):
        self.assertEqual(-1, search(self, nums=[4, 5, 6, 7, 0, 1, 2], target=3))

    def test_search_in_rotated_sorted_array_2(self):
        self.assertEqual(-1, search(self, nums=[1], target=0))


if __name__ == '__main__':
    unittest.main()
