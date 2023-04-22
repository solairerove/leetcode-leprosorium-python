import unittest

from dynamic_programming.MinimumInsertionStepsToMakeAStringPalindrome import min_insertions_top_down


class MyTestCase(unittest.TestCase):
    def test_min_insertions(self):
        self.assertEqual(0, min_insertions_top_down(self, "zzazz"))

    def test_min_insertions_1(self):
        self.assertEqual(2, min_insertions_top_down(self, "mbadm"))

    def test_min_insertions_2(self):
        self.assertEqual(5, min_insertions_top_down(self, "leetcode"))


if __name__ == '__main__':
    unittest.main()
