import unittest

from dynamic_programming.MaximumSumCircularSubarray import max_subarray_sum_circular


class MyTestCase(unittest.TestCase):
    def test_max_subarray_sum_circular(self):
        self.assertEqual(3, max_subarray_sum_circular(self, [1, -2, 3, -2]))

    def test_max_subarray_sum_circular_1(self):
        self.assertEqual(10, max_subarray_sum_circular(self, [5, -3, 5]))

    def test_max_subarray_sum_circular_2(self):
        self.assertEqual(-2, max_subarray_sum_circular(self, [-3, -2, -3]))


if __name__ == '__main__':
    unittest.main()
