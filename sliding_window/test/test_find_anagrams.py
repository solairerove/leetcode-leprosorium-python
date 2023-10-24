import unittest

from sliding_window.FindAllAnagramsInAString import find_anagrams


class MyTestCase(unittest.TestCase):
    def test_find_anagrams(self):
        self.assertEqual([0, 6], find_anagrams(self, s="cbaebabacd", p="abc"))

    def test_find_anagrams_1(self):
        self.assertEqual([0, 1, 2], find_anagrams(self, s="abab", p="ab"))


if __name__ == '__main__':
    unittest.main()
