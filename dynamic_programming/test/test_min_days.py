import unittest

from dynamic_programming.MinimumNumberOfDaysToEatNOranges import min_days


class MyTestCase(unittest.TestCase):
    def test_min_days(self):
        self.assertEqual(4, min_days(self, 10))

    def test_min_days_1(self):
        self.assertEqual(3, min_days(self, 6))


if __name__ == '__main__':
    unittest.main()
