import unittest

from dynamic_programming.BestTimeToBuyAndSellStockWithCooldown import max_profit


class MyTestCase(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(3, max_profit(self, [1, 2, 3, 0, 2]))

    def test_max_profit_1(self):
        self.assertEqual(0, max_profit(self, [1]))


if __name__ == '__main__':
    unittest.main()
