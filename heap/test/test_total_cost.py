import unittest

from heap.TotalCostToHireKWorkers import total_cost


class MyTestCase(unittest.TestCase):
    def test_total_cost(self):
        self.assertEqual(11, total_cost(self, costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))

    def test_total_cost_1(self):
        self.assertEqual(4, total_cost(self, costs=[1, 2, 4, 1], k=3, candidates=3))


if __name__ == '__main__':
    unittest.main()
