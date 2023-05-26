import unittest

from dynamic_programming.StoneGameII import stone_game_ii


class MyTestCase(unittest.TestCase):
    def test_stone_game_ii(self):
        self.assertEqual(10, stone_game_ii(self, [2, 7, 9, 4, 4]))

    def test_stone_game_ii_1(self):
        self.assertEqual(104, stone_game_ii(self, [1, 2, 3, 4, 5, 100]))


if __name__ == '__main__':
    unittest.main()
