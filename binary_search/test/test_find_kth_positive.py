import unittest

from binary_search.KthMissingPositiveNumber import find_kth_positive


class MyTestCase(unittest.TestCase):
    def test_find_kth_positive(self):
        self.assertEqual(9, find_kth_positive(self, [2, 3, 4, 7, 11], 5))

    def test_find_kth_positive_1(self):
        self.assertEqual(6, find_kth_positive(self, [1, 2, 3, 4], 2))


if __name__ == '__main__':
    unittest.main()
