import unittest

from arrays.LongestPalindromicSubstring import longest_palindrome


class MyTestCase(unittest.TestCase):
    def test_longest_palindrome(self):
        self.assertEqual("bab", longest_palindrome(self, "babad"))

    def test_longest_palindrome_1(self):
        self.assertEqual("bb", longest_palindrome(self, "cbbd"))


if __name__ == '__main__':
    unittest.main()
