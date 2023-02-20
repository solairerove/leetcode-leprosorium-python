import unittest

from dynamic_programming.OnesAndZeroes import find_max_form, find_max_form_rec


class MyTestCase(unittest.TestCase):
    def test_find_max_form(self):
        self.assertEqual(4, find_max_form(self, ["10", "0001", "111001", "1", "0"], 5, 3))
        self.assertEqual(4, find_max_form_rec(self, ["10", "0001", "111001", "1", "0"], 5, 3))

    def test_find_max_form_1(self):
        self.assertEqual(2, find_max_form(self, ["10", "0", "1"], 1, 1))
        self.assertEqual(2, find_max_form_rec(self, ["10", "0", "1"], 1, 1))


if __name__ == '__main__':
    unittest.main()
