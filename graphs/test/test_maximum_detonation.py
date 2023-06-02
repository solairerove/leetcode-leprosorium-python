import unittest

from graphs.DetonateTheMaximumBombs import maximum_detonation


class MyTestCase(unittest.TestCase):
    def test_maximum_detonation(self):
        self.assertEqual(2, maximum_detonation(self, [[2, 1, 3], [6, 1, 4]]))

    def test_maximum_detonation_1(self):
        self.assertEqual(1, maximum_detonation(self, [[1, 1, 5], [10, 10, 5]]))

    def test_maximum_detonation_2(self):
        self.assertEqual(5, maximum_detonation(self, [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))


if __name__ == '__main__':
    unittest.main()
