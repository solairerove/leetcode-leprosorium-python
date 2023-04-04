import unittest

from dynamic_programming.JumpGameII import jump


class MyTestCase(unittest.TestCase):
    def test_jump(self):
        self.assertEqual(2, jump(self, [2, 3, 1, 1, 4]))

    def test_jump_1(self):
        self.assertEqual(2, jump(self, [2, 3, 0, 1, 4]))


if __name__ == '__main__':
    unittest.main()
