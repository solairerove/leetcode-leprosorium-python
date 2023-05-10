import unittest

from arrays.SpiralMatrixII import generate_matrix


class MyTestCase(unittest.TestCase):
    def test_generate_matrix(self):
        self.assertEqual([[1, 2, 3], [8, 9, 4], [7, 6, 5]], generate_matrix(self, 3))

    def test_generate_matrix_1(self):
        self.assertEqual([[1]], generate_matrix(self, 1))


if __name__ == '__main__':
    unittest.main()
