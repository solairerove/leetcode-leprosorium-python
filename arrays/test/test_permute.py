import unittest

from arrays.Permutations import permute


class MyTestCase(unittest.TestCase):
    def test_permute(self):
        self.assertEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], permute(self, [1, 2, 3]))

    def test_permute_1(self):
        self.assertEqual([[0, 1], [1, 0]], permute(self, [0, 1]))

    def test_permute_2(self):
        self.assertEqual([[1]], permute(self, [1]))


if __name__ == '__main__':
    unittest.main()
