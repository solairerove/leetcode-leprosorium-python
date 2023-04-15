import unittest

from dynamic_programming.MaximumLengthOfSubarrayWithPositiveProduct import get_max_len


class MyTestCase(unittest.TestCase):
    def test_get_max_len(self):
        self.assertEqual(4, get_max_len(self, [1, -2, -3, 4]))

    def test_get_max_len_1(self):
        self.assertEqual(3, get_max_len(self, [0, 1, -2, -3, -4]))

    def test_get_max_len_2(self):
        self.assertEqual(2, get_max_len(self, [-1, -2, -3, 0, 1]))


if __name__ == '__main__':
    unittest.main()
