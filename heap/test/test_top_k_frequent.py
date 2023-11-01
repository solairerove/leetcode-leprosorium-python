import unittest

from heap.TopKFrequentElements import top_k_frequent_heap, top_k_frequent_linear, top_k_frequent_quickselect


class MyTestCase(unittest.TestCase):
    def test_top_k_frequent(self):
        self.assertEqual([1, 2], top_k_frequent_heap(self, [1, 1, 1, 2, 2, 3], 2))
        self.assertEqual([1, 2], top_k_frequent_linear(self, [1, 1, 1, 2, 2, 3], 2))
        self.assertEqual([1, 2], top_k_frequent_quickselect(self, [1, 1, 1, 2, 2, 3], 2))

    def test_top_k_frequent_1(self):
        self.assertEqual([1], top_k_frequent_heap(self, [1], 1))
        self.assertEqual([1], top_k_frequent_linear(self, [1], 1))
        self.assertEqual([1], top_k_frequent_quickselect(self, [1], 1))


if __name__ == '__main__':
    unittest.main()
