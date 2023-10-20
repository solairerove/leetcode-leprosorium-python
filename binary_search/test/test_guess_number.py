import unittest

from binary_search.GuessNumberHigherOrLower import guess_number


class MyTestCase(unittest.TestCase):
    def test_guess_number(self):
        self.assertEqual(6, guess_number(self, n=10, pick=6))

    def test_guess_number_1(self):
        self.assertEqual(1, guess_number(self, n=1, pick=1))

    def test_guess_number_2(self):
        self.assertEqual(1, guess_number(self, n=2, pick=1))


if __name__ == '__main__':
    unittest.main()
