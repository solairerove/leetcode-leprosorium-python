import unittest

from dynamic_programming.ProfitableSchemes import profitable_schemes_top_down, profitable_schemes


class MyTestCase(unittest.TestCase):
    def test_profitable_schemes(self):
        self.assertEqual(2, profitable_schemes(self, 5, 3, [2, 2], [2, 3]))
        self.assertEqual(2, profitable_schemes_top_down(self, 5, 3, [2, 2], [2, 3]))

    def test_profitable_schemes_1(self):
        self.assertEqual(7, profitable_schemes(self, 10, 5, [2, 3, 5], [6, 7, 8]))
        self.assertEqual(7, profitable_schemes_top_down(self, 10, 5, [2, 3, 5], [6, 7, 8]))


if __name__ == '__main__':
    unittest.main()
