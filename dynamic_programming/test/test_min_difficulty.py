import unittest

from dynamic_programming.MinimumDifficultyOfAJobSchedule import min_difficulty


class MyTestCase(unittest.TestCase):
    def test_min_difficulty(self):
        self.assertEqual(7, min_difficulty(self, [6, 5, 4, 3, 2, 1], 2))

    def test_min_difficulty_1(self):
        self.assertEqual(-1, min_difficulty(self, [9, 9, 9], 4))

    def test_min_difficulty_2(self):
        self.assertEqual(3, min_difficulty(self, [1, 1, 1], 3))


if __name__ == '__main__':
    unittest.main()
