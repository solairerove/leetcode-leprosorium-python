import unittest

from graphs.MinimumScoreOfAPathBetweenTwoCities import min_score


class MyTestCase(unittest.TestCase):
    def test_min_score(self):
        self.assertEqual(5, min_score(self, 4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))

    def test_min_score_1(self):
        self.assertEqual(2, min_score(self, 4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]))


if __name__ == '__main__':
    unittest.main()
