import unittest

from dynamic_programming.NumberOfIncreasingPathsInAGrid import count_paths


class MyTestCase(unittest.TestCase):
    def test_count_paths(self):
        self.assertEqual(8, count_paths(self, [[1, 1], [3, 4]]))

    def test_count_paths_1(self):
        self.assertEqual(3, count_paths(self, [[1], [2]]))


if __name__ == '__main__':
    unittest.main()
