import unittest

from graphs.LongestCycleInAGraph import longest_cycle


class MyTestCase(unittest.TestCase):
    def test_longest_cycle(self):
        self.assertEqual(3, longest_cycle(self, [3, 3, 4, 2, 3]))

    def test_longest_cycle_1(self):
        self.assertEqual(-1, longest_cycle(self, [2, -1, 3, 1]))


if __name__ == '__main__':
    unittest.main()
