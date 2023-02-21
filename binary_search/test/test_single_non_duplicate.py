import unittest

from binary_search.SingleElementInASortedArray import single_non_duplicate


class MyTestCase(unittest.TestCase):
    def test_single_non_duplicate(self):
        self.assertEqual(2, single_non_duplicate(self, [1, 1, 2, 3, 3, 4, 4, 8, 8]))

    def test_single_non_duplicate_1(self):
        self.assertEqual(10, single_non_duplicate(self, [3, 3, 7, 7, 10, 11, 11]))


if __name__ == '__main__':
    unittest.main()
