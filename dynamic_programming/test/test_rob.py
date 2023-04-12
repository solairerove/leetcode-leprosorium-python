import unittest

from dynamic_programming.HouseRobber import rob, rob_top_down, rob_bottom_up


class MyTestCase(unittest.TestCase):
    def test_rob(self):
        self.assertEqual(4, rob(self, [1, 2, 3, 1]))
        self.assertEqual(4, rob_top_down(self, [1, 2, 3, 1]))
        self.assertEqual(4, rob_bottom_up(self, [1, 2, 3, 1]))

    def test_rob_1(self):
        self.assertEqual(12, rob(self, [2, 7, 9, 3, 1]))
        self.assertEqual(12, rob_top_down(self, [2, 7, 9, 3, 1]))
        self.assertEqual(12, rob_bottom_up(self, [2, 7, 9, 3, 1]))


if __name__ == '__main__':
    unittest.main()
