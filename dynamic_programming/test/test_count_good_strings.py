import unittest

from dynamic_programming.CountWaysToBuildGoodStrings import count_good_strings


class MyTestCase(unittest.TestCase):
    def test_count_good_strings(self):
        self.assertEqual(8, count_good_strings(self, low=3, high=3, zero=1, one=1))

    def test_count_good_strings_1(self):
        self.assertEqual(5, count_good_strings(self, low=2, high=3, zero=1, one=2))


if __name__ == '__main__':
    unittest.main()
