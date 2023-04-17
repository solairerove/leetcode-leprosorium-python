import unittest

from dynamic_programming.BestTimeToBuyAndSellStockWithTransactionFee import max_profit


class MyTestCase(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(8, max_profit(self, [1, 3, 2, 8, 4, 9], 2))

    def test_max_profit_1(self):
        self.assertEqual(6, max_profit(self, [1, 3, 7, 5, 10, 3], 3))


if __name__ == '__main__':
    unittest.main()
