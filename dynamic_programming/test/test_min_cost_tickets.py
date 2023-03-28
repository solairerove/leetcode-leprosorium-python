import unittest

from dynamic_programming.MinimumCostForTickets import min_cost_tickets_all_days, min_cost_tickets_window, \
    min_cost_tickets_bottom_up


class MyTestCase(unittest.TestCase):
    def test_min_cost_tickets(self):
        self.assertEqual(11, min_cost_tickets_all_days(self, [1, 4, 6, 7, 8, 20], [2, 7, 15]))
        self.assertEqual(11, min_cost_tickets_window(self, [1, 4, 6, 7, 8, 20], [2, 7, 15]))
        self.assertEqual(11, min_cost_tickets_bottom_up(self, [1, 4, 6, 7, 8, 20], [2, 7, 15]))

    def test_min_cost_tickets_1(self):
        self.assertEqual(17, min_cost_tickets_all_days(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
        self.assertEqual(17, min_cost_tickets_window(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
        self.assertEqual(17, min_cost_tickets_bottom_up(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))


if __name__ == '__main__':
    unittest.main()
