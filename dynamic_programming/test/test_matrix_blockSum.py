import unittest

from dynamic_programming.MatrixBlockSum import matrix_block_sum


class MyTestCase(unittest.TestCase):
    def test_matrix_block_sum(self):
        self.assertEqual([[12, 21, 16], [27, 45, 33], [24, 39, 28]],
                         matrix_block_sum(self, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))

    def test_matrix_block_sum_1(self):
        self.assertEqual([[45, 45, 45], [45, 45, 45], [45, 45, 45]],
                         matrix_block_sum(self, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))


if __name__ == '__main__':
    unittest.main()
