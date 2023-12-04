import unittest

from stack.ValidParentheses import is_valid


class MyTestCase(unittest.TestCase):
    def test_is_valid(self):
        self.assertEqual(True, is_valid(self, "()"))

    def test_is_valid_1(self):
        self.assertEqual(True, is_valid(self, "()[]{}"))

    def test_is_valid_2(self):
        self.assertEqual(False, is_valid(self, "(]"))

    def test_is_valid_3(self):
        self.assertEqual(True, is_valid(self, "{[]}"))

    def test_is_valid_4(self):
        self.assertEqual(False, is_valid(self, "]"))


if __name__ == '__main__':
    unittest.main()
