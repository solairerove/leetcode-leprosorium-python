import unittest

from maths.AddBinary import add_binary


class MyTestCase(unittest.TestCase):
    def test_add_binary(self):
        self.assertEqual("100", add_binary(self, "11", "1"))

    def test_add_binary_1(self):
        self.assertEqual("10101", add_binary(self, "1010", "1011"))


if __name__ == '__main__':
    unittest.main()
