import unittest

from arrays.MissingNumber import missing_number


class MyTestCase(unittest.TestCase):
    def test_missing_number(self):
        self.assertEqual(2, missing_number(self, [3, 0, 1]))

    def test_missing_number_1(self):
        self.assertEqual(2, missing_number(self, [0, 1]))

    def test_missing_number_2(self):
        self.assertEqual(8, missing_number(self, [9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == '__main__':
    unittest.main()
