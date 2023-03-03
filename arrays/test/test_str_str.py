import unittest

from arrays.FindTheIndexOfTheFirstOccurrenceInAString import str_str


class MyTestCase(unittest.TestCase):
    def test_str_str(self):
        self.assertEqual(0, str_str(self, haystack="sadbutsad", needle="sad"))

    def test_str_str_1(self):
        self.assertEqual(-1, str_str(self, haystack="leetcode", needle="leeto"))

    def test_str_str_2(self):
        self.assertEqual(2, str_str(self, haystack="hello", needle="ll"))

    def test_str_str_3(self):
        self.assertEqual(-1, str_str(self, haystack="aaa", needle="aaaa"))

    def test_str_str_4(self):
        self.assertEqual(4, str_str(self, haystack="mississippi", needle="issip"))


if __name__ == '__main__':
    unittest.main()
