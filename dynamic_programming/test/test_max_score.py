import unittest

from dynamic_programming.MaximizeScoreAfterNOperations import max_score


class MyTestCase(unittest.TestCase):
    def test_max_score(self):
        self.assertEqual(1, max_score(self, [1, 2]))

    def test_max_score_1(self):
        self.assertEqual(11, max_score(self, [3, 4, 6, 8]))

    def test_max_score_2(self):
        self.assertEqual(14, max_score(self, [1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    unittest.main()
