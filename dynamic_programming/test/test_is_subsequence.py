import unittest

from dynamic_programming.IsSubsequence import is_subsequence_top_down, is_subsequence, is_subsequence_liner


class MyTestCase(unittest.TestCase):
    def test_is_subsequence(self):
        self.assertEqual(True, is_subsequence_top_down(self, "abc", "ahbgdc"))
        self.assertEqual(True, is_subsequence(self, "abc", "ahbgdc"))
        self.assertEqual(True, is_subsequence_liner(self, "abc", "ahbgdc"))

    def test_is_subsequence_1(self):
        self.assertEqual(False, is_subsequence_top_down(self, "axc", "ahbgdc"))
        self.assertEqual(False, is_subsequence(self, "axc", "ahbgdc"))
        self.assertEqual(False, is_subsequence_liner(self, "axc", "ahbgdc"))


if __name__ == '__main__':
    unittest.main()
