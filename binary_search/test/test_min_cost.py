import unittest

from binary_search.MinimumCostToMakeArrayEqual import min_cost


class MyTestCase(unittest.TestCase):
    def test_min_cost(self):
        self.assertEqual(8, min_cost(self, nums=[1, 3, 5, 2], cost=[2, 3, 1, 14]))

    def test_min_cost_1(self):
        self.assertEqual(0, min_cost(self, nums=[2, 2, 2, 2, 2], cost=[4, 2, 8, 1, 3]))


if __name__ == '__main__':
    unittest.main()
