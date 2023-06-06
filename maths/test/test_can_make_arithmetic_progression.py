import unittest

from maths.CanMakeArithmeticProgressionFromSequence import can_make_arithmetic_progression_sorting, \
    can_make_arithmetic_progression


class MyTestCase(unittest.TestCase):
    def test_can_make_arithmetic_progression(self):
        self.assertEqual(True, can_make_arithmetic_progression_sorting(self, [3, 5, 1]))
        self.assertEqual(True, can_make_arithmetic_progression(self, [3, 5, 1]))

    def test_can_make_arithmetic_progression_1(self):
        self.assertEqual(False, can_make_arithmetic_progression_sorting(self, [1, 2, 4]))
        self.assertEqual(False, can_make_arithmetic_progression(self, [1, 2, 4]))


if __name__ == '__main__':
    unittest.main()
