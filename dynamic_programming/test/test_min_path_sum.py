import unittest

from dynamic_programming.MinimumPathSum import min_path_sum_rec


class MyTestCase(unittest.TestCase):
    def test_min_path_sum(self):
        self.assertEqual(7, min_path_sum_rec(self, [[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

    def test_min_path_sum_1(self):
        self.assertEqual(12, min_path_sum_rec(self, [[1, 2, 3], [4, 5, 6]]))


if __name__ == '__main__':
    unittest.main()
