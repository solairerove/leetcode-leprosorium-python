import unittest

from dynamic_programming.LongestPalindromicSubstring import longest_palindrome


class MyTestCase(unittest.TestCase):
    def test_longest_palindrome(self):
        self.assertEqual("bab", longest_palindrome(self, "babad"))  # add assertion here

    def test_longest_palindrome_1(self):
        self.assertEqual("bb", longest_palindrome(self, "cbbd"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
