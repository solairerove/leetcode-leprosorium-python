import unittest

from graphs.ShortestPathWithAlternatingColors import shortest_alternating_paths


class MyTestCase(unittest.TestCase):
    def test_shortest_alternating_paths(self):
        self.assertEqual([0, 1, -1], shortest_alternating_paths(self, 3, [[0, 1], [1, 2]], []))

    def test_shortest_alternating_paths_1(self):
        self.assertEqual([0, 1, -1], shortest_alternating_paths(self, 3, [[0, 1]], [[2, 1]]))


if __name__ == '__main__':
    unittest.main()
