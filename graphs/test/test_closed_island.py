import unittest

from graphs.NumberOfClosedIslands import closed_island_dfs, closed_island_bfs, closed_island_union


class MyTestCase(unittest.TestCase):
    def test_closed_island(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]
        ]

        self.assertEqual(2, closed_island_dfs(self, [row[:] for row in grid]))
        self.assertEqual(2, closed_island_bfs(self, [row[:] for row in grid]))
        self.assertEqual(2, closed_island_union(self, [row[:] for row in grid]))

    def test_closed_island_1(self):
        grid = [
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0]
        ]
        self.assertEqual(1, closed_island_dfs(self, [row[:] for row in grid]))
        self.assertEqual(1, closed_island_bfs(self, [row[:] for row in grid]))
        self.assertEqual(1, closed_island_union(self, [row[:] for row in grid]))

    def test_closed_island_2(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(2, closed_island_dfs(self, [row[:] for row in grid]))
        self.assertEqual(2, closed_island_bfs(self, [row[:] for row in grid]))
        self.assertEqual(2, closed_island_union(self, [row[:] for row in grid]))

    def test_closed_island_3(self):
        grid = [
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        ]

        self.assertEqual(5, closed_island_dfs(self, [row[:] for row in grid]))
        self.assertEqual(5, closed_island_bfs(self, [row[:] for row in grid]))
        self.assertEqual(5, closed_island_union(self, [row[:] for row in grid]))


if __name__ == '__main__':
    unittest.main()
