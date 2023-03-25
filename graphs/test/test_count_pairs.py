import unittest

from graphs.CountUnreachablePairsOfNodesInAnUndirectedGraph import count_pairs


class MyTestCase(unittest.TestCase):
    def test_count_pairs(self):
        self.assertEqual(0, count_pairs(self, 3, [[0, 1], [0, 2], [1, 2]]))

    def test_count_pairs_1(self):
        self.assertEqual(14, count_pairs(self, 7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))


if __name__ == '__main__':
    unittest.main()
