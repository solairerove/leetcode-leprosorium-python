import unittest

from arrays.ProductOfArrayExceptSelf import product_except_self


class MyTestCase(unittest.TestCase):
    def test_product_except_self(self):
        self.assertEqual([24, 12, 8, 6], product_except_self(self, [1, 2, 3, 4]))

    def test_product_except_self_1(self):
        self.assertEqual([0, 0, 9, 0, 0], product_except_self(self, [-1, 1, 0, -3, 3]))


if __name__ == '__main__':
    unittest.main()
