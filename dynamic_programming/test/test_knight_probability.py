import unittest

from dynamic_programming.KnightProbabilityInChessboard import knight_probability_bfs


class MyTestCase(unittest.TestCase):
    def test_knight_probability(self):
        self.assertEqual(0.06250, knight_probability_bfs(self, n=3, k=2, row=0, column=0))

    def test_knight_probability_1(self):
        self.assertEqual(1.00000, knight_probability_bfs(self, n=1, k=0, row=0, column=0))


if __name__ == '__main__':
    unittest.main()
