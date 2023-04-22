import unittest

from dynamic_programming.MinimumFallingPathSum import min_falling_path_sum_top_down


class MyTestCase(unittest.TestCase):
    def test_min_falling_path_sum(self):
        self.assertEqual(13, min_falling_path_sum_top_down(self, [[2, 1, 3], [6, 5, 4], [7, 8, 9]]))

    def test_min_falling_path_sum_1(self):
        self.assertEqual(-59, min_falling_path_sum_top_down(self, [[-19, 57], [-40, -5]]))


if __name__ == '__main__':
    unittest.main()
