import unittest

from arrays.TwoSum import two_sum


class MyTestCase(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual([1, 0], two_sum(self, [2, 7, 11, 15], 9))

    def test_two_sum_1(self):
        self.assertEqual([2, 1], two_sum(self, [3, 2, 4], 6))

    def test_two_sum_2(self):
        self.assertEqual([1, 0], two_sum(self, [3, 3], 6))


if __name__ == '__main__':
    unittest.main()
