import unittest

from dynamic_programming.BestSightseeingPair import max_score_sightseeing_pair


class MyTestCase(unittest.TestCase):
    def test_max_score_sightseeing_pair(self):
        self.assertEqual(11, max_score_sightseeing_pair(self, [8, 1, 5, 2, 6]))

    def test_max_score_sightseeing_pair_1(self):
        self.assertEqual(2, max_score_sightseeing_pair(self, [1, 2]))


if __name__ == '__main__':
    unittest.main()
