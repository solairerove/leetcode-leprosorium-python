import unittest

from binary_search.MinimumSpeedToArriveOnTime import min_speed_on_time


class MyTestCase(unittest.TestCase):
    def test_min_speed_on_time(self):
        self.assertEqual(1, min_speed_on_time(self, dist=[1, 3, 2], hour=6))

    def test_min_speed_on_time_1(self):
        self.assertEqual(3, min_speed_on_time(self, dist=[1, 3, 2], hour=2.7))

    def test_min_speed_on_time_2(self):
        self.assertEqual(-1, min_speed_on_time(self, dist=[1, 3, 2], hour=1.9))


if __name__ == '__main__':
    unittest.main()
