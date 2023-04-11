import unittest

from dynamic_programming.MinCostClimbingStairs import min_cost_climbing_stairs, min_cost_climbing_stairs_top_down, \
    min_cost_climbing_stairs_bottom_up


class MyTestCase(unittest.TestCase):
    def test_min_cost_climbing_stairs(self):
        self.assertEqual(15, min_cost_climbing_stairs(self, [10, 15, 20]))
        self.assertEqual(15, min_cost_climbing_stairs_top_down(self, [10, 15, 20]))
        self.assertEqual(15, min_cost_climbing_stairs_bottom_up(self, [10, 15, 20]))

    def test_min_cost_climbing_stairs_1(self):
        self.assertEqual(6, min_cost_climbing_stairs(self, [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
        self.assertEqual(6, min_cost_climbing_stairs_top_down(self, [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
        self.assertEqual(6, min_cost_climbing_stairs_bottom_up(self, [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


if __name__ == '__main__':
    unittest.main()
