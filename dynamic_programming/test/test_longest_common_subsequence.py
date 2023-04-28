import unittest

from dynamic_programming.LongestCommonSubsequence import longest_common_subsequence_top_down, \
    longest_common_subsequence_bottom_up


class MyTestCase(unittest.TestCase):
    def test_longest_common_subsequence(self):
        self.assertEqual(3, longest_common_subsequence_top_down(self, "abcde", "ace"))
        self.assertEqual(3, longest_common_subsequence_bottom_up(self, "abcde", "ace"))

    def test_longest_common_subsequence_1(self):
        self.assertEqual(3, longest_common_subsequence_top_down(self, "abc", "abc"))
        self.assertEqual(3, longest_common_subsequence_bottom_up(self, "abc", "abc"))

    def test_longest_common_subsequence_2(self):
        self.assertEqual(0, longest_common_subsequence_top_down(self, "abc", "def"))
        self.assertEqual(0, longest_common_subsequence_bottom_up(self, "abc", "def"))

    def test_longest_common_subsequence_3(self):
        self.assertEqual(3, longest_common_subsequence_top_down(self, "hish", "fish"))
        self.assertEqual(3, longest_common_subsequence_bottom_up(self, "hish", "fish"))

    def test_longest_common_subsequence_4(self):
        self.assertEqual(2, longest_common_subsequence_top_down(self, "hish", "vista"))
        self.assertEqual(2, longest_common_subsequence_bottom_up(self, "hish", "vista"))


if __name__ == '__main__':
    unittest.main()
