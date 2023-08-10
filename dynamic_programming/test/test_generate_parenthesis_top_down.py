import unittest

from dynamic_programming.GenerateParentheses import generate_parenthesis_dfs, generate_parenthesis_bfs


class MyTestCase(unittest.TestCase):
    def test_generate_parenthesis(self):
        self.assertEqual(["((()))", "(()())", "(())()", "()(())", "()()()"], generate_parenthesis_dfs(self, 3))
        self.assertEqual(['()()()', '()(())', '(())()', '(()())', '((()))'], generate_parenthesis_bfs(self, 3))

    def test_generate_parenthesis_1(self):
        self.assertEqual(["()"], generate_parenthesis_dfs(self, 1))
        self.assertEqual(["()"], generate_parenthesis_bfs(self, 1))


if __name__ == '__main__':
    unittest.main()
