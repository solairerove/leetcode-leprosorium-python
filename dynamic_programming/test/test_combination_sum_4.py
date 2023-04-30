import unittest

from dynamic_programming.CombinationSumIV import combination_sum_4_top_down, combination_sum_4_bottom_up


class MyTestCase(unittest.TestCase):
    def test_combination_sum_4(self):
        self.assertEqual(7, combination_sum_4_top_down(self, [1, 2, 3], 4))
        self.assertEqual(7, combination_sum_4_bottom_up(self, [1, 2, 3], 4))

    def test_combination_sum_4_1(self):
        self.assertEqual(0, combination_sum_4_top_down(self, [9], 3))
        self.assertEqual(0, combination_sum_4_bottom_up(self, [9], 3))


if __name__ == '__main__':
    unittest.main()
