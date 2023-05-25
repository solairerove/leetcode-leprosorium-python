import unittest

from dynamic_programming.New21Game import new_21_game


class MyTestCase(unittest.TestCase):
    def test_new_21_game(self):
        self.assertEqual(0.9999999999999999, new_21_game(self, 10, 1, 10))

    def test_new_21_game_1(self):
        self.assertEqual(0.60000, new_21_game(self, 6, 1, 10))

    def test_new_21_game_2(self):
        self.assertEqual(0.7327777870686082, new_21_game(self, 21, 17, 10))


if __name__ == '__main__':
    unittest.main()
