import unittest

from graphs.MinimumNumberOfVerticesToReachAllNodes import find_smallest_set_of_vertices


class MyTestCase(unittest.TestCase):
    def test_find_smallest_set_of_vertices(self):
        self.assertEqual([0, 3], find_smallest_set_of_vertices(self, 6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))

    def test_find_smallest_set_of_vertices_1(self):
        self.assertEqual([0, 2, 3], find_smallest_set_of_vertices(self, 5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))


if __name__ == '__main__':
    unittest.main()
