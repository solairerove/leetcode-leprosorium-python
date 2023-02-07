import unittest

from dynamic_programming.PascalTriangle import generate_from_smart_guys, generate


class MyTestCase(unittest.TestCase):
    def test_generate(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], generate_from_smart_guys(self, 5))
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], generate(self, 5))

    def test_generate_1(self):
        self.assertEqual([[1]], generate_from_smart_guys(self, 1))
        self.assertEqual([[1]], generate(self, 1))


if __name__ == '__main__':
    unittest.main()
