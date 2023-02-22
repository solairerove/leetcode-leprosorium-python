import unittest

from binary_search.KokoEatingBananas import min_eating_speed


class MyTestCase(unittest.TestCase):
    def test_min_eating_speed(self):
        self.assertEqual(4, min_eating_speed(self, [3, 6, 7, 11], 8))

    def test_min_eating_speed_1(self):
        self.assertEqual(30, min_eating_speed(self, [30, 11, 23, 4, 20], 5))

    def test_min_eating_speed_2(self):
        self.assertEqual(23, min_eating_speed(self, [30, 11, 23, 4, 20], 6))


if __name__ == '__main__':
    unittest.main()
