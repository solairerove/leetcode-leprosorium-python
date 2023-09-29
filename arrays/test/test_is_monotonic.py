import unittest

from arrays.MonotonicArray import is_monotonic


class MyTestCase(unittest.TestCase):
    def test_is_monotonic(self):
        self.assertEqual(True, is_monotonic(self, nums=[1, 2, 2, 3]))

    def test_is_monotonic_1(self):
        self.assertEqual(True, is_monotonic(self, nums=[6, 5, 4, 4]))

    def test_is_monotonic_2(self):
        self.assertEqual(False, is_monotonic(self, nums=[1, 3, 2]))


if __name__ == '__main__':
    unittest.main()
