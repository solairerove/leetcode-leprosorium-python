import unittest

from sliding_window.LongestSubarrayOfOnesAfterDeletingOneElement import longest_subarray


class MyTestCase(unittest.TestCase):
    def test_longest_subarray(self):
        self.assertEqual(3, longest_subarray(self, nums=[1, 1, 0, 1]))

    def test_longest_subarray_1(self):
        self.assertEqual(5, longest_subarray(self, nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))

    def test_longest_subarray_2(self):
        self.assertEqual(2, longest_subarray(self, nums=[1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
