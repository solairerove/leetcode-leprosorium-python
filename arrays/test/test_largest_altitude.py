import unittest

from arrays.FindTheHighestAltitude import largest_altitude


class MyTestCase(unittest.TestCase):
    def test_largest_altitude(self):
        self.assertEqual(1, largest_altitude(self, [-5, 1, 5, 0, -7]))

    def test_largest_altitude_1(self):
        self.assertEqual(0, largest_altitude(self, [-4, -3, -2, -1, 4, 3, 2]))


if __name__ == '__main__':
    unittest.main()
