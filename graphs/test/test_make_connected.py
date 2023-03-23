import unittest

from graphs.NumberOfOperationsToMakeNetworkConnected import make_connected_dfs, make_connected_bfs


class MyTestCase(unittest.TestCase):
    def test_make_connected(self):
        self.assertEqual(1, make_connected_dfs(self, 4, [[0, 1], [0, 2], [1, 2]]))
        self.assertEqual(1, make_connected_bfs(self, 4, [[0, 1], [0, 2], [1, 2]]))

    def test_make_connected_1(self):
        self.assertEqual(2, make_connected_dfs(self, 6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
        self.assertEqual(2, make_connected_bfs(self, 6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))

    def test_make_connected_2(self):
        self.assertEqual(-1, make_connected_dfs(self, 6, [[0, 1], [0, 2], [0, 3], [1, 2]]))
        self.assertEqual(-1, make_connected_bfs(self, 6, [[0, 1], [0, 2], [0, 3], [1, 2]]))


if __name__ == '__main__':
    unittest.main()
