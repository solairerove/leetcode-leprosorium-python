import unittest

from arrays.FourSum import four_sum


class MyTestCase(unittest.TestCase):
    def test_four_sum(self):
        self.assertEqual([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
                         four_sum(self, nums=[1, 0, -1, 0, -2, 2], target=0))

    def test_four_sum_1(self):
        self.assertEqual([[2, 2, 2, 2]], four_sum(self, nums=[2, 2, 2, 2, 2], target=8))


if __name__ == '__main__':
    unittest.main()
