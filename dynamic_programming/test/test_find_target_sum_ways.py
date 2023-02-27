import unittest

from dynamic_programming.TargetSum import find_target_sum_ways, find_target_sum_ways_top_down


class MyTestCase(unittest.TestCase):
    def test_find_target_sum_ways(self):
        self.assertEqual(5, find_target_sum_ways(self, [1, 1, 1, 1, 1], 3))
        self.assertEqual(5, find_target_sum_ways_top_down(self, [1, 1, 1, 1, 1], 3))

    def test_find_target_sum_ways_1(self):
        self.assertEqual(1, find_target_sum_ways(self, [1], 1))
        self.assertEqual(1, find_target_sum_ways_top_down(self, [1], 1))


if __name__ == '__main__':
    unittest.main()
