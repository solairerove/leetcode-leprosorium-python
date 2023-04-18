import unittest

from arrays.MergeStringsAlternately import merge_alternately, merge_alternately_one_liner


class MyTestCase(unittest.TestCase):
    def test_merge_alternately(self):
        self.assertEqual("apbqcr", merge_alternately(self, "abc", "pqr"))
        self.assertEqual("apbqcr", merge_alternately_one_liner(self, "abc", "pqr"))

    def test_merge_alternately_1(self):
        self.assertEqual("apbqrs", merge_alternately(self, "ab", "pqrs"))
        self.assertEqual("apbqrs", merge_alternately_one_liner(self, "ab", "pqrs"))

    def test_merge_alternately_2(self):
        self.assertEqual("apbqcd", merge_alternately(self, "abcd", "pq"))
        self.assertEqual("apbqcd", merge_alternately_one_liner(self, "abcd", "pq"))


if __name__ == '__main__':
    unittest.main()
