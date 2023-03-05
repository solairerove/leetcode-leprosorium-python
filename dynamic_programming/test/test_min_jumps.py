import unittest

from dynamic_programming.JumpGameIV import min_jumps


class MyTestCase(unittest.TestCase):
    def test_min_jumps(self):
        self.assertEqual(3, min_jumps(self, [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))

    def test_min_jumps_1(self):
        self.assertEqual(0, min_jumps(self, [0]))

    def test_min_jumps_2(self):
        self.assertEqual(1, min_jumps(self, [7, 6, 9, 6, 9, 6, 9, 7]))


if __name__ == '__main__':
    unittest.main()
