import unittest

from graphs.NumberOfEnclaves import num_enclaves


class MyTestCase(unittest.TestCase):
    def test_num_enclaves(self):
        grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

        self.assertEqual(3, num_enclaves(self, [row[:] for row in grid]))

    def test_num_enclaves_1(self):
        grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]

        self.assertEqual(0, num_enclaves(self, [row[:] for row in grid]))


if __name__ == '__main__':
    unittest.main()
