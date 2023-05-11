import unittest

from dynamic_programming.UncrossedLines import max_uncrossed_lines


class MyTestCase(unittest.TestCase):
    def test_max_uncrossed_lines(self):
        self.assertEqual(3, max_uncrossed_lines(self, [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))

    def test_max_uncrossed_lines_1(self):
        self.assertEqual(2, max_uncrossed_lines(self, [1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))


if __name__ == '__main__':
    unittest.main()
