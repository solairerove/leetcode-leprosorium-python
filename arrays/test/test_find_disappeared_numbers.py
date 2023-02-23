import unittest

from arrays.FindAllNumbersDisappearedInAnArray import find_disappeared_numbers


class MyTestCase(unittest.TestCase):
    def test_find_disappeared_numbers(self):
        self.assertEqual([5, 6], find_disappeared_numbers(self, [4, 3, 2, 7, 8, 2, 3, 1]))

    def test_find_disappeared_numbers_1(self):
        self.assertEqual([2], find_disappeared_numbers(self, [1, 1]))


if __name__ == '__main__':
    unittest.main()
