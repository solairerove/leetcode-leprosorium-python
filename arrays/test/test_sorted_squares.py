import unittest

from arrays.SquaresOfASortedArray import sorted_squares


class MyTestCase(unittest.TestCase):
    def test_sorted_squares(self):
        self.assertEqual([0, 1, 9, 16, 100], sorted_squares(self, [-4, -1, 0, 3, 10]))

    def test_sorted_squares_1(self):
        self.assertEqual([4, 9, 9, 49, 121], sorted_squares(self, [-7, -3, 2, 3, 11]))


if __name__ == '__main__':
    unittest.main()
