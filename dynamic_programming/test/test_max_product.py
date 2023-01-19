import unittest

from dynamic_programming.MaximumProductSubarray import max_product


class MyTestCase(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(6, max_product(self, [2, 3, -2, 4]))  # add assertion here

    def test_max_product_1(self):
        self.assertEqual(0, max_product(self, [-2, 0, -1]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
