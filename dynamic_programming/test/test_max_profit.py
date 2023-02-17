import unittest

from dynamic_programming.BestTimeToBuyAndSellStock import max_profit


class MyTestCase(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(5, max_profit(self, [7, 1, 5, 3, 6, 4]))

    def test_max_profit_1(self):
        self.assertEqual(0, max_profit(self, [7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
