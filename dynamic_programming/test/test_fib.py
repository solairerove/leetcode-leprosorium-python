import unittest

from dynamic_programming.FibonacciNumber import fib, fib_rec


class MyTestCase(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(1, fib(self, 2))  
        self.assertEqual(1, fib_rec(self, 2))

    def test_fib_1(self):
        self.assertEqual(2, fib(self, 3))  
        self.assertEqual(2, fib_rec(self, 3))

    def test_fib_2(self):
        self.assertEqual(3, fib(self, 4))  
        self.assertEqual(3, fib_rec(self, 4))

    def test_fib_3(self):
        self.assertEqual(5, fib(self, 5))
        self.assertEqual(5, fib_rec(self, 5))

    def test_fib_4(self):
        self.assertEqual(8, fib(self, 6))
        self.assertEqual(8, fib_rec(self, 6))


if __name__ == '__main__':
    unittest.main()
