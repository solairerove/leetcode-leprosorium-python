import unittest

from dynamic_programming.MinimumInsertionStepsToMakeAStringPalindrome import min_insertions_top_down, \
    min_insertions_bottom_up


class MyTestCase(unittest.TestCase):
    def test_min_insertions(self):
        self.assertEqual(0, min_insertions_top_down(self, "zzazz"))
        self.assertEqual(0, min_insertions_bottom_up(self, "zzazz"))

    def test_min_insertions_1(self):
        self.assertEqual(2, min_insertions_top_down(self, "mbadm"))
        self.assertEqual(2, min_insertions_bottom_up(self, "mbadm"))

    def test_min_insertions_2(self):
        self.assertEqual(5, min_insertions_top_down(self, "leetcode"))
        self.assertEqual(5, min_insertions_bottom_up(self, "leetcode"))


if __name__ == '__main__':
    unittest.main()
