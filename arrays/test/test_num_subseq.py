import unittest

from arrays.NumberOfSubsequencesThatSatisfyTheGivenSumCondition import num_subseq


class MyTestCase(unittest.TestCase):
    def test_num_subseq(self):
        self.assertEqual(4, num_subseq(self, [3, 5, 6, 7], 9))

    def test_num_subseq_1(self):
        self.assertEqual(6, num_subseq(self, [3, 3, 6, 8], 10))


if __name__ == '__main__':
    unittest.main()
