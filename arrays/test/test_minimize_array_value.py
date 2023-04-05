import unittest

from arrays.MinimizeMaximumOfArray import minimize_array_value, minimize_array_value_plain


class MyTestCase(unittest.TestCase):
    def test_minimize_array_value(self):
        self.assertEqual(5, minimize_array_value(self, [3, 7, 1, 6]))
        self.assertEqual(5, minimize_array_value_plain(self, [3, 7, 1, 6]))

    def test_minimize_array_value_1(self):
        self.assertEqual(10, minimize_array_value(self, [10, 1]))
        self.assertEqual(10, minimize_array_value_plain(self, [10, 1]))


if __name__ == '__main__':
    unittest.main()
