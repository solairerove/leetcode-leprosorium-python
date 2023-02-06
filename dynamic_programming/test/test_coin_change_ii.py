import unittest

from dynamic_programming.CoinChangeII import change, change_classic_knapsack


class MyTestCase(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(4, change(self, 5, [1, 2, 5]))
        self.assertEqual(4, change_classic_knapsack(self, 5, [1, 2, 5]))

    def test_coin_change_1(self):
        self.assertEqual(0, change(self, 3, [2]))
        self.assertEqual(0, change_classic_knapsack(self, 3, [2]))

    def test_coin_change_2(self):
        self.assertEqual(1, change(self, 10, [10]))
        self.assertEqual(1, change_classic_knapsack(self, 10, [10]))

    def test_coin_change_3(self):
        self.assertEqual(1, change(self, 100, [1, 101, 102, 103]))
        self.assertEqual(1, change_classic_knapsack(self, 100, [1, 101, 102, 103]))


if __name__ == '__main__':
    unittest.main()
