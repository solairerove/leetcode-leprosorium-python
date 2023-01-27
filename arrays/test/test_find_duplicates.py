import unittest

from arrays.FindAllDuplicatesInAnArray import find_duplicates


class MyTestCase(unittest.TestCase):
    def test_find_duplicates(self):
        self.assertEqual([2, 3], find_duplicates(self, [4, 3, 2, 7, 8, 2, 3, 1]))

    def test_find_duplicates_1(self):
        self.assertEqual([1], find_duplicates(self, [1, 1, 2]))

    def test_find_duplicates_2(self):
        self.assertEqual([], find_duplicates(self, [1]))


if __name__ == '__main__':
    unittest.main()
