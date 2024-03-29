import unittest

from dynamic_programming.LongestIncreasingSubsequence import length_of_lis, length_of_lis_bottom_up, length_of_lis_bs


class MyTestCase(unittest.TestCase):
    def test_length_of_lis(self):
        self.assertEqual(4, length_of_lis_bottom_up(self, [10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(4, length_of_lis_bs(self, [10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(4, length_of_lis(self, [10, 9, 2, 5, 3, 7, 101, 18]))

    def test_length_of_lis_1(self):
        self.assertEqual(4, length_of_lis_bottom_up(self, [0, 1, 0, 3, 2, 3]))
        self.assertEqual(4, length_of_lis_bs(self, [0, 1, 0, 3, 2, 3]))
        self.assertEqual(4, length_of_lis(self, [0, 1, 0, 3, 2, 3]))

    def test_length_of_lis_2(self):
        self.assertEqual(1, length_of_lis_bottom_up(self, [7, 7, 7, 7, 7, 7, 7]))
        self.assertEqual(1, length_of_lis_bs(self, [7, 7, 7, 7, 7, 7, 7]))
        self.assertEqual(1, length_of_lis(self, [7, 7, 7, 7, 7, 7, 7]))


if __name__ == '__main__':
    unittest.main()
