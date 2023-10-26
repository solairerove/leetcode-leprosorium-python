import unittest

from arrays.RemoveInvalidParentheses import remove_invalid_parentheses


class MyTestCase(unittest.TestCase):
    def test_remove_invalid_parentheses(self):
        self.assertEqual(["(())()", "()()()"], remove_invalid_parentheses(self, s="()())()"))

    def test_remove_invalid_parentheses_1(self):
        self.assertEqual(["(a())()", "(a)()()"], remove_invalid_parentheses(self, s="(a)())()"))

    def test_remove_invalid_parentheses_2(self):
        self.assertEqual([""], remove_invalid_parentheses(self, s=")("))


if __name__ == '__main__':
    unittest.main()
