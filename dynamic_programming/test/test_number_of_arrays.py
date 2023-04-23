import unittest

from dynamic_programming.RestoreTheArray import number_of_arrays_top_down


class MyTestCase(unittest.TestCase):
    def test_number_of_arrays(self):
        self.assertEqual(1, number_of_arrays_top_down(self, "1000", 10000))

    def test_number_of_arrays_1(self):
        self.assertEqual(0, number_of_arrays_top_down(self, "1000", 10))

    def test_number_of_arrays_2(self):
        self.assertEqual(8, number_of_arrays_top_down(self, "1317", 2000))


if __name__ == '__main__':
    unittest.main()
