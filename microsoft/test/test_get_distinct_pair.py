import unittest

from microsoft.DistinctEvenPairSum import get_distinct_pair_using_set


class MyTestCase(unittest.TestCase):
    def test_get_distinct_pair(self):
        self.assertEqual(2, get_distinct_pair_using_set(self, [4, 2, 5, 8, 7, 3, 71]))

    def test_get_distinct_pair_1(self):
        self.assertEqual(1, get_distinct_pair_using_set(self, [14, 21, 16, 35, 22]))

    def test_get_distinct_pair_2(self):
        self.assertEqual(3, get_distinct_pair_using_set(self, [5, 5, 5, 5, 5, 5]))


if __name__ == '__main__':
    unittest.main()
