import unittest

from dynamic_programming.ReducingDishes import max_satisfaction, max_satisfaction_greedy


class MyTestCase(unittest.TestCase):
    def test_max_satisfaction(self):
        self.assertEqual(14, max_satisfaction(self, [-1, -8, 0, 5, -9]))
        self.assertEqual(14, max_satisfaction_greedy(self, [-1, -8, 0, 5, -9]))

    def test_max_satisfaction_1(self):
        self.assertEqual(20, max_satisfaction(self, [4, 3, 2]))
        self.assertEqual(20, max_satisfaction_greedy(self, [4, 3, 2]))


if __name__ == '__main__':
    unittest.main()
