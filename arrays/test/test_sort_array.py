import unittest

from arrays.SortAnArray import sort_array


class MyTestCase(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual([1, 2, 3, 5], sort_array(self, [5, 2, 3, 1]))

    def test_sort_array_1(self):
        self.assertEqual([0, 0, 1, 1, 2, 5], sort_array(self, [5, 1, 1, 2, 0, 0]))


if __name__ == '__main__':
    unittest.main()
