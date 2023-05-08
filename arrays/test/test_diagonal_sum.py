import unittest

from arrays.MatrixDiagonalSum import diagonal_sum


class MyTestCase(unittest.TestCase):
    def test_diagonal_sum(self):
        self.assertEqual(25, diagonal_sum(self, [[1, 2, 3],
                                                 [4, 5, 6],
                                                 [7, 8, 9]]))

    def test_diagonal_sum_1(self):
        self.assertEqual(8, diagonal_sum(self, [[1, 1, 1, 1],
                                                [1, 1, 1, 1],
                                                [1, 1, 1, 1],
                                                [1, 1, 1, 1]]))

    def test_diagonal_sum_2(self):
        self.assertEqual(5, diagonal_sum(self, [[5]]))

    def test_diagonal_sum_3(self):
        self.assertEqual(55, diagonal_sum(self, [
            [7, 3, 1, 9],
            [3, 4, 6, 9],
            [6, 9, 6, 6],
            [9, 5, 8, 5]
        ]
                                         ))


if __name__ == '__main__':
    unittest.main()
