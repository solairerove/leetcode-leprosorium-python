import unittest

from arrays.MergeStringsAlternately import merge_alternately


class MyTestCase(unittest.TestCase):
    def test_merge_alternately(self):
        self.assertEqual("apbqcr", merge_alternately(self, "abc", "pqr"))

    def test_merge_alternately_1(self):
        self.assertEqual("apbqrs", merge_alternately(self, "ab", "pqrs"))

    def test_merge_alternately_2(self):
        self.assertEqual("apbqcd", merge_alternately(self, "abcd", "pq"))


if __name__ == '__main__':
    unittest.main()
