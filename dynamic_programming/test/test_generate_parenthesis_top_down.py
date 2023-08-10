import unittest

from dynamic_programming.GenerateParentheses import generate_parenthesis_top_down


class MyTestCase(unittest.TestCase):
    def test_generate_parenthesis(self):
        self.assertEqual(["((()))", "(()())", "(())()", "()(())", "()()()"], generate_parenthesis_top_down(self, 3))

    def test_generate_parenthesis_1(self):
        self.assertEqual(["()"], generate_parenthesis_top_down(self, 1))


if __name__ == '__main__':
    unittest.main()
