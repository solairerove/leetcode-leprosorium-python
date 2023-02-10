import unittest

from dynamic_programming.LongestCommonSubsequence import longest_common_subsequence


class MyTestCase(unittest.TestCase):
    def test_longest_common_subsequence(self):
        self.assertEqual(3, longest_common_subsequence(self, "abcde", "ace"))

    def test_longest_common_subsequence_1(self):
        self.assertEqual(3, longest_common_subsequence(self, "abc", "abc"))

    def test_longest_common_subsequence_2(self):
        self.assertEqual(0, longest_common_subsequence(self, "abc", "def"))

    def test_longest_common_subsequence_3(self):
        self.assertEqual(3, longest_common_subsequence(self, "hish", "fish"))

    def test_longest_common_subsequence_4(self):
        self.assertEqual(2, longest_common_subsequence(self, "hish", "vista"))


if __name__ == '__main__':
    unittest.main()
