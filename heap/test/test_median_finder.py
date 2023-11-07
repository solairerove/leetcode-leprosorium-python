import unittest

from heap.FindMedianFromDataStream import MedianFinder


class MyTestCase(unittest.TestCase):
    def test_median_finder(self):
        median_finder = MedianFinder()
        median_finder.add_num(1)  # arr = [1]
        median_finder.add_num(2)  # arr = [1, 2]
        self.assertEqual(1.5, median_finder.find_median())  # return 1.5 (i.e., (1 + 2) / 2)
        median_finder.add_num(3)  # arr[1, 2, 3]
        self.assertEqual(2.0, median_finder.find_median())  # return 2.0


if __name__ == '__main__':
    unittest.main()
