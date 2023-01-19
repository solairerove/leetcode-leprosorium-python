import unittest

from dynamic_programming.FibonacciNumber import fib


class MyTestCase(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(1, fib(self, 2))  

    def test_fib_1(self):
        self.assertEqual(2, fib(self, 3))  

    def test_fib_2(self):
        self.assertEqual(3, fib(self, 4))  


if __name__ == '__main__':
    unittest.main()
