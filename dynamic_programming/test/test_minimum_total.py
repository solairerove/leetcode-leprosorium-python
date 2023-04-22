import unittest

from dynamic_programming.Triangle import minimum_total


class MyTestCase(unittest.TestCase):
    def test_minimum_total(self):
        self.assertEqual(11, minimum_total(self, [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))

    def test_minimum_total_1(self):
        self.assertEqual(-10, minimum_total(self, [[-10]]))


if __name__ == '__main__':
    unittest.main()
