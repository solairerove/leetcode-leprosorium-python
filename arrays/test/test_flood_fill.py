import unittest

from arrays.FloodFill import flood_fill


class MyTestCase(unittest.TestCase):
    def test_flood_fill(self):
        self.assertEqual([[2, 2, 2], [2, 2, 0], [2, 0, 1]],
                         flood_fill(self, image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))

    def test_flood_fill_1(self):
        self.assertEqual([[0, 0, 0], [0, 0, 0]],
                         flood_fill(self, image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0))


if __name__ == '__main__':
    unittest.main()
