import unittest

from dynamic_programming.ScrambleString import is_scramble


class MyTestCase(unittest.TestCase):
    def test_is_scramble(self):
        self.assertEqual(True, is_scramble(self, "great", "rgeat"))

    def test_is_scramble_2(self):
        self.assertEqual(False, is_scramble(self, "abcde", "caebd"))

    def test_is_scramble_3(self):
        self.assertEqual(True, is_scramble(self, "a", "a"))


if __name__ == '__main__':
    unittest.main()
