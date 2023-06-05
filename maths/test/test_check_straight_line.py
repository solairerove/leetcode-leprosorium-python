import unittest

from maths.CheckIfItIsAStraightLine import check_straight_line


class MyTestCase(unittest.TestCase):
    def test_check_straight_line(self):
        self.assertEqual(True, check_straight_line(self, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))

    def test_check_straight_line_1(self):
        self.assertEqual(False, check_straight_line(self, [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))


if __name__ == '__main__':
    unittest.main()
