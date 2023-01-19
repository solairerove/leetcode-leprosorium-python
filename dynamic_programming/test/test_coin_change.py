import unittest

from dynamic_programming.CoinChange import coin_change


class MyTestCase(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(3, coin_change(self, [1, 2, 5], 11))  

    def test_coin_change_1(self):
        self.assertEqual(-1, coin_change(self, [2], 3))  

    def test_coin_change_2(self):
        self.assertEqual(0, coin_change(self, [1], 0))  


if __name__ == '__main__':
    unittest.main()
