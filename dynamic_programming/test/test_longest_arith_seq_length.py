import unittest

from dynamic_programming.LongestArithmeticSubsequence import longest_arith_seq_length


class MyTestCase(unittest.TestCase):
    def test_longest_arith_seq_length(self):
        self.assertEqual(4, longest_arith_seq_length(self, [3, 6, 9, 12]))

    def test_longest_arith_seq_length_1(self):
        self.assertEqual(3, longest_arith_seq_length(self, [9, 4, 7, 2, 10]))


if __name__ == '__main__':
    unittest.main()
