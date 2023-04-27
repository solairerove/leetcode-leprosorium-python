import unittest

from dynamic_programming.WiggleSubsequence import wiggle_max_length


class MyTestCase(unittest.TestCase):
    def test_wiggle_max_length(self):
        self.assertEqual(6, wiggle_max_length(self, [1, 7, 4, 9, 2, 5]))

    def test_wiggle_max_length_1(self):
        self.assertEqual(7, wiggle_max_length(self, [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))

    def test_wiggle_max_length_2(self):
        self.assertEqual(2, wiggle_max_length(self, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_wiggle_max_length_3(self):
        self.assertEqual(3, wiggle_max_length(self, [3, 3, 3, 2, 5]))


if __name__ == '__main__':
    unittest.main()
