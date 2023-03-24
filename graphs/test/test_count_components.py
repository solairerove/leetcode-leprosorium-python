import unittest

from graphs.NumberOfConnectedComponentsInAnUndirectedGraph import count_components_dfs


class MyTestCase(unittest.TestCase):
    def test_count_components(self):
        self.assertEqual(2, count_components_dfs(self, 5, [[0, 1], [1, 2], [3, 4]]))

    def test_count_components_1(self):
        self.assertEqual(1, count_components_dfs(self, 5, [[0, 1], [1, 2], [2, 3], [3, 4]]))


if __name__ == '__main__':
    unittest.main()
