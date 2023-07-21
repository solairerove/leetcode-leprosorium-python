import unittest

from dynamic_programming.NumberOfLongestIncreasingSubsequence import find_number_of_lis


class MyTestCase(unittest.TestCase):
    def test_find_number_of_lis(self):
        self.assertEqual(2, find_number_of_lis(self, nums=[1, 3, 5, 4, 7]))

    def test_find_number_of_lis_1(self):
        self.assertEqual(5, find_number_of_lis(self, nums=[2, 2, 2, 2, 2]))


if __name__ == '__main__':
    unittest.main()
