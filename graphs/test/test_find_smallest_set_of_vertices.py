import unittest

from graphs.MinimumNumberOfVerticesToReachAllNodes import find_smallest_set_of_vertices_bfs, \
    find_smallest_set_of_vertices_dfs, find_smallest_set_of_vertices


class MyTestCase(unittest.TestCase):
    def test_find_smallest_set_of_vertices(self):
        self.assertEqual([0, 3], find_smallest_set_of_vertices(self, 6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
        self.assertEqual([0, 3], find_smallest_set_of_vertices_dfs(self, 6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
        self.assertEqual([0, 3], find_smallest_set_of_vertices_bfs(self, 6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))

    def test_find_smallest_set_of_vertices_1(self):
        self.assertEqual([0, 2, 3], find_smallest_set_of_vertices(self, 5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
        self.assertEqual([0, 2, 3], find_smallest_set_of_vertices_dfs(self, 5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
        self.assertEqual([0, 2, 3], find_smallest_set_of_vertices_bfs(self, 5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))

    def test_find_smallest_set_of_vertices_2(self):
        self.assertEqual([1], find_smallest_set_of_vertices(self, 3, [[1, 2], [1, 0], [0, 2]]))
        self.assertEqual([1], find_smallest_set_of_vertices_dfs(self, 3, [[1, 2], [1, 0], [0, 2]]))
        self.assertEqual([1], find_smallest_set_of_vertices_bfs(self, 3, [[1, 2], [1, 0], [0, 2]]))


if __name__ == '__main__':
    unittest.main()
