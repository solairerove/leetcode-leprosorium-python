import unittest

from dynamic_programming.PalindromicSubstrings import count_substrings


class MyTestCase(unittest.TestCase):
    def test_count_substrings(self):
        self.assertEqual(3, count_substrings(self, "abc"))  # add assertion here

    def test_count_substrings_1(self):
        self.assertEqual(6, count_substrings(self, "aaa"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
