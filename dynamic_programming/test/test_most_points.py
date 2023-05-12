import unittest

from dynamic_programming.SolvingQuestionsWithBrainpower import most_points


class MyTestCase(unittest.TestCase):
    def test_most_points(self):
        self.assertEqual(5, most_points(self, [[3, 2], [4, 3], [4, 4], [2, 5]]))

    def test_most_points_1(self):
        self.assertEqual(7, most_points(self, [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))


if __name__ == '__main__':
    unittest.main()
