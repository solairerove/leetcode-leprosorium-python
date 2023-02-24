import unittest

from heap.MinimizeDeviationInArray import minimum_deviation


class MyTestCase(unittest.TestCase):
    def test_minimum_deviation(self):
        self.assertEqual(1, minimum_deviation(self, [1, 2, 3, 4]))

    def test_minimum_deviation_1(self):
        self.assertEqual(3, minimum_deviation(self, [4, 1, 5, 20, 3]))

    def test_minimum_deviation_2(self):
        self.assertEqual(3, minimum_deviation(self, [2, 10, 8]))


if __name__ == '__main__':
    unittest.main()
