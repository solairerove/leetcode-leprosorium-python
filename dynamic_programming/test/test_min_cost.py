import unittest

from dynamic_programming.MinimumCostToCutAStick import min_cost


class MyTestCase(unittest.TestCase):
    def test_min_cost(self):
        self.assertEqual(16, min_cost(self, n=7, cuts=[1, 3, 4, 5]))

    def test_min_cost_1(self):
        self.assertEqual(22, min_cost(self, n=9, cuts=[5, 6, 1, 4, 2]))


if __name__ == '__main__':
    unittest.main()
