import unittest

from arrays.RansomNote import can_construct


class MyTestCase(unittest.TestCase):
    def test_ransom_note(self):
        self.assertEqual(False, can_construct(self, "a", "b"))

    def test_ransom_note_1(self):
        self.assertEqual(False, can_construct(self, "aa", "ab"))

    def test_ransom_note_2(self):
        self.assertEqual(True, can_construct(self, "aa", "aab"))


if __name__ == '__main__':
    unittest.main()
