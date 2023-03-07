import unittest

from arrays.TopKFrequentElements import top_k_frequent


class MyTestCase(unittest.TestCase):
    def test_top_k_frequent(self):
        self.assertEqual([1, 2], top_k_frequent(self, [1,1,1,2,2,3], 2))

    def test_top_k_frequent_1(self):
        self.assertEqual([1], top_k_frequent(self, [1], 2))


if __name__ == '__main__':
    unittest.main()
