import unittest

from greedy.EqualSumArraysWithMinimumNumberOfOperations import min_operations


class MyTestCase(unittest.TestCase):
    def test_min_operations(self):
        self.assertEqual(3, min_operations(self, [1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 2, 2]))

    def test_min_operations_1(self):
        self.assertEqual(-1, min_operations(self, [1, 1, 1, 1, 1, 1, 1], [6]))

    def test_min_operations_2(self):
        self.assertEqual(3, min_operations(self, [6, 6], [1]))

    def test_min_operations_3(self):
        self.assertEqual(8, min_operations(self, [3, 3, 2, 4, 2, 6, 2], [6, 2, 6, 6, 1, 1, 4, 6, 4, 6, 2, 5, 4, 2, 1]))


if __name__ == '__main__':
    unittest.main()
