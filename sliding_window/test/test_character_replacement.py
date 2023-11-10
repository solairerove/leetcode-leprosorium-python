import unittest

from sliding_window.LongestRepeatingCharacterReplacement import character_replacement


class MyTestCase(unittest.TestCase):
    def test_character_replacement(self):
        self.assertEqual(4, character_replacement(self, s="ABAB", k=2))

    def test_character_replacement_1(self):
        self.assertEqual(4, character_replacement(self, s="AABABBA", k=1))

    def test_character_replacement_2(self):
        self.assertEqual(6, character_replacement(self, s="ABCABCABAB", k=3))


if __name__ == '__main__':
    unittest.main()
