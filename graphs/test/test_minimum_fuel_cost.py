import unittest

from graphs.MinimumFuelCostToReportToTheCapital import minimum_fuel_cost_dfs, minimum_fuel_cost_bfs


class MyTestCase(unittest.TestCase):
    def test_minimum_fuel_cost(self):
        self.assertEqual(3, minimum_fuel_cost_dfs(self, [[0, 1], [0, 2], [0, 3]], 5))
        self.assertEqual(3, minimum_fuel_cost_bfs(self, [[0, 1], [0, 2], [0, 3]], 5))

    def test_minimum_fuel_cost_1(self):
        self.assertEqual(7, minimum_fuel_cost_dfs(self, [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2))
        self.assertEqual(7, minimum_fuel_cost_bfs(self, [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2))

    def test_minimum_fuel_cost_2(self):
        self.assertEqual(0, minimum_fuel_cost_dfs(self, [], 1))
        self.assertEqual(0, minimum_fuel_cost_bfs(self, [], 1))


if __name__ == '__main__':
    unittest.main()
