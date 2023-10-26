import unittest

from graphs.NumberOfIslands import num_islands_dfs, num_islands_dfs_shorter, num_islands_bfs


class MyTestCase(unittest.TestCase):
    def test_num_islands(self):
        self.assertEqual(1, num_islands_dfs(self, [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]))

        self.assertEqual(1, num_islands_dfs_shorter(self, [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]))

        self.assertEqual(1, num_islands_bfs(self, [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]))

    def test_num_islands_1(self):
        self.assertEqual(3, num_islands_dfs(self, [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]))

        self.assertEqual(3, num_islands_dfs_shorter(self, [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]))

        self.assertEqual(3, num_islands_bfs(self, [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]))


if __name__ == '__main__':
    unittest.main()
