import unittest

from heap.FindTheKthLargestIntegerInTheArray import kth_largest_number_heap


class MyTestCase(unittest.TestCase):
    def test_test_kth_largest_number(self):
        self.assertEqual("3", kth_largest_number_heap(self, nums=["3", "6", "7", "10"], k=4))

    def test_test_kth_largest_number_1(self):
        self.assertEqual("2", kth_largest_number_heap(self, nums=["2", "21", "12", "1"], k=3))

    def test_test_kth_largest_number_2(self):
        self.assertEqual("0", kth_largest_number_heap(self, nums=["0", "0"], k=2))


if __name__ == '__main__':
    unittest.main()
