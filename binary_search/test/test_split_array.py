import unittest

from binary_search.SplitArrayLargestSum import split_array_top_down, split_array_bs


class MyTestCase(unittest.TestCase):
    def test_split_array(self):
        # self.assertEqual(18, split_array_top_down(self, [7, 2, 5, 10, 8], 2))
        self.assertEqual(18, split_array_bs(self, [7, 2, 5, 10, 8], 2))

    def test_split_array_1(self):
        # self.assertEqual(9, split_array_top_down(self, [1, 2, 3, 4, 5], 2))
        self.assertEqual(9, split_array_bs(self, [1, 2, 3, 4, 5], 2))


if __name__ == '__main__':
    unittest.main()
