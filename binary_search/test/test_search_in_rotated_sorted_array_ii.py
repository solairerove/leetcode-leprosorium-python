import unittest

from binary_search.SearchInRotatedSortedArrayII import search


class MyTestCase(unittest.TestCase):
    def test_search_in_rotated_sorted_array_ii(self):
        self.assertEqual(True, search(self, nums=[2, 5, 6, 0, 0, 1, 2], target=0))

    def test_search_in_rotated_sorted_array_ii_1(self):
        self.assertEqual(False, search(self, nums=[2, 5, 6, 0, 0, 1, 2], target=3))


if __name__ == '__main__':
    unittest.main()
