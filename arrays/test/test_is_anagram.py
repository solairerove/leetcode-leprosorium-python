import unittest

from arrays.ValidAnagram import is_anagram


class MyTestCase(unittest.TestCase):
    def test_is_anagram(self):
        self.assertEqual(True, is_anagram(self, "anagram", "nagaram"))

    def test_is_anagram_1(self):
        self.assertEqual(False, is_anagram(self, "rat", "car"))

    def test_is_anagram_2(self):
        self.assertEqual(False, is_anagram(self, "aa", "a"))


if __name__ == '__main__':
    unittest.main()
