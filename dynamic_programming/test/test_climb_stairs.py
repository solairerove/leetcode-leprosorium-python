import unittest

from dynamic_programming.ClimbingStairs import climb_stairs


class MyTestCase(unittest.TestCase):
    def test_climb_stairs(self):
        self.assertEqual(2, climb_stairs(self, 2))  # add assertion here

    def test_climb_stairs_1(self):
        self.assertEqual(3, climb_stairs(self, 3))  # add assertion here


if __name__ == '__main__':
    unittest.main()