import unittest

from binary_search.MinimizeMaxDistanceToGasStation import minmax_gas_dist


class MyTestCase(unittest.TestCase):
    def test_minmax_gas_dist(self):
        self.assertEqual(0.5000001099795104, minmax_gas_dist(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))

    def test_minmax_gas_dist_1(self):
        self.assertEqual(14.000000314144437, minmax_gas_dist(self, [23, 24, 36, 39, 46, 56, 57, 65, 84, 98], 1))


if __name__ == '__main__':
    unittest.main()
