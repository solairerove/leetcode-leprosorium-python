import unittest

from dynamic_programming.CountingBits import count_bits


class MyTestCase(unittest.TestCase):
    def test_count_bits(self):
        self.assertEqual([0, 1, 1], count_bits(self, 2))

    def test_count_bits_1(self):
        self.assertEqual([0, 1, 1, 2, 1, 2], count_bits(self, 5))


if __name__ == '__main__':
    unittest.main()
