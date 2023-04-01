import unittest

from dynamic_programming.RangeSumQueryMutable import NumArray


class MyTestCase(unittest.TestCase):
    def test_sum_range_mutable(self):
        num_array = NumArray([1, 3, 5])
        self.assertEqual(9, num_array.sum_range(0, 2))
        num_array.update(1, 2)
        self.assertEqual(8, num_array.sum_range(0, 2))


if __name__ == '__main__':
    unittest.main()
