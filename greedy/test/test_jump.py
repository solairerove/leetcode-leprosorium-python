import unittest

from greedy.JumpGameII import jump, jump_bottom_up


class MyTestCase(unittest.TestCase):
    def test_jump(self):
        self.assertEqual(2, jump(self, [2, 3, 1, 1, 4]))
        self.assertEqual(2, jump_bottom_up(self, [2, 3, 1, 1, 4]))

    def test_jump_1(self):
        self.assertEqual(2, jump(self, [2, 3, 0, 1, 4]))
        self.assertEqual(2, jump_bottom_up(self, [2, 3, 0, 1, 4]))


if __name__ == '__main__':
    unittest.main()
