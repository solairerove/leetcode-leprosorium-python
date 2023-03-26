import unittest

from graphs.LongestCycleInAGraph import longest_cycle_dfs, longest_cycle_kahn


class MyTestCase(unittest.TestCase):
    def test_longest_cycle(self):
        self.assertEqual(3, longest_cycle_dfs(self, [3, 3, 4, 2, 3]))
        self.assertEqual(3, longest_cycle_kahn(self, [3, 3, 4, 2, 3]))

    def test_longest_cycle_1(self):
        self.assertEqual(-1, longest_cycle_dfs(self, [2, -1, 3, 1]))
        self.assertEqual(-1, longest_cycle_kahn(self, [2, -1, 3, 1]))


if __name__ == '__main__':
    unittest.main()
