import unittest

from dynamic_programming.MinimumDifficultyOfAJobSchedule import min_difficulty_top_down, \
    min_difficulty_bottom_up


class MyTestCase(unittest.TestCase):
    def test_min_difficulty(self):
        self.assertEqual(7, min_difficulty_top_down(self, [6, 5, 4, 3, 2, 1], 2))
        self.assertEqual(7, min_difficulty_bottom_up(self, [6, 5, 4, 3, 2, 1], 2))

    def test_min_difficulty_1(self):
        self.assertEqual(-1, min_difficulty_top_down(self, [9, 9, 9], 4))
        self.assertEqual(-1, min_difficulty_bottom_up(self, [9, 9, 9], 4))

    def test_min_difficulty_2(self):
        self.assertEqual(3, min_difficulty_top_down(self, [1, 1, 1], 3))
        self.assertEqual(3, min_difficulty_bottom_up(self, [1, 1, 1], 3))


if __name__ == '__main__':
    unittest.main()
