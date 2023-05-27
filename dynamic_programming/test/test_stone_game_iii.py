import unittest

from dynamic_programming.StoneGameIII import stone_game_iii


class MyTestCase(unittest.TestCase):
    def test_stone_game_iii(self):
        self.assertEqual("Bob", stone_game_iii(self, [1, 2, 3, 7]))

    def test_stone_game_iii_1(self):
        self.assertEqual("Alice", stone_game_iii(self, [1, 2, 3, -9]))

    def test_stone_game_iii_2(self):
        self.assertEqual("Tie", stone_game_iii(self, [1, 2, 3, 6]))


if __name__ == '__main__':
    unittest.main()
