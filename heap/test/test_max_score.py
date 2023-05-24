import unittest

from heap.MaximumSubsequenceScore import max_score


class MyTestCase(unittest.TestCase):
    def test_max_score(self):
        self.assertEqual(12, max_score(self, nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3))

    def test_max_score_1(self):
        self.assertEqual(30, max_score(self, nums1=[4, 2, 3, 1, 1], nums2=[7, 5, 10, 9, 6], k=1))


if __name__ == '__main__':
    unittest.main()
