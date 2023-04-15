import unittest

from dynamic_programming.MaximumValueOfKCoinsFromPiles import max_value_of_coins


class MyTestCase(unittest.TestCase):
    def test_max_value_of_coins(self):
        self.assertEqual(101, max_value_of_coins(self, [[1, 100, 3], [7, 8, 9]], 2))

    def test_max_value_of_coins_1(self):
        self.assertEqual(706, max_value_of_coins(
            self, [
                [100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]
            ], 7
        ))


if __name__ == '__main__':
    unittest.main()
