import unittest

from linked_list.FindTheDuplicateNumber import find_duplicate


class MyTestCase(unittest.TestCase):
    def test_find_duplicate(self):
        self.assertEqual(2, find_duplicate(self, [1, 3, 4, 2, 2]))  # add assertion here

    def test_find_duplicate_1(self):
        self.assertEqual(3, find_duplicate(self, [3, 1, 3, 4, 2]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
