import unittest

from dynamic_programming.LongestPalindromicSubsequence import longest_palindrome_subseq_top_down


class MyTestCase(unittest.TestCase):
    def test_longest_palindrome_subseq(self):
        self.assertEqual(4, longest_palindrome_subseq_top_down(self, "bbbab"))

    def test_longest_palindrome_subseq_1(self):
        self.assertEqual(2, longest_palindrome_subseq_top_down(self, "cbbd"))


if __name__ == '__main__':
    unittest.main()
