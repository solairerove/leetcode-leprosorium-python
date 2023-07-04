import unittest

from arrays.SingleNumberII import single_number


class MyTestCase(unittest.TestCase):
    def test_single_number_ii(self):
        self.assertEqual(3, single_number(self, nums=[2, 2, 3, 2]))

    def test_single_number_ii_1(self):
        self.assertEqual(99, single_number(self, nums=[0, 1, 0, 1, 0, 1, 99]))


if __name__ == '__main__':
    unittest.main()
