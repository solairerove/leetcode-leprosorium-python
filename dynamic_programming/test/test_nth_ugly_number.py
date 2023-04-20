import unittest

from dynamic_programming.UglyNumberII import nth_ugly_number_pre_calculated, nth_ugly_number


class MyTestCase(unittest.TestCase):
    def test_nth_ugly_number(self):
        self.assertEqual(12, nth_ugly_number_pre_calculated(self, 10))
        self.assertEqual(12, nth_ugly_number(self, 10))

    def test_nth_ugly_number_1(self):
        self.assertEqual(1, nth_ugly_number_pre_calculated(self, 1))
        self.assertEqual(1, nth_ugly_number(self, 1))


if __name__ == '__main__':
    unittest.main()
