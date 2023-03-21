import unittest

from arrays.Convert1DArrayInto2DArray import construct_2d_array


class MyTestCase(unittest.TestCase):
    def test_construct_2d_array(self):
        self.assertEqual([[1, 2], [3, 4]], construct_2d_array(self, [1, 2, 3, 4], 2, 2))

    def test_construct_2d_array_1(self):
        self.assertEqual([[1, 2, 3]], construct_2d_array(self, [1, 2, 3], 1, 3))

    def test_construct_2d_array_2(self):
        self.assertEqual([], construct_2d_array(self, [1, 2], 1, 1))

    def test_construct_2d_array_3(self):
        self.assertEqual([], construct_2d_array(self, [3], 1, 2))


if __name__ == '__main__':
    unittest.main()
