import unittest

from arrays.LetterCombinationsOfAPhoneNumber import letter_combinations


class MyTestCase(unittest.TestCase):
    def test_letter_combinations(self):
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], letter_combinations(self, "23"))

    def test_letter_combinations_1(self):
        self.assertEqual([], letter_combinations(self, ""))

    def test_letter_combinations_2(self):
        self.assertEqual(["a", "b", "c"], letter_combinations(self, "2"))


if __name__ == '__main__':
    unittest.main()
