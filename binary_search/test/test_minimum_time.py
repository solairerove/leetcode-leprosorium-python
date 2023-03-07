import unittest

from binary_search.MinimumTimeToCompleteTrips import minimum_time


class MyTestCase(unittest.TestCase):
    def test_minimum_time(self):
        self.assertEqual(3, minimum_time(self, [1, 2, 3], 5))

    def test_minimum_time_1(self):
        self.assertEqual(2, minimum_time(self, [2], 1))


if __name__ == '__main__':
    unittest.main()
