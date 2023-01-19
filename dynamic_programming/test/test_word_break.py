import unittest

from dynamic_programming.WordBreak import word_break, word_break_constant


class MyTestCase(unittest.TestCase):

    def test_word_break_constant(self):
        self.assertEqual(True, word_break_constant(self, "leetcode", ["leet", "code"]))

    def test_word_break_constant_1(self):
        self.assertEqual(True, word_break_constant(self, "applepenapple", ["apple", "pen"]))

    def test_word_break_constant_2(self):
        self.assertEqual(False, word_break_constant(self, "catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_word_break(self):
        self.assertEqual(True, word_break(self, "leetcode", ["leet", "code"]))

    def test_word_break_1(self):
        self.assertEqual(True, word_break(self, "applepenapple", ["apple", "pen"]))

    def test_word_break_2(self):
        self.assertEqual(False, word_break(self, "catsandog", ["cats", "dog", "sand", "and", "cat"]))


if __name__ == '__main__':
    unittest.main()
