import unittest

from graphs.RemoveMaxNumberOfEdgesToKeepGraphFullyTraversable import max_num_edges_to_remove


class MyTestCase(unittest.TestCase):
    def test_max_num_edges_to_remove(self):
        self.assertEqual(2, max_num_edges_to_remove(self, 4,
                                                    [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))

    def test_max_num_edges_to_remove_1(self):
        self.assertEqual(0, max_num_edges_to_remove(self, 4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))

    def test_max_num_edges_to_remove_2(self):
        self.assertEqual(-1, max_num_edges_to_remove(self, 4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]))


if __name__ == '__main__':
    unittest.main()
