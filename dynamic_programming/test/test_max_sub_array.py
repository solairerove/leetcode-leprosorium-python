import unittest

from dynamic_programming.MaximumSubarray import max_sub_array


class MyTestCase(unittest.TestCase):
    def test_max_sub_array(self):
        self.assertEqual(6, max_sub_array(self, [-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_max_sub_array_1(self):
        self.assertEqual(1, max_sub_array(self, [1]))

    def test_max_sub_array_2(self):
        self.assertEqual(23, max_sub_array(self, [5, 4, -1, 7, 8]))

    def test_max_sub_array_3(self):
        self.assertEqual(-1, max_sub_array(self, [-1]))

    def test_max_sub_array_4(self):
        self.assertEqual(-1, max_sub_array(self, [-1, -2]))


if __name__ == '__main__':
    unittest.main()
