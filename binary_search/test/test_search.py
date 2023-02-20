import unittest

from binary_search.BinarySearch import search


class MyTestCase(unittest.TestCase):
    def test_search(self):
        self.assertEqual(4, search(self, [-1, 0, 3, 5, 9, 12], 9))

    def test_search_1(self):
        self.assertEqual(-1, search(self, [-1, 0, 3, 5, 9, 12], 2))


if __name__ == '__main__':
    unittest.main()
