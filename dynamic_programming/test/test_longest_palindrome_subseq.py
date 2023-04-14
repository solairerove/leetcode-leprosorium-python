import unittest

from dynamic_programming.LongestPalindromicSubsequence import longest_palindrome_subseq_top_down, \
    longest_palindrome_subseq_bottom_up, longest_palindrome_subseq_space_optimized


class MyTestCase(unittest.TestCase):
    def test_longest_palindrome_subseq(self):
        self.assertEqual(4, longest_palindrome_subseq_top_down(self, "bbbab"))
        self.assertEqual(4, longest_palindrome_subseq_bottom_up(self, "bbbab"))
        self.assertEqual(4, longest_palindrome_subseq_space_optimized(self, "bbbab"))

    def test_longest_palindrome_subseq_1(self):
        self.assertEqual(2, longest_palindrome_subseq_top_down(self, "cbbd"))
        self.assertEqual(2, longest_palindrome_subseq_bottom_up(self, "cbbd"))
        self.assertEqual(2, longest_palindrome_subseq_space_optimized(self, "cbbd"))


if __name__ == '__main__':
    unittest.main()
