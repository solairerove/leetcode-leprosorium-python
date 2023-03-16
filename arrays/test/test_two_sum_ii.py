import unittest

from arrays.TwoSumII import two_sum


class MyTestCase(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual([1, 2], two_sum(self, [2, 7, 11, 15], 9))

    def test_two_sum_1(self):
        self.assertEqual([1, 3], two_sum(self, [2, 3, 4], 6))

    def test_two_sum_2(self):
        self.assertEqual([1, 2], two_sum(self, [-1, 0], -1))


if __name__ == '__main__':
    unittest.main()
