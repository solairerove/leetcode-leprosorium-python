import unittest

from heap.SmallestNumberInInfiniteSet import SmallestInfiniteSet


class MyTestCase(unittest.TestCase):
    def test_pop_smallest(self):
        smallest_infinite_set = SmallestInfiniteSet()
        smallest_infinite_set.add_back(2)
        self.assertEqual(1, smallest_infinite_set.pop_smallest())
        self.assertEqual(2, smallest_infinite_set.pop_smallest())
        self.assertEqual(3, smallest_infinite_set.pop_smallest())
        smallest_infinite_set.add_back(1)
        self.assertEqual(1, smallest_infinite_set.pop_smallest())
        self.assertEqual(4, smallest_infinite_set.pop_smallest())
        self.assertEqual(5, smallest_infinite_set.pop_smallest())


if __name__ == '__main__':
    unittest.main()
