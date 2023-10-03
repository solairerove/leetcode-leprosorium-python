import unittest

from arrays.NumberOfGoodPairs import num_identical_pairs


class MyTestCase(unittest.TestCase):
    def test_num_identical_pairs(self):
        self.assertEqual(4, num_identical_pairs(self, [1, 2, 3, 1, 1, 3]))

    def test_num_identical_pairs_1(self):
        self.assertEqual(6, num_identical_pairs(self, [1, 1, 1, 1]))

    def test_num_identical_pairs_2(self):
        self.assertEqual(0, num_identical_pairs(self, [1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
