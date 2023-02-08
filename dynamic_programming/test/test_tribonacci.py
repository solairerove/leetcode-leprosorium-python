import unittest

from dynamic_programming.NthTribonacciNumber import tribonacci


class MyTestCase(unittest.TestCase):
    def test_tribonacci(self):
        self.assertEqual(4, tribonacci(self, 4))

    def test_tribonacci_1(self):
        self.assertEqual(1389537, tribonacci(self, 25))


if __name__ == '__main__':
    unittest.main()
