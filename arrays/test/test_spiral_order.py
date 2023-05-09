import unittest

from arrays.SpiralMatrix import spiral_order


class MyTestCase(unittest.TestCase):
    def test_spiral_order(self):
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], spiral_order(self, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_spiral_order_1(self):
        self.assertEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
                         spiral_order(self, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))


if __name__ == '__main__':
    unittest.main()
