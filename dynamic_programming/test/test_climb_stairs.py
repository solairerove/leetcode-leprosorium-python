import unittest

from dynamic_programming.ClimbingStairs import climb_stairs, climb_stairs_rec, climb_stairs_bottom_up


class MyTestCase(unittest.TestCase):
    def test_climb_stairs(self):
        self.assertEqual(2, climb_stairs(self, 2))
        self.assertEqual(2, climb_stairs_rec(self, 2))
        self.assertEqual(2, climb_stairs_bottom_up(self, 2))

    def test_climb_stairs_1(self):
        self.assertEqual(3, climb_stairs(self, 3))
        self.assertEqual(3, climb_stairs_rec(self, 3))
        self.assertEqual(3, climb_stairs_bottom_up(self, 3))

    def test_climb_stairs_2(self):
        self.assertEqual(8, climb_stairs(self, 5))
        self.assertEqual(8, climb_stairs_rec(self, 5))
        self.assertEqual(8, climb_stairs_bottom_up(self, 5))


if __name__ == '__main__':
    unittest.main()
