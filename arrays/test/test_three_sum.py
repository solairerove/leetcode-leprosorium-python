import unittest

from arrays.ThreeSum import three_sum


class MyTestCase(unittest.TestCase):
    def test_three_sum(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], three_sum(self, [-1, 0, 1, 2, -1, -4]))

    def test_three_sum_1(self):
        self.assertEqual([], three_sum(self, [0, 1, 1]))

    def test_three_sum_2(self):
        self.assertEqual([[0, 0, 0]], three_sum(self, [0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
