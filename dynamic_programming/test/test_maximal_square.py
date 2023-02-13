import unittest

from dynamic_programming.MaximalSquare import maximal_square


class MyTestCase(unittest.TestCase):
    def test_maximal_square(self):
        self.assertEqual(4, maximal_square(self, [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                                                  ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))

    def test_maximal_square_1(self):
        self.assertEqual(1, maximal_square(self, [["0", "1"], ["1", "0"]]))

    def test_maximal_square_2(self):
        self.assertEqual(0, maximal_square(self, [["0"]]))

    if __name__ == '__main__':
        unittest.main()
