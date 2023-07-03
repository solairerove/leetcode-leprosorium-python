import unittest

from arrays.BuddyStrings import buddy_strings


class MyTestCase(unittest.TestCase):
    def test_buddy_strings(self):
        self.assertEqual(True, buddy_strings(self, s="ab", goal="ba"))

    def test_buddy_strings_1(self):
        self.assertEqual(False, buddy_strings(self, s="ab", goal="ab"))

    def test_buddy_strings_2(self):
        self.assertEqual(True, buddy_strings(self, s="aa", goal="aa"))


if __name__ == '__main__':
    unittest.main()
