import unittest

from arrays.ContainsDuplicate import contains_duplicate


class MyTestCase(unittest.TestCase):
    def test_contains_duplicate(self):
        self.assertEqual(True, contains_duplicate(self, [1, 2, 3, 1]))

    def test_contains_duplicate_1(self):
        self.assertEqual(False, contains_duplicate(self, [1, 2, 3, 4]))

    def test_contains_duplicate_2(self):
        self.assertEqual(True, contains_duplicate(self, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == '__main__':
    unittest.main()
