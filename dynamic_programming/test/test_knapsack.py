import unittest

from dynamic_programming.KnapsackProblem import knapsack_top_down, knapsack_bottom_up, knapsack_1d_dp


class MyTestCase(unittest.TestCase):
    def test_knapsack(self):
        self.assertEqual(3, knapsack_top_down(self, [1, 2, 3], [4, 5, 1], 3, 4))
        self.assertEqual(3, knapsack_bottom_up(self, [1, 2, 3], [4, 5, 1], 3, 4))
        self.assertEqual(3, knapsack_1d_dp(self, [1, 2, 3], [4, 5, 1], 3, 4))

    def test_knapsack_1(self):
        self.assertEqual(0, knapsack_top_down(self, [1, 2, 3], [4, 5, 6], 3, 3))
        self.assertEqual(0, knapsack_bottom_up(self, [1, 2, 3], [4, 5, 6], 3, 3))
        self.assertEqual(0, knapsack_1d_dp(self, [1, 2, 3], [4, 5, 6], 3, 3))

    def test_knapsack_2(self):
        self.assertEqual(220, knapsack_top_down(self, [60, 100, 120], [10, 20, 30], 3, 50))
        self.assertEqual(220, knapsack_bottom_up(self, [60, 100, 120], [10, 20, 30], 3, 50))
        self.assertEqual(220, knapsack_1d_dp(self, [60, 100, 120], [10, 20, 30], 3, 50))

    def test_knapsack_3(self):
        self.assertEqual(6, knapsack_top_down(self, [2, 3, 1, 4], [3, 4, 6, 5], 4, 8))
        self.assertEqual(6, knapsack_bottom_up(self, [2, 3, 1, 4], [3, 4, 6, 5], 4, 8))
        self.assertEqual(6, knapsack_1d_dp(self, [2, 3, 1, 4], [3, 4, 6, 5], 4, 8))

    def test_knapsack_4(self):
        self.assertEqual(3500, knapsack_top_down(self, [3000, 2000, 1500], [4, 3, 1], 3, 4))
        self.assertEqual(3500, knapsack_bottom_up(self, [3000, 2000, 1500], [4, 3, 1], 3, 4))
        self.assertEqual(3500, knapsack_1d_dp(self, [3000, 2000, 1500], [4, 3, 1], 3, 4))

    def test_knapsack_5(self):
        self.assertEqual(4000, knapsack_top_down(self, [3000, 2000, 1500, 2000], [4, 3, 1, 1], 4, 4))
        self.assertEqual(4000, knapsack_bottom_up(self, [3000, 2000, 1500, 2000], [4, 3, 1, 1], 4, 4))
        self.assertEqual(4000, knapsack_1d_dp(self, [3000, 2000, 1500, 2000], [4, 3, 1, 1], 4, 4))


if __name__ == '__main__':
    unittest.main()
