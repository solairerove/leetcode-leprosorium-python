import unittest

from binary_search.PeakIndexInAMountainArray import peak_index_in_mountain_array


class MyTestCase(unittest.TestCase):
    def test_peak_index_in_mountain_array(self):
        self.assertEqual(1, peak_index_in_mountain_array(self, arr=[0, 1, 0]))

    def test_peak_index_in_mountain_array_1(self):
        self.assertEqual(1, peak_index_in_mountain_array(self, arr=[0, 2, 1, 0]))

    def test_peak_index_in_mountain_array_2(self):
        self.assertEqual(1, peak_index_in_mountain_array(self, arr=[0, 10, 5, 2]))


if __name__ == '__main__':
    unittest.main()
