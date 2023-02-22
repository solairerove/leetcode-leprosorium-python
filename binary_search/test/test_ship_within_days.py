import unittest

from binary_search.CapacityToShipPackagesWithinDDays import ship_within_days


class MyTestCase(unittest.TestCase):
    def test_ship_within_days(self):
        self.assertEqual(15, ship_within_days(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

    def test_ship_within_days_1(self):
        self.assertEqual(6, ship_within_days(self, [3, 2, 2, 4, 1, 4], 3))

    def test_ship_within_days_2(self):
        self.assertEqual(3, ship_within_days(self, [1, 2, 3, 1, 1], 4))


if __name__ == '__main__':
    unittest.main()
