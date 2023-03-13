import unittest

from arrays.ValidPalindrome import is_palindrome


class MyTestCase(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(True, is_palindrome(self, "A man, a plan, a canal: Panama"))

    def test_is_palindrome_1(self):
        self.assertEqual(False, is_palindrome(self, "race a car"))

    def test_is_palindrome_2(self):
        self.assertEqual(True, is_palindrome(self, " "))


if __name__ == '__main__':
    unittest.main()
