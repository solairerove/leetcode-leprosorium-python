import unittest

from dynamic_programming.BestTimeToBuyAndSellStockIV import max_profit


class MyTestCase(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(2, max_profit(self, 2, [2, 4, 1]))

    def test_max_profit_1(self):
        self.assertEqual(7, max_profit(self, 2, [3, 2, 6, 5, 0, 3]))


if __name__ == '__main__':
    unittest.main()
