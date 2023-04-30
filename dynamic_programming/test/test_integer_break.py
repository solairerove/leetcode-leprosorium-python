import unittest

from dynamic_programming.IntegerBreak import integer_break


class MyTestCase(unittest.TestCase):
    def test_integer_break(self):
        self.assertEqual(1, integer_break(self, 2))

    def test_integer_break_1(self):
        self.assertEqual(36, integer_break(self, 10))


if __name__ == '__main__':
    unittest.main()
