import unittest

from heap.IPO import find_maximized_capital


class MyTestCase(unittest.TestCase):
    def test_find_maximized_capital(self):
        self.assertEqual(4, find_maximized_capital(self, 2, 0, [1, 2, 3], [0, 1, 1]))

    def test_find_maximized_capital_1(self):
        self.assertEqual(6, find_maximized_capital(self, 3, 0, [1, 2, 3], [0, 1, 2]))


if __name__ == '__main__':
    unittest.main()
