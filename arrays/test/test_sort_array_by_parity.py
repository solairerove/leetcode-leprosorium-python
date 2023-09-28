import unittest

from arrays.SortArrayByParity import sort_array_by_parity


class MyTestCase(unittest.TestCase):
    def test_sort_array_by_parity(self):
        self.assertEqual([4, 2, 1, 3], sort_array_by_parity(self, nums=[3, 1, 2, 4]))


if __name__ == '__main__':
    unittest.main()
