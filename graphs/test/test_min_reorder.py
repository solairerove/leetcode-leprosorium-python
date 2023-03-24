import unittest

from graphs.ReorderRoutesToMakeAllPathsLeadToTheCityZero import min_reorder_dfs


class MyTestCase(unittest.TestCase):
    def test_min_reorder(self):
        self.assertEqual(3, min_reorder_dfs(self, 6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))

    def test_min_reorder_1(self):
        self.assertEqual(2, min_reorder_dfs(self, 5, [[1, 0], [1, 2], [3, 2], [3, 4]]))

    def test_min_reorder_2(self):
        self.assertEqual(0, min_reorder_dfs(self, 3, [[1, 0], [2, 0]]))


if __name__ == '__main__':
    unittest.main()
