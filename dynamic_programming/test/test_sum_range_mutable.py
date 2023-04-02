import unittest

from dynamic_programming.RangeSumQueryMutable import NumArrayBIT, NumArraySegmentTree


class MyTestCase(unittest.TestCase):
    def test_sum_range_mutable(self):
        num_array_bit = NumArrayBIT([1, 3, 5])
        self.assertEqual(9, num_array_bit.sum_range(0, 2))
        num_array_bit.update(1, 2)
        self.assertEqual(8, num_array_bit.sum_range(0, 2))

        num_array_seg_tree = NumArraySegmentTree([1, 3, 5])
        self.assertEqual(9, num_array_seg_tree.sum_range(0, 2))
        num_array_seg_tree.update(1, 2)
        self.assertEqual(8, num_array_seg_tree.sum_range(0, 2))


if __name__ == '__main__':
    unittest.main()
