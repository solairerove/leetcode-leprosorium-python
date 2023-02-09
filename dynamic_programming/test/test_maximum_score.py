import unittest

from dynamic_programming.MaximumScoreFromPerformingMultiplicationOperations import maximum_score


class MyTestCase(unittest.TestCase):
    def test_maximum_score(self):
        self.assertEqual(14, maximum_score(self, [1, 2, 3], [3, 2, 1]))

    def test_maximum_score_1(self):
        self.assertEqual(102, maximum_score(self, [-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))


if __name__ == '__main__':
    unittest.main()
