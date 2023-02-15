import unittest

from maths.AddToArrayFormOfInteger import add_to_array_form


class MyTestCase(unittest.TestCase):
    def test_add_to_array_form(self):
        self.assertEqual([1, 2, 3, 4], add_to_array_form(self, [1, 2, 0, 0], 34))

    def test_add_to_array_form_1(self):
        self.assertEqual([4, 5, 5], add_to_array_form(self, [2, 7, 4], 181))

    def test_add_to_array_form_2(self):
        self.assertEqual([1, 0, 2, 1], add_to_array_form(self, [2, 1, 5], 806))


if __name__ == '__main__':
    unittest.main()
