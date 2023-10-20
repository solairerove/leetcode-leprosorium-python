import unittest

from binary_search.SearchA2DMatrix import search_matrix, search_matrix_2bs


class MyTestCase(unittest.TestCase):
    def test_search_matrix(self):
        self.assertEqual(True, search_matrix(self, matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
        self.assertEqual(True,
                         search_matrix_2bs(self, matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))

    def test_search_matrix_1(self):
        self.assertEqual(False,
                         search_matrix(self, matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
        self.assertEqual(False,
                         search_matrix_2bs(self, matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))


if __name__ == '__main__':
    unittest.main()
