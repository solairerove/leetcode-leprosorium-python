import unittest

from dynamic_programming.TrappingRainWater import trap


class MyTestCase(unittest.TestCase):
    def test_trap(self):
        self.assertEqual(6, trap(self, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_trap_1(self):
        self.assertEqual(9, trap(self, [4, 2, 0, 3, 2, 5]))


if __name__ == '__main__':
    unittest.main()
