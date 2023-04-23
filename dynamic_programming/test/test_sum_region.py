import unittest

from dynamic_programming.RangeSumQuery2DImmutable import NumMatrix


class MyTestCase(unittest.TestCase):
    def test_sum_region(self):
        num_matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(8, num_matrix.sum_region(2, 1, 4, 3))
        self.assertEqual(11, num_matrix.sum_region(1, 1, 2, 2))
        self.assertEqual(12, num_matrix.sum_region(1, 2, 2, 4))


if __name__ == '__main__':
    unittest.main()
