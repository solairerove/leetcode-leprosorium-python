import unittest

from arrays.LongestPalindrome import longest_palindrome


class MyTestCase(unittest.TestCase):
    def test_longest_palindrome(self):
        self.assertEqual(7, longest_palindrome(self, "abccccdd"))

    def test_longest_palindrome_1(self):
        self.assertEqual(1, longest_palindrome(self, "a"))


if __name__ == '__main__':
    unittest.main()
