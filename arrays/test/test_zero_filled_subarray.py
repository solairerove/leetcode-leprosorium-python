import unittest

from arrays.NumberOfZeroFilledSubarrays import zero_filled_subarray


class MyTestCase(unittest.TestCase):
    def test_zero_filled_subarray(self):
        self.assertEqual(6, zero_filled_subarray(self, [1, 3, 0, 0, 2, 0, 0, 4]))

    def test_zero_filled_subarray_1(self):
        self.assertEqual(9, zero_filled_subarray(self, [0, 0, 0, 2, 0, 0]))

    def test_zero_filled_subarray_2(self):
        self.assertEqual(0, zero_filled_subarray(self, [2, 10, 2019]))


if __name__ == '__main__':
    unittest.main()
