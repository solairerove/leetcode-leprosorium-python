import unittest

from maths.RomanToInteger import roman_to_int


class MyTestCase(unittest.TestCase):
    def test_roman_to_int(self):
        self.assertEqual(3, roman_to_int(self, "III"))

    def test_roman_to_int_1(self):
        self.assertEqual(58, roman_to_int(self, "LVIII"))

    def test_roman_to_int_2(self):
        self.assertEqual(1994, roman_to_int(self, "MCMXCIV"))


if __name__ == '__main__':
    unittest.main()
