import unittest

from dynamic_programming.PascalTriangle import generate_from_smart_guys


class MyTestCase(unittest.TestCase):
    def test_generate(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], generate_from_smart_guys(self, 5))


if __name__ == '__main__':
    unittest.main()
