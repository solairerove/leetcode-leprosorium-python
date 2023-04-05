import unittest

from arrays.JumpGameIII import can_reach


class MyTestCase(unittest.TestCase):
    def test_can_reach(self):
        self.assertEqual(True, can_reach(self, [4, 2, 3, 0, 3, 1, 2], 5))

    def test_can_reach_1(self):
        self.assertEqual(True, can_reach(self, [4, 2, 3, 0, 3, 1, 2], 0))


if __name__ == '__main__':
    unittest.main()
