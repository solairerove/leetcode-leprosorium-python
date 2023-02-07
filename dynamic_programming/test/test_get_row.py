import unittest

from dynamic_programming.PascalTriangleII import get_row, get_row_from_smart_guy, get_row_one_line


class MyTestCase(unittest.TestCase):
    def test_get_row(self):
        self.assertEqual([1, 3, 3, 1], get_row(self, 3))
        self.assertEqual([1, 3, 3, 1], get_row_from_smart_guy(self, 3))
        self.assertEqual([1, 3, 3, 1], get_row_one_line(self, 3))

    def test_get_row_1(self):
        self.assertEqual([1], get_row(self, 0))
        self.assertEqual([1], get_row_from_smart_guy(self, 0))
        self.assertEqual([1], get_row_one_line(self, 0))


if __name__ == '__main__':
    unittest.main()
