import unittest

from dynamic_programming.UniquePathsII import unique_paths_with_obstacles


class MyTestCase(unittest.TestCase):
    def test_unique_paths_with_obstacles(self):
        self.assertEqual(2, unique_paths_with_obstacles(self, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

    def test_unique_paths_with_obstacles_1(self):
        self.assertEqual(1, unique_paths_with_obstacles(self, [[0, 1], [0, 0]]))

    def test_unique_paths_with_obstacles_2(self):
        self.assertEqual(0, unique_paths_with_obstacles(self, [[1]]))


if __name__ == '__main__':
    unittest.main()
