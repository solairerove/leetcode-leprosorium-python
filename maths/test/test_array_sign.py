import unittest

from maths.SignOfTheProductOfAnArray import array_sign


class MyTestCase(unittest.TestCase):
    def test_array_sign(self):
        self.assertEqual(1, array_sign(self, [-1, -2, -3, -4, 3, 2, 1]))

    def test_array_sign_1(self):
        self.assertEqual(0, array_sign(self, [1, 5, 0, 2, -3]))

    def test_array_sign_2(self):
        self.assertEqual(-1, array_sign(self, [-1, 1, -1, 1, -1]))


if __name__ == '__main__':
    unittest.main()
