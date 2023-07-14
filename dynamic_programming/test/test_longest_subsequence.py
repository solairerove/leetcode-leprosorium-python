import unittest

from dynamic_programming.LongestArithmeticSubsequenceOfGivenDifference import longest_subsequence


class MyTestCase(unittest.TestCase):
    def test_longest_subsequence(self):
        self.assertEqual(4, longest_subsequence(self, arr=[1, 2, 3, 4], difference=1))

    def test_longest_subsequence_1(self):
        self.assertEqual(1, longest_subsequence(self, arr=[1, 3, 5, 7], difference=1))

    def test_longest_subsequence_2(self):
        self.assertEqual(4, longest_subsequence(self, arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))


if __name__ == '__main__':
    unittest.main()
