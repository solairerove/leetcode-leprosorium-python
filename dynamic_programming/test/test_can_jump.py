import unittest

from dynamic_programming.JumpGame import can_jump_greedy


class MyTestCase(unittest.TestCase):
    def test_can_jump(self):
        self.assertEqual(True, can_jump_greedy(self, [2, 3, 1, 1, 4]))

    def test_can_jump_1(self):
        self.assertEqual(False, can_jump_greedy(self, [3, 2, 1, 0, 4]))

    def test_can_jump_2(self):
        self.assertEqual(True, can_jump_greedy(self, [2, 0]))

    def test_can_jump_3(self):
        self.assertEqual(True, can_jump_greedy(self, [2, 5, 0, 0]))

    def test_can_jump_4(self):
        self.assertEqual(True, can_jump_greedy(self, [3, 0, 8, 2, 0, 0, 1]))


if __name__ == '__main__':
    unittest.main()
