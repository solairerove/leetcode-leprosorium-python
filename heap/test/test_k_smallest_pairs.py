import unittest

from heap.FindKPairsWithSmallestSums import k_smallest_pairs


class MyTestCase(unittest.TestCase):
    def test_k_smallest_pairs(self):
        self.assertEqual([[1, 2], [1, 4], [1, 6]], k_smallest_pairs(self, nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))

    def test_k_smallest_pairs_1(self):
        self.assertEqual([[1, 1], [1, 1]], k_smallest_pairs(self, nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))

    def test_k_smallest_pairs_2(self):
        self.assertEqual([[1, 3], [2, 3]], k_smallest_pairs(self, nums1=[1, 2], nums2=[3], k=3))


if __name__ == '__main__':
    unittest.main()
