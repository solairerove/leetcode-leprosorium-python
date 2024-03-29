import unittest

from arrays.Convert1DArrayInto2DArray import construct_2d_array, construct_2d_array_smart, construct_2d_array_one_liner


class MyTestCase(unittest.TestCase):
    def test_construct_2d_array(self):
        self.assertEqual([[1, 2], [3, 4]], construct_2d_array(self, [1, 2, 3, 4], 2, 2))
        self.assertEqual([[1, 2], [3, 4]], construct_2d_array_smart(self, [1, 2, 3, 4], 2, 2))
        self.assertEqual([[1, 2], [3, 4]], construct_2d_array_one_liner(self, [1, 2, 3, 4], 2, 2))

    def test_construct_2d_array_1(self):
        self.assertEqual([[1, 2, 3]], construct_2d_array(self, [1, 2, 3], 1, 3))
        self.assertEqual([[1, 2, 3]], construct_2d_array_smart(self, [1, 2, 3], 1, 3))
        self.assertEqual([[1, 2, 3]], construct_2d_array_one_liner(self, [1, 2, 3], 1, 3))

    def test_construct_2d_array_2(self):
        self.assertEqual([], construct_2d_array(self, [1, 2], 1, 1))
        self.assertEqual([], construct_2d_array_smart(self, [1, 2], 1, 1))
        self.assertEqual([], construct_2d_array_one_liner(self, [1, 2], 1, 1))

    def test_construct_2d_array_3(self):
        self.assertEqual([], construct_2d_array(self, [3], 1, 2))
        self.assertEqual([], construct_2d_array_smart(self, [3], 1, 2))
        self.assertEqual([], construct_2d_array_one_liner(self, [3], 1, 2))


if __name__ == '__main__':
    unittest.main()
