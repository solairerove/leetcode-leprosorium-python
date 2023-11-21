import unittest

from dynamic_programming.BestTimeToBuyAndSellStockII import max_profit, max_profit_lambda


class MyTestCase(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(7, max_profit(self, [7, 1, 5, 3, 6, 4]))
        self.assertEqual(7, max_profit_lambda(self, [7, 1, 5, 3, 6, 4]))

    def test_max_profit_1(self):
        self.assertEqual(4, max_profit(self, [1, 2, 3, 4, 5]))
        self.assertEqual(4, max_profit_lambda(self, [1, 2, 3, 4, 5]))

    def test_max_profit_2(self):
        self.assertEqual(0, max_profit(self, [7, 6, 4, 3, 1]))
        self.assertEqual(0, max_profit_lambda(self, [7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
