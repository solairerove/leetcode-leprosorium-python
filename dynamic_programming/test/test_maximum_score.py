import unittest

from dynamic_programming.MaximumScoreFromPerformingMultiplicationOperations import maximum_score_top_down, \
    maximum_score_bottom_up


class MyTestCase(unittest.TestCase):
    def test_maximum_score(self):
        self.assertEqual(14, maximum_score_top_down(self, [1, 2, 3], [3, 2, 1]))
        self.assertEqual(14, maximum_score_bottom_up(self, [1, 2, 3], [3, 2, 1]))

    def test_maximum_score_1(self):
        self.assertEqual(102, maximum_score_top_down(self, [-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))
        self.assertEqual(102, maximum_score_bottom_up(self, [-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))


if __name__ == '__main__':
    unittest.main()
