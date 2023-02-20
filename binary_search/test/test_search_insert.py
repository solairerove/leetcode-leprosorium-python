import unittest

from binary_search.SearchInsertPosition import search_insert


class MyTestCase(unittest.TestCase):
    def test_search_insert(self):
        self.assertEqual(2, search_insert(self, [1, 3, 5, 6], 5))

    def test_search_insert_1(self):
        self.assertEqual(1, search_insert(self, [1, 3, 5, 6], 2))

    def test_search_insert_2(self):
        self.assertEqual(4, search_insert(self, [1, 3, 5, 6], 7))

    def test_search_insert_3(self):
        self.assertEqual(0, search_insert(self, [1, 3, 5, 6], 0))


if __name__ == '__main__':
    unittest.main()
