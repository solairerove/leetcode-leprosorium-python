import unittest

from binary_search.CountNegativeNumbersInASortedMatrix import count_negatives, count_negatives_bs


class MyTestCase(unittest.TestCase):
    def test_count_negatives(self):
        self.assertEqual(8, count_negatives(self, [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
        self.assertEqual(8, count_negatives_bs(self, [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))

    def test_count_negatives_1(self):
        self.assertEqual(0, count_negatives(self, [[3, 2], [1, 0]]))
        self.assertEqual(0, count_negatives_bs(self, [[3, 2], [1, 0]]))


if __name__ == '__main__':
    unittest.main()
