import unittest

from graphs.NumberOfClosedIslands import closed_island_dfs


class MyTestCase(unittest.TestCase):
    def test_closed_island(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]
        ]
        self.assertEqual(2, closed_island_dfs(self, grid))

    def test_closed_island_1(self):
        grid = [
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0]
        ]
        self.assertEqual(1, closed_island_dfs(self, grid))

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
        self.assertEqual(2, closed_island_dfs(self, grid))


if __name__ == '__main__':
    unittest.main()
