import unittest

from graphs.SimilarStringGroups import num_similar_groups_bfs, num_similar_groups_dfs


class MyTestCase(unittest.TestCase):
    def test_num_similar_groups(self):
        self.assertEqual(2, num_similar_groups_bfs(self, ["tars", "rats", "arts", "star"]))
        self.assertEqual(2, num_similar_groups_dfs(self, ["tars", "rats", "arts", "star"]))

    def test_num_similar_groups_1(self):
        self.assertEqual(1, num_similar_groups_bfs(self, ["omv", "ovm"]))
        self.assertEqual(1, num_similar_groups_dfs(self, ["omv", "ovm"]))


if __name__ == '__main__':
    unittest.main()
