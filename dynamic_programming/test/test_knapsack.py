import unittest

from dynamic_programming.KnapsackProblem import knapsack_recursion


class MyTestCase(unittest.TestCase):
    def test_knapsack(self):
        self.assertEqual(3, knapsack_recursion(self, [1, 2, 3], [4, 5, 1], 3, 4))

    def test_knapsack_1(self):
        self.assertEqual(0, knapsack_recursion(self, [1, 2, 3], [4, 5, 6], 3, 3))

    def test_knapsack_2(self):
        self.assertEqual(220, knapsack_recursion(self, [60, 100, 120], [10, 20, 30], 3, 50))

    def test_knapsack_3(self):
        self.assertEqual(5, knapsack_recursion(self, [2, 3, 1, 4], [3, 4, 6, 5], 4, 8))


if __name__ == '__main__':
    unittest.main()
