import unittest

from arrays.MaximumNumberOfVowelsInASubstringOfGivenLength import max_vowels


class MyTestCase(unittest.TestCase):
    def test_max_vowels(self):
        self.assertEqual(3, max_vowels(self, "abciiidef", 3))

    def test_max_vowels_1(self):
        self.assertEqual(2, max_vowels(self, "aeiou", 2))

    def test_max_vowels_2(self):
        self.assertEqual(2, max_vowels(self, "leetcode", 3))


if __name__ == '__main__':
    unittest.main()
