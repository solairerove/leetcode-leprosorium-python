import unittest

from dynamic_programming.MaximumProductSubarray import max_product, max_product_from_smarter_guy


class MyTestCase(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(6, max_product(self, [2, 3, -2, 4]))  

    def test_max_product_1(self):
        self.assertEqual(0, max_product(self, [-2, 0, -1]))  

    def test_max_product_from_smarter_guy(self):
        self.assertEqual(6, max_product_from_smarter_guy(self, [2, 3, -2, 4]))  

    def test_max_product_from_smarter_guy_1(self):
        self.assertEqual(0, max_product_from_smarter_guy(self, [-2, 0, -1]))  


if __name__ == '__main__':
    unittest.main()
