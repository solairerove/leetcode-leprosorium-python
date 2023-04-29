import unittest

from graphs.CheckingExistenceOfEdgeLengthLimitedPaths import distance_limited_paths_exist


class MyTestCase(unittest.TestCase):
    def test_distance_limited_paths_exist(self):
        self.assertEqual([False, True],
                         distance_limited_paths_exist(self, 3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
                                                      [[0, 1, 2], [0, 2, 5]]))

    def test_distance_limited_paths_exist_1(self):
        self.assertEqual([True, False],
                         distance_limited_paths_exist(self, 5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
                                                      [[0, 4, 14], [1, 4, 13]]))


if __name__ == '__main__':
    unittest.main()
