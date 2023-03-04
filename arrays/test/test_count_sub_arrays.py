import unittest

from arrays.CountSubarraysWithFixedBounds import count_sub_arrays


class MyTestCase(unittest.TestCase):
    def test_count_sub_arrays(self):
        self.assertEqual(2, count_sub_arrays(self, [1, 3, 5, 2, 7, 5], 1, 5))

    def test_count_sub_arrays_1(self):
        self.assertEqual(10, count_sub_arrays(self, [1, 1, 1, 1], 1, 1))


if __name__ == '__main__':
    unittest.main()
