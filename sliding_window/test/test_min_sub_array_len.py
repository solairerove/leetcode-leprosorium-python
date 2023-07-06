import unittest

from sliding_window.MinimumSizeSubarraySum import min_sub_array_len


class MyTestCase(unittest.TestCase):
    def test_min_sub_array_len(self):
        self.assertEqual(2, min_sub_array_len(self, target=7, nums=[2, 3, 1, 2, 4, 3]))

    def test_min_sub_array_len_1(self):
        self.assertEqual(1, min_sub_array_len(self, target=4, nums=[1, 4, 4]))

    def test_min_sub_array_len_2(self):
        self.assertEqual(0, min_sub_array_len(self, target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
