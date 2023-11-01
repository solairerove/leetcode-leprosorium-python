import unittest

from heap.KthLargestElementInAnArray import find_kth_largest, find_kth_largest_heap


class MyTestCase(unittest.TestCase):
    def test_find_kth_largest(self):
        self.assertEqual(5, find_kth_largest(self, [3, 2, 1, 5, 6, 4], 2))
        self.assertEqual(5, find_kth_largest_heap(self, [3, 2, 1, 5, 6, 4], 2))

    def test_find_kth_largest_1(self):
        self.assertEqual(4, find_kth_largest(self, [3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
        self.assertEqual(4, find_kth_largest_heap(self, [3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


if __name__ == '__main__':
    unittest.main()
