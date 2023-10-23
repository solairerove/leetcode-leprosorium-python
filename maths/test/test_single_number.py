import unittest

from maths.SingleNumber import single_number, single_number_reduce


class MyTestCase(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(1, single_number(self, [2, 2, 1]))
        self.assertEqual(1, single_number_reduce(self, [2, 2, 1]))

    def test_single_number_1(self):
        self.assertEqual(4, single_number(self, [4, 1, 2, 1, 2]))
        self.assertEqual(4, single_number_reduce(self, [4, 1, 2, 1, 2]))

    def test_single_number_2(self):
        self.assertEqual(1, single_number(self, [1]))
        self.assertEqual(1, single_number_reduce(self, [1]))


if __name__ == '__main__':
    unittest.main()
