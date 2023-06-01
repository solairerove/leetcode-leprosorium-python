import unittest

from graphs.ShortestPathInBinaryMatrix import shortest_path_binary_matrix


class MyTestCase(unittest.TestCase):
    def test_shortest_path_binary_matrix(self):
        self.assertEqual(2, shortest_path_binary_matrix(self, [[0, 1], [1, 0]]))

    def test_shortest_path_binary_matrix_1(self):
        self.assertEqual(4, shortest_path_binary_matrix(self, [[0, 0, 0], [1, 1, 0], [1, 1, 0]]))

    def test_shortest_path_binary_matrix_2(self):
        self.assertEqual(-1, shortest_path_binary_matrix(self, [[1, 0, 0], [1, 1, 0], [1, 1, 0]]))


if __name__ == '__main__':
    unittest.main()
