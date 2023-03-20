import unittest

from arrays.ContainerWithMostWater import max_area


class MyTestCase(unittest.TestCase):
    def test_max_area(self):
        self.assertEqual(49, max_area(self, [1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def test_max_area_1(self):
        self.assertEqual(1, max_area(self, [1, 1]))


if __name__ == '__main__':
    unittest.main()
