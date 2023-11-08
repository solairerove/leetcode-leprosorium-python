import unittest

from sliding_window.SlidingWindowMedian import median_sliding_window


class MyTestCase(unittest.TestCase):
    def test_median_sliding_window(self):
        self.assertEqual([1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000],
                         median_sliding_window(self, nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

    def test_median_sliding_window_1(self):
        self.assertEqual([2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000],
                         median_sliding_window(self, nums=[1, 2, 3, 4, 2, 3, 1, 4, 2], k=3))

    def test_median_sliding_window_2(self):
        self.assertEqual([1073741824.00000, 1.50000, 2.50000, 3.50000, 4.50000, 5.50000, 6.50000, 1073741827.00000],
                         median_sliding_window(self, nums=[2147483647, 1, 2, 3, 4, 5, 6, 7, 2147483647], k=2))


if __name__ == '__main__':
    unittest.main()
