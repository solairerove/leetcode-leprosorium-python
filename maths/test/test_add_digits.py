import unittest

from maths.AddDigits import add_digits_rec


class MyTestCase(unittest.TestCase):
    def test_add_digits(self):
        self.assertEqual(2, add_digits_rec(self, 38))

    def test_add_digits_1(self):
        self.assertEqual(0, add_digits_rec(self, 0))


if __name__ == '__main__':
    unittest.main()
