import unittest

from dynamic_programming.JumpGame import can_jump_greedy, can_jump_top_down


class MyTestCase(unittest.TestCase):
    def test_can_jump(self):
        self.assertEqual(True, can_jump_greedy(self, [2, 3, 1, 1, 4]))
        self.assertEqual(True, can_jump_top_down(self, [2, 3, 1, 1, 4]))

    def test_can_jump_1(self):
        self.assertEqual(False, can_jump_greedy(self, [3, 2, 1, 0, 4]))
        self.assertEqual(False, can_jump_top_down(self, [3, 2, 1, 0, 4]))


if __name__ == '__main__':
    unittest.main()
