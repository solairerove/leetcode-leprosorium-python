import unittest

from dynamic_programming.PerfectSquares import num_squares


class MyTestCase(unittest.TestCase):
    def test_num_squares(self):
        self.assertEqual(3, num_squares(self, 12))

    def test_num_squares_1(self):
        self.assertEqual(2, num_squares(self, 13))


if __name__ == '__main__':
    unittest.main()
