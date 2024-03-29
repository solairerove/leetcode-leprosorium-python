import unittest

from dynamic_programming.HouseRobberII import rob, rob_top_down


class MyTestCase(unittest.TestCase):
    def test_rob(self):
        self.assertEqual(3, rob(self, [2, 3, 2]))
        self.assertEqual(3, rob_top_down(self, [2, 3, 2]))

    def test_rob_1(self):
        self.assertEqual(4, rob(self, [1, 2, 3, 1]))
        self.assertEqual(4, rob_top_down(self, [1, 2, 3, 1]))

    def test_rob_2(self):
        self.assertEqual(3, rob(self, [1, 2, 3]))
        self.assertEqual(3, rob_top_down(self, [1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
