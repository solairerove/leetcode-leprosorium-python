import unittest

from dynamic_programming.NthTribonacciNumber import tribonacci, tribonacci_from_smart_guy, tribonacci_top_down


class MyTestCase(unittest.TestCase):
    def test_tribonacci(self):
        self.assertEqual(4, tribonacci(self, 4))
        self.assertEqual(4, tribonacci_from_smart_guy(self, 4))
        self.assertEqual(4, tribonacci_top_down(self, 4))

    def test_tribonacci_1(self):
        self.assertEqual(1389537, tribonacci(self, 25))
        self.assertEqual(1389537, tribonacci_from_smart_guy(self, 25))
        self.assertEqual(1389537, tribonacci_top_down(self, 25))


if __name__ == '__main__':
    unittest.main()
