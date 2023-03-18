import unittest

from maths.SmallestGoodBase import smallest_good_base


class MyTestCase(unittest.TestCase):
    def test_smallest_good_base(self):
        self.assertEqual("3", smallest_good_base(self, "13"))

    def test_smallest_good_base_1(self):
        self.assertEqual("8", smallest_good_base(self, "4681"))

    def test_smallest_good_base_2(self):
        self.assertEqual("999999999999999999", smallest_good_base(self, "1000000000000000000"))


if __name__ == '__main__':
    unittest.main()
