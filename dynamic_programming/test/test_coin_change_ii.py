import unittest

from dynamic_programming.CoinChangeII import change


class MyTestCase(unittest.TestCase):
    def test_coin_change(self):
        self.assertEqual(4, change(self, 5, [1, 2, 5]))

    def test_coin_change_1(self):
        self.assertEqual(0, change(self, 3, [2]))

    def test_coin_change_2(self):
        self.assertEqual(1, change(self, 10, [10]))


if __name__ == '__main__':
    unittest.main()
