import unittest

from dynamic_programming.HouseRobberII import rob


class MyTestCase(unittest.TestCase):
    def test_test_rob(self):
        self.assertEqual(3, rob(self, [2, 3, 2]))  # add assertion here

    def test_test_rob_1(self):
        self.assertEqual(4, rob(self, [1, 2, 3, 1]))  # add assertion here

    def test_test_rob_2(self):
        self.assertEqual(3, rob(self, [1, 2, 3]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
