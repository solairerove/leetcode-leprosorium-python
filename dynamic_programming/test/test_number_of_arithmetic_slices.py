import unittest

from dynamic_programming.ArithmeticSlices import number_of_arithmetic_slices_top_down, number_of_arithmetic_slices


class MyTestCase(unittest.TestCase):
    def test_number_of_arithmetic_slices(self):
        self.assertEqual(3, number_of_arithmetic_slices_top_down(self, [1, 2, 3, 4]))
        self.assertEqual(3, number_of_arithmetic_slices(self, [1, 2, 3, 4]))

    def test_number_of_arithmetic_slices_1(self):
        self.assertEqual(0, number_of_arithmetic_slices_top_down(self, [1]))
        self.assertEqual(0, number_of_arithmetic_slices(self, [1]))


if __name__ == '__main__':
    unittest.main()
