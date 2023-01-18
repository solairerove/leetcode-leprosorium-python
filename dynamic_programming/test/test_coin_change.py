import unittest

from dynamic_programming.CoinChange import coin_change


class MyTestCase(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(3, coin_change(self, [1, 2, 5], 11))  # add assertion here

    def test_coin_change_1(self):
        self.assertEqual(-1, coin_change(self, [2], 3))  # add assertion here

    def test_coin_change_2(self):
        self.assertEqual(0, coin_change(self, [1], 0))  # add assertion here


if __name__ == '__main__':
    unittest.main()
