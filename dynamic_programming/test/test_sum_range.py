import unittest

from dynamic_programming.RangeSumQuery import NumArray


class MyTestCase(unittest.TestCase):
    def test_sum_range(self):
        num_array = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(1, num_array.sum_range(0, 2))
        self.assertEqual(-1, num_array.sum_range(2, 5))
        self.assertEqual(-3, num_array.sum_range(0, 5))


if __name__ == '__main__':
    unittest.main()
