import unittest

from dynamic_programming.HouseRobber import rob


class MyTestCase(unittest.TestCase):
    def test_rob(self):
        self.assertEqual(4, rob(self, [1, 2, 3, 1]))  

    def test_rob_1(self):
        self.assertEqual(12, rob(self, [2, 7, 9, 3, 1]))  


if __name__ == '__main__':
    unittest.main()
