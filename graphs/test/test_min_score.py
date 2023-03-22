import unittest

from graphs.MinimumScoreOfAPathBetweenTwoCities import Solution


class MyTestCase(unittest.TestCase):
    def test_min_score(self):
        solution = Solution()
        self.assertEqual(5, solution.min_score(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))

    def test_min_score_1(self):
        solution = Solution()
        self.assertEqual(2, solution.min_score(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]))


if __name__ == '__main__':
    unittest.main()
