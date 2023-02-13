import unittest

from maths.CountOddNumbersInAnIntervalRange import count_odds


class MyTestCase(unittest.TestCase):
    def test_count_odds(self):
        self.assertEqual(3, count_odds(self, 3, 7))

    def test_count_odds_1(self):
        self.assertEqual(1, count_odds(self, 8, 10))


if __name__ == '__main__':
    unittest.main()
