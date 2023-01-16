import unittest

from dynamic_programming.FibonacciNumber import fib


class MyTestCase(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(1, fib(self, 2))  # add assertion here

    def test_fib_1(self):
        self.assertEqual(2, fib(self, 3))  # add assertion here

    def test_fib_2(self):
        self.assertEqual(3, fib(self, 4))  # add assertion here


if __name__ == '__main__':
    unittest.main()
