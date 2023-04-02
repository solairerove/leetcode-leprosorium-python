import unittest

from dynamic_programming.JumpGame import can_jump


class MyTestCase(unittest.TestCase):
    def test_can_jump(self):
        self.assertEqual(True, can_jump(self, [2, 3, 1, 1, 4]))

    def test_can_jump_1(self):
        self.assertEqual(False, can_jump(self, [3, 2, 1, 0, 4]))


if __name__ == '__main__':
    unittest.main()
