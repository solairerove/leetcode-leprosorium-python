import unittest

from maths.MinimumFlipsToMakeAORBEqualToC import min_flips


class MyTestCase(unittest.TestCase):
    def test_min_flips(self):
        self.assertEqual(3, min_flips(self, a=2, b=6, c=5))

    def test_min_flips_1(self):
        self.assertEqual(1, min_flips(self, a=4, b=2, c=7))

    def test_min_flips_2(self):
        self.assertEqual(0, min_flips(self, a=1, b=2, c=3))


if __name__ == '__main__':
    unittest.main()
