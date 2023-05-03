import unittest

from arrays.FindTheDifferenceOfTwoArrays import find_difference_naive


class MyTestCase(unittest.TestCase):
    def test_find_difference(self):
        self.assertEqual([[1, 3], [4, 6]], find_difference_naive(self, [1, 2, 3], [2, 4, 6]))

    def test_find_difference_1(self):
        self.assertEqual([[3], []], find_difference_naive(self, [1, 2, 3, 3], [1, 1, 2, 2]))


if __name__ == '__main__':
    unittest.main()
