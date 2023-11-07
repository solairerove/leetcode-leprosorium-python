import unittest

from sliding_window.SlidingWindowMaximum import max_sliding_window


class MyTestCase(unittest.TestCase):
    def test_max_sliding_window(self):
        self.assertEqual([3, 3, 5, 5, 6, 7], max_sliding_window(self, nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

    def test_max_sliding_window_1(self):
        self.assertEqual([1], max_sliding_window(self, nums=[1], k=1))

    def test_max_sliding_window_2(self):
        self.assertEqual([3,3,2,5], max_sliding_window(self, nums=[1,3,1,2,0,5], k=3))


if __name__ == '__main__':
    unittest.main()
