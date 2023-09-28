import unittest

from arrays.SortArrayByParity import sort_array_by_parity, sort_array_by_parity_two_pass, sort_array_by_parity_sort


class MyTestCase(unittest.TestCase):
    def test_sort_array_by_parity(self):
        self.assertEqual([4, 2, 1, 3], sort_array_by_parity(self, nums=[3, 1, 2, 4]))
        self.assertEqual([2, 4, 3, 1], sort_array_by_parity_two_pass(self, nums=[3, 1, 2, 4]))
        self.assertEqual([2, 4, 3, 1], sort_array_by_parity_sort(self, nums=[3, 1, 2, 4]))


if __name__ == '__main__':
    unittest.main()
