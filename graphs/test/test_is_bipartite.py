import unittest

from graphs.IsGraphBipartite import is_bipartite


class MyTestCase(unittest.TestCase):
    def test_is_bipartite(self):
        self.assertEqual(False, is_bipartite(self, [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))

    def test_is_bipartite_1(self):
        self.assertEqual(True, is_bipartite(self, [[1, 3], [0, 2], [1, 3], [0, 2]]))


if __name__ == '__main__':
    unittest.main()
