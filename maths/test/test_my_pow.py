import unittest

from maths.PowXN import my_pow


class MyTestCase(unittest.TestCase):
    def test_my_pow(self):
        self.assertEqual(1024.00000, my_pow(self, x=2.00000, n=10))

    def test_my_pow_1(self):
        self.assertEqual(9.261000000000001, my_pow(self, 2.10000, n=3))

    def test_my_pow_2(self):
        self.assertEqual(0.25000, my_pow(self, x=2.00000, n=-2))

    def test_my_pow_3(self):
        self.assertEqual(1, my_pow(self, x=0.44528, n=0))


if __name__ == '__main__':
    unittest.main()
