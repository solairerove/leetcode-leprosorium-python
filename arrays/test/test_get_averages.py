import unittest

from arrays.KRadiusSubarrayAverages import get_averages


class MyTestCase(unittest.TestCase):
    def test_get_averages(self):
        self.assertEqual([-1, -1, -1, 5, 4, 4, -1, -1, -1], get_averages(self, [7, 4, 3, 9, 1, 8, 5, 2, 6], 3))

    def test_get_averages_1(self):
        self.assertEqual([100000], get_averages(self, [100000], 0))


if __name__ == '__main__':
    unittest.main()
